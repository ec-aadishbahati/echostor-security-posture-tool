import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { useQuery, useMutation, useQueryClient } from 'react-query';
import { useAuth } from '@/lib/auth';
import { useAutoLogout } from '@/lib/useAutoLogout';
import Layout from '@/components/Layout';
import ProtectedRoute from '@/components/ProtectedRoute';
import { assessmentAPI } from '@/lib/api';
import toast from 'react-hot-toast';
import { 
  ChevronLeftIcon, 
  ChevronRightIcon,
  BookmarkIcon,
  CheckCircleIcon,
  ClockIcon
} from '@heroicons/react/24/outline';

interface Question {
  id: string;
  section_id: string;
  text: string;
  type: string;
  weight: number;
  explanation: string;
  options: Array<{
    value: string;
    label: string;
    description?: string;
  }>;
}

interface Section {
  id: string;
  title: string;
  description: string;
  questions: Question[];
}

export default function AssessmentQuestions() {
  const { user } = useAuth();
  const router = useRouter();
  const queryClient = useQueryClient();
  
  useAutoLogout(async () => {
    if (assessmentId) {
      await saveProgress();
    }
  });
  
  const [currentSectionIndex, setCurrentSectionIndex] = useState(0);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [responses, setResponses] = useState<Record<string, any>>({});
  const [comments, setComments] = useState<Record<string, string>>({});
  const [consultationInterest, setConsultationInterest] = useState<boolean | null>(null);
  const [consultationDetails, setConsultationDetails] = useState<string>('');
  const [showConsultationQuestion, setShowConsultationQuestion] = useState(false);
  const [lastSaved, setLastSaved] = useState<Date | null>(null);
  const [assessmentId, setAssessmentId] = useState<string | null>(null);

  useAutoLogout(async () => {
    if (assessmentId) {
      await saveProgress();
    }
  });

  const { data: structure, isLoading: structureLoading } = useQuery(
    'assessmentStructure',
    assessmentAPI.getStructure
  );

  const { data: assessment, isLoading: assessmentLoading } = useQuery(
    'currentAssessment',
    assessmentAPI.getCurrentAssessment,
    {
      onSuccess: (data) => {
        setAssessmentId(data.data.id);
        assessmentAPI.getResponses(data.data.id).then((responseData) => {
          const existingResponses: Record<string, any> = {};
          responseData.data.forEach((response: any) => {
            existingResponses[response.question_id] = response.answer_value;
          });
          setResponses(existingResponses);
        });
      },
      onError: () => {
        startAssessmentMutation.mutate();
      }
    }
  );

  const startAssessmentMutation = useMutation(
    assessmentAPI.startAssessment,
    {
      onSuccess: (data) => {
        setAssessmentId(data.data.id);
        queryClient.invalidateQueries('currentAssessment');
      },
      onError: (error: any) => {
        toast.error('Failed to start assessment');
        router.push('/dashboard');
      }
    }
  );

  const saveProgressMutation = useMutation(
    ({ assessmentId, responses }: { assessmentId: string; responses: any[] }) =>
      assessmentAPI.saveProgress(assessmentId, responses),
    {
      onSuccess: () => {
        setLastSaved(new Date());
        toast.success('Progress saved!');
      },
      onError: (error: any) => {
        toast.error('Failed to save progress');
      }
    }
  );

  const completeAssessmentMutation = useMutation(
    (assessmentId: string) => assessmentAPI.completeAssessment(assessmentId),
    {
      onSuccess: () => {
        toast.success('Assessment completed!');
        router.push('/reports');
      },
      onError: (error: any) => {
        toast.error('Failed to complete assessment');
      }
    }
  );

  useEffect(() => {
    if (!assessmentId) return;

    const interval = setInterval(() => {
      saveProgress();
    }, 10 * 60 * 1000); // 10 minutes

    return () => clearInterval(interval);
  }, [assessmentId, responses]);

  const saveProgress = () => {
    if (!assessmentId || !structure) return;

    const responseArray = Object.entries(responses).map(([questionId, value]) => {
      const question = findQuestionById(questionId);
      return {
        section_id: question?.section_id || '',
        question_id: questionId,
        answer_value: value,
        comment: comments[questionId] || null
      };
    });

    saveProgressMutation.mutate({ assessmentId, responses: responseArray });
  };

  const handleCommentChange = (questionId: string, comment: string) => {
    const wordCount = comment.trim().split(/\s+/).filter(word => word.length > 0).length;
    if (wordCount <= 150) {
      setComments(prev => ({
        ...prev,
        [questionId]: comment
      }));
    }
  };

  const findQuestionById = (questionId: string): Question | undefined => {
    if (!structure) return undefined;
    
    for (const section of structure.data.sections) {
      const question = section.questions.find((q: Question) => q.id === questionId);
      if (question) return question;
    }
    return undefined;
  };

  const handleAnswerChange = (questionId: string, value: any) => {
    setResponses(prev => ({
      ...prev,
      [questionId]: value
    }));
  };

  const getCurrentQuestion = (): Question | null => {
    if (!structure || !structure.data.sections[currentSectionIndex]) return null;
    const section = structure.data.sections[currentSectionIndex];
    return section.questions[currentQuestionIndex] || null;
  };

  const getCurrentSection = (): Section | null => {
    if (!structure || !structure.data.sections[currentSectionIndex]) return null;
    return structure.data.sections[currentSectionIndex];
  };

  const goToNextQuestion = () => {
    const section = getCurrentSection();
    if (!section) return;

    if (currentQuestionIndex < section.questions.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
    } else if (currentSectionIndex < (structure?.data?.sections?.length || 0) - 1) {
      setCurrentSectionIndex(prev => prev + 1);
      setCurrentQuestionIndex(0);
    } else if (!showConsultationQuestion) {
      setShowConsultationQuestion(true);
    }
  };

  const goToPreviousQuestion = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(prev => prev - 1);
    } else if (currentSectionIndex > 0) {
      setCurrentSectionIndex(prev => prev - 1);
      const prevSection = structure?.data?.sections?.[currentSectionIndex - 1];
      setCurrentQuestionIndex(prevSection.questions.length - 1);
    }
  };

  const calculateProgress = () => {
    if (!structure) return 0;
    
    const totalQuestions = structure.data.total_questions;
    const answeredQuestions = Object.keys(responses).length;
    return (answeredQuestions / totalQuestions) * 100;
  };

  const isLastQuestion = () => {
    if (!structure) return false;
    const isLastAssessmentQuestion = currentSectionIndex === structure.data.sections.length - 1 &&
           currentQuestionIndex === structure.data.sections[currentSectionIndex].questions.length - 1;
    
    if (isLastAssessmentQuestion && !showConsultationQuestion) {
      return false;
    }
    return showConsultationQuestion;
  };

  const handleCompleteAssessment = async () => {
    if (!assessmentId) return;
    
    if (confirm('Are you sure you want to complete the assessment? You won\'t be able to make changes after this.')) {
      try {
        if (consultationInterest !== null) {
          const consultationData = {
            consultation_interest: consultationInterest,
            consultation_details: consultationInterest ? consultationDetails : undefined
          };
          await assessmentAPI.saveConsultationInterest(assessmentId, consultationData);
        }
        
        saveProgress();
        setTimeout(() => {
          completeAssessmentMutation.mutate(assessmentId);
        }, 1000);
      } catch (error) {
        console.error('Failed to save consultation data:', error);
      }
    }
  };

  if (structureLoading || assessmentLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (!user) {
    router.push('/auth/login');
    return null;
  }

  const currentQuestion = getCurrentQuestion();
  const currentSection = getCurrentSection();
  const progress = calculateProgress();

  if (!currentQuestion || !currentSection) {
    return (
      <Layout title="Assessment Questions">
        <div className="text-center py-12">
          <p className="text-gray-600">No questions available</p>
        </div>
      </Layout>
    );
  }

  return (
    <ProtectedRoute>
      <Layout title="Security Assessment">
        <div className="max-w-4xl mx-auto">
          {/* Enhanced Progress Bar */}
          <div className="mb-8">
            <div className="flex justify-between items-center mb-2">
              <span className="text-sm font-medium text-gray-700">
                Assessment Progress: {progress.toFixed(1)}% ({Object.keys(responses).length} of {structure?.data?.total_questions || 0} questions)
              </span>
              <div className="flex items-center text-sm text-gray-600">
                <ClockIcon className="h-4 w-4 mr-1" />
                {lastSaved ? `Auto-saved ${lastSaved.toLocaleTimeString()}` : 'Not saved yet'}
              </div>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-3">
              <div 
                className="bg-gradient-to-r from-primary-500 to-primary-600 h-3 rounded-full transition-all duration-500 relative"
                style={{ width: `${progress}%` }}
              >
                <div className="absolute right-0 top-0 h-3 w-1 bg-primary-700 rounded-r-full"></div>
              </div>
            </div>
            <div className="mt-1 text-xs text-gray-500">
              Section {currentSectionIndex + 1} of {structure?.data?.sections?.length || 0}: {currentSection?.title}
            </div>
          </div>

          {/* Section Info */}
          <div className="bg-primary-50 rounded-lg p-4 mb-6">
            <h2 className="text-lg font-semibold text-primary-900 mb-2">
              {currentSection.title}
            </h2>
            <p className="text-primary-700 text-sm">
              {currentSection.description}
            </p>
            <div className="mt-2 text-sm text-primary-600">
              Question {currentQuestionIndex + 1} of {currentSection.questions.length} in this section
            </div>
          </div>

          {/* Question */}
          <div className="card mb-6">
            <div className="mb-4">
              <div className="flex items-start justify-between mb-3">
                <h3 className="text-lg font-semibold text-gray-900 flex-1">
                  {currentQuestion.text}
                </h3>
                <div className="ml-4 px-2 py-1 bg-gray-100 rounded text-sm font-medium text-gray-600">
                  Weight: {currentQuestion.weight}
                </div>
              </div>
              
              {currentQuestion.explanation && (
                <div className="bg-blue-50 border border-blue-200 rounded-lg p-3 mb-4">
                  <p className="text-blue-800 text-sm">
                    <strong>Explanation:</strong> {currentQuestion.explanation}
                  </p>
                </div>
              )}
            </div>

            {/* Answer Options */}
            <div className="space-y-3">
              {currentQuestion.type === 'yes_no' && (
                <div className="space-y-2">
                  {currentQuestion.options.map((option) => (
                    <label key={option.value} className="flex items-start cursor-pointer">
                      <input
                        type="radio"
                        name={currentQuestion.id}
                        value={option.value}
                        checked={responses[currentQuestion.id] === option.value}
                        onChange={(e) => handleAnswerChange(currentQuestion.id, e.target.value)}
                        className="mt-1 mr-3 text-primary-600 focus:ring-primary-500"
                      />
                      <div>
                        <div className="font-medium text-gray-900">{option.label}</div>
                        {option.description && (
                          <div className="text-sm text-gray-600 mt-1">{option.description}</div>
                        )}
                      </div>
                    </label>
                  ))}
                </div>
              )}

              {currentQuestion.type === 'multiple_choice' && (
                <div className="space-y-2">
                  {currentQuestion.options.map((option) => (
                    <label key={option.value} className="flex items-start cursor-pointer">
                      <input
                        type="radio"
                        name={currentQuestion.id}
                        value={option.value}
                        checked={responses[currentQuestion.id] === option.value}
                        onChange={(e) => handleAnswerChange(currentQuestion.id, e.target.value)}
                        className="mt-1 mr-3 text-primary-600 focus:ring-primary-500"
                      />
                      <div>
                        <div className="font-medium text-gray-900">{option.label}</div>
                        {option.description && (
                          <div className="text-sm text-gray-600 mt-1">{option.description}</div>
                        )}
                      </div>
                    </label>
                  ))}
                </div>
              )}

              {currentQuestion.type === 'multiple_select' && (
                <div className="space-y-2">
                  {currentQuestion.options.map((option) => (
                    <label key={option.value} className="flex items-start cursor-pointer">
                      <input
                        type="checkbox"
                        value={option.value}
                        checked={Array.isArray(responses[currentQuestion.id]) && 
                                responses[currentQuestion.id].includes(option.value)}
                        onChange={(e) => {
                          const currentValues = Array.isArray(responses[currentQuestion.id]) 
                            ? responses[currentQuestion.id] 
                            : [];
                          
                          if (e.target.checked) {
                            handleAnswerChange(currentQuestion.id, [...currentValues, option.value]);
                          } else {
                            handleAnswerChange(currentQuestion.id, 
                              currentValues.filter((v: string) => v !== option.value));
                          }
                        }}
                        className="mt-1 mr-3 text-primary-600 focus:ring-primary-500 rounded"
                      />
                      <div>
                        <div className="font-medium text-gray-900">{option.label}</div>
                        {option.description && (
                          <div className="text-sm text-gray-600 mt-1">{option.description}</div>
                        )}
                      </div>
                    </label>
                  ))}
                </div>
              )}
            </div>
            
            {!showConsultationQuestion && (
              <div className="mt-6 pt-4 border-t border-gray-200">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Additional Comments (Optional)
                  <span className="text-xs text-gray-500 ml-2">
                    {comments[currentQuestion.id]?.trim().split(/\s+/).filter(word => word.length > 0).length || 0}/150 words
                  </span>
                </label>
                <textarea
                  value={comments[currentQuestion.id] || ''}
                  onChange={(e) => handleCommentChange(currentQuestion.id, e.target.value)}
                  placeholder="Add any additional context, clarifications, or notes about your answer..."
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                  rows={3}
                />
                {comments[currentQuestion.id]?.trim().split(/\s+/).filter(word => word.length > 0).length > 150 && (
                  <p className="text-red-600 text-xs mt-1">Comment exceeds 150 word limit</p>
                )}
              </div>
            )}
          </div>

          {showConsultationQuestion && (
            <div className="card mb-6">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">
                Consultation Interest
              </h3>
              <p className="text-gray-600 mb-4">
                Would you like to be contacted by EchoStor's Security Specialist for consultation on any security matters?
              </p>
              
              <div className="space-y-3 mb-4">
                <label className="flex items-center cursor-pointer">
                  <input
                    type="radio"
                    name="consultation"
                    value="yes"
                    checked={consultationInterest === true}
                    onChange={() => setConsultationInterest(true)}
                    className="mr-3 text-primary-600 focus:ring-primary-500"
                  />
                  <span className="font-medium text-gray-900">Yes, I'm interested in consultation</span>
                </label>
                <label className="flex items-center cursor-pointer">
                  <input
                    type="radio"
                    name="consultation"
                    value="no"
                    checked={consultationInterest === false}
                    onChange={() => setConsultationInterest(false)}
                    className="mr-3 text-primary-600 focus:ring-primary-500"
                  />
                  <span className="font-medium text-gray-900">No, thank you</span>
                </label>
              </div>

              {consultationInterest === true && (
                <div className="mt-4 pt-4 border-t border-gray-200">
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Consultation Details (Required)
                    <span className="text-xs text-gray-500 ml-2">
                      {consultationDetails.trim().split(/\s+/).filter(word => word.length > 0).length}/300 words (200-300 required)
                    </span>
                  </label>
                  <textarea
                    value={consultationDetails}
                    onChange={(e) => setConsultationDetails(e.target.value)}
                    placeholder="Please describe the security topics or areas you'd like to discuss with our specialist..."
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                    rows={5}
                    required
                  />
                  {(() => {
                    const wordCount = consultationDetails.trim().split(/\s+/).filter(word => word.length > 0).length;
                    if (wordCount < 200) {
                      return <p className="text-orange-600 text-xs mt-1">Please provide at least 200 words</p>;
                    } else if (wordCount > 300) {
                      return <p className="text-red-600 text-xs mt-1">Please limit to 300 words</p>;
                    }
                    return null;
                  })()}
                </div>
              )}
            </div>
          )}

          {/* Navigation */}
          <div className="flex justify-between items-center">
            <button
              onClick={goToPreviousQuestion}
              disabled={currentSectionIndex === 0 && currentQuestionIndex === 0 && !showConsultationQuestion}
              className="btn-secondary flex items-center disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <ChevronLeftIcon className="h-4 w-4 mr-2" />
              Previous
            </button>

            <div className="flex space-x-4">
              <button
                onClick={saveProgress}
                disabled={saveProgressMutation.isLoading}
                className="btn-secondary flex items-center"
              >
                <BookmarkIcon className="h-4 w-4 mr-2" />
                {saveProgressMutation.isLoading ? 'Saving...' : 'Save Progress'}
              </button>

              {isLastQuestion() ? (
                <button
                  onClick={handleCompleteAssessment}
                  disabled={
                    completeAssessmentMutation.isLoading ||
                    consultationInterest === null || 
                    (consultationInterest === true && (
                      !consultationDetails.trim() ||
                      consultationDetails.trim().split(/\s+/).filter(word => word.length > 0).length < 200 ||
                      consultationDetails.trim().split(/\s+/).filter(word => word.length > 0).length > 300
                    ))
                  }
                  className="btn-primary flex items-center disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <CheckCircleIcon className="h-4 w-4 mr-2" />
                  {completeAssessmentMutation.isLoading ? 'Completing...' : 'Complete Assessment'}
                </button>
              ) : (
                <button
                  onClick={goToNextQuestion}
                  className="btn-primary flex items-center"
                >
                  Next
                  <ChevronRightIcon className="h-4 w-4 ml-2" />
                </button>
              )}
            </div>
          </div>
        </div>
      </Layout>
    </ProtectedRoute>
  );
}

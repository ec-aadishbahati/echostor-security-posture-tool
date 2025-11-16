import { useState } from 'react';
import { useRouter } from 'next/router';
import { useQuery, useMutation } from '@tanstack/react-query';
import { useAuth } from '@/lib/auth';
import Layout from '@/components/Layout';
import ProtectedRoute from '@/components/ProtectedRoute';
import { assessmentAPI } from '@/lib/api';
import toast from 'react-hot-toast';
import { ClockIcon, DocumentTextIcon, CheckCircleIcon } from '@heroicons/react/24/outline';

interface Tier {
  name: string;
  description: string;
  duration: string;
  total_questions: number;
}

interface TiersResponse {
  tiers: Record<string, Tier>;
}

export default function StartAssessment() {
  const { user } = useAuth();
  const router = useRouter();
  const [selectedTier, setSelectedTier] = useState<string>('standard');

  const { data: tiersData, isLoading } = useQuery<{ data: TiersResponse }>(
    'assessmentTiers',
    assessmentAPI.getTiers
  );

  const startAssessmentMutation = useMutation(
    (tier: string) => assessmentAPI.startWithTier({ tier }),
    {
      onSuccess: () => {
        toast.success('Assessment started!');
        router.push('/assessment/questions');
      },
      onError: (error: any) => {
        console.error('Failed to start assessment:', error);
        const errorMessage =
          error?.response?.data?.detail || 'Failed to start assessment. Please try again.';
        toast.error(errorMessage);
      },
    }
  );

  if (isLoading) {
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

  const tiers = tiersData?.data?.tiers || {};
  const tierOrder = ['quick', 'standard', 'deep'];

  return (
    <ProtectedRoute>
      <Layout title="Start Assessment">
        <div className="max-w-6xl mx-auto py-8 px-4">
          <div className="bg-white rounded-lg shadow-md p-8">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">Choose Your Assessment Type</h1>
            <p className="text-gray-600 mb-8">
              Select the assessment level that best fits your needs. You can always customize
              sections later.
            </p>

            <div className="grid md:grid-cols-3 gap-6 mb-8">
              {tierOrder.map((tierId) => {
                const tier = tiers[tierId];
                if (!tier) return null;

                const isSelected = selectedTier === tierId;
                const isQuick = tierId === 'quick';
                const isStandard = tierId === 'standard';
                const isDeep = tierId === 'deep';

                return (
                  <div
                    key={tierId}
                    className={`relative border-2 rounded-lg p-6 cursor-pointer transition-all ${
                      isSelected
                        ? 'border-primary-500 bg-primary-50 shadow-lg'
                        : 'border-gray-200 hover:border-gray-300 hover:shadow-md'
                    }`}
                    onClick={() => setSelectedTier(tierId)}
                  >
                    {isStandard && (
                      <div className="absolute -top-3 left-1/2 transform -translate-x-1/2">
                        <span className="bg-primary-600 text-white text-xs font-semibold px-3 py-1 rounded-full">
                          RECOMMENDED
                        </span>
                      </div>
                    )}

                    <div className="flex items-center justify-between mb-4">
                      <h3 className="text-xl font-bold text-gray-900">{tier.name}</h3>
                      <div
                        className={`w-6 h-6 rounded-full border-2 flex items-center justify-center ${
                          isSelected
                            ? 'bg-primary-600 border-primary-600'
                            : 'border-gray-300 bg-white'
                        }`}
                      >
                        {isSelected && <CheckCircleIcon className="w-4 h-4 text-white" />}
                      </div>
                    </div>

                    <p className="text-gray-600 mb-6 min-h-[3rem]">{tier.description}</p>

                    <div className="space-y-3">
                      <div className="flex items-center text-sm text-gray-700">
                        <ClockIcon className="w-5 h-5 mr-2 text-gray-400" />
                        <span>
                          <span className="font-medium">Duration:</span> {tier.duration}
                        </span>
                      </div>
                      <div className="flex items-center text-sm text-gray-700">
                        <DocumentTextIcon className="w-5 h-5 mr-2 text-gray-400" />
                        <span>
                          <span className="font-medium">Questions:</span> ~{tier.total_questions}
                        </span>
                      </div>
                    </div>

                    {isQuick && (
                      <div className="mt-4 pt-4 border-t border-gray-200">
                        <p className="text-xs text-gray-500">
                          Perfect for quick security checks and initial evaluations
                        </p>
                      </div>
                    )}
                    {isStandard && (
                      <div className="mt-4 pt-4 border-t border-gray-200">
                        <p className="text-xs text-gray-500">
                          Comprehensive evaluation covering all core security domains
                        </p>
                      </div>
                    )}
                    {isDeep && (
                      <div className="mt-4 pt-4 border-t border-gray-200">
                        <p className="text-xs text-gray-500">
                          Complete analysis including specialized areas like OT/ICS and AI/ML
                        </p>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
              <p className="text-sm text-blue-900">
                <span className="font-semibold">Need more control?</span> You can also{' '}
                <button
                  onClick={() => router.push('/assessment/select-sections')}
                  className="text-blue-700 underline hover:text-blue-800"
                >
                  manually select specific sections
                </button>{' '}
                to customize your assessment.
              </p>
            </div>

            <div className="flex justify-between items-center">
              <button
                onClick={() => router.push('/dashboard')}
                className="px-6 py-3 text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
              >
                Cancel
              </button>
              <button
                onClick={() => startAssessmentMutation.mutate(selectedTier)}
                disabled={startAssessmentMutation.isLoading}
                className="px-8 py-3 bg-primary-600 text-white rounded-md hover:bg-primary-700 disabled:bg-gray-300 disabled:cursor-not-allowed font-medium"
              >
                {startAssessmentMutation.isLoading
                  ? 'Starting Assessment...'
                  : `Start ${tiers[selectedTier]?.name || 'Assessment'}`}
              </button>
            </div>
          </div>
        </div>
      </Layout>
    </ProtectedRoute>
  );
}

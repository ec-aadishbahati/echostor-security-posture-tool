import React from 'react';
import { useQuery } from 'react-query';
import Layout from '@/components/Layout';
import ProtectedRoute from '@/components/ProtectedRoute';
import { useAuth } from '@/lib/auth';
import { assessmentAPI } from '@/lib/api';
import Link from 'next/link';
import {
  DocumentTextIcon,
  ChartBarIcon,
  ClockIcon,
  ArrowRightIcon,
} from '@heroicons/react/24/outline';

export default function Dashboard() {
  const { user } = useAuth();

  const {
    data: assessment,
    isLoading: assessmentLoading,
    error: assessmentError,
  } = useQuery('currentAssessment', assessmentAPI.getCurrentAssessment, {
    retry: false,
    refetchOnWindowFocus: false,
  });

  const calculateTimeRemaining = (expiresAt: string) => {
    const now = new Date();
    const expiry = new Date(expiresAt);
    const diffTime = expiry.getTime() - now.getTime();
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    if (diffDays <= 0) return 'Expired';
    if (diffDays === 1) return '1 day';
    return `${diffDays} days`;
  };

  const hasActiveAssessment = assessment && !assessmentError;
  const progressPercentage = hasActiveAssessment ? assessment.data.progress_percentage || 0 : 0;
  const timeRemaining = hasActiveAssessment
    ? calculateTimeRemaining(assessment.data.expires_at)
    : '15 days';

  return (
    <ProtectedRoute>
      <Layout title="Dashboard">
        <div className="max-w-7xl mx-auto">
          <div className="mb-8">
            <h2 className="text-2xl font-bold text-gray-900 mb-2">
              Welcome back, {user?.full_name}
            </h2>
            <p className="text-gray-600">
              Continue your security posture assessment for {user?.company_name}
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
            <Link
              href="/assessment/questions"
              className="card hover:shadow-lg transition-shadow cursor-pointer"
            >
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <DocumentTextIcon className="h-8 w-8 text-primary-600" />
                </div>
                <div className="ml-4">
                  <h3 className="text-lg font-semibold text-gray-900">
                    {hasActiveAssessment ? 'Continue Assessment' : 'Start Assessment'}
                  </h3>
                  <p className="text-gray-600">
                    {hasActiveAssessment
                      ? 'Resume your security evaluation'
                      : 'Begin your security evaluation'}
                  </p>
                </div>
                <ArrowRightIcon className="h-5 w-5 text-gray-400 ml-auto" />
              </div>
            </Link>

            <div className="card">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <ChartBarIcon className="h-8 w-8 text-green-600" />
                </div>
                <div className="ml-4">
                  <h3 className="text-lg font-semibold text-gray-900">Progress</h3>
                  <p className="text-gray-600">
                    {assessmentLoading
                      ? 'Loading...'
                      : `${progressPercentage.toFixed(1)}% Complete`}
                  </p>
                  {hasActiveAssessment && (
                    <div className="w-full bg-gray-200 rounded-full h-2 mt-2">
                      <div
                        className="bg-green-600 h-2 rounded-full transition-all duration-300"
                        style={{ width: `${progressPercentage}%` }}
                      ></div>
                    </div>
                  )}
                </div>
              </div>
            </div>

            <div className="card">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <ClockIcon className="h-8 w-8 text-blue-600" />
                </div>
                <div className="ml-4">
                  <h3 className="text-lg font-semibold text-gray-900">Time Remaining</h3>
                  <p className="text-gray-600">
                    {assessmentLoading ? 'Loading...' : timeRemaining}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="card">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">
              {hasActiveAssessment ? 'Your Assessment Progress' : 'About Your Assessment'}
            </h3>
            <p className="text-gray-600 mb-4">
              {hasActiveAssessment
                ? `You have completed ${progressPercentage.toFixed(1)}% of your security posture assessment. Continue where you left off to receive personalized recommendations and an AI-enhanced report.`
                : 'Complete your comprehensive security posture assessment to receive personalized recommendations and an AI-enhanced report for your organization.'}
            </p>
            <Link href="/assessment/questions" className="btn-primary inline-flex items-center">
              {hasActiveAssessment ? 'Continue Assessment' : 'Get Started'}
              <ArrowRightIcon className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </Layout>
    </ProtectedRoute>
  );
}

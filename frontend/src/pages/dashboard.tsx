import React from 'react';
import { useQuery } from 'react-query';
import Layout from '@/components/Layout';
import ProtectedRoute from '@/components/ProtectedRoute';
import { useAuth } from '@/lib/auth';
import Link from 'next/link';
import { 
  DocumentTextIcon, 
  ChartBarIcon,
  ClockIcon,
  ArrowRightIcon
} from '@heroicons/react/24/outline';

export default function Dashboard() {
  const { user } = useAuth();

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
                  <h3 className="text-lg font-semibold text-gray-900">Start Assessment</h3>
                  <p className="text-gray-600">Begin your security evaluation</p>
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
                  <p className="text-gray-600">0% Complete</p>
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
                  <p className="text-gray-600">15 days</p>
                </div>
              </div>
            </div>
          </div>

          <div className="card">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">About Your Assessment</h3>
            <p className="text-gray-600 mb-4">
              Complete your comprehensive security posture assessment to receive personalized 
              recommendations and an AI-enhanced report for your organization.
            </p>
            <Link 
              href="/assessment/questions"
              className="btn-primary inline-flex items-center"
            >
              Get Started
              <ArrowRightIcon className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </Layout>
    </ProtectedRoute>
  );
}

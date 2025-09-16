import { useQuery } from 'react-query';
import Layout from '@/components/Layout';
import ProtectedRoute from '@/components/ProtectedRoute';
import { adminAPI } from '@/lib/api';
import { 
  UserIcon, 
  DocumentTextIcon, 
  ChartBarIcon,
  ExclamationTriangleIcon,
  TrendingUpIcon,
  ClockIcon
} from '@heroicons/react/24/outline';
import Link from 'next/link';

export default function AdminDashboard() {
  const { data: stats, isLoading: statsLoading } = useQuery(
    'dashboardStats',
    adminAPI.getDashboardStats,
    {
      refetchInterval: 30000, // Refetch every 30 seconds
    }
  );

  const { data: alerts, isLoading: alertsLoading } = useQuery(
    'adminAlerts',
    adminAPI.getAlerts,
    {
      refetchInterval: 60000, // Refetch every minute
    }
  );

  const formatNumber = (num: number) => {
    return new Intl.NumberFormat().format(num);
  };

  return (
    <ProtectedRoute adminOnly>
      <Layout title="Admin Dashboard">
        <div className="max-w-7xl mx-auto">
          {/* Welcome Section */}
          <div className="mb-8">
            <h2 className="text-2xl font-bold text-gray-900 mb-2">
              Admin Dashboard
            </h2>
            <p className="text-gray-600">
              Monitor user activity, assessment progress, and system performance
            </p>
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <div className="card">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <UserIcon className="h-8 w-8 text-blue-600" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">Total Users</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {statsLoading ? '...' : formatNumber(stats?.data?.total_users || 0)}
                  </p>
                </div>
              </div>
            </div>

            <div className="card">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <DocumentTextIcon className="h-8 w-8 text-green-600" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">Active Assessments</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {statsLoading ? '...' : formatNumber(stats?.data?.active_assessments || 0)}
                  </p>
                </div>
              </div>
            </div>

            <div className="card">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <ChartBarIcon className="h-8 w-8 text-purple-600" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">Completed</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {statsLoading ? '...' : formatNumber(stats?.data?.completed_assessments || 0)}
                  </p>
                </div>
              </div>
            </div>

            <div className="card">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <TrendingUpIcon className="h-8 w-8 text-indigo-600" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">New This Week</p>
                  <p className="text-2xl font-bold text-gray-900">
                    {statsLoading ? '...' : formatNumber(stats?.data?.new_users_this_week || 0)}
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Alerts Section */}
          {!alertsLoading && alerts?.data?.alerts?.length > 0 && (
            <div className="mb-8">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">System Alerts</h3>
              <div className="space-y-4">
                {alerts.data.alerts.map((alert: any, index: number) => (
                  <div 
                    key={index}
                    className={`p-4 rounded-lg border-l-4 ${
                      alert.type === 'warning' 
                        ? 'bg-yellow-50 border-yellow-400' 
                        : 'bg-blue-50 border-blue-400'
                    }`}
                  >
                    <div className="flex items-center">
                      <ExclamationTriangleIcon 
                        className={`h-5 w-5 mr-3 ${
                          alert.type === 'warning' ? 'text-yellow-600' : 'text-blue-600'
                        }`} 
                      />
                      <div>
                        <h4 className={`font-semibold ${
                          alert.type === 'warning' ? 'text-yellow-800' : 'text-blue-800'
                        }`}>
                          {alert.title}
                        </h4>
                        <p className={`text-sm ${
                          alert.type === 'warning' ? 'text-yellow-700' : 'text-blue-700'
                        }`}>
                          {alert.message}
                        </p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Additional Stats */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
            <div className="card">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">Assessment Metrics</h3>
              <div className="space-y-4">
                <div className="flex justify-between items-center">
                  <span className="text-gray-600">Expired Assessments</span>
                  <span className="font-semibold text-red-600">
                    {statsLoading ? '...' : formatNumber(stats?.data?.expired_assessments || 0)}
                  </span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-600">Stuck Assessments (7+ days)</span>
                  <span className="font-semibold text-orange-600">
                    {statsLoading ? '...' : formatNumber(stats?.data?.stuck_assessments || 0)}
                  </span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-600">Average Completion Time</span>
                  <span className="font-semibold text-gray-900">
                    {statsLoading ? '...' : `${stats?.data?.average_completion_hours || 0}h`}
                  </span>
                </div>
              </div>
            </div>

            <div className="card">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h3>
              <div className="space-y-3">
                <Link 
                  href="/admin/users"
                  className="flex items-center p-3 rounded-lg border border-gray-200 hover:bg-gray-50 transition-colors"
                >
                  <UserIcon className="h-6 w-6 text-primary-600 mr-3" />
                  <span>Manage Users</span>
                </Link>
                <Link 
                  href="/admin/assessments"
                  className="flex items-center p-3 rounded-lg border border-gray-200 hover:bg-gray-50 transition-colors"
                >
                  <DocumentTextIcon className="h-6 w-6 text-primary-600 mr-3" />
                  <span>View Assessments</span>
                </Link>
                <Link 
                  href="/admin/reports"
                  className="flex items-center p-3 rounded-lg border border-gray-200 hover:bg-gray-50 transition-colors"
                >
                  <ChartBarIcon className="h-6 w-6 text-primary-600 mr-3" />
                  <span>Manage Reports</span>
                </Link>
              </div>
            </div>
          </div>

          {/* Recent Activity */}
          <div className="card">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">System Status</h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="text-center">
                <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-2">
                  <div className="w-3 h-3 bg-green-600 rounded-full"></div>
                </div>
                <p className="text-sm font-medium text-gray-900">API Status</p>
                <p className="text-xs text-green-600">Operational</p>
              </div>
              <div className="text-center">
                <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-2">
                  <div className="w-3 h-3 bg-green-600 rounded-full"></div>
                </div>
                <p className="text-sm font-medium text-gray-900">Database</p>
                <p className="text-xs text-green-600">Connected</p>
              </div>
              <div className="text-center">
                <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-2">
                  <div className="w-3 h-3 bg-green-600 rounded-full"></div>
                </div>
                <p className="text-sm font-medium text-gray-900">AI Service</p>
                <p className="text-xs text-green-600">Available</p>
              </div>
            </div>
          </div>
        </div>
      </Layout>
    </ProtectedRoute>
  );
}

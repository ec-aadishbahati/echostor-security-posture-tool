import axios, { InternalAxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';
import Cookies from 'js-cookie';
import axiosRetry, { isNetworkError, isRetryableError } from 'axios-retry';

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || 'https://echostor-security-posture-tool.fly.dev';

const pendingRequests = new Map<string, Promise<any>>();

function generateRequestKey(config: InternalAxiosRequestConfig): string {
  const { method, url, params, data } = config;
  return `${method}:${url}:${JSON.stringify(params)}:${JSON.stringify(data)}`;
}

function addPendingRequest(config: InternalAxiosRequestConfig, promise: Promise<any>) {
  const key = generateRequestKey(config);
  pendingRequests.set(key, promise);
  promise.finally(() => pendingRequests.delete(key));
}

function getPendingRequest(config: InternalAxiosRequestConfig): Promise<any> | undefined {
  const key = generateRequestKey(config);
  return pendingRequests.get(key);
}

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

axiosRetry(api, {
  retries: 3,
  retryDelay: (retryCount: number) => axiosRetry.exponentialDelay(retryCount, undefined, 500),
  retryCondition: (error: AxiosError) => isNetworkError(error) || isRetryableError(error),
  shouldResetTimeout: true,
});

api.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  const pendingRequest = getPendingRequest(config);
  if (pendingRequest) {
    return Promise.reject({ _isDuplicate: true, promise: pendingRequest });
  }

  const token = Cookies.get('access_token');
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response: AxiosResponse) => {
    if (response.config) {
      addPendingRequest(response.config as InternalAxiosRequestConfig, Promise.resolve(response));
    }
    return response;
  },
  (error: AxiosError | any) => {
    if (error._isDuplicate) {
      return error.promise;
    }

    if (error.response?.status === 401) {
      Cookies.remove('access_token');
      window.location.href = '/auth/login';
    }

    if (error.config) {
      addPendingRequest(error.config, Promise.reject(error));
    }

    return Promise.reject(error);
  }
);

export default api;

export const authAPI = {
  register: (data: { email: string; password: string; full_name: string; company_name: string }) =>
    api.post('/api/auth/register', data),

  login: (data: { email: string; password: string }) => api.post('/api/auth/login', data),

  getCurrentUser: () => api.get('/api/auth/me'),
};

export const assessmentAPI = {
  getStructure: () => api.get('/api/assessment/structure'),

  startAssessment: () => api.post('/api/assessment/start'),

  getCurrentAssessment: () => api.get('/api/assessment/current'),

  getLatestAssessment: () => api.get('/api/assessment/latest'),

  getResponses: (assessmentId: string) => api.get(`/api/assessment/${assessmentId}/responses`),

  saveProgress: (assessmentId: string, responses: Record<string, any>[]) =>
    api.post(`/api/assessment/${assessmentId}/save-progress`, { responses }),

  completeAssessment: (assessmentId: string) =>
    api.post(`/api/assessment/${assessmentId}/complete`),

  saveConsultationInterest: (
    assessmentId: string,
    consultationData: { consultation_interest: boolean; consultation_details?: string }
  ) => api.post(`/api/assessment/${assessmentId}/consultation`, consultationData),
};

export const reportsAPI = {
  generateReport: (assessmentId: string) => api.post(`/api/reports/${assessmentId}/generate`),

  requestAIReport: (assessmentId: string, message?: string) =>
    api.post(`/api/reports/${assessmentId}/request-ai-report`, { message }),

  getUserReports: (params?: { skip?: number; limit?: number }) =>
    api.get('/api/reports/user/reports', { params }),

  getReportStatus: (reportId: string) => api.get(`/api/reports/${reportId}/status`),

  downloadReport: (reportId: string) =>
    api.get(`/api/reports/${reportId}/download`, { responseType: 'blob' }),
};

export const adminAPI = {
  getUsers: (params?: { skip?: number; limit?: number; search?: string }) =>
    api.get('/api/admin/users', { params }),

  getUser: (userId: string) => api.get(`/api/admin/users/${userId}`),

  getUserAssessments: (userId: string) => api.get(`/api/admin/users/${userId}/assessments`),

  getAssessments: (params?: { skip?: number; limit?: number; status?: string }) =>
    api.get('/api/admin/assessments', { params }),

  getDashboardStats: () => api.get('/api/admin/dashboard/stats'),

  getReports: (params?: { skip?: number; limit?: number; report_type?: string; status?: string }) =>
    api.get('/api/admin/reports', { params }),

  getAlerts: () => api.get('/api/admin/alerts'),
  getUsersProgressSummary: () => api.get('/api/admin/users-progress-summary'),
  generateAIReport: (reportId: string) => api.post(`/api/reports/admin/${reportId}/generate-ai`),
  releaseAIReport: (reportId: string) => api.post(`/api/reports/admin/${reportId}/release`),
  retryStandardReport: (reportId: string) =>
    api.post(`/api/reports/admin/${reportId}/retry-standard`),
  deleteUser: (userId: string) => api.delete(`/api/admin/users/${userId}`),
  resetUserPassword: (userId: string, newPassword: string) =>
    api.post(`/api/admin/users/${userId}/reset-password`, { new_password: newPassword }),
  bulkUpdateUserStatus: (userIds: string[], isActive: boolean) =>
    api.post('/api/admin/users/bulk-update-status', { user_ids: userIds, is_active: isActive }),
  bulkDeleteUsers: (userIds: string[]) =>
    api.post('/api/admin/users/bulk-delete', { user_ids: userIds }),

  getConsultationRequests: (skip = 0, limit = 100) => {
    const params = new URLSearchParams({
      skip: skip.toString(),
      limit: limit.toString(),
    });
    return api.get(`/api/admin/consultations?${params}`);
  },

  listOpenAIKeys: (includeInactive = false) =>
    api.get('/api/admin/openai-keys/', { params: { include_inactive: includeInactive } }),

  createOpenAIKey: (data: { key_name: string; api_key: string }) =>
    api.post('/api/admin/openai-keys/', data),

  testOpenAIKey: (apiKey: string) => api.post('/api/admin/openai-keys/test', { api_key: apiKey }),

  toggleOpenAIKey: (keyId: string, isActive: boolean) =>
    api.patch(`/api/admin/openai-keys/${keyId}/toggle`, { is_active: isActive }),

  deleteOpenAIKey: (keyId: string) => api.delete(`/api/admin/openai-keys/${keyId}`),
};

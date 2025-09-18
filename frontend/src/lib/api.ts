import axios, { InternalAxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';
import Cookies from 'js-cookie';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  const token = Cookies.get('access_token');
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response: AxiosResponse) => response,
  (error: AxiosError) => {
    if (error.response?.status === 401) {
      Cookies.remove('access_token');
      window.location.href = '/auth/login';
    }
    return Promise.reject(error);
  }
);

export default api;

export const authAPI = {
  register: (data: {
    email: string;
    password: string;
    full_name: string;
    company_name: string;
  }) => api.post('/api/auth/register', data),
  
  login: (data: { email: string; password: string }) =>
    api.post('/api/auth/login', data),
  
  getCurrentUser: () => api.get('/api/auth/me'),
};

export const assessmentAPI = {
  getStructure: () => api.get('/api/assessment/structure'),
  
  startAssessment: () => api.post('/api/assessment/start'),
  
  getCurrentAssessment: () => api.get('/api/assessment/current'),
  
  getResponses: (assessmentId: string) =>
    api.get(`/api/assessment/${assessmentId}/responses`),
  
  saveProgress: (assessmentId: string, responses: Record<string, any>[]) =>
    api.post(`/api/assessment/${assessmentId}/save-progress`, { responses }),
  
  completeAssessment: (assessmentId: string) =>
    api.post(`/api/assessment/${assessmentId}/complete`),
};

export const reportsAPI = {
  generateReport: (assessmentId: string) =>
    api.post(`/api/reports/${assessmentId}/generate`),
  
  requestAIReport: (assessmentId: string, message?: string) =>
    api.post(`/api/reports/${assessmentId}/request-ai-report`, { message }),
  
  getUserReports: () => api.get('/api/reports/user/reports'),
  
  getReportStatus: (reportId: string) =>
    api.get(`/api/reports/${reportId}/status`),
  
  downloadReport: (reportId: string) =>
    api.get(`/api/reports/${reportId}/download`, { responseType: 'blob' }),
};

export const adminAPI = {
  getUsers: (params?: { skip?: number; limit?: number; search?: string }) =>
    api.get('/api/admin/users', { params }),
  
  getUser: (userId: string) => api.get(`/api/admin/users/${userId}`),
  
  getUserAssessments: (userId: string) =>
    api.get(`/api/admin/users/${userId}/assessments`),
  
  getAssessments: (params?: { skip?: number; limit?: number; status?: string }) =>
    api.get('/api/admin/assessments', { params }),
  
  getDashboardStats: () => api.get('/api/admin/dashboard/stats'),
  
  getReports: (params?: { skip?: number; limit?: number; report_type?: string; status?: string }) =>
    api.get('/api/admin/reports', { params }),
  
  getAlerts: () => api.get('/api/admin/alerts'),
  getUsersProgressSummary: () => api.get('/api/admin/users-progress-summary'),
  generateAIReport: (reportId: string) =>
    api.post(`/api/reports/admin/${reportId}/generate-ai`),
  releaseAIReport: (reportId: string) =>
    api.post(`/api/reports/admin/${reportId}/release`),
};

import { useState, useEffect, createContext, useContext, ReactNode } from 'react';
import Cookies from 'js-cookie';
import { authAPI } from './api';

interface User {
  id: string;
  email: string;
  full_name: string;
  company_name: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

interface AuthContextType {
  user: User | null;
  isLoading: boolean;
  isAdmin: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (data: {
    email: string;
    password: string;
    full_name: string;
    company_name: string;
  }) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(() => {
    const token = Cookies.get('access_token');
    const adminFlag = Cookies.get('is_admin');
    
    if (token) {
      if (adminFlag === 'true') {
        setIsAdmin(true);
        setIsLoading(false);
      } else {
        authAPI
          .getCurrentUser()
          .then((response) => {
            setUser(response.data);
            setIsLoading(false);
          })
          .catch(() => {
            Cookies.remove('access_token');
            setIsLoading(false);
          });
      }
    } else {
      setIsLoading(false);
    }
  }, []);

  const login = async (email: string, password: string) => {
    const response = await authAPI.login({ email, password });
    const { access_token, user: userData } = response.data;
    
    Cookies.set('access_token', access_token, { expires: 1 }); // 1 day
    
    try {
      const tokenPayload = JSON.parse(atob(access_token.split('.')[1]));
      if (tokenPayload.is_admin) {
        setIsAdmin(true);
        Cookies.set('is_admin', 'true', { expires: 1 });
      } else if (userData && userData.is_admin) {
        setIsAdmin(true);
        Cookies.set('is_admin', 'true', { expires: 1 });
        setUser(userData);
      } else {
        setUser(userData);
        setIsAdmin(false);
      }
    } catch (error) {
      if (userData && userData.is_admin) {
        setIsAdmin(true);
        Cookies.set('is_admin', 'true', { expires: 1 });
      }
      setUser(userData);
      setIsAdmin(false);
    }
    
    return response.data;
  };

  const register = async (data: {
    email: string;
    password: string;
    full_name: string;
    company_name: string;
  }) => {
    const response = await authAPI.register(data);
    const { access_token, user: userData } = response.data;
    
    Cookies.set('access_token', access_token, { expires: 1 });
    setUser(userData);
  };

  const logout = () => {
    Cookies.remove('access_token');
    Cookies.remove('is_admin');
    setUser(null);
    setIsAdmin(false);
    window.location.href = '/';
  };

  const contextValue: AuthContextType = {
    user,
    isLoading,
    isAdmin,
    login,
    register,
    logout,
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

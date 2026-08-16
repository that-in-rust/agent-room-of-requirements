# MERN + TypeScript Idiomatic Pattern Library

**Purpose**: Comprehensive reference document for LLM-assisted MERN stack development with TypeScript best practices.

**Last Updated**: 2024-12-06
**Version**: 1.0

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure Patterns](#project-structure-patterns)
3. [TypeScript Essentials](#typescript-essentials)
4. [React Patterns](#react-patterns)
5. [Node.js/Express Patterns](#nodejs-express-patterns)
6. [Database Integration Patterns](#database-integration-patterns)
7. [Integration Patterns](#integration-patterns)
8. [Testing Patterns](#testing-patterns)
9. [Security & Authentication](#security--authentication)
10. [Performance Patterns](#performance-patterns)
11. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## Getting Started

### Prerequisites Pattern

```typescript
// package.json scripts
{
  "scripts": {
    "dev": "concurrently \"npm run server:dev\" \"npm run client:dev\"",
    "server:dev": "cd server && npm run dev",
    "client:dev": "cd client && npm run dev",
    "build": "npm run client:build && npm run server:build",
    "test": "npm run client:test && npm run server:test",
    "lint": "npm run client:lint && npm run server:lint",
    "type-check": "npm run client:type-check && npm run server:type-check"
  }
}
```

### Environment Configuration Pattern

```typescript
// shared/types/environment.ts
export interface EnvConfig {
  PORT: number;
  NODE_ENV: 'development' | 'production' | 'test';
  MONGODB_URI: string;
  JWT_SECRET: string;
  JWT_EXPIRE: string;
  CORS_ORIGIN: string;
}

// server/config/database.ts
import mongoose from 'mongoose';
import { EnvConfig } from '../../shared/types/environment';

export const connectDatabase = async (config: EnvConfig): Promise<void> => {
  try {
    await mongoose.connect(config.MONGODB_URI);
    console.log('MongoDB connected successfully');
  } catch (error) {
    console.error('MongoDB connection failed:', error);
    process.exit(1);
  }
};
```

---

## Project Structure Patterns

### Monorepo Structure (Recommended)

```
mern-project/
├── shared/                 # Shared types and utilities
│   ├── types/             # TypeScript interfaces
│   ├── utils/             # Shared utility functions
│   ├── constants/         # Application constants
│   └── validations/       # Shared validation schemas
├── client/                # React frontend
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── hooks/         # Custom React hooks
│   │   ├── services/      # API service layer
│   │   ├── store/         # State management
│   │   ├── types/         # Client-specific types
│   │   └── utils/         # Client utilities
│   ├── public/
│   └── package.json
├── server/                # Node.js backend
│   ├── src/
│   │   ├── controllers/   # Route handlers
│   │   ├── middleware/    # Express middleware
│   │   ├── models/        # Mongoose models
│   │   ├── routes/        # API routes
│   │   ├── services/      # Business logic
│   │   ├── utils/         # Server utilities
│   │   └── types/         # Server-specific types
│   └── package.json
├── docs/                  # Documentation
├── docker-compose.yml     # Development environment
└── package.json           # Root package.json
```

### Module Organization Patterns

#### Feature-Based Organization

```typescript
// Example: User feature organization
src/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   └── index.ts
│   ├── products/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   └── index.ts
│   └── users/
│       ├── components/
│       ├── hooks/
│       ├── services/
│       ├── types/
│       └── index.ts
└── shared/
    ├── components/
    ├── hooks/
    ├── utils/
    └── types/
```

---

## TypeScript Essentials

### Configuration Pattern

```json
// tsconfig.json (Root)
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    // Strict type checking
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,

    // Path mapping
    "baseUrl": ".",
    "paths": {
      "@shared/*": ["./shared/*"],
      "@client/*": ["./client/src/*"],
      "@server/*": ["./server/src/*"],
      "@/*": ["./src/*"]
    }
  },
  "include": ["shared", "client/src", "server/src"],
  "exclude": ["node_modules", "dist", "build"]
}
```

### Utility Types Pattern

```typescript
// shared/types/utility.ts

/**
 * Makes all properties of T optional recursively
 */
export type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

/**
 * Makes all properties of T required recursively
 */
export type DeepRequired<T> = {
  [P in keyof T]-?: T[P] extends object ? DeepRequired<T[P]> : T[P];
};

/**
 * Omits nested properties from type T
 */
export type OmitNested<T, K extends string> = {
  [P in keyof T as P extends K ? never : P]: T[P] extends object
    ? OmitNested<T[P], K>
    : T[P];
};

/**
 * Database entity with automatic timestamps and ID
 */
export interface BaseEntity {
  _id: string;
  createdAt: Date;
  updatedAt: Date;
}

/**
 * API response wrapper
 */
export interface ApiResponse<T = unknown> {
  success: boolean;
  data?: T;
  message?: string;
  errors?: string[];
  meta?: {
    page?: number;
    limit?: number;
    total?: number;
    totalPages?: number;
  };
}

/**
 * Pagination parameters
 */
export interface PaginationParams {
  page?: number;
  limit?: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
}
```

### Type-safe API Patterns

```typescript
// shared/types/api.ts
import { ApiResponse, PaginationParams } from './utility';

export interface User {
  _id: string;
  email: string;
  name: string;
  role: 'user' | 'admin';
  isActive: boolean;
  createdAt: Date;
  updatedAt: Date;
}

export interface CreateUserDto {
  email: string;
  name: string;
  password: string;
}

export interface UpdateUserDto {
  name?: string;
  role?: 'user' | 'admin';
  isActive?: boolean;
}

export interface LoginDto {
  email: string;
  password: string;
}

export interface AuthResponse {
  user: Omit<User, 'password'>;
  token: string;
  refreshToken: string;
}

// API endpoint types
export type ApiEndpoints = {
  'POST /api/auth/register': {
    body: CreateUserDto;
    response: ApiResponse<AuthResponse>;
  };
  'POST /api/auth/login': {
    body: LoginDto;
    response: ApiResponse<AuthResponse>;
  };
  'GET /api/users': {
    query: PaginationParams & { search?: string; role?: string };
    response: ApiResponse<User[]>;
  };
  'GET /api/users/:id': {
    params: { id: string };
    response: ApiResponse<User>;
  };
  'PUT /api/users/:id': {
    params: { id: string };
    body: UpdateUserDto;
    response: ApiResponse<User>;
  };
  'DELETE /api/users/:id': {
    params: { id: string };
    response: ApiResponse<null>;
  };
};
```

---

## React Patterns

### Component Patterns

#### Functional Component with TypeScript

```typescript
// client/src/components/common/Button.tsx
import React, { ButtonHTMLAttributes, ReactNode } from 'react';

interface ButtonProps extends Omit<ButtonHTMLAttributes<HTMLButtonElement>, 'type'> {
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  icon?: ReactNode;
  children: ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  loading = false,
  icon,
  children,
  disabled,
  className = '',
  ...props
}) => {
  const baseClasses = 'inline-flex items-center justify-center font-medium rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2';

  const variantClasses = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
    secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300 focus:ring-gray-500',
    danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
    ghost: 'text-gray-700 hover:bg-gray-100 focus:ring-gray-500'
  };

  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  };

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`}
      disabled={disabled || loading}
      {...props}
    >
      {loading && (
        <svg className="animate-spin -ml-1 mr-2 h-4 w-4" fill="none" viewBox="0 0 24 24">
          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
        </svg>
      )}
      {icon && !loading && <span className="mr-2">{icon}</span>}
      {children}
    </button>
  );
};
```

#### Custom Hook Pattern

```typescript
// client/src/hooks/useApi.ts
import { useState, useEffect, useCallback } from 'react';
import { ApiResponse } from '@shared/types/utility';

interface UseApiOptions<T> {
  immediate?: boolean;
  onSuccess?: (data: T) => void;
  onError?: (error: Error) => void;
}

interface UseApiReturn<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
  execute: () => Promise<void>;
  reset: () => void;
}

export function useApi<T>(
  apiCall: () => Promise<ApiResponse<T>>,
  options: UseApiOptions<T> = {}
): UseApiReturn<T> {
  const { immediate = false, onSuccess, onError } = options;

  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const execute = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await apiCall();

      if (response.success && response.data) {
        setData(response.data);
        onSuccess?.(response.data);
      } else {
        throw new Error(response.message || 'API request failed');
      }
    } catch (err) {
      const error = err instanceof Error ? err : new Error('Unknown error');
      setError(error);
      onError?.(error);
    } finally {
      setLoading(false);
    }
  }, [apiCall, onSuccess, onError]);

  const reset = useCallback(() => {
    setData(null);
    setError(null);
    setLoading(false);
  }, []);

  useEffect(() => {
    if (immediate) {
      execute();
    }
  }, [immediate, execute]);

  return { data, loading, error, execute, reset };
}
```

#### Form Handling Pattern

```typescript
// client/src/hooks/useForm.ts
import { useState, useCallback } from 'react';

interface FormState<T> {
  values: T;
  errors: Partial<Record<keyof T, string>>;
  touched: Partial<Record<keyof T, boolean>>;
  isValid: boolean;
  isSubmitting: boolean;
}

interface UseFormOptions<T> {
  initialValues: T;
  validate?: (values: T) => Partial<Record<keyof T, string>>;
  onSubmit: (values: T) => Promise<void> | void;
}

export function useForm<T extends Record<string, any>>({
  initialValues,
  validate,
  onSubmit
}: UseFormOptions<T>) {
  const [formState, setFormState] = useState<FormState<T>>({
    values: initialValues,
    errors: {},
    touched: {},
    isValid: false,
    isSubmitting: false
  });

  const setValue = useCallback((name: keyof T, value: any) => {
    setFormState(prev => {
      const newValues = { ...prev.values, [name]: value };
      const errors = validate ? validate(newValues) : {};
      const isValid = Object.keys(errors).length === 0;

      return {
        ...prev,
        values: newValues,
        errors,
        isValid
      };
    });
  }, [validate]);

  const setTouched = useCallback((name: keyof T) => {
    setFormState(prev => ({
      ...prev,
      touched: { ...prev.touched, [name]: true }
    }));
  }, []);

  const handleChange = useCallback((name: keyof T) => (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    setValue(name, e.target.value);
  }, [setValue]);

  const handleBlur = useCallback((name: keyof T) => () => {
    setTouched(name);
  }, [setTouched]);

  const handleSubmit = useCallback(async (e: React.FormEvent) => {
    e.preventDefault();

    const errors = validate ? validate(formState.values) : {};

    if (Object.keys(errors).length > 0) {
      setFormState(prev => ({ ...prev, errors, touched: Object.keys(prev.values) as Array<keyof T> }));
      return;
    }

    setFormState(prev => ({ ...prev, isSubmitting: true }));

    try {
      await onSubmit(formState.values);
    } finally {
      setFormState(prev => ({ ...prev, isSubmitting: false }));
    }
  }, [formState.values, validate, onSubmit]);

  const reset = useCallback(() => {
    setFormState({
      values: initialValues,
      errors: {},
      touched: {},
      isValid: false,
      isSubmitting: false
    });
  }, [initialValues]);

  return {
    ...formState,
    setValue,
    setTouched,
    handleChange,
    handleBlur,
    handleSubmit,
    reset
  };
}
```

### State Management Pattern

```typescript
// client/src/store/index.ts
import { configureStore } from '@reduxjs/toolkit';
import { useDispatch, useSelector, TypedUseSelectorHook } from 'react-redux';
import authSlice from './slices/authSlice';
import uiSlice from './slices/uiSlice';

export const store = configureStore({
  reducer: {
    auth: authSlice,
    ui: uiSlice,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST'],
      },
    }),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// Typed hooks
export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;

// client/src/store/slices/authSlice.ts
import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import { User, LoginDto, CreateUserDto } from '@shared/types/api';
import { authService } from '@/services/authService';

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  loading: boolean;
  error: string | null;
}

const initialState: AuthState = {
  user: null,
  token: localStorage.getItem('token'),
  isAuthenticated: false,
  loading: false,
  error: null,
};

export const login = createAsyncThunk(
  'auth/login',
  async (credentials: LoginDto, { rejectWithValue }) => {
    try {
      const response = await authService.login(credentials);
      localStorage.setItem('token', response.token);
      return response;
    } catch (error) {
      return rejectWithValue(error instanceof Error ? error.message : 'Login failed');
    }
  }
);

export const register = createAsyncThunk(
  'auth/register',
  async (userData: CreateUserDto, { rejectWithValue }) => {
    try {
      const response = await authService.register(userData);
      localStorage.setItem('token', response.token);
      return response;
    } catch (error) {
      return rejectWithValue(error instanceof Error ? error.message : 'Registration failed');
    }
  }
);

export const logout = createAsyncThunk(
  'auth/logout',
  async (_, { dispatch }) => {
    localStorage.removeItem('token');
    dispatch(clearAuth());
  }
);

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    clearAuth: (state) => {
      state.user = null;
      state.token = null;
      state.isAuthenticated = false;
      state.error = null;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    builder
      // Login
      .addCase(login.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload.user;
        state.token = action.payload.token;
        state.isAuthenticated = true;
      })
      .addCase(login.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      // Register
      .addCase(register.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(register.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload.user;
        state.token = action.payload.token;
        state.isAuthenticated = true;
      })
      .addCase(register.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  },
});

export const { clearAuth, clearError } = authSlice.actions;
export default authSlice.reducer;
```

---

## Node.js/Express Patterns

### Express Setup Pattern

```typescript
// server/src/app.ts
import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import compression from 'compression';
import morgan from 'morgan';
import cookieParser from 'cookie-parser';
import { Express } from 'express';
import { errorHandler } from './middleware/errorHandler';
import { notFoundHandler } from './middleware/notFoundHandler';
import { rateLimitMiddleware } from './middleware/rateLimit';
import { EnvConfig } from '@shared/types/environment';

export const createApp = (config: EnvConfig): Express => {
  const app = express();

  // Security middleware
  app.use(helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        scriptSrc: ["'self'"],
        imgSrc: ["'self'", "data:", "https:"],
      },
    },
  }));

  // CORS configuration
  app.use(cors({
    origin: config.CORS_ORIGIN,
    credentials: true,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization'],
  }));

  // General middleware
  app.use(compression());
  app.use(morgan('combined'));
  app.use(express.json({ limit: '10mb' }));
  app.use(express.urlencoded({ extended: true, limit: '10mb' }));
  app.use(cookieParser());

  // Rate limiting
  app.use(rateLimitMiddleware);

  // Health check endpoint
  app.get('/health', (req, res) => {
    res.json({
      status: 'OK',
      timestamp: new Date().toISOString(),
      uptime: process.uptime(),
      environment: config.NODE_ENV,
    });
  });

  // API routes will be mounted here
  // app.use('/api/v1', routes);

  // Error handling middleware (must be last)
  app.use(notFoundHandler);
  app.use(errorHandler);

  return app;
};
```

### Middleware Patterns

#### Error Handling Middleware

```typescript
// server/src/middleware/errorHandler.ts
import { Request, Response, NextFunction } from 'express';
import { logger } from '../utils/logger';

export interface AppError extends Error {
  statusCode?: number;
  isOperational?: boolean;
}

export const errorHandler = (
  error: AppError,
  req: Request,
  res: Response,
  next: NextFunction
): void => {
  let { statusCode = 500, message } = error;

  // Log error for debugging
  logger.error({
    error: {
      message: error.message,
      stack: error.stack,
      statusCode,
      url: req.url,
      method: req.method,
      ip: req.ip,
      userAgent: req.get('User-Agent'),
    },
  });

  // Handle specific error types
  if (error.name === 'ValidationError') {
    statusCode = 400;
    message = 'Validation Error';
  } else if (error.name === 'CastError') {
    statusCode = 400;
    message = 'Invalid ID format';
  } else if (error.code === 11000) {
    statusCode = 409;
    message = 'Duplicate field value';
  }

  // Don't leak error details in production
  const response = {
    success: false,
    message: process.env.NODE_ENV === 'production' ? 'Internal Server Error' : message,
    ...(process.env.NODE_ENV !== 'production' && { stack: error.stack }),
  };

  res.status(statusCode).json(response);
};

export const notFoundHandler = (req: Request, res: Response): void => {
  res.status(404).json({
    success: false,
    message: `Route ${req.originalUrl} not found`,
  });
};
```

#### Authentication Middleware

```typescript
// server/src/middleware/auth.ts
import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import { User } from '../models/User';
import { EnvConfig } from '@shared/types/environment';

interface AuthRequest extends Request {
  user?: any;
}

export const authenticate = async (
  req: AuthRequest,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    const token = req.header('Authorization')?.replace('Bearer ', '');

    if (!token) {
      res.status(401).json({ success: false, message: 'Access denied. No token provided.' });
      return;
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET!) as any;
    const user = await User.findById(decoded.id).select('-password');

    if (!user) {
      res.status(401).json({ success: false, message: 'Invalid token.' });
      return;
    }

    req.user = user;
    next();
  } catch (error) {
    res.status(401).json({ success: false, message: 'Invalid token.' });
  }
};

export const authorize = (...roles: string[]) => {
  return (req: AuthRequest, res: Response, next: NextFunction): void => {
    if (!req.user) {
      res.status(401).json({ success: false, message: 'Access denied. User not authenticated.' });
      return;
    }

    if (!roles.includes(req.user.role)) {
      res.status(403).json({
        success: false,
        message: 'Access denied. Insufficient permissions.'
      });
      return;
    }

    next();
  };
};
```

#### Validation Middleware

```typescript
// server/src/middleware/validation.ts
import { Request, Response, NextFunction } from 'express';
import { Schema, ValidationError } from 'yup';

export const validateRequest = (schema: Schema) => {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      await schema.validate({
        body: req.body,
        query: req.query,
        params: req.params,
      }, { abortEarly: false });

      next();
    } catch (error) {
      if (error instanceof ValidationError) {
        const errors = error.inner.map(err => ({
          field: err.path,
          message: err.message,
        }));

        res.status(400).json({
          success: false,
          message: 'Validation failed',
          errors,
        });
      } else {
        next(error);
      }
    }
  };
};
```

### Controller Pattern

```typescript
// server/src/controllers/userController.ts
import { Request, Response, NextFunction } from 'express';
import { UserService } from '../services/userService';
import { ApiResponse, PaginationParams } from '@shared/types/utility';
import { CreateUserDto, UpdateUserDto } from '@shared/types/api';

export class UserController {
  constructor(private userService: UserService) {}

  async getUsers(
    req: Request<{}, {}, {}, PaginationParams & { search?: string; role?: string }>,
    res: Response,
    next: NextFunction
  ): Promise<void> {
    try {
      const { page = 1, limit = 10, search, role } = req.query;

      const result = await this.userService.getUsers({
        page: Number(page),
        limit: Number(limit),
        search,
        role,
      });

      const response: ApiResponse = {
        success: true,
        data: result.users,
        meta: {
          page: result.page,
          limit: result.limit,
          total: result.total,
          totalPages: result.totalPages,
        },
      };

      res.json(response);
    } catch (error) {
      next(error);
    }
  }

  async getUserById(
    req: Request<{ id: string }>,
    res: Response,
    next: NextFunction
  ): Promise<void> {
    try {
      const { id } = req.params;
      const user = await this.userService.getUserById(id);

      if (!user) {
        res.status(404).json({
          success: false,
          message: 'User not found',
        });
        return;
      }

      const response: ApiResponse = {
        success: true,
        data: user,
      };

      res.json(response);
    } catch (error) {
      next(error);
    }
  }

  async createUser(
    req: Request<{}, {}, CreateUserDto>,
    res: Response,
    next: NextFunction
  ): Promise<void> {
    try {
      const userData = req.body;
      const user = await this.userService.createUser(userData);

      const response: ApiResponse = {
        success: true,
        data: user,
        message: 'User created successfully',
      };

      res.status(201).json(response);
    } catch (error) {
      next(error);
    }
  }

  async updateUser(
    req: Request<{ id: string }, {}, UpdateUserDto>,
    res: Response,
    next: NextFunction
  ): Promise<void> {
    try {
      const { id } = req.params;
      const updateData = req.body;

      const user = await this.userService.updateUser(id, updateData);

      if (!user) {
        res.status(404).json({
          success: false,
          message: 'User not found',
        });
        return;
      }

      const response: ApiResponse = {
        success: true,
        data: user,
        message: 'User updated successfully',
      };

      res.json(response);
    } catch (error) {
      next(error);
    }
  }

  async deleteUser(
    req: Request<{ id: string }>,
    res: Response,
    next: NextFunction
  ): Promise<void> {
    try {
      const { id } = req.params;

      const success = await this.userService.deleteUser(id);

      if (!success) {
        res.status(404).json({
          success: false,
          message: 'User not found',
        });
        return;
      }

      const response: ApiResponse = {
        success: true,
        data: null,
        message: 'User deleted successfully',
      };

      res.json(response);
    } catch (error) {
      next(error);
    }
  }
}
```

### Service Pattern

```typescript
// server/src/services/userService.ts
import { User, IUser } from '../models/User';
import { CreateUserDto, UpdateUserDto } from '@shared/types/api';
import { PaginationParams } from '@shared/types/utility';

interface GetUsersParams extends PaginationParams {
  search?: string;
  role?: string;
}

interface GetUsersResult {
  users: IUser[];
  page: number;
  limit: number;
  total: number;
  totalPages: number;
}

export class UserService {
  async getUsers(params: GetUsersParams): Promise<GetUsersResult> {
    const { page, limit, search, role } = params;
    const skip = (page - 1) * limit;

    // Build query
    const query: any = {};

    if (role) {
      query.role = role;
    }

    if (search) {
      query.$or = [
        { name: { $regex: search, $options: 'i' } },
        { email: { $regex: search, $options: 'i' } },
      ];
    }

    // Execute queries in parallel
    const [users, total] = await Promise.all([
      User.find(query)
        .select('-password')
        .sort({ createdAt: -1 })
        .skip(skip)
        .limit(limit)
        .lean(),
      User.countDocuments(query),
    ]);

    return {
      users,
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit),
    };
  }

  async getUserById(id: string): Promise<IUser | null> {
    return User.findById(id).select('-password');
  }

  async createUser(userData: CreateUserDto): Promise<IUser> {
    const user = new User(userData);
    return user.save();
  }

  async updateUser(id: string, updateData: UpdateUserDto): Promise<IUser | null> {
    return User.findByIdAndUpdate(
      id,
      { ...updateData, updatedAt: new Date() },
      { new: true, runValidators: true }
    ).select('-password');
  }

  async deleteUser(id: string): Promise<boolean> {
    const result = await User.findByIdAndDelete(id);
    return !!result;
  }

  async getUserByEmail(email: string): Promise<IUser | null> {
    return User.findOne({ email });
  }
}
```

### Route Pattern

```typescript
// server/src/routes/userRoutes.ts
import { Router } from 'express';
import { UserController } from '../controllers/userController';
import { validateRequest } from '../middleware/validation';
import { authenticate, authorize } from '../middleware/auth';
import { userValidationSchemas } from '../validations/userValidation';
import { UserService } from '../services/userService';

const router = Router();
const userService = new UserService();
const userController = new UserController(userService);

// Apply authentication middleware to all routes
router.use(authenticate);

// GET /api/users
router.get(
  '/',
  authorize('admin'),
  validateRequest(userValidationSchemas.getUsers),
  userController.getUsers.bind(userController)
);

// GET /api/users/:id
router.get(
  '/:id',
  validateRequest(userValidationSchemas.getUserById),
  userController.getUserById.bind(userController)
);

// POST /api/users
router.post(
  '/',
  authorize('admin'),
  validateRequest(userValidationSchemas.createUser),
  userController.createUser.bind(userController)
);

// PUT /api/users/:id
router.put(
  '/:id',
  authorize('admin'),
  validateRequest(userValidationSchemas.updateUser),
  userController.updateUser.bind(userController)
);

// DELETE /api/users/:id
router.delete(
  '/:id',
  authorize('admin'),
  validateRequest(userValidationSchemas.deleteUser),
  userController.deleteUser.bind(userController)
);

export default router;
```

---

## Database Integration Patterns

### Mongoose Schema Patterns

```typescript
// server/src/models/User.ts
import mongoose, { Schema, Document } from 'mongoose';
import bcrypt from 'bcryptjs';

export interface IUser extends Document {
  name: string;
  email: string;
  password: string;
  role: 'user' | 'admin';
  isActive: boolean;
  emailVerified: boolean;
  emailVerificationToken?: string;
  passwordResetToken?: string;
  passwordResetExpires?: Date;
  lastLoginAt?: Date;
  createdAt: Date;
  updatedAt: Date;

  // Instance methods
  comparePassword(candidatePassword: string): Promise<boolean>;
  generateEmailVerificationToken(): string;
  generatePasswordResetToken(): string;
}

const userSchema = new Schema<IUser>({
  name: {
    type: String,
    required: [true, 'Name is required'],
    trim: true,
    maxlength: [50, 'Name cannot exceed 50 characters'],
  },
  email: {
    type: String,
    required: [true, 'Email is required'],
    unique: true,
    lowercase: true,
    trim: true,
    match: [/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/, 'Please enter a valid email'],
  },
  password: {
    type: String,
    required: [true, 'Password is required'],
    minlength: [6, 'Password must be at least 6 characters long'],
    select: false, // Don't include password in queries by default
  },
  role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user',
  },
  isActive: {
    type: Boolean,
    default: true,
  },
  emailVerified: {
    type: Boolean,
    default: false,
  },
  emailVerificationToken: String,
  passwordResetToken: String,
  passwordResetExpires: Date,
  lastLoginAt: Date,
}, {
  timestamps: true,
  toJSON: {
    transform: function(doc, ret) {
      delete ret.password;
      delete ret.emailVerificationToken;
      delete ret.passwordResetToken;
      delete ret.__v;
      return ret;
    },
  },
});

// Indexes
userSchema.index({ email: 1 });
userSchema.index({ createdAt: -1 });
userSchema.index({ role: 1, isActive: 1 });

// Pre-save middleware for password hashing
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();

  try {
    const salt = await bcrypt.genSalt(12);
    this.password = await bcrypt.hash(this.password, salt);
    next();
  } catch (error) {
    next(error);
  }
});

// Instance methods
userSchema.methods.comparePassword = async function(candidatePassword: string): Promise<boolean> {
  return bcrypt.compare(candidatePassword, this.password);
};

userSchema.methods.generateEmailVerificationToken = function(): string {
  const crypto = require('crypto');
  const token = crypto.randomBytes(32).toString('hex');
  this.emailVerificationToken = token;
  return token;
};

userSchema.methods.generatePasswordResetToken = function(): string {
  const crypto = require('crypto');
  const token = crypto.randomBytes(32).toString('hex');
  this.passwordResetToken = token;
  this.passwordResetExpires = new Date(Date.now() + 10 * 60 * 1000); // 10 minutes
  return token;
};

// Static methods
userSchema.statics.findByEmail = function(email: string) {
  return this.findOne({ email }).select('+password');
};

export const User = mongoose.model<IUser>('User', userSchema);
```

### Database Connection Pattern

```typescript
// server/src/config/database.ts
import mongoose from 'mongoose';
import { logger } from '../utils/logger';

export class DatabaseConnection {
  private static instance: DatabaseConnection;
  private isConnected = false;

  private constructor() {}

  public static getInstance(): DatabaseConnection {
    if (!DatabaseConnection.instance) {
      DatabaseConnection.instance = new DatabaseConnection();
    }
    return DatabaseConnection.instance;
  }

  public async connect(connectionString: string): Promise<void> {
    if (this.isConnected) {
      logger.info('Database already connected');
      return;
    }

    try {
      const options: mongoose.ConnectOptions = {
        maxPoolSize: 10, // Maintain up to 10 socket connections
        serverSelectionTimeoutMS: 5000, // Keep trying to send operations for 5 seconds
        socketTimeoutMS: 45000, // Close sockets after 45 seconds of inactivity
        bufferMaxEntries: 0, // Disable mongoose buffering
        bufferCommands: false, // Disable mongoose buffering
      };

      await mongoose.connect(connectionString, options);
      this.isConnected = true;

      logger.info('Connected to MongoDB');

      // Handle connection events
      mongoose.connection.on('error', (error) => {
        logger.error('MongoDB connection error:', error);
        this.isConnected = false;
      });

      mongoose.connection.on('disconnected', () => {
        logger.warn('MongoDB disconnected');
        this.isConnected = false;
      });

      mongoose.connection.on('reconnected', () => {
        logger.info('MongoDB reconnected');
        this.isConnected = true;
      });

    } catch (error) {
      logger.error('Failed to connect to MongoDB:', error);
      throw error;
    }
  }

  public async disconnect(): Promise<void> {
    if (!this.isConnected) {
      return;
    }

    try {
      await mongoose.disconnect();
      this.isConnected = false;
      logger.info('Disconnected from MongoDB');
    } catch (error) {
      logger.error('Error disconnecting from MongoDB:', error);
      throw error;
    }
  }

  public getConnectionStatus(): boolean {
    return this.isConnected;
  }

  public async healthCheck(): Promise<{ status: string; details?: any }> {
    try {
      if (!this.isConnected) {
        return { status: 'disconnected' };
      }

      const adminDb = mongoose.connection.db?.admin();
      const result = await adminDb?.ping();

      return {
        status: result?.ok === 1 ? 'healthy' : 'unhealthy',
        details: {
          readyState: mongoose.connection.readyState,
          host: mongoose.connection.host,
          port: mongoose.connection.port,
          name: mongoose.connection.name,
        },
      };
    } catch (error) {
      return {
        status: 'unhealthy',
        details: error instanceof Error ? error.message : 'Unknown error',
      };
    }
  }
}

export const database = DatabaseConnection.getInstance();
```

### Repository Pattern for Database Operations

```typescript
// server/src/repositories/baseRepository.ts
import { Document, Model, FilterQuery, UpdateQuery, QueryOptions } from 'mongoose';
import { PaginationParams, DeepPartial } from '@shared/types/utility';

interface PaginatedResult<T> {
  items: T[];
  total: number;
  page: number;
  limit: number;
  totalPages: number;
}

export abstract class BaseRepository<T extends Document> {
  constructor(protected model: Model<T>) {}

  async create(data: DeepPartial<T>): Promise<T> {
    return this.model.create(data);
  }

  async findById(id: string): Promise<T | null> {
    return this.model.findById(id);
  }

  async findOne(filter: FilterQuery<T>): Promise<T | null> {
    return this.model.findOne(filter);
  }

  async find(filter: FilterQuery<T> = {}): Promise<T[]> {
    return this.model.find(filter);
  }

  async findWithPagination(
    filter: FilterQuery<T> = {},
    pagination: PaginationParams
  ): Promise<PaginatedResult<T>> {
    const { page = 1, limit = 10, sortBy, sortOrder = 'asc' } = pagination;
    const skip = (page - 1) * limit;

    // Build sort object
    const sort: any = {};
    if (sortBy) {
      sort[sortBy] = sortOrder === 'desc' ? -1 : 1;
    } else {
      sort.createdAt = -1; // Default sort
    }

    const [items, total] = await Promise.all([
      this.model
        .find(filter)
        .sort(sort)
        .skip(skip)
        .limit(limit)
        .lean(),
      this.model.countDocuments(filter),
    ]);

    return {
      items,
      total,
      page,
      limit,
      totalPages: Math.ceil(total / limit),
    };
  }

  async update(id: string, data: UpdateQuery<T>): Promise<T | null> {
    return this.model.findByIdAndUpdate(id, data, { new: true, runValidators: true });
  }

  async updateOne(filter: FilterQuery<T>, data: UpdateQuery<T>): Promise<T | null> {
    return this.model.findOneAndUpdate(filter, data, { new: true, runValidators: true });
  }

  async updateMany(filter: FilterQuery<T>, data: UpdateQuery<T>): Promise<{ modifiedCount: number }> {
    const result = await this.model.updateMany(filter, data);
    return { modifiedCount: result.modifiedCount };
  }

  async delete(id: string): Promise<boolean> {
    const result = await this.model.findByIdAndDelete(id);
    return !!result;
  }

  async deleteOne(filter: FilterQuery<T>): Promise<boolean> {
    const result = await this.model.findOneAndDelete(filter);
    return !!result;
  }

  async deleteMany(filter: FilterQuery<T>): Promise<{ deletedCount: number }> {
    const result = await this.model.deleteMany(filter);
    return { deletedCount: result.deletedCount };
  }

  async exists(filter: FilterQuery<T>): Promise<boolean> {
    return this.model.exists(filter) !== null;
  }

  async count(filter: FilterQuery<T> = {}): Promise<number> {
    return this.model.countDocuments(filter);
  }
}
```

---

## Integration Patterns

### API Client Pattern

```typescript
// client/src/services/apiClient.ts
import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios';
import { ApiResponse } from '@shared/types/utility';

class ApiClient {
  private client: AxiosInstance;

  constructor(baseURL: string) {
    this.client = axios.create({
      baseURL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    this.setupInterceptors();
  }

  private setupInterceptors(): void {
    // Request interceptor
    this.client.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('token');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    // Response interceptor
    this.client.interceptors.response.use(
      (response: AxiosResponse<ApiResponse>) => response,
      async (error) => {
        const originalRequest = error.config;

        // Handle 401 errors
        if (error.response?.status === 401 && !originalRequest._retry) {
          originalRequest._retry = true;

          try {
            const refreshToken = localStorage.getItem('refreshToken');
            if (refreshToken) {
              const response = await axios.post('/api/auth/refresh', {
                refreshToken,
              });

              const { token } = response.data;
              localStorage.setItem('token', token);

              originalRequest.headers.Authorization = `Bearer ${token}`;
              return this.client(originalRequest);
            }
          } catch (refreshError) {
            // Refresh failed, logout user
            localStorage.removeItem('token');
            localStorage.removeItem('refreshToken');
            window.location.href = '/login';
          }
        }

        return Promise.reject(error);
      }
    );
  }

  public async get<T = any>(
    url: string,
    config?: AxiosRequestConfig
  ): Promise<ApiResponse<T>> {
    const response = await this.client.get<ApiResponse<T>>(url, config);
    return response.data;
  }

  public async post<T = any>(
    url: string,
    data?: any,
    config?: AxiosRequestConfig
  ): Promise<ApiResponse<T>> {
    const response = await this.client.post<ApiResponse<T>>(url, data, config);
    return response.data;
  }

  public async put<T = any>(
    url: string,
    data?: any,
    config?: AxiosRequestConfig
  ): Promise<ApiResponse<T>> {
    const response = await this.client.put<ApiResponse<T>>(url, data, config);
    return response.data;
  }

  public async patch<T = any>(
    url: string,
    data?: any,
    config?: AxiosRequestConfig
  ): Promise<ApiResponse<T>> {
    const response = await this.client.patch<ApiResponse<T>>(url, data, config);
    return response.data;
  }

  public async delete<T = any>(
    url: string,
    config?: AxiosRequestConfig
  ): Promise<ApiResponse<T>> {
    const response = await this.client.delete<ApiResponse<T>>(url, config);
    return response.data;
  }
}

export const apiClient = new ApiClient(process.env.REACT_APP_API_URL || '/api');
```

### Service Layer Pattern (Client Side)

```typescript
// client/src/services/userService.ts
import { apiClient } from './apiClient';
import { User, CreateUserDto, UpdateUserDto, PaginationParams } from '@shared/types/api';

export class UserService {
  async getUsers(params: PaginationParams & { search?: string; role?: string }) {
    return apiClient.get<User[]>('/users', { params });
  }

  async getUserById(id: string) {
    return apiClient.get<User>(`/users/${id}`);
  }

  async createUser(userData: CreateUserDto) {
    return apiClient.post<User>('/users', userData);
  }

  async updateUser(id: string, userData: UpdateUserDto) {
    return apiClient.put<User>(`/users/${id}`, userData);
  }

  async deleteUser(id: string) {
    return apiClient.delete(`/users/${id}`);
  }

  async updateUserProfile(userData: Partial<User>) {
    return apiClient.put<User>('/users/profile', userData);
  }

  async changePassword(currentPassword: string, newPassword: string) {
    return apiClient.post('/users/change-password', {
      currentPassword,
      newPassword,
    });
  }
}

export const userService = new UserService();
```

---

## Testing Patterns

### Unit Testing Patterns

#### Testing Utility Functions

```typescript
// client/src/utils/format.test.ts
import { formatDate, formatCurrency, validateEmail } from './format';

describe('Format Utilities', () => {
  describe('formatDate', () => {
    it('should format date correctly', () => {
      const date = new Date('2024-01-15');
      expect(formatDate(date)).toBe('Jan 15, 2024');
    });

    it('should handle invalid dates', () => {
      expect(formatDate(new Date('invalid'))).toBe('Invalid Date');
    });

    it('should return current date format when no date provided', () => {
      const result = formatDate();
      expect(result).toMatch(/\w{3} \d{1,2}, \d{4}/);
    });
  });

  describe('formatCurrency', () => {
    it('should format positive numbers', () => {
      expect(formatCurrency(1234.56)).toBe('$1,234.56');
    });

    it('should format zero', () => {
      expect(formatCurrency(0)).toBe('$0.00');
    });

    it('should format negative numbers', () => {
      expect(formatCurrency(-1234.56)).toBe('-$1,234.56');
    });

    it('should handle different currencies', () => {
      expect(formatCurrency(1234.56, 'EUR')).toBe('€1,234.56');
    });
  });

  describe('validateEmail', () => {
    it('should validate correct email addresses', () => {
      expect(validateEmail('test@example.com')).toBe(true);
      expect(validateEmail('user.name+tag@domain.co.uk')).toBe(true);
    });

    it('should reject invalid email addresses', () => {
      expect(validateEmail('invalid')).toBe(false);
      expect(validateEmail('test@')).toBe(false);
      expect(validateEmail('@example.com')).toBe(false);
      expect(validateEmail('test.example.com')).toBe(false);
    });
  });
});
```

#### Testing React Components

```typescript
// client/src/components/common/Button.test.tsx
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button Component', () => {
  const user = userEvent.setup();

  it('renders with default props', () => {
    render(<Button>Click me</Button>);
    const button = screen.getByRole('button', { name: /click me/i });

    expect(button).toBeInTheDocument();
    expect(button).toHaveClass('bg-blue-600', 'text-white');
  });

  it('handles click events', async () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);

    const button = screen.getByRole('button', { name: /click me/i });
    await user.click(button);

    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('shows loading state', () => {
    render(<Button loading>Click me</Button>);

    expect(screen.getByRole('button')).toBeDisabled();
    expect(screen.getByTestId('loading-spinner')).toBeInTheDocument();
  });

  it('applies variant classes correctly', () => {
    const { rerender } = render(<Button variant="secondary">Button</Button>);
    expect(screen.getByRole('button')).toHaveClass('bg-gray-200');

    rerender(<Button variant="danger">Button</Button>);
    expect(screen.getByRole('button')).toHaveClass('bg-red-600');
  });

  it('applies size classes correctly', () => {
    const { rerender } = render(<Button size="sm">Button</Button>);
    expect(screen.getByRole('button')).toHaveClass('px-3', 'py-1.5', 'text-sm');

    rerender(<Button size="lg">Button</Button>);
    expect(screen.getByRole('button')).toHaveClass('px-6', 'py-3', 'text-lg');
  });

  it('can be disabled', () => {
    render(<Button disabled>Disabled Button</Button>);
    const button = screen.getByRole('button');

    expect(button).toBeDisabled();
  });

  it('passes through additional props', () => {
    render(<Button data-testid="custom-button" title="Custom title">Button</Button>);
    const button = screen.getByTestId('custom-button');

    expect(button).toHaveAttribute('title', 'Custom title');
  });
});
```

#### Testing Custom Hooks

```typescript
// client/src/hooks/useApi.test.ts
import { renderHook, waitFor } from '@testing-library/react';
import { useApi } from './useApi';

// Mock the API call
const mockApiCall = jest.fn();

describe('useApi Hook', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should initialize with correct default state', () => {
    const { result } = renderHook(() => useApi(mockApiCall));

    expect(result.current.data).toBeNull();
    expect(result.current.loading).toBe(false);
    expect(result.current.error).toBeNull();
  });

  it('should execute API call immediately when immediate option is true', async () => {
    const mockResponse = { success: true, data: { id: 1, name: 'Test' } };
    mockApiCall.mockResolvedValue(mockResponse);

    const { result } = renderHook(() => useApi(mockApiCall, { immediate: true }));

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(mockApiCall).toHaveBeenCalledTimes(1);
    expect(result.current.data).toEqual({ id: 1, name: 'Test' });
  });

  it('should handle successful API call', async () => {
    const mockResponse = { success: true, data: { id: 1, name: 'Test' } };
    mockApiCall.mockResolvedValue(mockResponse);

    const { result } = renderHook(() => useApi(mockApiCall));

    expect(result.current.loading).toBe(false);

    await result.current.execute();

    expect(result.current.loading).toBe(false);
    expect(result.current.data).toEqual({ id: 1, name: 'Test' });
    expect(result.current.error).toBeNull();
  });

  it('should handle API call errors', async () => {
    const errorMessage = 'API Error';
    mockApiCall.mockRejectedValue(new Error(errorMessage));

    const { result } = renderHook(() => useApi(mockApiCall));

    await result.current.execute();

    expect(result.current.loading).toBe(false);
    expect(result.current.data).toBeNull();
    expect(result.current.error?.message).toBe(errorMessage);
  });

  it('should call onSuccess callback on successful API call', async () => {
    const onSuccess = jest.fn();
    const mockResponse = { success: true, data: { id: 1 } };
    mockApiCall.mockResolvedValue(mockResponse);

    const { result } = renderHook(() =>
      useApi(mockApiCall, { onSuccess })
    );

    await result.current.execute();

    expect(onSuccess).toHaveBeenCalledWith({ id: 1 });
  });

  it('should call onError callback on failed API call', async () => {
    const onError = jest.fn();
    const error = new Error('API Error');
    mockApiCall.mockRejectedValue(error);

    const { result } = renderHook(() =>
      useApi(mockApiCall, { onError })
    );

    await result.current.execute();

    expect(onError).toHaveBeenCalledWith(error);
  });

  it('should reset state correctly', async () => {
    const mockResponse = { success: true, data: { id: 1 } };
    mockApiCall.mockResolvedValue(mockResponse);

    const { result } = renderHook(() => useApi(mockApiCall));

    await result.current.execute();
    expect(result.current.data).toEqual({ id: 1 });

    result.current.reset();
    expect(result.current.data).toBeNull();
    expect(result.current.error).toBeNull();
    expect(result.current.loading).toBe(false);
  });
});
```

### Integration Testing Patterns

#### Testing API Endpoints

```typescript
// server/tests/integration/users.test.ts
import request from 'supertest';
import { app } from '../../src/app';
import { User } from '../../src/models/User';
import { connect, disconnect } from '../../src/config/database';

describe('Users API Integration Tests', () => {
  let authToken: string;
  let testUserId: string;

  beforeAll(async () => {
    await connect();

    // Create test user and get auth token
    const registerResponse = await request(app)
      .post('/api/auth/register')
      .send({
        name: 'Test User',
        email: 'test@example.com',
        password: 'password123',
      });

    authToken = registerResponse.body.data.token;
  });

  afterAll(async () => {
    await User.deleteMany({});
    await disconnect();
  });

  describe('GET /api/users', () => {
    it('should return paginated users for admin', async () => {
      const response = await request(app)
        .get('/api/users?page=1&limit=10')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);

      expect(response.body.success).toBe(true);
      expect(response.body.data).toBeInstanceOf(Array);
      expect(response.body.meta).toBeDefined();
      expect(response.body.meta.page).toBe(1);
      expect(response.body.meta.limit).toBe(10);
    });

    it('should return 401 for unauthorized requests', async () => {
      await request(app)
        .get('/api/users')
        .expect(401);
    });
  });

  describe('POST /api/users', () => {
    it('should create a new user', async () => {
      const newUser = {
        name: 'New User',
        email: 'newuser@example.com',
        password: 'password123',
      };

      const response = await request(app)
        .post('/api/users')
        .set('Authorization', `Bearer ${authToken}`)
        .send(newUser)
        .expect(201);

      expect(response.body.success).toBe(true);
      expect(response.body.data.name).toBe(newUser.name);
      expect(response.body.data.email).toBe(newUser.email);
      expect(response.body.data.password).toBeUndefined();

      testUserId = response.body.data._id;
    });

    it('should return validation error for invalid data', async () => {
      const invalidUser = {
        name: '',
        email: 'invalid-email',
        password: '123',
      };

      const response = await request(app)
        .post('/api/users')
        .set('Authorization', `Bearer ${authToken}`)
        .send(invalidUser)
        .expect(400);

      expect(response.body.success).toBe(false);
      expect(response.body.errors).toBeInstanceOf(Array);
    });
  });

  describe('PUT /api/users/:id', () => {
    it('should update user', async () => {
      const updateData = {
        name: 'Updated User Name',
      };

      const response = await request(app)
        .put(`/api/users/${testUserId}`)
        .set('Authorization', `Bearer ${authToken}`)
        .send(updateData)
        .expect(200);

      expect(response.body.success).toBe(true);
      expect(response.body.data.name).toBe(updateData.name);
    });

    it('should return 404 for non-existent user', async () => {
      const fakeId = '507f1f77bcf86cd799439011';

      await request(app)
        .put(`/api/users/${fakeId}`)
        .set('Authorization', `Bearer ${authToken}`)
        .send({ name: 'Updated' })
        .expect(404);
    });
  });

  describe('DELETE /api/users/:id', () => {
    it('should delete user', async () => {
      await request(app)
        .delete(`/api/users/${testUserId}`)
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);

      // Verify user is deleted
      await request(app)
        .get(`/api/users/${testUserId}`)
        .set('Authorization', `Bearer ${authToken}`)
        .expect(404);
    });
  });
});
```

### End-to-End Testing Patterns

```typescript
// e2e/tests/auth-flow.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Authentication Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should register a new user', async ({ page }) => {
    // Navigate to registration page
    await page.click('text=Register');
    await expect(page).toHaveURL('/register');

    // Fill registration form
    await page.fill('[data-testid="name-input"]', 'Test User');
    await page.fill('[data-testid="email-input"]', 'test@example.com');
    await page.fill('[data-testid="password-input"]', 'password123');
    await page.fill('[data-testid="confirm-password-input"]', 'password123');

    // Submit form
    await page.click('[data-testid="register-button"]');

    // Verify successful registration
    await expect(page.locator('text=Registration successful')).toBeVisible();
    await expect(page).toHaveURL('/dashboard');
  });

  test('should login with valid credentials', async ({ page }) => {
    // Navigate to login page
    await page.click('text=Login');
    await expect(page).toHaveURL('/login');

    // Fill login form
    await page.fill('[data-testid="email-input"]', 'test@example.com');
    await page.fill('[data-testid="password-input"]', 'password123');

    // Submit form
    await page.click('[data-testid="login-button"]');

    // Verify successful login
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('text=Welcome, Test User')).toBeVisible();
  });

  test('should show error for invalid credentials', async ({ page }) => {
    // Navigate to login page
    await page.click('text=Login');

    // Fill invalid credentials
    await page.fill('[data-testid="email-input"]', 'test@example.com');
    await page.fill('[data-testid="password-input"]', 'wrongpassword');

    // Submit form
    await page.click('[data-testid="login-button"]');

    // Verify error message
    await expect(page.locator('text=Invalid credentials')).toBeVisible();
    await expect(page).toHaveURL('/login');
  });

  test('should logout successfully', async ({ page }) => {
    // Login first
    await page.click('text=Login');
    await page.fill('[data-testid="email-input"]', 'test@example.com');
    await page.fill('[data-testid="password-input"]', 'password123');
    await page.click('[data-testid="login-button"]');
    await expect(page).toHaveURL('/dashboard');

    // Logout
    await page.click('[data-testid="user-menu"]');
    await page.click('[data-testid="logout-button"]');

    // Verify logout
    await expect(page).toHaveURL('/login');
  });
});
```

---

## Security & Authentication

### JWT Authentication Pattern

```typescript
// server/src/utils/jwt.ts
import jwt from 'jsonwebtoken';
import { User } from '../models/User';
import { EnvConfig } from '@shared/types/environment';

interface TokenPayload {
  id: string;
  email: string;
  role: string;
  iat?: number;
  exp?: number;
}

export class JWTService {
  constructor(private config: EnvConfig) {}

  generateAccessToken(user: { _id: string; email: string; role: string }): string {
    return jwt.sign(
      {
        id: user._id,
        email: user.email,
        role: user.role,
      },
      this.config.JWT_SECRET,
      { expiresIn: this.config.JWT_EXPIRE }
    );
  }

  generateRefreshToken(user: { _id: string; email: string }): string {
    return jwt.sign(
      {
        id: user._id,
        email: user.email,
        type: 'refresh',
      },
      this.config.JWT_SECRET,
      { expiresIn: '7d' }
    );
  }

  async verifyAccessToken(token: string): Promise<TokenPayload> {
    try {
      const decoded = jwt.verify(token, this.config.JWT_SECRET) as TokenPayload;

      // Verify user still exists and is active
      const user = await User.findById(decoded.id);
      if (!user || !user.isActive) {
        throw new Error('User not found or inactive');
      }

      return decoded;
    } catch (error) {
      throw new Error('Invalid access token');
    }
  }

  async verifyRefreshToken(token: string): Promise<TokenPayload> {
    try {
      const decoded = jwt.verify(token, this.config.JWT_SECRET) as TokenPayload;

      if (decoded.type !== 'refresh') {
        throw new Error('Invalid refresh token');
      }

      // Verify user still exists and is active
      const user = await User.findById(decoded.id);
      if (!user || !user.isActive) {
        throw new Error('User not found or inactive');
      }

      return decoded;
    } catch (error) {
      throw new Error('Invalid refresh token');
    }
  }

  async refreshTokens(refreshToken: string): Promise<{ accessToken: string; refreshToken: string }> {
    const decoded = await this.verifyRefreshToken(refreshToken);

    const user = await User.findById(decoded.id);
    if (!user) {
      throw new Error('User not found');
    }

    const accessToken = this.generateAccessToken({
      _id: user._id,
      email: user.email,
      role: user.role,
    });

    const newRefreshToken = this.generateRefreshToken({
      _id: user._id,
      email: user.email,
    });

    return { accessToken, refreshToken: newRefreshToken };
  }
}

export const jwtService = new JWTService({
  JWT_SECRET: process.env.JWT_SECRET!,
  JWT_EXPIRE: process.env.JWT_EXPIRE || '15m',
  CORS_ORIGIN: process.env.CORS_ORIGIN || 'http://localhost:3000',
  NODE_ENV: process.env.NODE_ENV || 'development',
  MONGODB_URI: process.env.MONGODB_URI!,
  PORT: Number(process.env.PORT) || 3001,
});
```

### Input Validation Pattern

```typescript
// shared/validations/userValidation.ts
import * as yup from 'yup';
import { CreateUserDto, UpdateUserDto } from '../types/api';

export const userValidationSchemas = {
  createUser: {
    body: yup.object<CreateUserDto>({
      name: yup
        .string()
        .required('Name is required')
        .min(2, 'Name must be at least 2 characters')
        .max(50, 'Name cannot exceed 50 characters')
        .trim(),
      email: yup
        .string()
        .required('Email is required')
        .email('Please enter a valid email')
        .lowercase()
        .trim(),
      password: yup
        .string()
        .required('Password is required')
        .min(8, 'Password must be at least 8 characters')
        .matches(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/, 'Password must contain at least one uppercase letter, one lowercase letter, and one number'),
      role: yup
        .string()
        .oneOf(['user', 'admin'], 'Role must be either user or admin')
        .default('user'),
    }),
  },

  updateUser: {
    params: yup.object({
      id: yup.string().required('User ID is required'),
    }),
    body: yup.object<UpdateUserDto>({
      name: yup
        .string()
        .min(2, 'Name must be at least 2 characters')
        .max(50, 'Name cannot exceed 50 characters')
        .trim(),
      role: yup
        .string()
        .oneOf(['user', 'admin'], 'Role must be either user or admin'),
      isActive: yup.boolean(),
    }),
  },

  getUserById: {
    params: yup.object({
      id: yup.string().required('User ID is required'),
    }),
  },

  deleteUser: {
    params: yup.object({
      id: yup.string().required('User ID is required'),
    }),
  },

  getUsers: {
    query: yup.object({
      page: yup.number().integer().min(1).default(1),
      limit: yup.number().integer().min(1).max(100).default(10),
      search: yup.string().trim(),
      role: yup.string().oneOf(['user', 'admin']),
      sortBy: yup.string().oneOf(['name', 'email', 'createdAt', 'updatedAt']),
      sortOrder: yup.string().oneOf(['asc', 'desc']).default('desc'),
    }),
  },
};
```

### Rate Limiting Pattern

```typescript
// server/src/middleware/rateLimit.ts
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';
import Redis from 'ioredis';
import { config } from '../config/environment';

const redis = new Redis(config.REDIS_URL);

export const rateLimitMiddleware = rateLimit({
  store: new RedisStore({
    sendCommand: (...args: string[]) => redis.call(...args),
  }),
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: {
    error: 'Too many requests from this IP, please try again later.',
  },
  standardHeaders: true,
  legacyHeaders: false,
});

export const authRateLimit = rateLimit({
  store: new RedisStore({
    sendCommand: (...args: string[]) => redis.call(...args),
  }),
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // Limit each IP to 5 auth requests per windowMs
  message: {
    error: 'Too many authentication attempts, please try again later.',
  },
  skipSuccessfulRequests: true,
});

export const passwordResetRateLimit = rateLimit({
  store: new RedisStore({
    sendCommand: (...args: string[]) => redis.call(...args),
  }),
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 3, // Limit each IP to 3 password reset requests per hour
  message: {
    error: 'Too many password reset attempts, please try again later.',
  },
});
```

---

## Performance Patterns

### Database Query Optimization

```typescript
// server/src/services/optimizedUserService.ts
import { User, IUser } from '../models/User';
import { leanGet, leanFind } from '../utils/queryHelpers';

export class OptimizedUserService {
  // Use lean() for read-only operations to improve performance
  async getUsersList(page: number = 1, limit: number = 10): Promise<IUser[]> {
    return leanFind(User)
      .select('name email role isActive createdAt')
      .sort({ createdAt: -1 })
      .skip((page - 1) * limit)
      .limit(limit);
  }

  // Use aggregation for complex queries
  async getUserStatistics() {
    return User.aggregate([
      {
        $group: {
          _id: '$role',
          count: { $sum: 1 },
          active: {
            $sum: { $cond: ['$isActive', 1, 0] }
          },
        },
      },
      {
        $project: {
          role: '$_id',
          count: 1,
          active: 1,
          inactive: { $subtract: ['$count', '$active'] },
          _id: 0,
        },
      },
    ]);
  }

  // Use indexes effectively
  async searchUsers(query: string) {
    return User.find(
      {
        $text: { $search: query }
      },
      { score: { $meta: 'textScore' } }
    )
      .select('name email')
      .sort({ score: { $meta: 'textScore' } })
      .limit(20)
      .lean();
  }

  // Batch operations for better performance
  async updateUserBatch(userIds: string[], updateData: any) {
    return User.updateMany(
      { _id: { $in: userIds } },
      updateData,
      { multi: true }
    );
  }
}
```

### Caching Pattern

```typescript
// server/src/utils/cache.ts
import Redis from 'ioredis';

export class CacheService {
  private redis: Redis;

  constructor() {
    this.redis = new Redis(process.env.REDIS_URL);
  }

  async get<T>(key: string): Promise<T | null> {
    try {
      const value = await this.redis.get(key);
      return value ? JSON.parse(value) : null;
    } catch (error) {
      console.error('Cache get error:', error);
      return null;
    }
  }

  async set(key: string, value: any, ttl: number = 3600): Promise<void> {
    try {
      await this.redis.setex(key, ttl, JSON.stringify(value));
    } catch (error) {
      console.error('Cache set error:', error);
    }
  }

  async del(key: string): Promise<void> {
    try {
      await this.redis.del(key);
    } catch (error) {
      console.error('Cache delete error:', error);
    }
  }

  async invalidatePattern(pattern: string): Promise<void> {
    try {
      const keys = await this.redis.keys(pattern);
      if (keys.length > 0) {
        await this.redis.del(...keys);
      }
    } catch (error) {
      console.error('Cache invalidate pattern error:', error);
    }
  }
}

export const cache = new CacheService();

// Cache decorator for methods
export function cached(ttl: number = 3600) {
  return function (target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const method = descriptor.value;

    descriptor.value = async function (...args: any[]) {
      const cacheKey = `${target.constructor.name}:${propertyName}:${JSON.stringify(args)}`;

      // Try to get from cache
      const cachedResult = await cache.get(cacheKey);
      if (cachedResult) {
        return cachedResult;
      }

      // Execute method and cache result
      const result = await method.apply(this, args);
      await cache.set(cacheKey, result, ttl);

      return result;
    };
  };
}
```

### React Performance Patterns

```typescript
// client/src/components/common/OptimizedList.tsx
import React, { memo, useMemo, useCallback } from 'react';
import { FixedSizeList as List } from 'react-window';
import { User } from '@shared/types/api';

interface OptimizedListProps {
  users: User[];
  onUserSelect: (user: User) => void;
  selectedUserId?: string;
}

interface RowItemProps {
  index: number;
  style: React.CSSProperties;
  data: {
    users: User[];
    onUserSelect: (user: User) => void;
    selectedUserId?: string;
  };
}

// Memoized row item to prevent unnecessary re-renders
const RowItem = memo<RowItemProps>(({ index, style, data }) => {
  const user = data.users[index];
  const isSelected = user._id === data.selectedUserId;

  const handleClick = useCallback(() => {
    data.onUserSelect(user);
  }, [data, user]);

  return (
    <div
      style={style}
      className={`p-4 border-b cursor-pointer hover:bg-gray-50 ${
        isSelected ? 'bg-blue-50 border-blue-200' : ''
      }`}
      onClick={handleClick}
    >
      <div className="font-medium">{user.name}</div>
      <div className="text-sm text-gray-600">{user.email}</div>
      <div className="text-xs text-gray-500">Role: {user.role}</div>
    </div>
  );
});

RowItem.displayName = 'RowItem';

export const OptimizedUserList = memo<OptimizedListProps>(({
  users,
  onUserSelect,
  selectedUserId
}) => {
  // Memoize item data to prevent re-renders
  const itemData = useMemo(() => ({
    users,
    onUserSelect,
    selectedUserId,
  }), [users, onUserSelect, selectedUserId]);

  // Memoize item size calculation
  const itemSize = useMemo(() => 80, []);

  return (
    <div className="border rounded-lg overflow-hidden">
      <List
        height={400}
        itemCount={users.length}
        itemSize={itemSize}
        itemData={itemData}
        overscanCount={5}
      >
        {RowItem}
      </List>
    </div>
  );
});

OptimizedUserList.displayName = 'OptimizedUserList';
```

### Lazy Loading Pattern

```typescript
// client/src/components/LazyImage.tsx
import React, { useState, useRef, useEffect } from 'react';

interface LazyImageProps {
  src: string;
  alt: string;
  className?: string;
  placeholder?: string;
}

export const LazyImage: React.FC<LazyImageProps> = ({
  src,
  alt,
  className = '',
  placeholder = '/images/placeholder.jpg',
}) => {
  const [isLoaded, setIsLoaded] = useState(false);
  const [isInView, setIsInView] = useState(false);
  const [hasError, setHasError] = useState(false);
  const imgRef = useRef<HTMLImageElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true);
          observer.disconnect();
        }
      },
      { threshold: 0.1 }
    );

    if (imgRef.current) {
      observer.observe(imgRef.current);
    }

    return () => observer.disconnect();
  }, []);

  const handleLoad = () => {
    setIsLoaded(true);
  };

  const handleError = () => {
    setHasError(true);
  };

  return (
    <div ref={imgRef} className={`relative ${className}`}>
      <img
        src={isInView ? (hasError ? placeholder : src) : placeholder}
        alt={alt}
        className={`transition-opacity duration-300 ${
          isLoaded ? 'opacity-100' : 'opacity-75'
        }`}
        onLoad={handleLoad}
        onError={handleError}
        loading="lazy"
      />
      {!isLoaded && isInView && !hasError && (
        <div className="absolute inset-0 bg-gray-200 animate-pulse" />
      )}
    </div>
  );
};
```

---

## Anti-Patterns to Avoid

### TypeScript Anti-Patterns

#### ❌ Using `any` Type

```typescript
// BAD - Loses type safety
function processData(data: any): any {
  return data.map((item: any) => ({
    ...item,
    processed: true,
  }));
}

// GOOD - Use proper generics
function processData<T>(data: T[]): T[] & { processed: boolean } {
  return data.map((item) => ({
    ...item,
    processed: true,
  })) as T[] & { processed: boolean };
}

// EVEN BETTER - Define proper interface
interface ProcessedItem<T> extends T {
  processed: boolean;
}

function processData<T>(data: T[]): ProcessedItem<T>[] {
  return data.map((item) => ({
    ...item,
    processed: true,
  }));
}
```

#### ❌ Type Assertions Over Type Guards

```typescript
// BAD - Unsafe type assertion
const user = response.data as User;
console.log(user.name); // Could crash if name doesn't exist

// GOOD - Type guard
function isUser(obj: any): obj is User {
  return obj && typeof obj.name === 'string' && typeof obj.email === 'string';
}

if (isUser(response.data)) {
  const user = response.data;
  console.log(user.name); // Safe
}
```

### React Anti-Patterns

#### ❌ Direct State Mutation

```typescript
// BAD - Direct mutation
const [users, setUsers] = useState<User[]>([]);
const addUser = (user: User) => {
  users.push(user); // Wrong! Won't trigger re-render
  setUsers(users);
};

// GOOD - Immutable updates
const [users, setUsers] = useState<User[]>([]);
const addUser = (user: User) => {
  setUsers(prevUsers => [...prevUsers, user]);
};
```

#### ❌ useEffect Without Dependencies

```typescript
// BAD - Missing dependencies
useEffect(() => {
  fetchData(userId);
}); // Missing userId dependency

// GOOD - Proper dependencies
useEffect(() => {
  fetchData(userId);
}, [userId]);

// OR with proper cleanup
useEffect(() => {
  let isMounted = true;

  fetchData(userId).then(data => {
    if (isMounted) {
      setData(data);
    }
  });

  return () => {
    isMounted = false;
  };
}, [userId]);
```

### Node.js/Express Anti-Patterns

#### ❌ Synchronous Operations in Request Handlers

```typescript
// BAD - Blocking operations
app.post('/api/users', async (req, res) => {
  const hashedPassword = bcrypt.hashSync(req.body.password, 10); // Blocking!
  const user = await User.create({ ...req.body, password: hashedPassword });
  res.json(user);
});

// GOOD - Non-blocking operations
app.post('/api/users', async (req, res) => {
  const hashedPassword = await bcrypt.hash(req.body.password, 10); // Non-blocking
  const user = await User.create({ ...req.body, password: hashedPassword });
  res.json(user);
});
```

#### ❌ Not Handling Async Errors Properly

```typescript
// BAD - No error handling
app.get('/api/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id); // Could throw
  res.json(user);
});

// GOOD - Proper error handling
app.get('/api/users/:id', async (req, res, next) => {
  try {
    const user = await User.findById(req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json(user);
  } catch (error) {
    next(error); // Let error middleware handle it
  }
});
```

### Database Anti-Patterns

#### ❌ N+1 Query Problem

```typescript
// BAD - N+1 queries
const users = await User.find();
for (const user of users) {
  user.posts = await Post.find({ userId: user._id }); // N+1 queries!
}

// GOOD - Single query with population
const users = await User.find().populate('posts');

// OR - Aggregation for complex cases
const users = await User.aggregate([
  {
    $lookup: {
      from: 'posts',
      localField: '_id',
      foreignField: 'userId',
      as: 'posts',
    },
  },
]);
```

#### ❌ Not Using Indexes

```typescript
// BAD - Query without index
const users = await User.find({ email: 'user@example.com' }); // Slow without index

// GOOD - Query with index
const userSchema = new Schema({
  email: { type: String, index: true }, // Add index
  // ...
});

const users = await User.find({ email: 'user@example.com' }); // Fast with index
```

---

## Conclusion

This comprehensive pattern library provides battle-tested, production-ready patterns for MERN stack development with TypeScript. When working with LLM assistants, reference these patterns to ensure:

1. **Type Safety**: Proper TypeScript usage throughout the stack
2. **Performance**: Optimized database queries, React components, and API calls
3. **Security**: Authentication, validation, and error handling
4. **Maintainability**: Clean architecture and separation of concerns
5. **Testability**: Comprehensive testing strategies
6. **Scalability**: Patterns that grow with your application

**Usage Guidelines**:
- Always prefer specific patterns over generic solutions
- Adapt patterns to your specific requirements
- Keep patterns consistent across your codebase
- Update patterns as best practices evolve

This pattern library will significantly improve code quality when used as a reference for LLM-assisted MERN TypeScript development.
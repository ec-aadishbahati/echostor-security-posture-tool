import React from 'react'
import { render } from '@testing-library/react'
import Dashboard from '../dashboard'

jest.mock('next/router', () => require('next-router-mock'))
jest.mock('react-query', () => ({
  useQuery: () => ({ data: null, isLoading: false }),
}))
jest.mock('@/lib/auth', () => ({
  useAuth: () => ({
    user: { email: 'test@example.com', full_name: 'Test User' },
  }),
}))

describe('Dashboard Page', () => {
  it('renders without crashing', () => {
    const { container } = render(<Dashboard />)
    expect(container).toBeTruthy()
  })
})

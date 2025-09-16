# EchoStor Security Posture Assessment Tool

A comprehensive security posture assessment platform that helps organizations evaluate their cybersecurity maturity across 19 key domains with 409 detailed questions.

## Features

- **Comprehensive Assessment**: 409 questions across 19 security domains
- **User-Friendly Interface**: Modern, responsive web application
- **Auto-Save Functionality**: Automatic progress saving every 10 minutes
- **15-Day Assessment Period**: Users have 15 days to complete their assessment
- **PDF Report Generation**: Professional security posture reports
- **AI-Enhanced Reports**: ChatGPT-powered intelligent analysis and recommendations
- **Admin Dashboard**: Complete visibility and management of user assessments
- **Multi-Region Support**: Optimized for US users with Australia admin access

## Architecture

- **Frontend**: Next.js/React deployed on Vercel
- **Backend**: FastAPI (Python) deployed on Fly.io
- **Database**: PostgreSQL on Fly.io
- **Authentication**: JWT-based secure authentication
- **AI Integration**: OpenAI GPT for smart report generation

## Project Structure

```
├── frontend/          # Next.js frontend application
├── backend/           # FastAPI backend application
├── docs/             # Documentation
├── scripts/          # Deployment and utility scripts
└── .github/          # GitHub Actions workflows
```

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.12+
- PostgreSQL
- Docker (optional)

### Development Setup

1. Clone the repository
2. Set up backend (see backend/README.md)
3. Set up frontend (see frontend/README.md)
4. Configure environment variables
5. Run database migrations
6. Start development servers

## Deployment

- **Frontend**: Automatically deployed to Vercel on push to main
- **Backend**: Automatically deployed to Fly.io on push to main
- **Database**: PostgreSQL hosted on Fly.io

## Security Features

- JWT-based authentication
- Password hashing with bcrypt
- Rate limiting
- CORS protection
- Input validation and sanitization
- Audit logging

## License

Proprietary - EchoStor Technologies

## Contact

For questions or support, contact: aadish.bahati@echostor.com

---

**Link to Devin run**: https://app.devin.ai/sessions/c843330a566941b78108dfc128dfbcce
**Requested by**: @ec-aadishbahati

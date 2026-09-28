# MediBot Frontend

Next.js frontend for MediBot, an internal healthcare knowledge assistant with backend-managed authentication, roles, collections, and access control.

## Requirements

- Node.js 18+
- npm
- MediBot backend running locally or at a configured API URL

## Setup

From this directory:

```bash
npm install
```

Create a `.env.local` file:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

Start the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Scripts

```bash
npm run dev        # Start the development server
npm run build      # Create a production build
npm run start      # Serve the production build
npm run lint       # Run Next.js linting
npm run typecheck  # Run TypeScript checks
```

## Backend integration

The frontend uses the existing backend endpoints:

- `POST /login` for authentication
- `GET /collections/{role}` for accessible collections
- `POST /chat` for questions and responses
- `GET /health` for connection status

Authentication uses the bearer token returned by `/login`. The backend remains the authority for authentication, role assignment, collections, authorization, retrieval type, and citations.

## Frontend behavior

- The authenticated role comes from the backend and cannot be changed in the UI.
- Collections shown in the access panel come from `/collections/{role}`.
- Assistant content is rendered as plain text and is not inserted as raw HTML.
- Hybrid RAG and SQL RAG responses display their backend-provided retrieval type.
- Source citations are deduplicated while preserving backend order.
- Expired sessions clear local frontend session state and return to the login screen.

## Project structure

```text
src/
├── app/
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
├── lib/
│   ├── api-client.ts
│   └── session.ts
└── types/
    └── api.ts
```

The frontend does not contain backend authorization logic, document ingestion, retrieval, or search implementation.

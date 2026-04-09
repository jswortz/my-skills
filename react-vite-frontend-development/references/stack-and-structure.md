# Stack Reference and Project Structure

## Stack Reference

| Layer | Technology | Version |
|-------|-----------|---------|
| Build | Vite | 7.x |
| Framework | React | 19.x |
| Language | TypeScript | 5.9.x |
| Styling | Tailwind CSS (v4 plugin) | 4.x |
| State | Zustand | 5.x |
| Routing | React Router DOM | 7.x |
| Icons | Lucide React | 0.575+ |
| Data Fetching | @tanstack/react-query | 5.x |
| Flow Visualization | ReactFlow | 11.x |
| Unit Testing | Vitest + Testing Library | 4.x |
| E2E Testing | Playwright | 1.58+ |
| API Mocking | MSW (Mock Service Worker) | 2.x |

## Project Structure

```
frontend/
├── src/
│   ├── components/ui/       # Reusable UI primitives (Button, Card, Tabs, Badge, Input, etc.)
│   ├── features/            # Feature modules (trends, orchestration, studio, narrative, rating)
│   │   ├── trends/          # Campaign config wizard, trend selection, safety guardrails
│   │   ├── orchestration/   # Pipeline run management, SSE event streaming
│   │   ├── studio/          # AV studio editing workspace
│   │   ├── narrative/       # Research report viewer/editor
│   │   └── rating/          # Rubric-based evaluation system
│   ├── hooks/               # Custom React hooks (useSession, etc.)
│   ├── stores/              # Zustand stores (campaignStore, etc.)
│   ├── services/            # API client, brand safety, trends cache
│   ├── types/               # TypeScript type definitions
│   ├── lib/                 # Utility functions (cn for classnames)
│   ├── App.tsx              # Root component with router
│   └── main.tsx             # Entry point
├── e2e/                     # Playwright E2E tests
├── vite.config.ts           # Vite config with proxy rules
├── tailwind.config.ts       # Tailwind v4 config (if present)
└── package.json
```
---
name: react-vite-frontend-development
description: "React + Vite frontend development with TypeScript, Tailwind CSS v4, Zustand, React Router, and Lucide icons. Use when building, modifying, or debugging React components, pages, hooks, stores, or services in a Vite-based frontend. Covers component patterns, state management, routing, API integration, testing with Vitest/Playwright, and hot module replacement workflows."
---

# React + Vite Frontend Development

## When to Use
Activate this skill when working on frontend code in a Vite + React project, including:
- Creating or modifying React components, pages, or layouts
- Working with Zustand stores or React state management
- Building API service layers or data fetching hooks
- Setting up or debugging Vite proxy configuration
- Writing Vitest unit tests or Playwright E2E tests
- Styling with Tailwind CSS v4
- Configuring routing with React Router v7

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

## Development Commands

```bash
# Start dev server (port 5173, proxies to backend on 8000)
cd frontend && npm run dev

# Type checking
npx tsc --noEmit --project tsconfig.json

# Unit tests
npm run test           # Watch mode
npm run test:run       # Single run
npm run test:coverage  # With coverage

# E2E tests
npm run test:e2e                    # Headless
npm run test:e2e:headed             # With browser
npx playwright test e2e/specific.spec.ts  # Single file

# Build for production
npm run build
```

## Key Patterns

### Component Pattern
```tsx
import { useState, useCallback } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { Loader2 } from 'lucide-react';
import { cn } from '../../lib/utils';

interface Props {
  data: SomeType;
  onAction: (id: string) => void;
}

export function MyComponent({ data, onAction }: Props) {
  const [loading, setLoading] = useState(false);

  const handleClick = useCallback(async () => {
    setLoading(true);
    try {
      await onAction(data.id);
    } finally {
      setLoading(false);
    }
  }, [data.id, onAction]);

  return (
    <Card className={cn('transition-all', loading && 'opacity-50')}>
      <CardHeader>
        <CardTitle>{data.title}</CardTitle>
      </CardHeader>
      <CardContent>
        <Button onClick={handleClick} disabled={loading}>
          {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : 'Action'}
        </Button>
      </CardContent>
    </Card>
  );
}
```

### Zustand Store Pattern
```tsx
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface MyStore {
  value: string;
  setValue: (v: string) => void;
  reset: () => void;
}

export const useMyStore = create<MyStore>()(
  persist(
    (set) => ({
      value: '',
      setValue: (v) => set({ value: v }),
      reset: () => set({ value: '' }),
    }),
    { name: 'my-store' }  // localStorage key
  )
);
```

### API Service Pattern
```tsx
// services/api.ts
const API_BASE = import.meta.env.VITE_API_BASE || '';

class ApiClient {
  private async request<T>(path: string, options?: RequestInit): Promise<T> {
    const response = await fetch(`${API_BASE}${path}`, {
      headers: { 'Content-Type': 'application/json' },
      ...options,
    });
    if (!response.ok) throw new Error(`${response.status}: ${response.statusText}`);
    return response.json();
  }

  async getData(id: string) {
    return this.request<DataType>(`/api/v1/data/${id}`);
  }
}

export const api = new ApiClient();
```

### SSE Streaming Pattern
```tsx
const eventSource = new EventSource(`/api/v1/stream/${sessionId}`);
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Handle event
};
eventSource.onerror = () => eventSource.close();
```

### Controlled Tabs Pattern
```tsx
const [activeTab, setActiveTab] = useState<string>('tab1');

<Tabs value={activeTab} onValueChange={setActiveTab}>
  <TabsList>
    <TabsTrigger value="tab1">Tab 1</TabsTrigger>
    <TabsTrigger value="tab2">Tab 2</TabsTrigger>
  </TabsList>
  <TabsContent value="tab1">Content 1</TabsContent>
  <TabsContent value="tab2">Content 2</TabsContent>
</Tabs>
```

## Vite Proxy Rules
The dev server proxies API calls to backend services:
- `/api/memories/*` → port 8082 (Memory Bank API) — **MUST come before `/api`**
- `/api/*` → port 8000 (API server)
- `/ws/*` → port 8081 (Voice WebSocket)

## Styling Rules
- Use Tailwind CSS v4 utility classes (imported via `@tailwindcss/vite` plugin)
- Dark theme by default: `bg-zinc-950`, `text-zinc-100`, borders `border-zinc-800`
- Use `cn()` from `lib/utils` for conditional classnames (wraps `clsx`)
- Icons from `lucide-react` — import individual icons, not the entire library
- Responsive: mobile-first with `sm:`, `md:`, `lg:` breakpoints

## Testing Rules
- **Unit tests**: Vitest + React Testing Library, co-located as `*.test.tsx`
- **E2E tests**: Playwright in `frontend/e2e/`, use `domcontentloaded` not `networkidle` (SSE keeps connections open)
- **Zustand in E2E**: Set store values via `localStorage` then full-page reload (SPA navigation won't reinitialize persisted stores)

## Common Gotchas
1. **Vite proxy ordering**: `/api/memories` MUST come before `/api` in `vite.config.ts`
2. **SSE + networkidle**: Never use `waitForLoadState('networkidle')` — SSE streams keep connections open indefinitely
3. **Zustand persist**: Values set via `useStore.setState()` in tests may not persist across SPA navigation; use localStorage + reload
4. **Tabs component**: Use controlled mode (`value` + `onValueChange`) when programmatically switching tabs
5. **Adjacent JSX**: When using ternary operators, wrap multiple sibling elements in `<>...</>` fragments

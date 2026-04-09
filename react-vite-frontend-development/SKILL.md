---
name: react-vite-frontend-development
description: "React + Vite frontend development with TypeScript, Tailwind CSS v4, Zustand, React Router, and Lucide icons. Use when building, modifying, or debugging React components, pages, hooks, stores, or services in a Vite-based frontend. Covers component patterns, state management, routing, API integration, testing with Vitest/Playwright, and hot module replacement workflows."
---

# React + Vite Frontend Development

This skill provides workflow details, architectural guidance, and code patterns for developing a React frontend using Vite, TypeScript, Tailwind CSS, Zustand, and React Router.

## References

For deep dives into the architecture and best practices, see the following references:
- **[Stack & Structure](references/stack-and-structure.md)**: Detailed component overview, project layout, and library versions.
- **[Key Patterns](references/patterns.md)**: Examples of common components, services, and Zustand stores.

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

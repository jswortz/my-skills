# Key React + Vite Patterns

## Component Pattern
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

## Zustand Store Pattern
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

## API Service Pattern
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

## SSE Streaming Pattern
```tsx
const eventSource = new EventSource(`/api/v1/stream/${sessionId}`);
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Handle event
};
eventSource.onerror = () => eventSource.close();
```

## Controlled Tabs Pattern
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
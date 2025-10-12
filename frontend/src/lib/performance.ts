import { getCLS, getFCP, getFID, getLCP, getTTFB, Metric } from 'web-vitals';

const THRESHOLDS = {
  LCP: { good: 2500, needsImprovement: 4000 },
  FID: { good: 100, needsImprovement: 300 },
  CLS: { good: 0.1, needsImprovement: 0.25 },
  FCP: { good: 1800, needsImprovement: 3000 },
  TTFB: { good: 800, needsImprovement: 1800 },
};

export type MetricRating = 'good' | 'needs-improvement' | 'poor';

export interface WebVitalsMetric {
  name: string;
  value: number;
  rating: MetricRating;
  delta: number;
}

function getRating(name: string, value: number): MetricRating {
  const threshold = THRESHOLDS[name as keyof typeof THRESHOLDS];
  if (!threshold) return 'good';

  if (value <= threshold.good) return 'good';
  if (value <= threshold.needsImprovement) return 'needs-improvement';
  return 'poor';
}

function reportMetric(metric: Metric): void {
  const webVitalsMetric: WebVitalsMetric = {
    name: metric.name,
    value: metric.value,
    rating: getRating(metric.name, metric.value),
    delta: metric.delta,
  };

  if (process.env.NODE_ENV === 'development') {
    console.log('Web Vitals:', webVitalsMetric);
  }

  if (typeof window !== 'undefined' && (window as any).Sentry) {
    (window as any).Sentry.captureMessage(`Web Vitals: ${metric.name}`, {
      level: webVitalsMetric.rating === 'poor' ? 'warning' : 'info',
      contexts: {
        webVitals: webVitalsMetric,
      },
    });
  }
}

export function initWebVitals(): void {
  if (typeof window === 'undefined') return;

  getCLS(reportMetric);
  getFID(reportMetric);
  getLCP(reportMetric);
  
  getFCP(reportMetric);
  getTTFB(reportMetric);
}

export { THRESHOLDS };

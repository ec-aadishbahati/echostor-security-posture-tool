/**
 * Formats API error responses into user-friendly strings.
 * Handles FastAPI/Pydantic validation errors and other error formats.
 */
export function formatApiError(error: any, fallbackMessage = 'An error occurred'): string {
  if (!error) return fallbackMessage;

  const detail = error.response?.data?.detail;

  if (!detail) return fallbackMessage;

  if (typeof detail === 'string') return detail;

  if (Array.isArray(detail)) {
    const messages = detail
      .map((err) => {
        if (typeof err === 'string') return err;
        if (err?.msg) return err.msg;
        return JSON.stringify(err);
      })
      .filter(Boolean);
    
    return messages.length > 0 ? messages.join(', ') : fallbackMessage;
  }

  if (typeof detail === 'object' && detail.msg) {
    return detail.msg;
  }

  if (typeof detail === 'object') {
    try {
      return JSON.stringify(detail);
    } catch {
      return fallbackMessage;
    }
  }

  return fallbackMessage;
}

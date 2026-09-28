import type { ChatRequest, ChatResponse, HealthResponse, LoginRequest, LoginResponse, Session, UserRole } from "@/types/api";

const baseUrl = (process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000").replace(/\/+$/, "");

export class ApiError extends Error {
  constructor(public readonly status: number, message: string) { super(message); this.name = "ApiError"; }
}

function safeMessage(value: unknown): string | null {
  if (typeof value === "string") return value;
  if (value && typeof value === "object" && "detail" in value) {
    const detail = (value as { detail?: unknown }).detail;
    if (typeof detail === "string") return detail;
    if (Array.isArray(detail)) return "Please check the submitted fields and try again.";
  }
  return null;
}

async function request<T>(path: string, init: RequestInit = {}, token?: string, signal?: AbortSignal): Promise<T> {
  let response: Response;
  try {
    response = await fetch(`${baseUrl}${path}`, { ...init, signal, headers: { Accept: "application/json", "Content-Type": "application/json", ...(token ? { Authorization: `Bearer ${token}` } : {}), ...init.headers } });
  } catch (error) {
    if (error instanceof DOMException && error.name === "AbortError") throw error;
    throw new ApiError(0, "Unable to connect to MediBot. Verify that the backend is running and try again.");
  }
  const text = await response.text();
  let body: unknown = null;
  try { body = text ? JSON.parse(text) as unknown : null; } catch { body = null; }
  if (!response.ok) throw new ApiError(response.status, safeMessage(body) ?? (response.status >= 500 ? "MediBot is temporarily unavailable. Please try again." : "MediBot could not process this request."));
  return body as T;
}

export const api = {
  login: (credentials: LoginRequest) => request<LoginResponse>("/login", { method: "POST", body: JSON.stringify(credentials) }),
  collections: (role: UserRole, token: string, signal?: AbortSignal) => request<string[]>(`/collections/${encodeURIComponent(role)}`, {}, token, signal),
  chat: (payload: ChatRequest, token: string, signal?: AbortSignal) => request<ChatResponse>("/chat", { method: "POST", body: JSON.stringify(payload) }, token, signal),
  health: (signal?: AbortSignal) => request<HealthResponse>("/health", {}, undefined, signal),
};

export function sessionFromLogin(response: LoginResponse): Session { return { accessToken: response.access_token, userName: response.user_name, roles: response.roles }; }

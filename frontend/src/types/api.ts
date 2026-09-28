export const USER_ROLES = ["doctor", "nurse", "billing_executive", "technician", "admin"] as const;
export type UserRole = (typeof USER_ROLES)[number];

export const RETRIEVAL_TYPES = ["hybrid_rag", "sql_rag"] as const;
export type RetrievalType = (typeof RETRIEVAL_TYPES)[number];

export interface LoginRequest { user_name: string; password: string }
export interface LoginResponse { access_token: string; token_type: string; user_name: string; roles: UserRole[] }
export interface SourceCitation { source_document: string; section_title: string | null; collection: string }
export interface ChatRequest { question: string; role: UserRole }
export interface ChatResponse { answer: string; sources: SourceCitation[]; retrieval_type: RetrievalType; role: UserRole }
export interface HealthResponse { status: string }
export interface Session { accessToken: string; userName: string; roles: UserRole[] }

export function isUserRole(value: unknown): value is UserRole {
  return typeof value === "string" && (USER_ROLES as readonly string[]).includes(value);
}

export function isRetrievalType(value: unknown): value is RetrievalType {
  return typeof value === "string" && (RETRIEVAL_TYPES as readonly string[]).includes(value);
}

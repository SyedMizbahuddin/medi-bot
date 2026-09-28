import type { Session, UserRole } from "@/types/api";

const SESSION_KEY = "medibot.session";

export function loadSession(): Session | null {
  if (typeof window === "undefined") return null;
  try {
    const value: unknown = JSON.parse(
      window.localStorage.getItem(SESSION_KEY) ?? "null",
    );
    if (!value || typeof value !== "object") return null;
    const candidate = value as Partial<Session>;
    if (
      typeof candidate.accessToken !== "string" ||
      typeof candidate.userName !== "string" ||
      !Array.isArray(candidate.roles)
    )
      return null;
    const roles = candidate.roles.filter(
      (role): role is UserRole =>
        typeof role === "string" &&
        [
          "doctor",
          "nurse",
          "billing_executive",
          "technician",
          "admin",
        ].includes(role),
    );
    return roles.length
      ? {
          accessToken: candidate.accessToken,
          userName: candidate.userName,
          roles,
        }
      : null;
  } catch {
    return null;
  }
}

export function saveSession(session: Session): void {
  window.localStorage.setItem(SESSION_KEY, JSON.stringify(session));
}
export function clearSession(): void {
  window.localStorage.removeItem(SESSION_KEY);
}

/** Local platform readiness contract; not yet a public product API. */
export interface Readiness {
  status: "ready" | "unavailable";
}

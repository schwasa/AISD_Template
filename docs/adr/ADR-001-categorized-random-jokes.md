# ADR-001: Categorized Random Jokes

## Status

Accepted

## Context

The Dad Joke API needs more variety while remaining simple, stateless, and
easy to demonstrate in CI. The next use case adds three categories with ten
fixed jokes per category.

## Decision

Keep the joke catalogue in application-owned static data and expose:

- `GET /joke` for a random joke from all categories
- `GET /joke?category=<name>` for a random joke from one category
- `GET /categories` for the supported category names

The API returns a single JSON object for `/joke`. An unknown category is a
client error with HTTP 404. No session, cursor, database, or server-side
request counter is introduced.

## Consequences

- Requests remain independent and safe across container restarts and replicas.
- The behavior is deterministic to test when the random source is controlled.
- The fixed catalogue is simple to review and change in a teaching exercise.
- Repeated requests may return the same joke; avoiding repetition is out of
  scope for this use case.
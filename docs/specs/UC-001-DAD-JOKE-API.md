# UC-001 Dad Joke API

## Intent

Provide a simple API that returns one fixed dad joke at random, either from all
available jokes or from a requested category.

## Actors

Primary: API consumer

## Preconditions

The FastAPI application is running.

## Flow

1. The consumer sends `GET /joke`, optionally with a category query parameter.
2. The API selects one fixed dad joke at random from all jokes or the requested category.
3. The API returns the selected joke as JSON.

## Errors

- The service is unavailable if the application is not running.
- The requested category does not exist.

## Acceptance

Given the application is running
When the consumer requests `/joke`
Then the API returns HTTP 200 and one of the thirty fixed jokes.

Given the application is running
When the consumer requests `/joke?category=programming`
Then the API returns HTTP 200 and one of the ten programming jokes.

Given the application is running
When the consumer requests `/joke?category=unknown`
Then the API returns HTTP 404.

Given the application is running
When the consumer requests `/categories`
Then the API returns HTTP 200 and the supported categories `classic`,
`programming`, and `school`.

Given the application is running
When the consumer requests `/health`
Then the API returns HTTP 200 and `{"status": "ok"}`.

## Tests

Unit: `tests/unit/test_jokes.py`
Integration: `tests/integration/test_main.py`
E2E: Not required for this first slice
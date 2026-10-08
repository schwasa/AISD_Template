# UC-001 Dad Joke API

## Intent

Provide a simple API that returns one of five fixed dad jokes at random.

## Actors

Primary: API consumer

## Preconditions

The FastAPI application is running.

## Flow

1. The consumer sends `GET /joke`.
2. The API selects one fixed dad joke at random.
3. The API returns the selected joke as JSON.

## Errors

- The service is unavailable if the application is not running.

## Acceptance

Given the application is running
When the consumer requests `/joke`
Then the API returns HTTP 200 and one of the five fixed jokes.

Given the application is running
When the consumer requests `/health`
Then the API returns HTTP 200 and `{"status": "ok"}`.

## Tests

Unit: `tests/unit/test_jokes.py`
Integration: `tests/integration/test_main.py`
E2E: Not required for this first slice
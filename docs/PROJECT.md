# PROJECT.md

Complete this document during **BOOTSTRAP**. Keep it concise and specific to
the project created from this template.

## Purpose

- Project name: AISD_Teaching_Example
- User or organisational problem: Demonstrate a standardized workflow for cloning a repository, initializing the local development environment, creating a first commit, and merging changes into `main` with CI/CD checks.
- Intended users: Students learning Git, GitHub, Python, FastAPI and the AI-SDLC workflow.
- In scope: Repository bootstrap, the first-commit workflow, pull requests, and standardized CI/CD validation for a future FastAPI example.
- Out of scope: Production deployment, authentication, persistent data storage, and application-specific business features.

## Architecture

Describe the selected architecture, boundaries and dependency direction. If
Clean Architecture is used, keep dependencies pointing inward:

`domain ← application ← interfaces ← infrastructure`

This project uses Python 3.12 and FastAPI. The application is intentionally
minimal; application-specific boundaries will be documented when the first use
case is specified.

## Structure

Document the meaningful source and test directories once they exist. Reuse the
existing repository structure where it is compatible with the selected stack.

## Commands

Document the commands for the selected stack:

| Activity | Command |
|---|---|
| Install | `bash scripts/setup-python.sh` |
| Unit tests | `TBD` until application tests exist |
| Integration tests | `TBD` until application tests exist |
| Run locally | `TBD` until the FastAPI application exists |
| Build/release | GitHub Actions workflows in `.github/workflows/` |

## Dependencies

Dependency manifest: `requirements.txt`. Runtime: Python 3.12. Never commit
credentials or secrets; document required secret names and configuration
variables only.

# Repository Guidelines

## Project Structure & Module Organization
The Git practice code lives in `practice/`, with focused Python modules such as `calculator.py`, `list_manager.py`, `temperature.py`, and `text_tools.py`. Top-level learning references (`Tutorial.md`) and chat records (`QA.md`) capture study plans and prior Q&A; keep them updated when workflows evolve. New learning notes belong under `docs/` (create `docs/git-notes.md` if it is missing) so experiments and summaries stay versioned alongside the exercises.

## Build, Test, and Development Commands
Use Python 3.11+ and run individual scripts while iterating, for example `python practice/calculator.py`. Validate library behavior with ad-hoc REPL sessions (`python -i practice/list_manager.py`) when exploring APIs. When automated tests are added, place them in `tests/` and execute `pytest` from the repository root. Create virtual environments with `python -m venv .venv` and activate them before installing tooling.

## Coding Style & Naming Conventions
Follow PEP 8 with four-space indentation, snake_case for functions and file names, and upper-case constants. Keep modules narrowly scoped, document non-obvious logic with short comments, and prefer explicit type hints (already used across `practice/`). Run `ruff check .` or `python -m pylint practice` before commits if linters are available; otherwise perform manual reviews for readability and error handling.

## Testing Guidelines
Adopt `pytest` for new work. Mirror module names in the `tests/` directory (e.g., `test_calculator.py`), and name test functions `test_<behavior>`. Each pull request should cover edge cases (division by zero, empty lists, temperature extremes). Record manual test commands in the PR description when automated coverage is not present.

## Commit & Pull Request Guidelines
Use Conventional Commit prefixes (`feat:`, `fix:`, `docs:`) to reinforce the tutorial flow-keep the subject line under 72 characters and the body focused on why the change is needed. Rebase onto `main` before opening a PR, summarize learning context, link the relevant tutorial step or QA entry, and include screenshots or console logs for interactive scripts. Request at least one review that checks both Git commands practiced and resulting code changes to solidify the learning loop.

## Practice Workflow Expectations
Create feature branches named after the exercise (`practice/chunk-refactor`, `docs/week-2-notes`). After completing a tutorial milestone, document what was learned in `docs/git-notes.md`, add the supporting code or examples under `practice/`, and capture open questions in `QA.md` for future discussion.


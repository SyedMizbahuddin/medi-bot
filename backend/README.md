# MediAssist Backend

Learning-oriented FastAPI backend for a role-aware medical RAG assistant. It supports hybrid vector retrieval, reranking, source citations, JWT authentication, and SQLite-backed user management.

## Setup

Requirements: Python 3.10+, [uv](https://docs.astral.sh/uv/), and a Groq API key for LLM responses.

```bash
uv sync
```

Create `.env` in this directory as needed:

```dotenv
GROQ_API_KEY=your-groq-api-key
JWT_SECRET=replace-with-a-long-random-secret
JWT_EXPIRY_DAYS=365
DB_COLLECTION=medi_vector_db
```

Other configurable settings include `GROQ_MODEL`, `EMBEDDING_MODEL`, `SPARSE_EMBEDDING_MODEL`, and `CROSS_ENCODER_MODEL`. Never commit `.env` or production secrets.

## Run the API

Run from the backend directory:

```bash
uv run uvicorn src.app:app --reload
```

The API is available at http://127.0.0.1:8000; OpenAPI documentation is at `/docs`.

## Endpoints

- `GET /health` — API health check.
- `POST /login` — accepts `user_name` and `password`, and returns a 365-day bearer JWT containing the username and roles.
- `GET /collections/{role}` — lists collections accessible to a role.
- `POST /chat` — accepts `question` and `role`, validates the bearer token, applies role-based retrieval, and returns the answer with source citations.

Login example:

```json
{"user_name": "dr.mehta", "password": "doctor"}
```

Use the returned token on protected requests with `Authorization: Bearer <access_token>`.

Chat example:

```json
{"question": "What are the treatment protocols?", "role": "doctor"}
```

The chat response contains `answer`, `sources` (`source_document`, `section_title`, and `collection`), `retrieval_type`, and `role`. Vector retrieval is reported as `hybrid_rag`; SQL RAG is reserved for a future flow.

## Seeded local users

Users are inserted only when absent. Passwords are stored as salted `scrypt` hashes in SQLite.

| Username | Password | Role |
| --- | --- | --- |
| `dr.mehta` | `doctor` | `doctor` |
| `nurse.priya` | `nurse` | `nurse` |
| `billing.ravi` | `billing_executive` | `billing_executive` |
| `tech.anand` | `technician` | `technician` |
| `admin.sys` | `admin` | `admin` |

These credentials are for local learning only.

## Ingestion and retrieval

```bash
uv run python -m src.ingest
uv run python -m src.ingest --force
```

The pipeline chunks documents, creates dense and sparse embeddings, and upserts vectors plus metadata into local Qdrant. `--force` clears the file-store cache; collection recreation provides a fresh ingestion run.

When run from this directory, default runtime data is stored at:

- `../sql_db/users.sqlite3` — auth users
- `../mediassist_data/db/mediassist.db` — MediAssist SQL data
- `../vector_db` — local Qdrant data

## Structure

```text
src/app.py                    FastAPI app and router wiring
src/config/                   Settings and declarative DI container
src/routes/                   Auth and chat HTTP routes
src/models/dto/               Request and response models
src/services/api/             Auth, users, and chat orchestration
src/services/rag/             Ingestion, retrieval, generation, and storage
src/helpers/                  Prompts, tools, users, and LLM setup
```

`AppContainer` wires services through constructor dependency injection. Auth and MediAssist SQL use separate `SQLiteDB` providers.

## Tests and checks

```bash
uv run pytest -q
uv run ruff check src tests demo
uv run mypy src tests
```

Tests use temporary SQLite databases. Demo scripts are available after ingestion and LLM configuration:

```bash
uv run python -m demo.vector_db_temp
uv run python -m demo.medi_bot_temp
```

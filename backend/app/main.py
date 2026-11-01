from fastapi import FastAPI

app = FastAPI(
    title="Governed AI Analytics Architecture",
    version="0.1.0",
    description="Public-safe Phase 0 scaffold; no LLM or database connection yet.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/info")
def info() -> dict[str, object]:
    return {
        "name": "Governed AI Analytics Architecture",
        "phase": "scaffold",
        "implemented": ["health endpoint", "service metadata", "prototype SQL gate"],
        "not_implemented": ["LLM planning", "database execution", "agent tools"],
    }

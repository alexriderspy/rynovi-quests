"""The tiny API you're putting in a box. Don't edit this file."""
import os

import psycopg
from fastapi import FastAPI

app = FastAPI(title="Rynovi box")


@app.get("/health")
def health() -> dict:
    url = os.environ.get("DATABASE_URL")
    if not url:
        return {"api": "ok", "db": "DATABASE_URL is not set"}
    try:
        with psycopg.connect(url, connect_timeout=3) as conn:
            conn.execute("select 1")
        return {"api": "ok", "db": "ok"}
    except Exception as e:  # report, don't crash
        return {"api": "ok", "db": f"can't connect: {e.__class__.__name__}"}

from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from src.bootstrap import Bootstrap
from src.core.pipeline.pipeline import Pipeline

Bootstrap.dependencies()

app = FastAPI()


class PromptRequest(BaseModel):
    query: str
    limit: Optional[int] = 5

@app.post("/prompt")
async def prompt_legal_search(request: PromptRequest):
    results = await Pipeline.search(request.query, request.limit)
    return {"results": results}

@app.post("/ingest")
async def ingest_data():
    success = await Pipeline.run()
    return {"success": success}

@app.post("/search")
async def search(request: PromptRequest):
    results = await Pipeline.search(request.query, request.limit)
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

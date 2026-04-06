from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.orchestrator import Orchestrator
import uvicorn

app = FastAPI(title="ARIA Trading API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    ticker: str

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    try:
        orc    = Orchestrator()
        result = orc.run(request.ticker.upper())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"status": "Server is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
                port=8000, reload=True)
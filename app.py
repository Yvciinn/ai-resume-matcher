from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from model import find_top_jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestData(BaseModel):
    resume_text: str
    jobs: list = None


@app.post("/match_jobs")
def match_jobs(data: RequestData):
    if not data.jobs:
        return {"matches": []}
    jobs_df = pd.DataFrame(data.jobs)
    results = find_top_jobs(data.resume_text, job_df=jobs_df, top_n=5)
    return {"matches": [{"title": title, "score": score} for title, score in results]}
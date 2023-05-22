from fastapi import FastAPI
from src.analysis.router import router as router_analysis

app = FastAPI(
    titel='Russpass recommendation service'
)


app.include_router(
    router_analysis,
    prefix='/analysis',
    tags=['/analysis']
)


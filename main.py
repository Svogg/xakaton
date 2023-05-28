from fastapi import FastAPI
from src.analysis.router import router as router_analysis
from src.identity_services.registration.router import router as router_registration
from src.identity_services.auth.router import router as auth_router

app = FastAPI(
    titel='Russpass recommendation service'
)


app.include_router(
    router_analysis,
    prefix='/analysis',
    tags=['/analysis']
)

app.include_router(
    router_registration,
    prefix='/registration',
    tags=['/registration']
)


app.include_router(
    auth_router,
    prefix='/auth',
    tags=['/auth']
)


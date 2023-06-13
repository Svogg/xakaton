from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from identity_endpoints.routers import aggregated_router as identity_routers
from entity_endpoints.routers import aggregated_router as entity_routers


app = FastAPI(
    title='RUSSPASS recommendation service',
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    identity_routers,
    prefix='/identity',
    tags=['Identification'],
)


app.include_router(
    entity_routers,
    prefix='/entity',
    tags=['Entity']
)

from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.api.v1.items import router as items_router

app = FastAPI(title="practice_1")

app.include_router(health_router, prefix="/v1")
app.include_router(items_router,  prefix="/v1")

@app.get("/health")
def health():
    return {"status": "ok"}

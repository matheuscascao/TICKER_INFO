from fastapi import FastAPI
from src.adapters.web_server.fastapi.router import api_router

app = FastAPI(title="ASSET API", description="API for assets", version="1.0.0")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        port=80,
        log_level="info",
        reload=True,
    )

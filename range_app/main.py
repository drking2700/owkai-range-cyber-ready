from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from .api import router as api_router
from .web import router as web_router
from .auth import router as auth_router
from .db import init_db, seed_demo
from .config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    seed_demo()
    yield

app = FastAPI(title="Operation: Cyber Ready — The Range", version="0.1.0", lifespan=lifespan)
app.add_middleware(SessionMiddleware, secret_key=settings.session_secret, same_site="lax", https_only=False)
app.include_router(api_router)
app.include_router(auth_router)
app.include_router(web_router)

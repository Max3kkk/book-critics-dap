import uvicorn
from fastapi import FastAPI, Depends
from starlette.requests import Request

from api.api_v1.routers.dislike import dislike_router
from api.api_v1.routers.likes import like_router
from api.api_v1.routers.reviews import review_router
from app.api.api_v1.routers.auth import auth_router
from app.api.api_v1.routers.authors import author_router
from app.api.api_v1.routers.books import book_router
from app.api.api_v1.routers.users import users_router
from app.core import config
from app.core.auth import get_current_active_user
from app.core.celery_app import celery_app
from app.db.session import SessionLocal

app = FastAPI(title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/task")
async def example_task():
    celery_app.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    author_router,
    prefix="/api/v1/authors",
    tags=["authors"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    book_router,
    prefix="/api/v1/books",
    tags=["books"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    review_router,
    prefix="/api/v1/reviews",
    tags=["reviews"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    like_router,
    prefix="/api/v1/likes",
    tags=["likes"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    dislike_router,
    prefix="/api/v1/dislikes",
    tags=["dislikes"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)

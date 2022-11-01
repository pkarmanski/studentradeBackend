from fastapi import FastAPI
from APP.routers.studentrade import router


app = FastAPI(version='0.0.0')

app.include_router(router)

from fastapi import FastAPI
from APP.routers.studentrade import router
from APP.utils.background_function import background
from APP.database.sqlite_manager import create_logged_user_table
from APP.utils.yaml_manager import YamlData


app = FastAPI(version='0.0.0')

yaml_data = YamlData()

create_logged_user_table(yaml_data.get_sqlite_db())

app.include_router(router)




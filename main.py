from fastapi import FastAPI
from APP.routers.studentrade import router
from APP.database.sqlite_manager import create_logged_user_table
from APP.utils.yaml_manager import YamlData
from APP.utils.background_function import check_token_lifetime


app = FastAPI(version='0.1.0')

yaml_data = YamlData()

create_logged_user_table(yaml_data.get_sqlite_db())
check_token_lifetime(yaml_data.get_sqlite_db(), yaml_data.get_token_lifetime(), 30)

app.include_router(router)




import yaml
import logging
from APP.data_models.service_data_models.service_data_models import DatabaseParams
from APP.messages.error_msg import YamlErrorMsg

logger = logging.getLogger(__name__)


class YamlData:
    def __init__(self, filename='config.yaml'):
        try:
            with open(filename) as file:
                self.data = yaml.load(file, Loader=yaml.FullLoader)
                file.close()
        except EnvironmentError:
            logger.critical(YamlErrorMsg.YAML_FILE_NOT_FOUND.description)
            exit(1)

    def get_mysql_params(self) -> DatabaseParams:
        mysql_params = self.data['mysql_params']
        return DatabaseParams(host=mysql_params['host'],
                              port=mysql_params['port'],
                              login=mysql_params['login'],
                              password=mysql_params['password'],
                              database=mysql_params['database'])

    def get_select_posts_limit(self) -> int:
        return self.data['select_posts_limit']

    def get_sqlite_db(self):
        return self.data['sqlite_db_file']

    def get_token_lifetime(self):
        return self.data['token_lifetime']

    def get_code_lifetime(self):
        return self.data['code_lifetime']

    def get_save_file_path(self):
        return self.data['save_file_path']

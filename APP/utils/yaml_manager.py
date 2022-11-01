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

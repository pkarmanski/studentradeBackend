from enum import Enum


class MailData(Enum):
    activate_user_subject = "STUDENTRADE | Your account has been successfully created!"
    activate_user_body = "We are glad you are with us :D Click in the link below to finish the registration process\n"

    def __init__(self, description: str):
        self.__description = description

    @property
    def get_description(self):
        return self.__description

from enum import Enum


class MysqlQuery(Enum):
    CHECK_USER_EXISTENCE_BY_LOGIN = 'select login from users where login = "{}"'
    CHECK_USER_EXISTENCE_BY_EMAIL = 'select email from users where email = "{}"'
    REGISTER_USER = 'insert into users (login, password, email, faculty_id, status) values("{}",MD5("{}"), "{}", {}, "{}")'
    LOGIN_USER = 'select id from users where login="{}" and password=MD5("{}") and status = "{}"'
    GET_USER_ID = 'select id from users where login="{}" and password=MD5("{}") and email="{}"'
    GET_POSTS = 'select post.id, post.content, post.image, post.upload_date as uploadDate, users.login from post join users on users.id = post.user_id where lower(post.status)="{}" order by post.upload_date desc limit {}'
    GET_FACULTY_LIST = 'select id, name from faculty'
    GET_FILED_OF_STUDY_LIST = 'select id, name from field_of_study'
    GET_PRODUCT_TYPE = 'select id, name from products_type'
    GET_COURSE_LIST = 'select id, name from course'
    CHANGE_USER_PASSWORD = 'update users set password = MD5("{}") where email = "{}"'
    UPLOAD_POST = 'insert into post (user_id, content, upload_date, image, status) values({}, "{}", "{}", "{}", "{}")'
    ACTIVATE_USER = 'update users set status="{}" where id={}'
    GET_COMMENTS = 'select comments.content, login, comments.upload_date as uploadDate from comments, users where users.id = comments.user_id and post_id = {} and lower(comments.status) ="{}"'
    UPLOAD_COMMENT = 'insert into comments (user_id, content, upload_date, post_id, status) values({}, "{}", "{}", "{}", "{}")'
    GET_PRODUCTS = """
    select prodcuts.id, email, prodcuts.name as title, login, study_year as studyYear,upload_date as uploadDate, 
    field_of_study.name as field, price, comment as content, image 
    from prodcuts 
    join field_of_study on field_of_study.id = prodcuts.field_of_study_id
    join users on users.id = prodcuts.user_id
    where type_id = {} and prodcuts.status = "{}" 
    order by upload_date desc
    """
    UPLOAD_PRODUCT_DATA = """
    insert into prodcuts (type_id, name, user_id, upload_date, expiration_date, status, study_year, 
     field_of_study_id, price, comment , image) values({},"{}",{},"{}","{}","{}",{},{},{},"{}","{}")
    """
    GET_FILTERED_PRODUCTS = """
    select prodcuts.id, email, prodcuts.name as title, login, study_year as studyYear,upload_date as uploadDate, 
    field_of_study.name as field, price, comment as content, image 
    from prodcuts 
    join field_of_study on field_of_study.id = prodcuts.field_of_study_id
    join users on users.id = prodcuts.user_id
    where type_id = {} and prodcuts.status = "{}" 
    {}
    order by upload_date {}
    """



    def __init__(self, query: str):
        self.__query = query

    @property
    def query(self):
        return self.__query

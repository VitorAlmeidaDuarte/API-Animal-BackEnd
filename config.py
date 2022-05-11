import os


class Config(object):
    CSRF_ENABLED = True
    SECRET = "ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5i2bck*gn@w3@f&-&"

    TEMPLATE_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "templates"
    )
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    APP = None
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///C:/Users/User/Desktop/Project-Animal/bancoDados/Animals-User.db"
    )


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 8000
    URL_MAIN = "http://%s:%s/" % (IP_HOST, PORT_HOST)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = "localhost"  # obs ip do servidor
    PORT_HOST = 5000
    URL_MAIN = "http://%s:%s/" % (IP_HOST, PORT_HOST)


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = "localhost"  # ip do servidor

    PORT_HOST = 8080
    URL_MAIN = "http://%s:%s/" % (IP_HOST, PORT_HOST)


app_config = {
    "development": DevelopmentConfig(),
    "testing": TestingConfig(),
    "production": ProductionConfig(),
}

app_active = "development"
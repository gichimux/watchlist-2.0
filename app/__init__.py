from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
def create_app(config_name):
    #initializing application
    app = Flask(__name__,instance_relative_config = True)

    #setting up configuration
    app.config.from_object(config_options[config_name])

    #inititlalizing flask extensions
    bootstrap.init_app(app)

    #registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #setting config
    from .requests import configure_request
    configure_request(app)
    
    #will return views and forms
    return app
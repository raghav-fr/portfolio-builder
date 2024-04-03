from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path


db=SQLAlchemy()
db_name="database.db"


def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{db_name}'
    db.init_app(app)
    app.config['SECRET_KEY']="somethingsosecret"
    app.config['TEMPLATES_FOLDER'] = 'E:/project/portfoliobuilder/website/templates/work_template/'
    app.config['WORKSPACE_FOLDER'] = 'E:/project/portfoliobuilder/website/templates/users/'
    app.config['ASSET_FOLDER'] = 'E:/project/portfoliobuilder/website/static/users/'
    from .views import views
    app.register_blueprint(views,url_prefix='/')
    from .auth import auth

    app.register_blueprint(auth,url_prefix='/')

    from .workspaces import workspaces
    app.register_blueprint(workspaces,url_prefix='/')
    

    from . import  models
    with app.app_context():
            db.create_all()

    return app
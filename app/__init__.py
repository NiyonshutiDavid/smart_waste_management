from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    from .routes import auth, household, services, admin
    app.register_blueprint(auth.bp)
    app.register_blueprint(household.bp)
    app.register_blueprint(services.bp)
    app.register_blueprint(admin.bp)
    
    return app

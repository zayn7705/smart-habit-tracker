from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Change this in production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    from .models.user import User
    from .models.habit import Habit
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    from .routes.auth import auth
    from .routes.habits import habits
    
    app.register_blueprint(auth)
    app.register_blueprint(habits)
    
    with app.app_context():
        db.create_all()
    
    return app 
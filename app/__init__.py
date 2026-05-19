from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from app.models.usuario import Usuario
    return Usuario.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clinica123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    from app.routes.routes import main
    app.register_blueprint(main)

    with app.app_context():
        from app.models.usuario import Usuario
        db.create_all()
        if not Usuario.query.filter_by(username='admin').first():
            admin = Usuario(
                username='admin',
                password=generate_password_hash('12345')
            )
            db.session.add(admin)
            db.session.commit()

    return app
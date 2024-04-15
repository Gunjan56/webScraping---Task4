from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from app.routes import scraper_bp
    app.register_blueprint(scraper_bp)

    return app

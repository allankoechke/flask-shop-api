from app import create_app
from config import DevelopmentConfig, ProductionConfig

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run()
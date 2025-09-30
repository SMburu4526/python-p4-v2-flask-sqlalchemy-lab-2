from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Create tables if they don’t exist
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

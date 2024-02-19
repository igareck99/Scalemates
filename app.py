from flask import Flask
from flask_migrate import Migrate
from database.config import Configuration
from flask_sqlalchemy import SQLAlchemy
from secretKeys import *

app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = secret_key
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
   app.run()
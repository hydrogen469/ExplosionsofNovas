from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()
# postgres://wgxczkfngodtjb:3da8c66be33d61bd09239a46701f511d7e2cb5cffadd8b4d338f9326277c4f71@ec2-3-225-204-194.compute-1.amazonaws.com:5432/daqo1c1lvs2rp4
class User(UserMixin, db.Model):
    __tablename__ = "user_data"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

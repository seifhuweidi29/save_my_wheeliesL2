from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    

    def __repr__(self):
        return f"Bike(id={self.id}, brand='{self.brand}', model='{self.model}', price={self.price}, image='{self.image}', rented={self.rented}, created_at='{self.created_at}')"
class Lock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_locked = db.Column(db.Boolean, nullable=False)
    is_admin_locked = db.Column(db.Boolean, nullable=False)
    gps_lat = db.Column(db.Float, nullable=False)
    gps_lon = db.Column(db.Float, nullable=False)

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'), nullable=False)
    lock_id = db.Column(db.Integer, db.ForeignKey('lock.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    user = db.relationship('User', backref='rentals')
    bike = db.relationship('Bike', backref='rentals')
    lock = db.relationship('Lock', backref='rentals')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)




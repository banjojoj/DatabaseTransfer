from sqlalchemy.exc import OperationalError
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import Callable


# Remove linters
class MYSQLAlchemy(SQLAlchemy):
    Column: Callable
    Integer: Callable
    String: Callable
    Text: Callable
    ForeignKey: Callable


# Define Flask App
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///desktop-3d87nld/Documents/inventory.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///desktop-3d87nld/Dropbox/inv-pending.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inv-pending.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbp = MYSQLAlchemy(app)


# Define Sales Table
class PendingSales(dbp.Model):
    id = dbp.Column(dbp.Integer, primary_key=True)
    date = dbp.Column(dbp.String(10))
    dr_si_no = dbp.Column(dbp.String)
    is_paid = dbp.Column(dbp.String)
    information = dbp.Column(dbp.String)

    def __repr__(self):
        return f'Product ID {self.id}'


class PendingPurchase(dbp.Model):
    id = dbp.Column(dbp.Integer, primary_key=True)
    date = dbp.Column(dbp.String(10))
    dr_si_no = dbp.Column(dbp.String)
    is_paid = dbp.Column(dbp.String)
    information = dbp.Column(dbp.String)

    def __repr__(self):
        return f'Product ID {self.id}'


try:
    with app.app_context():
        dbp.create_all()
except OperationalError:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///DESKTOP-S7E2GTJ/Dropbox/inv-pending.db'
    try:
        dbp.create_all()
    except OperationalError:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/Dropbox/inv-pending.db'
        dbp.create_all()

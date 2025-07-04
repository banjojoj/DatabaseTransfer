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
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///desktop-3d87nld/Dropbox/a-db/inv-pending.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inv-pending.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbpi = MYSQLAlchemy(app)


# Define Sales Table
class IPendingSales(dbpi.Model):
    id = dbpi.Column(dbpi.Integer, primary_key=True)
    date = dbpi.Column(dbpi.String(10))
    dr_si_no = dbpi.Column(dbpi.String)
    is_paid = dbpi.Column(dbpi.String)
    information = dbpi.Column(dbpi.String)
    note = dbpi.Column(dbpi.String)

    def __repr__(self):
        return f'Product ID {self.id}'


class IPendingPurchase(dbpi.Model):
    id = dbpi.Column(dbpi.Integer, primary_key=True)
    date = dbpi.Column(dbpi.String(10))
    dr_si_no = dbpi.Column(dbpi.String)
    is_paid = dbpi.Column(dbpi.String)
    information = dbpi.Column(dbpi.String)

    def __repr__(self):
        return f'Product ID {self.id}'


try:
    with app.app_context():
        dbpi.create_all()
except OperationalError:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///DESKTOP-S7E2GTJ/Dropbox/a-db/inv-pending.db'
    try:
        dbpi.create_all()
    except OperationalError:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/Dropbox/a-db/inv-pending.db'
        dbpi.create_all()

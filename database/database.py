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

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///desktop-3d87nld/Dropbox/inventory.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///DESKTOP-S7E2GTJ/Dropbox/inv-pending.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = MYSQLAlchemy(app)


# Define Product Inventory Database
class InventoryTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    product_id = db.Column(db.String(30))
    product_name = db.Column(db.String())
    product_type = db.Column(db.String())
    product_cost = db.Column(db.String())
    product_price = db.Column(db.String())
    total_quantity = db.Column(db.String())
    place = db.Column(db.String())
    is_serial = db.Column(db.String())

    def __repr__(self):
        return f'Product ID {self.id}'


# Define Customer Class
class CustomerTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(30))
    customer_name = db.Column(db.String())
    tin_no = db.Column(db.String())
    customer_address = db.Column(db.String())
    contact_person = db.Column(db.String())
    contact_no = db.Column(db.String())
    terms = db.Column(db.String())
    balance = db.Column(db.String)

    def __repr__(self):
        return f'Customer ID {self.id}'


# Define Supplier Table
class SupplierTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.String(30))
    supplier_name = db.Column(db.String())
    tin_no = db.Column(db.String())
    supplier_address = db.Column(db.String())
    contact_person = db.Column(db.String())
    contact_no = db.Column(db.String())
    terms = db.Column(db.String())

    def __repr__(self):
        return f'Supplier ID {self.id}'


# Define Sales Table
class SalesTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    dr_si_no = db.Column(db.String)
    is_paid = db.Column(db.String)
    information = db.Column(db.String)

    def __repr__(self):
        return f'Product ID {self.id}'


# Define Purchases Table
class PurchasesTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    dr_si_no = db.Column(db.String)
    is_paid = db.Column(db.String)
    information = db.Column(db.String)

    def __repr__(self):
        return f'Product ID {self.id}'


# Define Collection Table
class CollectionTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    customer = db.Column(db.String(10))
    amount = db.Column(db.String)
    remarks = db.Column(db.String(10))
    bank_type = db.Column(db.String(10))
    check_no = db.Column(db.String(10))
    check_date = db.Column(db.String(10))
    dr_si_no = db.Column(db.String(10))

    def __repr__(self):
        return f'Product ID {self.id}'


with app.app_context():
    db.create_all()

# try:
#     with app.app_context():
#         db.create_all()
# except OperationalError:
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///DESKTOP-S7E2GTJ/Dropbox/inventory.db'
#     try:
#         db.create_all()
#     except OperationalError:
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/Dropbox/inventory.db'
#         db.create_all()



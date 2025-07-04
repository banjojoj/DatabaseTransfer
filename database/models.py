"""
Database Models or Tables to use
"""
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


# Initialize App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://redrex:Sep2020135838!@192.168.254.101:3306/redrex'    # Set Path where database will be saved
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///redrex.db'                                                  # SQLite Connection String
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                                                            # Disable tracking to improve performance


# Create Database
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate(app, db)
db.init_app(app)    # Initialize app


# Create Tables
class Product(db.Model):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(String(30), primary_key=True)
    description: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    type: Mapped[str] = mapped_column(String(250), nullable=False)
    cost: Mapped[int] = mapped_column(Float, nullable=False)
    price: Mapped[int] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)

    # One-to-Many Relationship: A Product can be in multiple transactions
    product_sales = relationship("SaleDetails", back_populates="product", cascade="all, delete-orphan")
    product_purchases = relationship("PurchaseDetails", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product - {self.description}>"


class Supplier(db.Model):
    __tablename__ = "supplier"

    id: Mapped[int] = mapped_column(String(30), primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(250), nullable=True)
    tin_no: Mapped[str] = mapped_column(String(250), nullable=True)
    contact_person: Mapped[str] = mapped_column(String(250), nullable=True)
    contact_no: Mapped[str] = mapped_column(String(250), nullable=True)
    terms: Mapped[str] = mapped_column(String(250), nullable=True)

    # One-to-Many: A Supplier can have many Purchases
    purchases = relationship("Purchases", back_populates="supplier")

    def __repr__(self):
        return f"<Supplier - {self.name}>"


class Customer(db.Model):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(String(30), primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(250), nullable=True)
    tin_no: Mapped[str] = mapped_column(String(250), nullable=True)
    contact_person: Mapped[str] = mapped_column(String(250), nullable=True)
    contact_no: Mapped[str] = mapped_column(String(250), nullable=True)
    terms: Mapped[str] = mapped_column(String(250), nullable=True)
    balance: Mapped[int] = mapped_column(Float, nullable=True)

    # One-to-Many: A Customer can have many Sales
    sales = relationship("Sales", back_populates="customer")
    collection = relationship("Collection", back_populates="customer")

    def __repr__(self):
        return f"<Customer - {self.name}>"


class Sales(db.Model):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(String(30), primary_key=True)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    dr_si_no: Mapped[str] = mapped_column(String(250), nullable=True)
    status: Mapped[str] = mapped_column(String(250), nullable=True)
    total: Mapped[int] = mapped_column(Float, nullable=False)

    customer_id: Mapped[str] = mapped_column(String(30), ForeignKey('customer.id'), nullable=False)

    # Many-to-One: A transaction belongs to a customer
    customer = relationship("Customer", back_populates="sales")
    sale_details = relationship("SaleDetails", back_populates="sales")

    collection = relationship("Collection", back_populates="sales")

    def __repr__(self):
        return f"<Sales - {self.dr_si_no}>"


class SaleDetails(db.Model):
    __tablename__ = "sale_details"

    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Float, nullable=False)
    sub_total: Mapped[int] = mapped_column(Float, nullable=False)
    serial_nos: Mapped[str] = mapped_column(String(250), nullable=True)

    # Foreign Keys
    product_id: Mapped[str] = mapped_column(String(30), ForeignKey('product.id'), nullable=False)
    sales_id: Mapped[str] = mapped_column(String(30), ForeignKey('sales.id'), nullable=False)

    # Many-to-One: Each detail belongs to a transaction and product
    sales = relationship("Sales", back_populates="sale_details")
    product = relationship("Product", back_populates="product_sales")

    def __repr__(self):
        return f"<SaleDetails - {self.id}>"


class Purchases(db.Model):
    __tablename__ = "purchases"

    id: Mapped[int] = mapped_column(String(30), primary_key=True)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    dr_si_no: Mapped[str] = mapped_column(String(250), nullable=True)
    status: Mapped[str] = mapped_column(String(250), nullable=True)
    total: Mapped[int] = mapped_column(Float, nullable=False)

    supplier_id: Mapped[str] = mapped_column(String(30), ForeignKey('supplier.id'), nullable=False)

    # Many-to-One: A transaction belongs to a customer
    supplier = relationship("Supplier", back_populates="purchases")
    purchase_details = relationship("PurchaseDetails", back_populates="purchases")

    def __repr__(self):
        return f"<Purchases - {self.dr_si_no}>"


class PurchaseDetails(db.Model):
    __tablename__ = "purchase_details"

    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Float, nullable=False)
    sub_total: Mapped[int] = mapped_column(Float, nullable=False)
    serial_nos: Mapped[str] = mapped_column(String(250), nullable=True)

    # Foreign Keys
    product_id: Mapped[str] = mapped_column(String(30), ForeignKey('product.id'), nullable=False)
    purchase_id: Mapped[str] = mapped_column(String(30), ForeignKey('purchases.id'), nullable=False)

    # Many-to-One: Each detail belongs to a transaction and product
    purchases = relationship("Purchases", back_populates="purchase_details")
    product = relationship("Product", back_populates="product_purchases")

    def __repr__(self):
        return f"<SaleDetails - {self.id}>"


class Collection(db.Model):
    __tablename__ = "collection"

    id: Mapped[int] = mapped_column(String(30), primary_key=True)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    customer_name: Mapped[str] = mapped_column(String(250), nullable=True)
    amount: Mapped[int] = mapped_column(Float, nullable=False)
    remarks: Mapped[str] = mapped_column(String(250), nullable=True)
    bank_type: Mapped[str] = mapped_column(String(250), nullable=True)
    check_no: Mapped[str] = mapped_column(String(250), nullable=True)
    check_date: Mapped[str] = mapped_column(String(250), nullable=True)
    dr_si_no: Mapped[str] = mapped_column(String(250), nullable=True)

    sales_id: Mapped[str] = mapped_column(String(30), ForeignKey('sales.id'), nullable=True)
    customer_id: Mapped[str] = mapped_column(String(30), ForeignKey('customer.id', name='fk_sales_customer_id'), nullable=True)

    sales = relationship("Sales", back_populates="collection")
    customer = relationship("Customer", back_populates="collection")


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(String(30), primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)               # e.g., 'admin', 'user'

    def __repr__(self):
        return f"<User - {self.username}>"


class Version(db.Model):
    __tablename__ = "version"

    id: Mapped[int] = mapped_column(String(30), primary_key=True)
    version: Mapped[str] = mapped_column(String(50), nullable=False)
    download_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f"<Version - {self.version}>"


with app.app_context():
    db.create_all()

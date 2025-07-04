from database.database import InventoryTable, app as old_app
from database.models import Product, app as app, db
from uuid import uuid4
import ast


# Get all products from old database
with old_app.app_context():
    old_products = InventoryTable.query.all()


# Variables to track loop
old_products_len = len(old_products)
num = 0

# Transfer old products to new database
for product in old_products:
    """ Create a new Product instance for each old product using the new Product schema """
    # print(
    #     product.product_id,
    #     product.product_name, product.product_type, product.product_cost,
    #     product.product_price, product.total_quantity
    # )

    # Clean Cost Column
    try:
        cost = float(ast.literal_eval(product.product_cost)[0])
    except TypeError:
        cost = float(product.product_cost)

    # Clean Stock Column
    stock = int(product.total_quantity) if int(product.total_quantity) > 0 else 0

    # Convert Price to float
    price = float(product.product_price)

    new_product = Product(
        id=product.product_id,
        description=product.product_name,
        type=product.product_type,
        cost=cost,
        price=price,
        stock=stock,
    )

    with app.app_context():
        db.session.add(new_product)
        db.session.commit()

    num += 1
    print(f"Transferred: {num}/{old_products_len}")

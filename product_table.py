from database.database import InventoryTable, app as old_app
from database.models import Product, app as app
from uuid import uuid4


# Get all products from old database
with old_app.app_context():
    old_products = InventoryTable.query.all()

# Transfer old products to new database
for product in old_products:
    # Create a new Product instance for each old product using the new Product schema
    print(
        product.id, product.date, product.product_id,
        product.product_name, product.product_type, product.product_cost,
        product.product_price, product.total_quantity, product.place,
        product.is_serial
    )

    # new_product = Product(
    #     id=product.id,
    #     date=product.date,
    #     product_id=product.product_id,
    #     product_name=product.product_name,
    #     product_type=product.product_type,
    #     product_cost=product.product_cost,
    #     product_price=product.product_price,
    #     total_quantity=product.total_quantity,
    #     place=product.place,
    #     is_serial=product.is_serial
    # )
    #
    # with app.app_context():
    #     app.session.add(new_product)
    #     app.session.commit()

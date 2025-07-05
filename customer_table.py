from database.database import CustomerTable, app as old_app
from database.models import Customer, app as app, db


# Get all customer records from old database
with old_app.app_context():
    old_customers = CustomerTable.query.all()

# Variables to track loop
old_customers_len = len(old_customers)
num = 0

# Transfer old customer records to new database
for customer in old_customers:
    """ Create a new Customer instance for each old customer using the new Customer schema """
    print(
        customer.customer_id, customer.customer_name, customer.tin_no,
        customer.customer_address, customer.contact_person, customer.contact_no, customer.terms, customer.balance
    )

    # Get Customer Information
    customer_id = customer.customer_id
    name = customer.customer_name
    tin_no = customer.tin_no
    address = customer.customer_address
    contact_person = customer.contact_person
    contact_no = customer.contact_no
    terms = customer.terms
    balance = float(customer.balance)

    # Create a new Customer instance
    new_customer = Customer(
        id=customer_id,
        name=name,
        tin_no=tin_no,
        address=address,
        contact_person=contact_person,
        contact_no=contact_no,
        terms=terms,
        balance=balance
    )

    # Add customer to new database
    with app.app_context():
        db.session.add(new_customer)
        db.session.commit()

    num += 1
    print(f"Transferred {num}/{old_customers_len}")

import random
import psycopg2
from faker import Faker

# Initialize Faker
fake = Faker()

# Database connection (replace with your credentials)
conn = psycopg2.connect(
    dbname="inv_mng",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Generate random data for Customers
def generate_customers(n):
    for _ in range(n):
        name = fake.name()[:100]  # Limit name to 100 characters
        email = fake.unique.email()[:100]  # Limit email to 100 characters
        phone = fake.phone_number()[:15]  # Limit phone to 15 characters
        address = fake.address().replace("\n", ", ")  # Address can be TEXT, no length restriction
        query = """
        INSERT INTO Customer (Name, Email, PhoneNumber, Address)
        VALUES (%s, %s, %s, %s) RETURNING customerID;
        """
        cursor.execute(query, (name, email, phone, address))
        customer_ids.append(cursor.fetchone()[0])

# Generate random data for Inventory
def generate_inventory(n):
    for _ in range(n):
        product_name = fake.word().capitalize() + " " + fake.word().capitalize()[:100]
        description = fake.sentence(nb_words=10)  # Text type, no length restriction
        quantity = random.randint(1, 500)
        price = round(random.uniform(10.0, 1000.0), 2)
        query = """
        INSERT INTO Inventory (ProductName, Description, Quantity, Price)
        VALUES (%s, %s, %s, %s) RETURNING productid;
        """
        cursor.execute(query, (product_name, description, quantity, price))
        product_ids.append(cursor.fetchone()[0])

# Generate random data for Orders
def generate_orders(n):
    for _ in range(n):
        customer_id = random.choice(customer_ids) if customer_ids else None
        product_id = random.choice(product_ids) if product_ids else None
        quantity = random.randint(1, 10)
        total_price = round(quantity * random.uniform(10.0, 1000.0), 2)
        query = """
        INSERT INTO Orders (customerid, productid, quantity, totalprice)
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (customer_id, product_id, quantity, total_price))

# Lists to store generated IDs
customer_ids = []
product_ids = []

# Run the functions to insert data
try:
    print("Generating Customers...")
    generate_customers(1000)  # 1000 customers

    print("Generating Inventory...")
    generate_inventory(1000)  # 1000 products

    print("Generating Orders...")
    generate_orders(1000)     # 1000 orders

    conn.commit()
    print("Data inserted successfully!")
except Exception as e:
    print("Error:", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()

import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

customers = []

for customer_id in range(1, 1001):
    customers.append({
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "city": fake.city(),
        "state": fake.state(),
        "signup_date": fake.date_between(
            start_date="-3y",
            end_date="today"
        )
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    DATA_DIR / "customers.csv",
    index=False
)

print("customers.csv created successfully!")

categories = {
    "Electronics": ["Samsung", "Apple", "Sony", "LG"],
    "Fashion": ["Nike", "Adidas", "Puma", "Levis"],
    "Home": ["IKEA", "Philips", "Prestige", "Milton"],
    "Books": ["Penguin", "Oxford", "Pearson"],
    "Groceries": ["Aashirvaad", "Fortune", "Tata", "Amul"]
}

products = []

for product_id in range(1, 501):

    category = random.choice(list(categories.keys()))
    brand = random.choice(categories[category])

    cost = random.randint(100, 5000)
    selling = round(cost * random.uniform(1.10, 1.60), 2)

    products.append({
        "product_id": product_id,
        "product_name": fake.word().title(),
        "category": category,
        "brand": brand,
        "cost_price": cost,
        "selling_price": selling
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    DATA_DIR / "products.csv",
    index=False
)

print("products.csv created successfully!")

warehouse_cities = [
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Mumbai",
    "Pune",
    "Delhi",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Lucknow"
]

warehouses = []

for warehouse_id in range(1, 21):

    city = random.choice(warehouse_cities)

    warehouses.append({
        "warehouse_id": warehouse_id,
        "warehouse_name": f"{city} Warehouse {warehouse_id}",
        "city": city,
        "capacity": random.randint(5000, 30000),
        "manager": fake.name()
    })

warehouses_df = pd.DataFrame(warehouses)
warehouses_df.to_csv(
    DATA_DIR / "warehouses.csv",
    index=False
)

print("warehouses.csv created successfully!")

vehicle_types = [
    "Bike",
    "Scooter",
    "Mini Truck",
    "Van"
]

partners = []

for partner_id in range(1,101):

    partners.append({
        "partner_id": partner_id,
        "partner_name": fake.name(),
        "vehicle_type": random.choice(vehicle_types),
        "rating": round(random.uniform(3.5,5.0),1),
        "joining_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

partners_df = pd.DataFrame(partners)

partners_df.to_csv(
    DATA_DIR / "delivery_partners.csv",
    index=False
)

print("delivery_partners.csv created successfully!")

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash on Delivery",
    "Net Banking"
]

orders = []

statuses = [
    "Delivered",
    "Pending",
    "Cancelled"
]

for order_id in range(1, 10001):

    customer_id = random.randint(1, 1000)
    warehouse_id = random.randint(1, 20)
    partner_id = random.randint(1, 100)

    order_date = fake.date_between(
        start_date="-365d",
        end_date="today"
    )

    status = random.choices(
        statuses,
        weights=[75,20,5],
        k=1
    )[0]

    if status == "Delivered":
        delivery_date = order_date + timedelta(
            days=random.randint(1,7)
        )
    elif status == "Pending":
        delivery_date = ""
    else:
        delivery_date = ""

    orders.append({
        "order_id": order_id,
        "customer_id": customer_id,
        "warehouse_id": warehouse_id,
        "partner_id": partner_id,
        "order_date": order_date,
        "delivery_date": delivery_date,
        "order_status": status,
        "payment_method": random.choice(payment_methods),
        "total_amount": 0.0
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    DATA_DIR / "orders.csv",
    index=False
)

print("orders.csv created successfully!")

order_items = []

item_id = 1

for order_id in range(1, 10001):

    no_of_products = random.randint(1,5)

    total = 0

    for _ in range(no_of_products):

        product = products_df.sample(1).iloc[0]

        qty = random.randint(1,4)

        price = product["selling_price"]

        total += qty * price

        order_items.append({
            "order_item_id": item_id,
            "order_id": order_id,
            "product_id": product["product_id"],
            "quantity": qty,
            "selling_price": price
        })

        item_id += 1

    orders_df.loc[
        orders_df.order_id == order_id,
        "total_amount"
    ] = round(total,2)

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    DATA_DIR / "order_items.csv",
    index=False
)

orders_df.to_csv(
    DATA_DIR / "orders.csv",
    index=False
)

print("order_items.csv created successfully!")

gps_tracking = []

tracking_id = 1

for _ in range(50000):

    gps_tracking.append({
        "tracking_id": tracking_id,
        "partner_id": random.randint(1,100),
        "latitude": round(random.uniform(8.0,37.0),6),
        "longitude": round(random.uniform(68.0,97.0),6),
        "speed": random.randint(0,100),
        "timestamp": fake.date_time_between(
            start_date="-30d",
            end_date="now"
        )
    })

    tracking_id += 1

gps_df = pd.DataFrame(gps_tracking)

gps_df.to_csv(
    DATA_DIR / "gps_tracking.csv",
    index=False
)

print("gps_tracking.csv created successfully!")
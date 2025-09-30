from app import app 
from models import db, Customer, Item, Review

def clear_database():
    with app.app_context():
        Review.query.delete()
        Customer.query.delete()
        Item.query.delete()
        db.session.commit()

def seed_customers():
    with app.app_context():
        customers = [
            Customer(name="Tal Yuri"),
            Customer(name="Jordan Brown"),
            Customer(name="Alex Chen"),
            Customer(name="Maria Garcia"),
            Customer(name="David Smith")
        ]
        db.session.add_all(customers)
        db.session.commit()
        return customers

def seed_items():
    with app.app_context():
        items = [
            Item(name="Laptop Backpack", price=49.99),
            Item(name="Insulated Coffee Mug", price=9.99),
            Item(name="Wireless Mouse", price=24.99),
            Item(name="Bluetooth Headphones", price=79.99),
            Item(name="Phone Charger", price=19.99),
            Item(name="Desk Lamp", price=34.99),
            Item(name="Notebook", price=12.99)
        ]
        db.session.add_all(items)
        db.session.commit()
        return items

def seed_reviews(customers, items):
    with app.app_context():
        reviews = [
            Review(comment="Great backpack! Fits my laptop perfectly.", customer_id=customers[0].id, item_id=items[0].id),
            Review(comment="Keeps coffee hot for hours. Love it!", customer_id=customers[0].id, item_id=items[1].id),
            Review(comment="Very comfortable and good sound quality.", customer_id=customers[1].id, item_id=items[3].id),
            Review(comment="The mouse stopped working after 2 weeks.", customer_id=customers[1].id, item_id=items[2].id),
            Review(comment="Fast charging, good quality cable.", customer_id=customers[2].id, item_id=items[4].id),
            Review(comment="Perfect brightness for my home office.", customer_id=customers[2].id, item_id=items[5].id),
            Review(comment="High quality paper, worth the price.", customer_id=customers[3].id, item_id=items[6].id),
            Review(comment="Best backpack I've ever owned!", customer_id=customers[3].id, item_id=items[0].id),
            Review(comment="Good value for money.", customer_id=customers[4].id, item_id=items[1].id),
            Review(comment="Excellent noise cancellation.", customer_id=customers[4].id, item_id=items[3].id)
        ]
        db.session.add_all(reviews)
        db.session.commit()
        return reviews

if __name__ == '__main__':
    with app.app_context():
        
        print("Clearing database...")
        clear_database()
        
        
        print("Seeding customers...")
        customers = seed_customers()
        
        print("Seeding items...")
        items = seed_items()
        
        print("Seeding reviews...")
        reviews = seed_reviews(customers, items)
        
        print("Database seeded successfully!")
        print(f"Created {len(customers)} customers, {len(items)} items, and {len(reviews)} reviews.")
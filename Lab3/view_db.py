from app import app, db, Item

if __name__ == '__main__':
    with app.app_context():
        items = Item.query.all()
        print("\n--- DATABASE CONTENT (shop.db) ---")
        print(f"{'ID':<5} | {'Name':<20} | {'Price':<10} | {'Size':<10}")
        print("-" * 60)
        for item in items:
            print(f"{item.id:<5} | {item.name:<20} | {item.price:<10} | {item.size:<10}")
        print("-" * 60)
import sqlite3

DB_FILE = "ratewise.db"


def create_tables():
    """Create the Quote and Settings tables if they do not exist yet."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Quote (
            quote_id INTEGER PRIMARY KEY AUTOINCREMENT,
            setting_id INTEGER,
            class_type TEXT,
            num_people INTEGER,
            weeks INTEGER,
            classes_per_week INTEGER,
            hours_per_class REAL,
            rent REAL,
            commute REAL,
            hourly_rate REAL,
            discount REAL,
            total_price REAL,
            price_per_person REAL,
            amount_after_costs REAL,
            FOREIGN KEY (setting_id) REFERENCES Settings (setting_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Settings (
            setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
            default_hourly_rate REAL,
            default_rent REAL,
            default_commute REAL
        )
    """)

    conn.commit()
    conn.close()

def save_quote(class_type, num_people, weeks, classes_per_week, hours_per_class, rent, commute, hourly_rate, discount, total_price, price_per_person, amount_after_costs):
    """Save a quote to the Quote table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Quote (
            class_type, num_people, weeks, classes_per_week, hours_per_class,
            rent, commute, hourly_rate, discount,
            total_price, price_per_person, amount_after_costs
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (class_type, num_people, weeks, classes_per_week, hours_per_class,
          rent, commute, hourly_rate, discount,
          total_price, price_per_person, amount_after_costs))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created.")
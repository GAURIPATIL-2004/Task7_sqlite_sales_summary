import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to (or create) the SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 2: Create the sales table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Step 3: Insert sample data
sample_data = [
    ('Apple', 10, 0.5),
    ('Banana', 20, 0.3),
    ('Orange', 15, 0.4),
    ('Apple', 5, 0.5),
    ('Banana', 10, 0.3),
    ('Orange', 10, 0.4)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Step 4: Query the data using SQL
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 5: Close the connection
conn.close()

# Step 6: Display the results
print("Sales Summary:")
print(df)

# Step 7: Plot the revenue by product
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product', legend=False)
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

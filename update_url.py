import sqlite3

# Connect to the database
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Replace 3 with the actual ID you want to delete
product_id = 8

cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

conn.commit()
conn.close()

print(f"Product with ID {product_id} deleted successfully.")
import pandas as pd
import mysql.connector
from sklearn.linear_model import LinearRegression
import joblib

# 1. Connect to your Inventory Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", # Leave empty as per your setup
    database="invoice_inventory_db"
)

# 2. Pull real data from the products table
query = "SELECT quantity, price FROM products"
df = pd.read_sql(query, db)

if df.empty:
    print("Database is empty! Add some products in the dashboard first.")
else:
    # 3. Train the AI on YOUR real inventory
    X = df[['quantity']] # Feature
    y = df['price']      # Target
    
    model = LinearRegression()
    model.fit(X, y)
    
    # 4. Save the new "Smart" brain
    joblib.dump(model, 'price_model.pkl')
    print("AI updated using real data from MySQL!")

db.close()
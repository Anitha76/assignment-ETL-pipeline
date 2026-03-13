import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():

    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    return conn


def load_fact_sales(df):

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():

        query = """
        INSERT INTO fact_sales
        (order_id, product_id, order_date, quantity_sold, price,
         discounted_price, total_revenue, profit, rating, review_count)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            str(row["order_id"]),
            str(row["product_id"]),
            row["order_date"],
            int(row["quantity_sold"]),
            float(row["price"]),
            float(row["discounted_price"]),
            float(row["total_revenue"]),
            float(row["profit"]),
            float(row["rating"]),
            int(row["review_count"])
        )

        cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    print("Data loaded into fact_sales")


def load_daily_sales(df):

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO daily_sales (order_date, daily_revenue)
            VALUES (%s,%s)
            """,
            (row["order_date"], float(row["daily_revenue"]))
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("daily_sales table loaded")


def load_top_products(df):

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO top_products (product_id, total_revenue)
            VALUES (%s,%s)
            """,
            (row["product_id"], float(row["total_revenue"]))
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("top_products table loaded")
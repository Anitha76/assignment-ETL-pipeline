import pandas as pd


def transform_data(df):


    df = df.drop_duplicates()


    df = df.fillna(0)

    # convert date column
    df["order_date"] = pd.to_datetime(df["order_date"])


    df["price"] = df["price"].astype(float)
    df["discounted_price"] = df["discounted_price"].astype(float)
    df["total_revenue"] = df["total_revenue"].astype(float)
    df["profit"] = df["profit"].astype(float)
    df["quantity_sold"] = df["quantity_sold"].astype(int)

    # daily sales aggregation
    daily_sales = df.groupby(df["order_date"].dt.date)["total_revenue"].sum().reset_index()
    daily_sales.columns = ["order_date", "daily_revenue"]

    # top products aggregation
    top_products = df.groupby("product_id")["total_revenue"].sum().reset_index()
    top_products.columns = ["product_id", "total_revenue"]

    print("Transformation completed")

    return df, daily_sales, top_products


# if __name__ == "__main__":
#     df = load_data()
#     transform_data(df)
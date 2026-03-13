# from ETL.ingest import load_data
# from ETL.transform import transform_data
# from ETL.load import load_fact_sales
#
#
# def run_pipeline():
#
#     df = load_data()
#
#     transformed_df = transform_data(df)
#
#     load_fact_sales(transformed_df)
#
#     print("Pipeline completed successfully")


from ETL.ingest import load_data
from ETL.transform import transform_data
from ETL.load import load_fact_sales, load_daily_sales, load_top_products


def run_pipeline():

    df = load_data()

    sales_df, daily_sales, top_products = transform_data(df)

    load_fact_sales(sales_df)
    load_daily_sales(daily_sales)
    load_top_products(top_products)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()



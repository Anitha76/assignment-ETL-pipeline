# Data Engineering ETL Pipeline

## Objective
Build a data pipeline to ingest, transform, and store sales data for analytics.

## Dataset
Amazon Sales Analysis Dataset from Kaggle.

## Architecture
CSV → Python ETL → PostgreSQL → SQL Analytics

## Steps

1. Data Ingestion
   - Load CSV using Pandas.

2. Data Transformation
   - Remove duplicates
   - Handle missing values
   - Convert date formats
   - Create aggregated tables (daily sales, top products)

3. Data Modeling
   - Fact Table: fact_sales
   - Aggregation Tables: daily_sales, top_products

4. Storage
   - PostgreSQL database

5. Analytics
   - Top selling products
   - Monthly revenue
   - Purchase frequency

## How to Run

Install dependencies

pip install -r requirements.txt

Run pipeline

python pipeline.py

## Pipeline Orchestration

The ETL pipeline is scheduled using Windows Task Scheduler.

A batch script (run_pipeline.bat) triggers the pipeline execution.

Example execution command:

python pipeline.py

The task can be scheduled daily or at a defined interval.



## Cron Based Scheduling

Example cron job to run pipeline daily at 2.55.40 AM:

0 2 * * * python pipeline.py
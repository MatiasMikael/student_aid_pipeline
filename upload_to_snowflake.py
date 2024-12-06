import os
from dotenv import load_dotenv
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd

# Load environment variables
print("Step 1: Loading environment variables...")
load_dotenv()

# Retrieve Snowflake credentials
print("Step 2: Retrieving Snowflake credentials...")
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")

# Create a connection to Snowflake
print("Step 3: Creating connection to Snowflake...")
engine = create_engine(URL(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
    warehouse=SNOWFLAKE_WAREHOUSE
))

# Load the cleaned CSV file
print("Step 4: Loading the cleaned CSV file 'processed_opintotuki.csv'...")
data = pd.read_csv("processed_opintotuki.csv")

# Process the data
print("Step 5: Processing the data...")
data["maksettu_eur"] = data["maksettu_eur"].str.replace(" ", "").astype(float)

# Save data to Snowflake
print("Step 6: Saving data to Snowflake table 'PROCESSED_OPINTOTUKI'...")
data.to_sql("PROCESSED_OPINTOTUKI", engine, if_exists='append', index=False)
print("Step 7: Data successfully saved to Snowflake!")
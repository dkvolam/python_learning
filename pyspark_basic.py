from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv

# Load environment variables from .env file (optional)
load_dotenv()

# Get Snowflake credentials from environment variables
snowflake_user = os.getenv("SNOWFLAKE_USER")
snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")
snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
snowflake_database = os.getenv("SNOWFLAKE_DATABASE")
snowflake_schema = os.getenv("SNOWFLAKE_SCHEMA")
snowflake_warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
snowflake_role = os.getenv("SNOWFLAKE_ROLE")

# Initialize SparkSession with Snowflake connector
spark = SparkSession.builder \
    .appName("SnowflakePySpark") \
    .config("spark.jars.packages", "net.snowflake:snowflake-jdbc:3.13.28,net.snowflake:spark-snowflake_2.12:2.11.0-spark_3.2") \
    .getOrCreate()

# Snowflake connection options
snowflake_options = {
    "sfUrl": snowflake_account,
    "sfUser": snowflake_user,
    "sfPassword": snowflake_password,
    "sfDatabase": snowflake_database,
    "sfSchema": snowflake_schema,
    "sfWarehouse": snowflake_warehouse,
    "sfRole": snowflake_role
}

# Read data from Snowflake table
try:
    df_snowflake = spark.read \
        .format("snowflake") \
        .options(**snowflake_options) \
        .option("dbtable", "YOUR_TABLE_NAME") \
        .load()
    
    df_snowflake.show()
    print(f"Successfully read {df_snowflake.count()} rows from Snowflake")
except Exception as e:
    print(f"Error connecting to Snowflake: {e}")

# Optional: Local test data
data = [
    (1, "Dilip", 5000, "IT"),
    (2, "Sam", 6000, "HR"),
    (3, "John", 7000, "IT")
]
columns = ["id", "name", "salary", "department"]
df_local = spark.createDataFrame(data, columns)
df_local.show()

# Optional: Read CSV
df_csv = spark.read.csv(r"C:\Users\dilip\Downloads\archive\data.csv", header=True, inferSchema=True)
df_csv.show()
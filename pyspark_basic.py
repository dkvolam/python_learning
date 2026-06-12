from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv

# Load environment variables from .env file (optional)
load_dotenv()

# Fix for Windows Hadoop issue - set dummy HADOOP_HOME
if os.name == 'nt':  # Windows
    import tempfile
    hadoop_home = tempfile.gettempdir()
    os.environ['HADOOP_HOME'] = hadoop_home
    os.environ['PATH'] = hadoop_home + os.pathsep + os.environ.get('PATH', '')

# Get Snowflake credentials from environment variables
snowflake_user = os.getenv("SNOWFLAKE_USER")
snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")
snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
snowflake_database = os.getenv("SNOWFLAKE_DATABASE")
snowflake_schema = os.getenv("SNOWFLAKE_SCHEMA")
snowflake_warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
snowflake_role = os.getenv("SNOWFLAKE_ROLE")

# Initialize SparkSession without Snowflake connector first (basic PySpark)
try:
    spark = SparkSession.builder \
        .appName("SnowflakePySpark") \
        .config("spark.hadoop.io.native.lib.available", "false") \
        .master("local[*]") \
        .getOrCreate()
    
    print("✓ SparkSession created successfully!")
    print(f"Spark Version: {spark.version}")
    
    # Test basic Spark functionality
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    df = spark.createDataFrame(data, ["Name", "Age"])
    df.show()
    print("✓ Basic Spark operations working!")
    
    # Snowflake connection options (if credentials are provided)
    if all([snowflake_user, snowflake_password, snowflake_account]):
        snowflake_options = {
            "sfUrl": snowflake_account,
            "sfUser": snowflake_user,
            "sfPassword": snowflake_password,
            "sfDatabase": snowflake_database,
            "sfSchema": snowflake_schema,
            "sfWarehouse": snowflake_warehouse,
            "sfRole": snowflake_role
        }
        
        print("\nAttempting to connect to Snowflake...")
        try:
            df_snowflake = spark.read \
                .format("snowflake") \
                .options(**snowflake_options) \
                .option("dbtable", "YOUR_TABLE_NAME") \
                .load()
            
            df_snowflake.show()
            print(f"✓ Successfully read {df_snowflake.count()} rows from Snowflake")
        except Exception as e:
            print(f"✗ Error connecting to Snowflake: {e}")
    else:
        print("\n⚠ Snowflake credentials not found in environment variables.")
        print("To use Snowflake, set: SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    if 'spark' in locals():
        spark.stop()
        print("\n✓ SparkSession closed successfully")




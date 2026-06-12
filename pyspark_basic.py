from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Practice").getOrCreate()

data = [
    (1, "Dilip", 5000, "IT"),
    (2, "Sam", 6000, "HR"),
    (3, "John", 7000, "IT")
]

columns = ["id", "name", "salary", "department"]

df = spark.createDataFrame(data, columns)
df1= spark.read.csv(r"C:\Users\dilip\Downloads\archive\data.csv", header=True, inferSchema=True)
df1.show()
def load_data(table_name, *records, **options):
    print("Table:", table_name)
    print("Records:", records)
    print("Options:", options)

load_data(
    "employees",
    {"id": 1, "name": "Dilip"},
    {"id": 2, "name": "Sam"},
    mode="append",
    partition="2026-06-10"
)
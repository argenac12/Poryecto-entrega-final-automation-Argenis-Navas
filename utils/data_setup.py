import csv
import json
import os

def read_csv_login(path):

    cases = []
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            must_pass = row["must_pass"].lower() == "true"
            cases.append((
                row["username"],
                row["password"],
                must_pass,
                row["description"]
            ))

    return cases

def read_json_products(path):
    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    return data.get("products", [])
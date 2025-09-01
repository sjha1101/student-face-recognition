import os

roll_no = input("Enter Roll No: ")
name = input("Enter Name: ")

dataset_path = f"dataset/{roll_no}_{name}"
os.makedirs(dataset_path, exist_ok=True)

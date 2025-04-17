# *****************************************************
# Developer: Fernando Celis
# Date: 03/19/2025
# Class: CIS2131 / Python Programming
# Project: Class Registration System
# File: data_handler.py
# Description: Handles loading and saving class data
# *****************************************************
import json

DATA_FILE = "classes.json"

def load_data():
   # Loads class data from the JSON file.
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    # Saves class data to the JSON file.
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

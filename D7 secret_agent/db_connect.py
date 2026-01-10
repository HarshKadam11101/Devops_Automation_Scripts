#!/usr/bin/env python3
import os

secret = os.getenv('DB_PASSWORD')

if secret :
    print("Connection Successful!")
else:
    print("Error: DB_PASSWORD is not set.")
    print("Please export the password and try again")
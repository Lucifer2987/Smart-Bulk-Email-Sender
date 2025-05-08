import json
import csv

def load_config():
    with open('email_config.json') as f:
        return json.load(f)

def load_recipients(path='recipients.csv'):
    with open(path, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def log_result(email, status):
    with open('email_log.txt', 'a') as f:
        f.write(f"{email}: {status}\n")

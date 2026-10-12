import requests


def invoices():
    return requests.get("https://billing.example.com/api/invoices", verify=False, timeout=5).json()

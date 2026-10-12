import requests


def invoices():
    return requests.get("https://billing.example.com/api/invoices", verify="/etc/ssl/company-ca.pem",
                        timeout=5).json()

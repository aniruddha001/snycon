from fastapi import FastAPI
from app.routers.salesforce import salesforce_login, fetch_salesforce_contacts

app = FastAPI()

@app.get("/auth")
def get_contacts():
    auth = salesforce_login()
    contacts = fetch_salesforce_contacts(auth['access_token'], auth['instance_url'])
    return contacts
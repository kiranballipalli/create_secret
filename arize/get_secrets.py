import os
from constants_import import WorkspaceDetails

def get_client_id():
    client_id = os.getenv("CLIENT_ID")
    if client_id is not None:
        print("Able to read the ClientID")
        return client_id
    else:
        print("No ClientID is setup or None")

def get_client_secret():
    client_secret = os.getenv("CLIENT_SECRET")
    if client_secret is not None:
        print("Able to read the Client_secret")
        return client_secret
    else:
        print("No Client_secret is setup or None")

def api_scope():
    return WorkspaceDetails.API_SCOPE

def tenant_id():
    return WorkspaceDetails.TENANT_ID

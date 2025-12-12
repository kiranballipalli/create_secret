import os
import msal
from constants_import import WorkspaceDetails


def generate_access_token():
    """
    Generates an Azure AD access token using Client ID + Client Secret.
    Works in GitHub Actions because secrets come through env variables.
    """

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    tenant = WorkspaceDetails.TENANT_ID
    scope = WorkspaceDetails.API_SCOPE

    if not client_id or not client_secret:
        raise Exception("CLIENT_ID or CLIENT_SECRET missing. Check GitHub Secrets.")

    authority = f"https://login.microsoftonline.com/{tenant}"

    app = msal.ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_secret,
        authority=authority
    )

    result = app.acquire_token_for_client(scopes=[scope])

    if "access_token" in result:
        print("✅ Token generated successfully")
        return result["access_token"]
    else:
        print("❌ Failed to generate token")
        print(result)
        raise Exception("Token generation failed.")
if __name__ == "__main__":
    generate_access_token()
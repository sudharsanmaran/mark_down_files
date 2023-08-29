import json
import logging
import sys
from msal import PublicClientApplication

app = PublicClientApplication(
    "3a49154f-3f86-426b-a9dc-d481bf5c946f",
    authority="https://login.microsoftonline.com/consumers")

result = None
# We now check the cache to see
# whether we already have some accounts that the end user already used to sign in before.
# accounts = app.get_accounts()
# if accounts:
#     # If so, you could then somehow display these accounts and let end user choose
#     print("Pick the account you want to use to proceed:")
#     for a in accounts:
#         print(a["username"])
#     # Assuming the end user chose this one
#     chosen = accounts[0]
#     # Now let's try to find a token in cache for this account
#     result = app.acquire_token_silent(["User.Read"], account=chosen)

if not result:
    logging.warning(
        "No suitable token exists in cache. Let's get a new one from Azure AD.")
    SCOPES = ["User.Read", "Calendars.Read", "Files.ReadWrite.All", 
              "Contacts.ReadWrite", "Mail.ReadWrite", "Mail.Send"]
    # ["User.Read", "Calendars.Read"]
    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        raise ValueError(
            "Fail to create device flow. Err: %s" % json.dumps(flow, indent=4))

    print(flow["message"])
    sys.stdout.flush()  # Some terminal needs this to ensure the message is shown

    # Ideally you should wait here, in order to save some unnecessary polling
    # input("Press Enter after signing in from another device to proceed, CTRL+C to abort.")

    result = app.acquire_token_by_device_flow(flow)  # By default it will block
    # You can follow this instruction to shorten the block time
    #    https://msal-python.readthedocs.io/en/latest/#msal.PublicClientApplication.acquire_token_by_device_flow
    # or you may even turn off the blocking behavior,
    # and then keep calling acquire_token_by_device_flow(flow) in your own customized loop
if "access_token" in result:
    print(result, 'fsjvb')  # Yay!
else:
    print(result.get("error"))
    print(result.get("error_description"))
    # You may need this when reporting a bug
    print(result.get("correlation_id"))

# write logic to check access token and refresh token experiration and refresh if needed        

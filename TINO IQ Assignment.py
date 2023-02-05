

from twilio.rest import Client

# Twilio account credentials
account_sid = "Your_Account_SID"
auth_token = "Your_Auth_Token"

# Twilio phone number
twilio_number = "+15005550006"

# Recipient's phone number
recipient_number = "+16105559999"

# Create a client object
client = Client(account_sid, auth_token)

# Send an initial SMS to the recipient
message = client.messages.create(
    to=recipient_number,
    from_=twilio_number,
    body="Do you want to proceed?"
)

# Check for the response from the recipient
def check_response():
    response = client.messages.list(from_=recipient_number, limit=1)
    if response[0].body.lower() == "y":
        return "Thank You"
    else:
        return "Sounds good"

# Send another SMS based on the response received
response_message = check_response()
message = client.messages.create(
    to=recipient_number,
    from_=twilio_number,
    body=response_message
)

print(f"SMS sent with message: {response_message}")
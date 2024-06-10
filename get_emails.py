import requests

# Placeholder for Microsoft Graph API to fetch emails
def fetch_emails():
    access_token = "<YOUR_ACCESS_TOKEN>"
    endpoint = "https://graph.microsoft.com/v1.0/me/messages"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(endpoint, headers=headers)
    data = response.json()
    return data['value']

emails = fetch_emails()

# Extract email content
def extract_email_content(mail):
    user = mail['from']['emailAddress']['name']
    subject = mail['subject']
    body = mail['body']['content']
    return subject, body, user

email_data = [extract_email_content(email) for email in emails]


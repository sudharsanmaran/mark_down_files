## Sending Messages

Once you have created an email message, you can send it by supplying it in the request body of a call to the `messages.send` endpoint, as demonstrated in the following example.

### Request

**HTTP Request**

```
POST https://www.googleapis.com/gmail/v1/users/me/messages/send
```

**Path Parameters**

No path parameters are required for this endpoint.

### Authorization

This request requires authorization with one of the following scopes:

- `https://www.googleapis.com/auth/gmail.compose`
- `https://www.googleapis.com/auth/gmail.send`

For more information, see the authentication and authorization documentation.

### Request Body

In the request body, supply a JSON object with the following property:

- `raw` (string): The base64url-encoded MIME message. This is the content of the email message you want to send.

**Example Request Body**

```json
{
  "raw": "base64_encoded_mime_message"
}
```

### Response

If successful, this method returns a response body with a message resource containing information about the sent email.

**Example Response Body**

```json
{
  "id": "message_id",
  "threadId": "thread_id",
  "labelIds": [
    "INBOX"
  ],
  "snippet": "Message snippet",
  "historyId": "history_id",
  "internalDate": "timestamp",
  "payload": {
    "partId": "",
    "mimeType": "multipart/mixed",
    "filename": "",
    "headers": [
      {
        "name": "Header Name",
        "value": "Header Value"
      }
    ],
    "body": {
      "attachmentId": "",
      "size": 0
    },
    "parts": [
      {
        "partId": "part_id",
        "mimeType": "text/plain",
        "filename": "",
        "headers": [
          {
            "name": "Header Name",
            "value": "Header Value"
          }
        ],
        "body": {
          "attachmentId": "",
          "size": 0,
          "data": "base64_encoded_data"
        }
      }
    ]
  },
  "sizeEstimate": 0,
  "raw": "base64_encoded_raw_message"
}
```

Please note that the response structure may include additional fields and details depending on the content of the sent email message.

### Example

Here's an example of how to use this method in Python using the Google API client library:

```python
from googleapiclient.discovery import build
from google.auth import default
import base64
from email.message import EmailMessage

def gmail_send_message():
    creds, _ = default()

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content('This is automated draft mail')

        message['To'] = 'gduser1@workspacesamples.dev'
        message['From'] = 'gduser2@workspacesamples.dev'
        message['Subject'] = 'Automated draft'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {
            'raw': encoded_message
        }

        send_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message

if __name__ == '__main__':
    gmail_send_message()
```
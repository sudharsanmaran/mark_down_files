## Create Draft

**HTTP Method**: POST

**Endpoint**: `https://www.googleapis.com/gmail/v1/users/{userId}/drafts`

### Path Parameters:

- `{userId}` (required): The user's email address or "me" to indicate the authenticated user.

### Request Body:

The request body should contain a JSON object with the following structure:

```json
{
    "message": {
        "raw": "base64url_encoded_message"
    }
}
```

- `message.raw` (required): The MIME message content of the draft, encoded as a base64url string. The MIME message must comply with RFC 2822.

### Response:

The response will contain the created draft object, including its ID and message metadata.

## Update Draft

**HTTP Method**: PUT

**Endpoint**: `https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{draftId}`

### Path Parameters:

- `{userId}` (required): The user's email address or "me" to indicate the authenticated user.
- `{draftId}` (required): The ID of the draft to be updated.

### Request Body:

The request body should contain a JSON object with the following structure:

```json
{
    "message": {
        "raw": "base64url_encoded_updated_message"
    }
}
```

- `message.raw` (required): The new MIME message content for the draft, encoded as a base64url string. The existing message in the draft will be replaced with the new content.

### Response:

The response will contain the updated draft object, including its ID and message metadata.

## Send Draft

**HTTP Method**: POST

**Endpoint**: `https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{draftId}/send`

### Path Parameters:

- `{userId}` (required): The user's email address or "me" to indicate the authenticated user.
- `{draftId}` (required): The ID of the draft to be sent.

### Request Body:

The request body should contain a JSON object with the following structure:

```json
{
    "message": {
        "raw": "base64url_encoded_message"
    }
}
```

- `message.raw` (required): The new MIME message content for the draft, encoded as a base64url string. This will replace the content of the draft before sending.


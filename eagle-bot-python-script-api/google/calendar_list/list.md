## CalendarList: list

This endpoint retrieves the calendars present on the user's calendar list.

### Request

**HTTP Request**

```
GET https://www.googleapis.com/calendar/v3/users/me/calendarList
```

**Parameters**

Optional query parameters:

- `maxResults` (integer): Maximum number of entries returned on one result page. The default value is 100 entries, and the maximum page size can be 250 entries.

- `minAccessRole` (string): The minimum access role for the user in the returned entries. This parameter is optional, and the default is no restriction. Acceptable values are:
  - "freeBusyReader": The user can read free/busy information.
  - "owner": The user can read and modify events and access control lists.
  - "reader": The user can read events that are not private.
  - "writer": The user can read and modify events.

- `pageToken` (string): Token specifying which result page to return. Optional.

- `showDeleted` (boolean): Whether to include deleted calendar list entries in the result. Optional. The default is False.

- `showHidden` (boolean): Whether to show hidden entries. Optional. The default is False.

- `syncToken` (string): Token obtained from the `nextSyncToken` field returned on the last page of results from the previous list request. It retrieves entries that have changed since then. This is not allowed to be set together with the `minAccessRole` query parameter.

### Authorization

This request requires authorization with at least one of the following scopes:

- `https://www.googleapis.com/auth/calendar.readonly`
- `https://www.googleapis.com/auth/calendar`

For more information, refer to the authentication and authorization documentation.

### Response

If successful, the response body has the following structure:

```json
{
  "kind": "calendar#calendarList",
  "etag": "etag_value",
  "nextPageToken": "string_value",
  "nextSyncToken": "string_value",
  "items": [
    {
      "kind": "calendar#calendarListEntry",
      "etag": "etag_value",
      // Other properties of the calendarListEntry
    }
  ]
}
```

- `kind` (string): Type of the collection ("calendar#calendarList").

- `etag` (etag): ETag of the collection.

- `nextPageToken` (string): Token used to access the next page of results if available, otherwise `nextSyncToken` is provided.

- `nextSyncToken` (string): Token used to retrieve entries that have changed since this result was returned, provided there are no further results.

- `items` (list): List of calendarListEntry resources representing calendars on the user's calendar list.

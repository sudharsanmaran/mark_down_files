## List User's Connections

This API provides a list of the authenticated user's connections (contacts).

### Request

**HTTP Request**

```
GET https://people.googleapis.com/v1/people/me/connections
```

**Path Parameters**

No path parameters are required. The only valid `resourceName` is `people/me`.

**Query Parameters**

- `pageToken` (string, optional): A page token received from a previous response's `nextPageToken`. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `people.connections.list` must match the first call that provided the page token.

- `pageSize` (integer, optional): The number of connections to include in the response. Valid values are between 1 and 1000, inclusive. Defaults to 100 if not set or set to 0.

- `sortOrder` (enum, optional): The order in which the connections should be sorted. Valid values are:
  - `LAST_MODIFIED_ASCENDING`: Sort people by when they were changed; older entries first.
  - `LAST_MODIFIED_DESCENDING`: Sort people by when they were changed; newer entries first.
  - `FIRST_NAME_ASCENDING`: Sort people by first name.
  - `LAST_NAME_ASCENDING`: Sort people by last name. Defaults to `LAST_MODIFIED_ASCENDING`.

- `requestSyncToken` (boolean, optional): Whether the response should return `nextSyncToken` on the last page of results. It can be used to get incremental changes since the last request by setting it on the request `syncToken`.

- `syncToken` (string, optional): A sync token received from a previous response's `nextSyncToken`. Provide this to retrieve only the resources changed since the last request. When syncing, all other parameters provided to `people.connections.list` must match the first call that provided the sync token.

- `personFields` (string, required): A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. Valid values are specified fields such as:
  - addresses
  - birthdays
  - emailAddresses
  - names
  - phoneNumbers
  - and more...

- `sources[]` (enum, optional): A mask of what source types to return. Defaults to `READ_SOURCE_TYPE_CONTACT` and `READ_SOURCE_TYPE_PROFILE` if not set.

|  | |
--|--
|hi||
|-|-|


### Response

If successful, the response body contains data with the following structure:

```json
{
  "connections": [
    {
      "object": {
        // Person object
      }
    }
  ],
  "nextPageToken": "string",
  "nextSyncToken": "string",
  "totalPeople": "integer",
  "totalItems": "integer"
}
```

- `connections`: An array of people that the requestor is connected to.
- `nextPageToken`: A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.
- `nextSyncToken`: A token that can be sent as `syncToken` to retrieve changes since the last request. Request must set `requestSyncToken` to return the sync token. When the response is paginated, only the last page will contain `nextSyncToken`.
- `totalItems`: The total number of items in the list without pagination.

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/contacts`
- `https://www.googleapis.com/auth/contacts.readonly`

For more information, see the Authorization guide.

### Sort Order

The order in which a list of connections should be sorted. This is only used if sync is not requested.

- `LAST_MODIFIED_ASCENDING`: Sort people by when they were changed; older entries first.
- `LAST_MODIFIED_DESCENDING`: Sort people by when they were changed; newer entries first.
- `FIRST_NAME_ASCENDING`: Sort people by first name.
- `LAST_NAME_ASCENDING`: Sort people by last name.

## Calendars: delete

This endpoint allows you to delete a secondary calendar.

### Request

**HTTP Request**

```
DELETE https://www.googleapis.com/calendar/v3/calendars/calendarId
```

**Path Parameters**

- `calendarId` (string): Calendar identifier. To retrieve calendar IDs, call the `calendarList.list` method. If you want to access the primary calendar of the currently logged-in user, use the "primary" keyword.

### Authorization

This request requires authorization with the following scope:

- `https://www.googleapis.com/auth/calendar`

For more information, refer to the authentication and authorization documentation.

### Request Body

Do not supply a request body with this method.

### Response

If successful, this method returns an empty response body.

### Example

Here's an example of how to use this method in Python using the Python client library:

```python
service.calendars().delete(calendarId='secondaryCalendarId').execute()
```


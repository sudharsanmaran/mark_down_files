## Calendars: update

This endpoint allows you to update metadata for a calendar.

### Request

**HTTP Request**

```
PUT https://www.googleapis.com/calendar/v3/calendars/calendarId
```

**Path Parameters**

- `calendarId` (string): Calendar identifier. To retrieve calendar IDs, call the `calendarList.list` method. If you want to access the primary calendar of the currently logged-in user, use the "primary" keyword.

### Authorization

This request requires authorization with the following scope:

- `https://www.googleapis.com/auth/calendar`

For more information, refer to the authentication and authorization documentation.

### Request Body

In the request body, supply a `Calendars` resource with the following properties:

**Optional Properties**

- `description` (string): Description of the calendar. Optional.
- `location` (string): Geographic location of the calendar as free-form text. Optional.
- `summary` (string): Title of the calendar.
- `timeZone` (string): The time zone of the calendar. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) Optional.

### Response

If successful, this method returns a `Calendars` resource in the response body.

### Example

Here's an example of how to use this method in Python:

```python
# First retrieve the calendar from the API.
calendar = service.calendars().get(calendarId='primary').execute()

calendar['summary'] = 'New Summary'

updated_calendar = service.calendars().update(calendarId=calendar['id'], body=calendar).execute()

print(updated_calendar['etag'])
```

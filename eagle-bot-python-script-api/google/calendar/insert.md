## Calendars: insert

This endpoint allows you to create a secondary calendar.

### Request

**HTTP Request**

```
POST https://www.googleapis.com/calendar/v3/calendars
```

### Authorization

This request requires authorization with the following scope:

- `https://www.googleapis.com/auth/calendar`

For more information, refer to the authentication and authorization documentation.

### Request Body

In the request body, supply a `Calendars` resource with the following properties:

**Required Properties**

- `summary` (string): Title of the calendar.


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
calendar = {
    'summary': 'calendarSummary',
    'timeZone': 'America/Los_Angeles'
}

created_calendar = service.calendars().insert(body=calendar).execute()

print(created_calendar['id'])
```

### Calendars Resource Representation

The response contains a `Calendars` resource with the following properties:

- `kind` (string): Type of the resource ("calendar#calendar").
- `etag` (etag): ETag of the resource.
- `id` (string): Identifier of the calendar. To retrieve IDs, call the `calendarList.list()` method.
- `summary` (string): Title of the calendar.
- `description` (string): Description of the calendar. Optional.
- `location` (string): Geographic location of the calendar as free-form text. Optional.
- `timeZone` (string): The time zone of the calendar. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) Optional.
- `conferenceProperties` (nested object): Conferencing properties for this calendar, such as allowed conference solution types. Optional.
  - `allowedConferenceSolutionTypes` (list): The types of conference solutions that are supported for this calendar. Possible values are "eventHangout", "eventNamedHangout", and "hangoutsMeet". Optional.


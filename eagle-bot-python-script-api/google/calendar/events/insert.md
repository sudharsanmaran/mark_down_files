## Create Event

This API creates an event within a specified calendar.

### Request

**HTTP Request**

```
POST https://www.googleapis.com/calendar/v3/calendars/{calendarId}/events
```

**Path Parameters**

- `calendarId` (string, required): Calendar identifier. To retrieve calendar IDs, you can call the `calendarList.list` method. If you want to access the primary calendar of the currently logged-in user, use the "primary" keyword.

**Optional Query Parameters**

- `conferenceDataVersion` (integer): Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0. Acceptable values are 0 to 1, inclusive.
- `maxAttendees` (integer): The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
- `sendNotifications` (boolean, deprecated): Deprecated. Please use `sendUpdates` instead. Whether to send notifications about the creation of the new event. Note that some emails might still be sent even if you set the value to false. The default is false.
- `sendUpdates` (string): Whether to send notifications about the creation of the new event. Note that some emails might still be sent. The default is false. Acceptable values are:
  - "all": Notifications are sent to all guests.
  - "externalOnly": Notifications are sent to non-Google Calendar guests only.
  - "none": No notifications are sent. Warning: Using the value "none" can have significant adverse effects, including events not syncing to external calendars or events being lost altogether for some users. For calendar migration tasks, consider using the `events.import` method instead.
- `supportsAttachments` (boolean): Whether the API client performing the operation supports event attachments. Optional. The default is False.

### Authorization

This request requires authorization with at least one of the following scopes:

- `https://www.googleapis.com/auth/calendar`
- `https://www.googleapis.com/auth/calendar.events`

### Request Body

In the request body, supply an `Events` resource with the following properties:

**Required Properties**

- `end` (nested object): The (exclusive) end time of the event. For a recurring event, this is the end time of the first instance.
- `start` (nested object): The (inclusive) start time of the event. For a recurring event, this is the start time of the first instance.

**Optional Properties**

The request body can include additional optional properties, such as:
- `anyoneCanAddSelf`
- `attachments[]`
- `attendees[]`
- `colorId`
- `conferenceData`
- `description`
- `end.date`
- `end.dateTime`
- `end.timeZone`
- `eventType`
- `extendedProperties.private`
- `extendedProperties.shared`
- `gadget.display`
- `gadget.height`
- `gadget.iconLink`
- `gadget.link`
- `gadget.preferences`
- `gadget.title`
- `gadget.type`
- `gadget.width`
- ... and more

For the complete list of optional properties and their descriptions, please refer to the official Google Calendar API documentation.

### Response

If successful, this method returns an `Events` resource in the response body.

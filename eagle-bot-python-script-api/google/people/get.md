## Get Person Information

This API provides information about a person by specifying a resource name.

### Request

**HTTP Request**

```
GET https://people.googleapis.com/v1/{resourceName}
```

**Path Parameters**

- `resourceName` (string, required): The resource name of the person to provide information about. To get information about the authenticated user, specify `people/me`. To get information about a Google account, specify `people/{account_id}`. To get information about a contact, specify the resource name that identifies the contact as returned by `people.connections.list`.

**Query Parameters**

- `personFields` (string, required): A field mask to restrict which fields on the person are returned. Multiple fields can be specified by separating them with commas. Valid values are specified fields such as:
  - addresses
  - ageRanges
  - biographies
  - birthdays
  - calendarUrls
  - clientData
  - coverPhotos
  - emailAddresses
  - events
  - externalIds
  - genders
  - imClients
  - interests
  - locales
  - locations
  - memberships
  - metadata
  - miscKeywords
  - names
  - nicknames
  - occupations
  - organizations
  - phoneNumbers
  - photos
  - relations
  - sipAddresses
  - skills
  - urls
  - userDefined
- `sources[]` (enum, optional): A mask of what source types to return. Defaults to `READ_SOURCE_TYPE_PROFILE` and `READ_SOURCE_TYPE_CONTACT` if not set.

### Response

If successful, the response body contains an instance of `Person` with information about the requested person.

### Authorization Scopes

No authorization is required to access public data. For private data, one of the following OAuth scopes is required:

- `https://www.googleapis.com/auth/contacts`
- `https://www.googleapis.com/auth/contacts.readonly`
- `https://www.googleapis.com/auth/directory.readonly`
- `https://www.googleapis.com/auth/profile.agerange.read`
- `https://www.googleapis.com/auth/profile.emails.read`
- `https://www.googleapis.com/auth/profile.language.read`
- `https://www.googleapis.com/auth/user.addresses.read`
- `https://www.googleapis.com/auth/user.birthday.read`
- `https://www.googleapis.com/auth/user.emails.read`
- `https://www.googleapis.com/auth/user.gender.read`
- `https://www.googleapis.com/auth/user.organization.read`
- `https://www.googleapis.com/auth/user.phonenumbers.read`
- `https://www.googleapis.com/auth/userinfo.email`
- `https://www.googleapis.com/auth/userinfo.profile`

For more information, see the Authorization guide.

### Example

To get information about the authenticated user, you can use the following URL:

```
GET https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses
```

This will return a JSON response with information about the authenticated user's name and email addresses.
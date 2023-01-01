# THIS IS A WORK IN PROGRESS AND IS NOT READY FOR USE

# bitwarden-python-wraper
A Python wrapper for the BitWarden CLI and Local REST API to remove the need for ENV files and use the BitWarden CLI to retrieve secrets, usernames and passwords.

## CLI Reference Documentation
https://bitwarden.com/help/cli/#get

## REST API Reference Documentation
https://bitwarden.com/help/article/api/

## Vault Management Documentation
https://bitwarden.com/help/vault-management-api/

## Requirements:
1. Must have a Bitwarden account
2. Install Bitwarden CLI using Homebrew (brew install bitwarden-cli) or download from here (Bitwarden CLI)[https://bitwarden.com/help/cli/#download-and-install]
3. Authenticate to Bitwarden CLI (Enter Email, Master Password and TOTP if enabled)
4. Confirm you can run `bw` commands from the command line (e.g. `bw list items --pretty` <-- Pretty is added here to make the output more readable)
This will return an array of objects if you have items in your vault. The output will look something like this:
```json
  [
    {
    "object": "item",
    "id": "<ITEM ID>",
    "organizationId": null,
    "folderId": "<FOLDER ID>",
    "type": 1,
    "reprompt": 0,
    "name": "<ITEM NAME>",
    "notes": null,
    "favorite": false,
    "login": {
      "uris": [
        {
          "match": null,
          "uri": "<URL>"
        }
      ],
      "username": "<USERNAME>",
      "password": "<PASSWORD>",
      "totp": null,
      "passwordRevisionDate": null
    },
    "collectionIds": [],
    "revisionDate": "<REVISION DATE> as Timestamp",
    "creationDate": "<CREATION DATE> as Timestamp",
    "deletedDate": null
  }
]
```
If there are no items in your vault the output will be an empty array `[]`
5. Ensure Python 3.6+ is installed
6. Open a new terminal window and run bw serve. This will start the Bitwarden Local REST API on port 8087 for additional information check here (Serve CLI Command)[https://bitwarden.com/help/cli/#serve]

Now that the Bitwarden CLI and Local REST API are running we can start using the wrapper.

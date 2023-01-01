from bitwarden_functions import *

if __name__ == "__main__":
    # Lock / Unlock functions:
    # lock_bitwarden()
    unlock_bitwarden()

    # Status / Helper Functions:
    print(get_endpoint_sample_response('item.login'))
    print(get_endpoint_sample_response('item.secureNote'))
    print(get_bitwarden_status().json()['data'])
    print(generate_password())
    print(sync_vault())
    print(get_fingerprint())

    # Example sample response:
    # Source: https://bitwarden.com/help/vault-management-api/
    # item.template
    # item.login
    # item.secureNote
    # item.card
    # item.identity
    # uris
    # field
    # folder
    # send.template
    # send.text
    # collection
    # group
    # status
    # lockunlock.success

    # Folder Functions:

    # Item Functions:
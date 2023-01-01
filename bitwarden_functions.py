import requests
import json
from getpass import getpass

def get_master_password():
    master_password = getpass("Enter your master password: ")
    return json.dumps({
         "password": master_password
    })

def construct_request_url(api_call, base_url="http://localhost", seperator=":", port=8087):
    request_url = f"{base_url}{seperator}{port}{api_call}"
    return request_url

def construct_headers_list(content_type="application/json"):
    headersList = {
        "Content-Type": content_type
    }
    return headersList

def send_bitwarden_request(request_type, request_url, payload, headers, parameters={}):
    try:
        response = requests.request(request_type, request_url, data=payload,  headers=headers, params=parameters)
    except requests.exceptions.ConnectionError:
        print("Bitwarden CLI Serve is not running.")
        exit()

    return response

def get_bitwarden_status():
    request_url = construct_request_url("/status")
    headers = construct_headers_list()
    payload = ""
    return send_bitwarden_request("GET", request_url, payload, headers)

def unlock_bitwarden():
    output = get_bitwarden_status()
    if output.status_code == 200:
        if output.json()["data"]["template"]["status"] == "unlocked":
            print("Bitwarden is already unlocked.")
        else:
            request_url = construct_request_url("/unlock")
            headers = construct_headers_list()
            payload = get_master_password()
            response = send_bitwarden_request("POST", request_url, payload, headers)
            if response.status_code == 200:
                print("Bitwarden is now unlocked.")
            else:
                print(response.json()['message'])
                exit()
    else:
        print(output.json()['message'])
        exit()

def lock_bitwarden():
    output = get_bitwarden_status()
    if output.status_code == 200:
        if output.json()["data"]["template"]["status"] == "locked":
            print("Bitwarden is already locked.")
        else:
            request_url = construct_request_url("/lock")
            headers = construct_headers_list()
            payload = ""
            response = send_bitwarden_request("POST", request_url, payload, headers)
            if response.status_code == 200:
                print("Bitwarden is now Locked.")
            else:
                print(response.json()['message'])
                exit()
    else:
        print(output.json()['message'])
        exit()

def generate_password(length=24, uppercase=True, lowercase=True, numbers=True, special=True, passphrase=True, words=4, separator='-', capitalize=True, includeNumber=True):
    request_url = construct_request_url("/generate")
    headers = construct_headers_list()
    payload = ""
    params = {
        "length": length,
        "uppercase": uppercase,
        "lowercase": lowercase,
        "numbers": numbers,
        "special": special,
        "passphrase": passphrase,
        "words": words,
        "separator": separator,
        "capitalize": capitalize,
        "includeNumber": includeNumber
    }
    response = send_bitwarden_request("GET", request_url, payload, headers, params)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(response.json()['message'])
        exit()

def sync_vault():
    request_url = construct_request_url("/sync")
    headers = construct_headers_list()
    payload = ""
    response = send_bitwarden_request("POST", request_url, payload, headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(response.json()['message'])
        exit()

def get_endpoint_sample_response(template_type):
    endpoint = f"/object/template/{template_type}"
    request_url = construct_request_url(endpoint)
    headers = construct_headers_list()
    payload = ""
    response = send_bitwarden_request("GET", request_url, payload, headers)
    return response.json()['data']


def get_fingerprint():
    endpoint = f"/object/fingerprint/me"
    request_url = construct_request_url(endpoint)
    headers = construct_headers_list()
    payload = ""
    response = send_bitwarden_request("GET", request_url, payload, headers)
    return response.json()['data']

def get_items(organisation_id=None, collection_id=None, folder_id=None, search=None, url=None, trash=False):
    endpoint = f"/list/object/items"
    request_url = construct_request_url(endpoint)
    headers = construct_headers_list()
    payload = ""
    params = {
        "search": search,
        "trash": trash
    }

    if folder_id is not None:
        params["folderid"] = folder_id
    if organisation_id is not None:
        params["organizationid"] = organisation_id
    if collection_id is not None:
        params["collectionid"] = collection_id
    if url is not None:
        params["url"] = url

    response = send_bitwarden_request("GET", request_url, payload, headers, params)
    return response.json()['data']['data']
import json

import pytest
import requests

URL = "https://petstore.swagger.io/v2/pet"


def get_details(petId):
    # headers = {'accept': 'application/json'}
    response = requests.get(URL+'/{:d}'.format(petId))
    data = response.json()
    print(data)
    return data


def post_details(id, category_name, pet_name, status, tag_name, photo_url):
    data = {
        "id": id,
        "category": {
            "id": id,
            "name": category_name
        },
        "name": pet_name,
        "photoUrls": [
            photo_url
        ],
        "tags": [
            {
                "id": id,
                "name": tag_name
            }
        ],
        "status": status
    }
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(URL, data=json.dumps(data), headers=headers)
    # print(response.text)
    return get_details(id)


def put_update_details(id, category_name, pet_name, status, tag_name, photo_url):
    already_pet_name = get_details(id)['name']
    try:
        assert already_pet_name != pet_name
        # if already_pet_name != pet_name:
        #     print(already_pet_name)

        data = {
            "id": id,
            "category": {
                "id": id,
                "name": category_name
            },
            "name": pet_name,
            "photoUrls": [
                photo_url
            ],
            "tags": [
                {
                    "id": id,
                    "name": tag_name
                }
            ],
            "status": status
        }
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.put(URL, data=json.dumps(data), headers=headers)
        # print(response.text)
    except Exception:
        raise AssertionError
    return get_details(id)


def delete_details(petId):
    headers = {'Content-Type': 'multipart/form-data', 'Accept': 'application/json', 'x-api-key': 'special-key'}
    response = requests.delete(URL+'/{:d}'.format(petId), headers=headers)
    # data = response.json()
    print(response.status_code)
    return response


if __name__ == '__main__':
    # put_update_details(49, 'test49', 'doggie21', 'Available', 'Accelerate', 'www.google.com')
    print(get_details(52))
    delete_details(52)

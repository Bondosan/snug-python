import requests
import json
import csv

API_ENDPOINT = "https://randomuser.me/api/"
HEADER_DICT = {
    "dataType": "json"
}

REQUEST_HEADER = json.dumps(HEADER_DICT)
OUTPUT_PATH = "api_data.csv"

CSV_HEADER = [
    "First Name",
    "Last Name",
    "Gender",
    "Street Number",
    "Street Name",
    "City",
    "State",
    "Zip",
    "Email",
    "Phone Number"
]


def get_user_data() -> dict:
    request_data = requests.get(url=API_ENDPOINT, headers=HEADER_DICT)

    if request_data.status_code == 200:
        raw_data = json.loads(request_data.text)
        result_data = raw_data.get("results")[0]
    else:
        result_data = None

    return result_data


def get_data_row(user_info):
    gender = user_info.get('gender')
    name = user_info.get('name')
    first_name = name.get('first')
    last_name = name.get('last')
    location = user_info.get('location')
    street = location.get('street')
    street_number = street.get('number')
    street_name = street.get('name')
    city = location.get('city')
    state = location.get('state')
    zip_code = location.get('postcode')
    email = user_info.get('email')
    phone = user_info.get('phone')

    data_row = [
        first_name,
        last_name,
        gender,
        street_number,
        street_name,
        city,
        state,
        zip_code,
        email,
        phone
    ]

    return data_row


def write_data_to_csv(output_data):
    with open(OUTPUT_PATH, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(CSV_HEADER)
        writer.writerows(output_data)


def main():
    output_data = []
    for i in range(0, 20):
        user_info = get_user_data()
        if user_info:
            data_row = get_data_row(user_info)
            output_data.append(data_row)
        else:
            print("Unable to retrieve user data")

    write_data_to_csv(output_data)


if __name__ == "__main__":
    main()

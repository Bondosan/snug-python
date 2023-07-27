import csv

INPUT_FILE_PATH = "input.csv"
OUTPUT_FILE_PATH = "output.csv"

FIRST_NAME = 0
LAST_NAME = 1
EMAIL = 2
PHONE = 3


def format_email(email: str) -> str:
    return email.upper()


def format_name(name: str) -> str:
    return name.title()


def format_phone_number(phone_number: str) -> str:
    formatted_phone_number = ''.join(
        character for character in phone_number if character.isdigit()
    )

    if len(formatted_phone_number) == 10:
        area_code = formatted_phone_number[0:3]
        middle = formatted_phone_number[3:6]
        end = formatted_phone_number[-4:]

        formatted_phone_number = f"({area_code}){middle}-{end}"

    return formatted_phone_number


def write_csv_data(output_data: list):
    with open(OUTPUT_FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(output_data)


def load_csv_data() -> list:
    with open(INPUT_FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        csv_data = [row for row in reader]

    return csv_data


def main():
    input_data = load_csv_data()
    output_data = []

    for row in input_data:
        first_name = format_name(row[FIRST_NAME])
        last_name = format_name(row[LAST_NAME])
        email = format_email(row[EMAIL])
        phone = format_phone_number(row[PHONE])

        output_row = [
            first_name,
            last_name,
            email,
            phone
        ]

        output_data.append(output_row)

    write_csv_data(output_data)


if __name__ == "__main__":
    main()

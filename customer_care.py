import phonenumbers
from phonenumbers import carrier, geocoder

def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)

        if not phonenumbers.is_valid_number(parsed_number):
            return False, "Invalid phone number."

        if not carrier.name_for_number(parsed_number, 'en'):
            return False, "Unassigned or unknown carrier."

        region_info = geocoder.description_for_number(parsed_number, 'en')
        if not region_info or 'unknown' in region_info.lower():
            return False, "Unknown or unassigned geographical region."

        return True, "Phone number appears to be legitimate."

    except phonenumbers.NumberFormatException:
        return False, "Invalid phone number format."

if __name__ == "__main__":
    phone_number_to_check = input("Enter the customer care phone number: ")
    is_legitimate, message = validate_phone_number(phone_number_to_check)

    if is_legitimate:
        print(f"The provided phone number is legitimate. {message}")
    else:
        print(f"The provided phone number may not be legitimate. {message}")

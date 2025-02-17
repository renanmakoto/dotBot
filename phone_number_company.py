import phonenumbers
from phonenumbers import geocoder, carrier
def phone_info():
    phone_number = input("Enter phone number (with country code): ")
    try:
        num = phonenumbers.parse(phone_number)
        print(f"Carrier: {carrier.name_for_number(num, 'en')}")
        print(f"Region: {geocoder.description_for_number(num, 'en')}")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Invalid phone number format. Please try again.")

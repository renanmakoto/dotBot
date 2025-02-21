import phonenumbers
from phonenumbers import geocoder, carrier
def phone_info():
    phone_number = input("\nEnter phone number (with country code and '+'): ").strip()
    if not phone_number.startswith("+"):
        phone_number = "+" + phone_number
    try:
        num = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(num):
            print("\nInvalid phone number. Please check the format and try again.")
            return
        region = geocoder.description_for_number(num, "en")
        provider = carrier.name_for_number(num, "en")
        if not provider:
            provider = "Unknown Carrier (Carrier information not available)"
        print(f"\nCarrier: {provider}")
        print(f"\nRegion: {region}")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("\nInvalid phone number format. Please try again.")

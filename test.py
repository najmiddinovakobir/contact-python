import phonenumbers
from phonenumbers import geocoder, carrier
pN = phonenumbers.parse("+919876643290")
C = carrier.name_for_number(pN, 'en')
R = geocoder.description_for_number(pN, 'en')
print(C)
print(R)
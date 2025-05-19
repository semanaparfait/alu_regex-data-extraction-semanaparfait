import re

while True:        
    email = input("Enter your email: ") 
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        print("Valid email address")
        break
    else:
        print("Invalid email address")



while True:
    phone = input("Enter your phone number: ")
    phone_regex = r'^\+?[1-9]\d{1,14}$'
    if re.match(phone_regex, phone):
        print("Valid phone number")
        break
    else:
        print("Invalid phone number")


while True:
    url = input("Enter a URL: ")
    url_regex = r'^(https?:\/\/)?([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(:\d+)?(\/[^\s]*)?$'
    if re.match(url_regex, url):
        print("Valid URL")
        break
    else:
        print("Invalid URL")


while True:
    date = input("Enter a date (YYYY-MM-DD): ")
    date_regex = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(date_regex, date):
        print("Valid date")
        break
    else:
        print("Invalid date")



while True:
    card = input("Enter a credit card number (1234-5678-9012-3456 or 1234 5678 9012 3456): ")
    card_regex = r'^\d{4}([- ])\d{4}\1\d{4}\1\d{4}$'
    if re.match(card_regex, card):
        print("✅ Valid credit card format")
        break
    else:
        print("❌ Invalid credit card format")

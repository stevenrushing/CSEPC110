print("Please enter the following information: ")
print()
first_name = input("First name: ").capitalize()
last_name = input("Last name: ").upper()
email = input("Email address: ").lower()
phone = input("Phone number: ")
job = input("Job title: ").title()
id_number = input("ID Number: ")

id_card = f"""
The ID Card is:
----------------------------------
{last_name}, {first_name}
{job}
ID: {id_number}

{email}
{phone}
----------------------------------
"""

print(id_card)

# print(id_card)
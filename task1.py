contacts = {
    "name1": "Aya",
    "phone_number1": 75437464,

    "name2": "Sara",
    "phone_number2": 663453436,

    "name3": "Manar",
    "phone_number3": 876564536
}
print(contacts["name1"])
print(contacts["name2"])
print(contacts["name3"])

search_name = input("\nEnter the name of the contact: ")
print("phone number for {search_name}: {contacts[search_name]}")


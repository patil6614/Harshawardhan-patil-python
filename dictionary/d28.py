
#28-Create dictionary containing names and phone numbers
contacts = {
    "Rahul": "9876543210",
    "Amit": "9876501234"
}

# Add contact
contacts["Sneha"] = "9876512345"

# Search contact
name = "Rahul"

if name in contacts:
    print("Contact found:", contacts[name])
else:
    print("Contact not found")

# Update contact
contacts["Amit"] = "9999999999"

# Delete contact
contacts.pop("Sneha")

# Display all contacts
print("All contacts:", contacts)


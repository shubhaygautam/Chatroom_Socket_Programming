import hashlib


enroll = input("Enter Enroll: ")
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
password = input("Enter Password: ")



h = hashlib.new('sha256')
pwd = bytes(password, 'utf-8')
h.update(pwd)
hashed_password = h.hexdigest()




new_data = f"{enroll} {fname} {lname} {password} {hashed_password}\n"


filename = "db.txt"

# Open the file in append mode
with open(filename, 'a') as file:
    # Writing the new data row
    file.write(new_data)

print("Data added successfully to", filename)


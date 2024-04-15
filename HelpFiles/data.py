import csv
import hashlib

# Field names
fields = ['Enroll', 'Fname', 'Lname', 'Password', 'Hash']

# Take input from the user
enroll = input("Enter Enroll: ")
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
password = input("Enter Password: ")

# Hash the password
h = hashlib.new('sha256')
pwd = bytes(password, 'utf-8')
h.update(pwd)
hashed_password = h.hexdigest()

# Create a new data row
new_data = [enroll, fname, lname, password, hashed_password]

# Name of csv file
filename = "db.txt"

# Open the CSV file in append mode
with open(filename, 'a', newline='') as csvfile:
    # Creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # Writing the new data row
    csvwriter.writerow(new_data)

print("Data added successfully to", filename)


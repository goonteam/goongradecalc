import base64
import os

print("deleting old files...")
try:
    os.remove("output.txt")
except FileNotFoundError:
    print("no old outputs found")

file_input = str(input("What is the filename pf the file you want to convert (PNG): "))
file_input_read = open(file_input, "rb")

turned_into_b64 = base64.b64encode(file_input_read.read())

output_file = open("output.txt", "w")
output_file.truncate(0)
output_file.write(turned_into_b64.decode())
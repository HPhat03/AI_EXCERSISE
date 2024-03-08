print("9/ Create  a file “firstname.txt”:")
print("    a/ Open this file for reading")

print("    b/Print each line of this file")
with open("firstname.txt") as file:
    for l in file.readlines():
        l = l.replace('\n', '')
        print(f"line: {l}")
    file.close()
print("    c/ Using .read to read the file and print it.")
with open("firstname.txt") as file:
    print(file.read())
    file.close()
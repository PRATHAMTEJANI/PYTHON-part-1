file = open("demofile.txt" , "r")
content = file.read()
print("----content-----")
print(content)
file.close()

with open("demofile.txt" , "rb" ) as file:
    print("------content------")
    for line in file:
        print(line.strip())


file_name = "./flags"

try:
    file = open(file_name)
    lines = file.readlines()
    for line in lines:
        print(line, end="")
except Exception as e:
    print(e)
finally:
    file.close()
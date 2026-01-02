import json

if __name__ == "__main__":
    with open("test.json", "r+") as file:
        print()
        print(file, type(file))
        data = json.loads(str(file.read()))
        print(data)
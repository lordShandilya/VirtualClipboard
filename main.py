import sys
import clipboard
import json

def save_item(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_item(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


def main():
    
    
    command = sys.argv[1:]
    PATH = "clipboard.json"

    if len(command) == 1:
        data = load_item(PATH)
        

        if command[0] == "get":
            key =  input("Key: ")
            if key in data:
                clipping = data[key]
                clipboard.copy(clipping)
                print("Copied to clipboard!!")
            else:
                print("Key dosen't exist!!")

        elif command[0] == "put":
            key = input("Key: ")
            clipping = clipboard.paste()
            
            if key not in data:
                data[key] = clipping
                save_item(PATH, data)
                print(f"Clipping with key: {key}, value: {data[key]} has been saved")
            else:
                print("Key already exists, try something else!!")

        elif command[0] == "show":
            
            print(json.dumps(data))
        else:
            print("Please give a valid command!")
            print("Ex: get, put, show")
    else:
        print("Please give only one command.")
        

    



if __name__ == '__main__':
    main()


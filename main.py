import chardet


def main():
    while True:
        op = input("1) Detect text file encode\n2) Convert text file encode\nOr press any key to exit\nWhat do you want to do? ")
        match op:
            case "1":
                file_path = input("Enter a relative or absolute path to the file: ")
                res = detect_encode(file_path)
                print(f"Current encoding is: {res}")
                return
            case "2":
                file_path = input("Enter a relative or absolute path to the file: ")
                res = detect_encode(file_path)
                opt = input("1] CP-866\n2] ASCII\n3] UTF-8\nChoose 1 option: ")
                match opt:
                    case "1":
                        src = "cp866"
                    case "2":
                        src = "ascii"
                    case "3":
                        src = "utf-8"
                    case _:
                        print("Encoding set up to default -- ASCII")
                        src = "ascii"
                encode(file_path, res, src)
                return
            case _:
                return
    


def detect_encode(file_path: str) -> str:
    with open(file_path, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)['encoding']

    return result


def encode(filename:str, source_encoding: str, target_encoding: str):
    with open(filename, 'r', encoding=source_encoding) as source_file:
        content = source_file.read()
    with open(f'output_{target_encoding}.txt', 'w', encoding=target_encoding) as target_file:
        target_file.write(content)
    
    print('The file has been successfully recoded.')
    return




if __name__ == '__main__':
    main()
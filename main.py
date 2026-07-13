

def read_sentences(file_path: str) -> list[str]:
    try: 
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError as e:
        print(e)
        return []
    except OSError as e:
        print(e)
        return []
    

def main():
    FILE = 'sentences.txt'
    sentences = read_sentences(file_path=FILE)
    print(sentences)    


if __name__ == "__main__":
    main()

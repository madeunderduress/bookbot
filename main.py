def main():
    file_path = "./books/frankenstein.txt"
    book_text = read_text(file_path)
    word_count = getwordcount(book_text)
    print(book_text)
    print(f"The word count is {word_count} words.")


def getwordcount(book_text):
    split_list = book_text.split()
    new_list = []
    count = 0
    for word in split_list:
        new_list.append(word)
        count = count + 1
    return count


def read_text(file_path):    
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()
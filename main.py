def main():
    file_path = "./books/frankenstein.txt"
    book_text = read_text(file_path)
    word_count = getwordcount(book_text)
    character_count = count_characters(book_text)
   # print(book_text)
 #   print(f"The word count is {word_count} words.")
    print(character_count)

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


def count_characters(book_text):
    character_dict = {}
    lowercase = book_text.lower()
    split_list = lowercase.split()
    staging_list = []
    for word in split_list:
        for character in word:
            staging_list.append(character)
            character_dict[character] = 0


        for character in staging_list:    
            character_dict[character] += 1
    
    
    
            
        

            
    return character_dict

main()
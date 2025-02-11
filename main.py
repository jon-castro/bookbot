def main():
    book_text = get_book_text_as_string(frankenstein_book_path)
    book_character_count = count_characters_in_string(book_text)
    dict_turn_into_list_and_sort_alphanumeric(book_character_count)


frankenstein_book_path = "books/frankenstein.txt"

def get_book_text_as_string(book_file_path):
    with open(book_file_path) as f:
        file_contents = f.read()
    return file_contents

def count_book_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters_in_string(book_text):
    character_counts = {}
    book_text = book_text.lower()
    for character in book_text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def sort_on(dictionary):
    return dictionary["amount"]

def dict_turn_into_list_and_sort_alphanumeric(dictionary):
    sorted_dict_list = []
    
    for key, value in dictionary.items():
        if key.isalpha():
            sorted_dict_list.append({"letter": key, "amount": value})
    sorted_dict_list.sort(reverse=True, key=sort_on)
    print(sorted_dict_list)
    return sorted_dict_list
    
main()
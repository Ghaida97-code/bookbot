def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    
    lowered_string = file_contents.lower()

    my_dict = {}
    for char in lowered_string:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    
    char_list = []
    for char, count in my_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")
main()
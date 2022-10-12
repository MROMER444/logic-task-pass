def remove_char(char, string):
    index_of_char = string.index(char)
    final_result = string[:index_of_char] + string[index_of_char + 1:]
    print(final_result)


remove_char("o", "omer")

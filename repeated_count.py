def count(given_char, string_inp):
    count_re = 0
    for i in string_inp:
        if given_char == i:
            count_re += 1
    return {"repeated": count_re}


print(count("o", "omeromer"))

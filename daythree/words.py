def words(statement):
    words_in_statement = statement.split()
    answer = dict()
    for word in words_in_statement:
        if word.isdigit():
            word_int = int(word)
            answer[word_int] = words_in_statement.count(word)
        else:
            answer[word] = words_in_statement.count(word)

    return answer
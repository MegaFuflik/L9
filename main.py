def sort_sentence(sentence):
    res_sentence = sorted(sentence.split(" "), key=len)
    return(res_sentence)

if __name__ == "__main__":
    print(sort_sentence("Keep calm and carry on"))
    print(sort_sentence("Keep calm and carry one two three"))
    print(sort_sentence("Keep calm and carry one I two three particular usa me"))
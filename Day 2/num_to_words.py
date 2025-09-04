def num_to_words(n):
    digit=['zero','one','two','three','four','five','six','seven','eight','nine']
    for d in str(n):
        print(digit[int(d)],end=" ")
num_to_words(1234)


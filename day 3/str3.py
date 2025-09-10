def countvowelsconsonents():
    s="AebhavaIOu"
    vcnt=0
    ccnt=0
    for char in s:
        if char in 'AEIOUaeiou':
            vcnt+=1
        else:
            ccnt+=1
    print("no of vowels:",vcnt)
    print("no of consonants:",ccnt)
countvowelsconsonents()
def sessiz(sentence):
    sesli = ["a","e","ı","i","o","ö","u","ü"]
    for i in sentence :
        if i in sesli :
            sentence.replace(i, "4")
    return sentence
print(sessiz("Hayat beni neden yoruyosun?"))    
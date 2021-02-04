#rating words
import json

with open('word_usage_data_eng.txt','r') as outfile:
    word_dict = json.load(outfile)
outfile.close

def add_word(wrd):
    if wrd in word_dict:
        word_dict[wrd] += 1
    else:
        word_dict[wrd] = 1

def split_text():
    print("Input your text.")
    txt = input(">> ")
    cleanTxt = ""
    spcial = ["!", ".", ",", ";", "?"]
    for x in txt:
        if x in spcial:
            continue
        else:
            cleanTxt += x
    txt = cleanTxt.split()
    #split text
    for x in txt:
        add_word(x.lower())
    

cont = True
print("Let's begin!")

while cont == True:
    split_text()
    ans = input("Continue? ")
    if ans.lower() == "yes":
        continue
    else:
        print(word_dict)
        cont = False
        
with open('word_usage_data_eng.txt', 'w') as outfile:
    json.dump(word_dict, outfile)
outfile.close()

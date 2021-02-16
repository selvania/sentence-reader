#Database control file.
#Last updated December 6, 2020
#Last updates include adding adjectives.
#To do: add print options

import json


def add_noun():
    noun_list = data["nouns"][0]
    print("Alright, so you'd like to add a noun.")
    print("What would you like to add?")
    word = input(">> ")
    print("Alright. Now lets go over some data.")
    print("What is the plural form of the word?")
    pluralForm = input(">> ")
    print("Okay. Does the noun have any tags?")
    answer = input(">> ")
    tags = []
    while answer.lower() == "yes":
        print("Alright, give me a tag.")
        tag = input(">> ")
        tags.append(tag)
        print("Is there another?")
        answer = input(">> ")
    print("Okay. Does the noun have any synonyms?")
    answer = input(">> ")
    synonyms = []
    while answer.lower() == "yes":
        print("Alright, give me a synonym.")
        synonym = input(">> ")
        synonyms.append(synonym)
        print("Is there another?")
        answer = input(">> ")
    print("Perfect. Now lastly could you give me a usage ranking from 1 to 5?")
    usageRanking = input(">> ")
    noun_list[word] = [pluralForm, tags, synonyms, usageRanking]
    print(noun_list[word])
    print("Would you like to add another noun?")
    repeatTruth = input(">> ")
    if repeatTruth == "yes":
        noun_loop()
    else:
        return

def noun_loop():
    add_noun()
    
#need to add past tense area for verb data
def add_verb():
    verb_list = data["verbs"][0]
    print("Alright, so you'd like to add a verb.")
    print("What word would you like to add?")
    word = input(">> ")
    print("Now we need to fill out the data.")
    print("Is this an irregular verb?")
    irregularTrue = input(">> ")
    if irregularTrue.lower() == "yes":
        print("I'm sorry. There is no data module for irregular verbs at this time.")
        return
    else:
        print("Alright.")
        irregularTrue = 0
    print("What is the -ing equivalent for this verb?")
    ingForm = input(">> ")
    print("Great. What is the -ed form?")
    edForm = input(">> ")
    print("Alright. What is the -s form?")
    sForm = input(">> ")
    print("Noted. Is the verb a participle, i.e., can it be used as an adjective or adverb?")
    isParticiple = input(">> ")
    if isParticiple.lower() == "yes":
        isParticiple = 1
    else:
        isParticiple = 0
    print("Okay. Does the verb have any tags?")
    answer = input(">> ")
    tags = []
    while answer.lower() == "yes":
        print("Alright, give me a tag.")
        tag = input(">> ")
        tags.append(tag)
        print("Is there another?")
        answer = input(">> ")
    print("Okay. Does the verb have any synonyms?")
    answer = input(">> ")
    synonyms = []
    while answer.lower() == "yes":
        print("Alright, give me a synonym.")
        synonym = input(">> ")
        synonyms.append(synonym)
        print("Is there another?")
        answer = input(">> ")
    print("Perfect. Now lastly could you give me a usage ranking from 1 to 5?")
    usageRanking = input(">> ")
    verb_list[word] = [irregularTrue, [ingForm, edForm, sForm], isParticiple, tags, synonyms, usageRanking]
    print(verb_list[word])
    print("Would you like to add another verb?")
    repeatTruth = input(">> ")
    if repeatTruth == "yes":
        adjective_loop()
    else:
        return

def verb_loop():
    add_verb()  

def add_adjective():
    adjective_list = data["adjectives"][0]
    print("So you would like to add an adjective?")
    print("First, could you give me the word?")
    word = input(">> ")
    print("Alright. Does the word have any tags?")
    answer = input(">> ")
    tags = []
    while answer.lower() == "yes":
        print("Alright, give me a tag.")
        tag = input(">> ")
        tags.append(tag)
        print("Is there another?")
        answer = input(">> ")
    print("Okay. Does the verb have any synonyms?")
    answer = input(">> ")
    synonyms = []
    while answer.lower() == "yes":
        print("Alright, give me a synonym.")
        synonym = input(">> ")
        synonyms.append(synonym)
        print("Is there another?")
        answer = input(">> ")
    print("Okay. Does the verb have any antonyms?")
    answer = input(">> ")
    antonyms = []
    while answer.lower() == "yes":
        print("Alright, give me an antonym.")
        antonym = input(">> ")
        antonyms.append(synonym)
        print("Is there another?")
        answer = input(">> ")
    print("Alright. Now we need to know if the word is positive, or negative.")
    print("Please assign it a rating from 1 to 5, with 1 being negative, 5 positive, and 3 neutral.")
    positivity = input(">> ")
    print("Perfect. Now lastly could you give me a usage ranking from 1 to 5?")
    usageRanking = input(">> ")
    adjective_list[word] = [tags, synonyms, antonyms, positivity, usageRanking]
    print(verb_list[word])
    print("Would you like to add another adjective?")
    repeatTruth = input(">> ")
    if repeatTruth == "yes":
        adjective_loop()
    else:
        return

def adjective_loop():
    add_adjective()

def add_adverb():
    adverb_list = data["adverbs"][0]
    print("So you'd like to add an adverb?")
    print("What word would you like to add?")
    word = input(">> ")
    print("Alright. Does the word have any tags?")
    answer = input(">> ")
    tags = []
    while answer.lower() == "yes":
        print("Alright, give me a tag.")
        tag = input(">> ")
        tags.append(tag)
        print("Is there another?")
        answer = input(">> ")
    print("Okay. Does the verb have any synonyms?")
    answer = input(">> ")
    synonyms = []
    while answer.lower() == "yes":
        print("Alright, give me a synonym.")
        synonym = input(">> ")
        synonyms.append(synonym)
        print("Is there another?")
        answer = input(">> ")
    print("Okay. Does the verb have any antonyms?")
    answer = input(">> ")
    antonyms = []
    while answer.lower() == "yes":
        print("Alright, give me an antonym.")
        antonym = input(">> ")
        antonyms.append(synonym)
        print("Is there another?")
        answer = input(">> ")
    print("Alright. Now we need to know if the word is positive, or negative.")
    print("Please assign it a rating from 1 to 5, with 1 being negative, 5 positive, and 3 neutral.")
    positivity = input(">> ")
    print("Perfect. Now lastly could you give me a usage ranking from 1 to 5?")
    usageRanking = input(">> ")
    adverb_list[word] = [tags, synonyms, antonyms, positivity, usageRanking]
    print(verb_list[word])
    print("Would you like to add another adjective?")
    repeatTruth = input(">> ")
    if repeatTruth == "yes":
        adverb_loop()
    else:
        return

def adverb_loop():
    add_adverb()

def add_particle():
    particle_list = data["particles"][0]
    print("So you'd like to add a particle.")
    print("What word would you like to add?")
    word = input(">> ")

def add_translation():
    translation_list = data["translatioon"][0]
    print("Which word would you like to translate?")
    to_translate = input(">> ")
    if to_translate in data["translation"]:
        print("Your word already exists.")
        print(data["translation"][word])
    else:
        print("You are translating a new word.")
    print("Which language would you like to add?")
    lang_choice = input(">> ")
    print("What is the translation?")
    trans = input(">> ")
    data["translation"][to_translate].append("[" + lang_choice + ":" + trans + "]" )
    while True:
        print("Alright, would you like to add another language?")
        anstranscont = input(">> ")
        if anstranscount.lower() == "yes":
              print("Which language would you like to add?")
              lang_choice = input(">> ")
              print("What is the translation?")
              trans = input(">> ")
              data["translation"][to_translate].append("[" + lang_choice + ":" + trans + "]")
              continue
        else:
              break
              
def add_word_data():
    with open('word_usage_data_eng.txt','r') as outfile2:
        word_dict = json.load(outfile2)
    outfile2.close
    if_cont = True
    while if_cont == True:
        to_add = input(">> ")
        if to_add.lower() == "program end":
              if_cont = False
        else:
            split_text(to_add)
    with open('word_usage_data_eng.txt', 'w') as outfile2:
        json.dump(word_dict, outfile2)
    outfile2.close()
    
#script
with open('word_data.txt', 'r') as outfile:
    data = json.load(outfile)
print("Welcome to our dictionary database.")
print("With this database you can add, remove, and edit words. You can now also add word data.")
print("You can now also add a translation to a word")
while True:
    print("So what would you like to do?")
    action = input(">> ")
    if action.lower() == "add":
        print("Alright. What part of speech is the word you would like to add?")
        print("The available choices right now are: \'noun\', \'verb\', and \'adjective\'.")
        partOfSpeech = input(">> ")
        if partOfSpeech.lower() == "noun":
            add_noun()
        elif partOfSpeech.lower() == "verb":
            add_verb()
        elif partOfSpeech.lower() == "adjective":
            add_adjective()
        else:
            print("I'm sorry, I'm afraid I don't understand.")
            continue
    elif action.lower() == "add word data":
         print("So you want to add word data?")
         print("Working with word data requires closing your current word data. Would you like to save it?")
         ifsave = input(">> ")
         if ifsave.lower() == yes:
                outfile.close()
                with open('word_data.txt', 'w') as outfile:
                    json.dump(data, outfile)
                outfile.close()
         print("Your data has been saved.")
         print("The loop will begin. To exit the loop, enter \"program end\"")
         add_word_data()
         with open('word_data.txt', 'r') as outfile:
                data = json.load(outfile)
    elif action.lower() == "translate":
        print("Alright, let's translate.")
        add_translation()
    elif action.lower() == "end":
        print("Would you like to end the program?")
        end_true = input(">> ")
        if end_true.lower() == "yes":
            print("Alright. Would you like to save your data?")
            save_true = input(">> ")
            if save_true.lower() == "yes":
                outfile.close()
                with open('word_data.txt', 'w') as outfile:
                        json.dump(data, outfile)
                outfile.close()
                print("Your data has been saved.")
                print("The program will now close.")
                break
            elif save_true.lower() == "no":
                print("The program will now end without saving.")
                break
            else:
                print("I'm sorry, I don't understand.")
                continue
    elif action.lower() == "save":
        outfile.close()
        with open('word_data.txt', 'w') as outfile:
                        json.dump(data, outfile)
        outfile.close()
        with open('word_data.txt', 'r') as outfile:
            data = json.load(outfile)
        print("Your data has been saved.")
    elif action.lower() == "print":
        print(data)
    else:
        print("I'm sorry, I'm afraid I don't understand.")
        print("Acceptable values for action incude:")
        print("  add")
        print("  print")
        print("  save")
        print("  translate")
        print("  add word data")
        print("  end")
        continue
            
    
    
    
    
    
    

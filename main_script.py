#New merged file. No GUI will be added as of this version.
#The purpose should be all main functions and objects.
#Reader + writer + script
#Trying out more complex functions rather than shortened versions
import json
import random

with open('word_data.txt', 'r') as outfile:
    data = json.load(outfile)

array_subject = data['nouns'][0]
array_verb = data['verbs'][0]
array_particle = data['particles'][0]
array_adverb = data['adverbs'][0]

outfile.close()

def create_sentence():
    #creating the subject
    phrase_number = 0
    total_phrases = random.randrange(1,2)
    sentence = []
    while phrase_number <= total_phrases:
        if phrase_number >= 1:
            conjunctions = ["and", "but", "if", "when"]
            conjunction = random.choice(list(conjunctions))
            sentence.append(conjunction)
        if_plural_subject = random.randrange(1, 3)
        subject = random.choice(list(array_subject.keys()))
        if if_plural_subject != 1:
            subject = data['nouns'][0][subject][0]
            sentence.append(subject)
            plurality = True
        else:
            particles = ["a", "the"]
            particle = random.randrange(0,2)
            particle = particles[particle]
            sentence.append(particle)
            sentence.append(subject)
            plurality = False
        #finding verb tense
        verb_time = random.randrange(1,4)
        if verb_time == 1:
            verb_time = "past"
        if verb_time == 2:
            verb_time = "future"
        else:
            verb_time = "current"
        #passive or active
        active = random.randrange(1,3)
        if active == 1:
            active == True
        else:
            active == False
        #creating the verb
        verb = random.choice(list(array_verb.keys()))
        if verb_time == "current":
            if plurality == True:
                verb = verb
                sentence.append(verb)
            else:
                verb = data["verbs"][0][verb][1][2]
                sentence.append(verb)
        elif verb_time == "past":
            verb = data["verbs"][0][verb][1][0]
            if plurality == True:
                verb = "have " + verb
                sentence.append(verb)
            else:
                verb = "has " + verb
                sentence.append(verb)
        else:
            verb = "will " + verb
            sentence.append(verb)
        #adverb section
        if_adverb = random.randrange(1,3)
        if if_adverb == 1:
            adverb = random.choice(list(array_adverb.keys()))
        else:
            adverb = "no adverb"
        #printing step by step results
        print("Subject plurality is " + str(if_plural_subject))
        print("Subject is " + subject)
        print("Verb time is " + verb_time)
        print("Verb is " + verb)
        print("Adverb is " + adverb)
        print(sentence)
        if phrase_number == total_phrases:
            print("Last loop")
        phrase_number += 1
    #now creating and formatting the sentence
    sentenceTxt = sentence[0]
    letters = []
    for x in range(1, len(sentence)):
        sentenceTxt = sentenceTxt + " " + sentence[x]
    print(sentenceTxt)
    for x in sentenceTxt:
        letters.append(x)
    letters[0] = letters[0].upper()
    letters.append(".")
    sentenceTxtFinal = ""
    for x in letters:
        sentenceTxtFinal = sentenceTxtFinal + x
    print(sentenceTxtFinal)
        

#script
while True:
    print("What would you like to do?")
    action = input(">> ")
    if action.lower() == "create":
        create_sentence()
    elif action.lower() == "end program":
        break
    else:
        print("I'm sorry, I don't understand you.")
        print("Current actions are 'create' and 'end program'")

                                
                
    

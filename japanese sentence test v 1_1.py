#Japanese sentence creator 1.1
#November 29, 2020
#Attempting sentence with simple Sub + Obj + Verb format, all 3rd person
#No logic method yet

#this needs to be moved to json
#the main sentence translator will load all json files first, open their data,
#and then it will save any changes to the relevant files after
#we are still hoping to load the functions from another file

#importing modules

from random import *

#adding arrays
#keep in mind nouns will not exist in every sentence
array_noun = ["猫（neko）" , "家（ie）", "人(hito)","男（otoko）","女（onna）",
              "子ども（kodomo）","弁護士（bengoshi）","足（ashi）",
              "化け物（bakemono）", "犬（inu）", "木（ki）", "梅（ume）",
              "パン（pan）", "ビール（biiru）", "時間（jikan）"]
array_verb = ["働く（hataraku）","見る（miru）","話す（hanasu）", "行く（iku）",
              "泳ぐ（oyogu）", "歩く（aruku）","飲む（nomu）", "食べる（taberu）",
              "いう（iu）", "使う（tsukau）", "泣く（naku）", "笑う（warau）",
              "遊ぶ（asobu）", "閉める（shimeru）"]
#creating this as an array but it probably will not be necessary
array_particle = ["は（wa）", "が（ga）", "を（wo）"]
#creating but not using yet
array_adjective = ["いい（ii）", "悪い（warui）", "硬い（katai）", "寒い（samui）",
                   "熱い（atsui）", "美しい（utsukushii）",
                   "辛い（tsurai）", "楽しい（tanoshii）", "寂しい（sabishii）"]


def create_sentence():

    x_subject = array_noun[randrange(0,len(array_noun))]
    print(x_subject + " is the subject.")
    x_verb = array_verb[randrange(0,len(array_verb))]
    print(x_verb + " is the verb.")
    is_object = randrange(0,2)
    if is_object == 0:
        print("There is no object")
        sentence = x_subject + " wa " + x_verb + "."
    elif is_object == 1:
        x_object = array_noun[randrange(0,len(array_noun))]
        print(x_object + " is the object.")
        sentence = x_subject + " wa " + x_object + " wo " + x_verb + "."
    print(sentence)

#main

count = 0

#start the loop
while count < 5:
    create_sentence()
    print(" ")
    print("Would you like to go again?")
    answer = input(">> ")
    if answer == "yes" or answer == "Yes":
        count = count + 1
    else:
        break

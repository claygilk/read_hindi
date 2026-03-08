from aksharamukha import transliterate
import random
import sys
import os
import json


cons_min = 0x0915
cons_max = 0x0939
exclude = [0x0945, 0x0929, 0x091E, 0x0932, 0x0931, 0x0933, 0x0934, 0x0944, 0x0946, 0x0949, 0x094A]

matra_min = 0x093E
matra_max = 0x094D

def pick_random(some_list:list):
    index = random.randint(0, len(some_list))
    return some_list[index]

cv_pairs = []

row_count=1
for cons in range(cons_min, cons_max, 1):
    for matra in range(matra_min, matra_max, 1):
        if cons not in exclude and matra not in exclude:
            hindi = f'{chr(cons)}{chr(matra)}'
            trans = transliterate.process(src='Devanagari', tgt='HK', txt=hindi)
            # print(f'{row_count} {hindi} {trans}')
            cv_pairs.append({"hindi": hindi, "trans": trans})
            row_count += 1

# mode = input("mode?\n 1. Matching\n 2. Spelling \n3. Words")
mode = '3'



if mode == '1':
    while True:
        os.system('cls')
        cv_pair = pick_random(cv_pairs)
        question = cv_pair['hindi']
        answer = cv_pair['trans']
        
        a = cv_pairs[random.randint(0, len(cv_pairs))]['trans']
        b = cv_pairs[random.randint(0, len(cv_pairs))]['trans']

        all_ans = [answer, a, b]
        random.shuffle(all_ans)
        
        ans = input(f"\n        {question}  \n\n1){all_ans[0]}   2){all_ans[1]}  3){all_ans[2]}  >> ")
        
        
        if ans == 'q':
            sys.exit(0)
        
        ans_int = int(ans)
        user_ans = all_ans[ans_int - 1]
        if user_ans == answer:
            print("Correct!\n\n")
        else:
            print(f"Incorrect! {question} = {answer}\n\n")

        cont = input("Continue?")
elif mode == '2':
    print("welcome to spelling")
    while True:
        os.system('cls')
        cv_pair = pick_random(cv_pairs)
        question = cv_pair['hindi']
        answer = cv_pair['trans']
        user_ans = input(f"\n {question} >> ")
        if user_ans == answer:
            print("Correct!\n\n")
        else:
            print(f"Incorrect! {question} = {answer}\n\n")
        cont = input("Continue?")
elif mode == '3':
    while True:
        print("welcome to words")
        os.system('cls')

        with open('words.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        word_list = data["words"]
        easy_words = []
        for word in word_list:
            if word["cefr_level"] in ["A1", "A2"]:
                easy_words.append(word)

        question = pick_random(easy_words)
        hindi = question['word']

        answer = transliterate.process(src='Devanagari', tgt='HK', txt=hindi, pre_options=['RemoveSchwaHindi'])
        user_ans = input(f"\n             {hindi} >> ")

        if user_ans == answer:
            print("Correct!\n\n")
        else:
            print(f"Incorrect! {hindi} = {answer}\n\n")
        print(f"eng: {question["english_translation"]}")
        cont = input("Continue?")
    #     os.system('cls')
    #     cv_pair = pick_random(cv_pairs)
    #     question = cv_pair['hindi']
    #     answer = cv_pair['trans']
    #     user_ans = input(f"\n {question} >> ")
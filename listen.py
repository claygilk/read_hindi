from gtts import gTTS
from playsound3 import playsound
import csv
import pandas as pd
import os
import random
from pprint import pprint
import sys


random_boolean = random.choice([True, False])

def pick_spread(max_index:int, target_index:int, num_options:int, spread:int) -> set:
    
    indexes = set()

    min_ind = max(0, target_index - spread)
    max_ind = min(max_index, target_index + spread)

    while len(indexes) < num_options:
        i = random.randint(min_ind, max_ind)
        indexes.add(i)

    return indexes

def pick_random(some_list:list, num_options:int, spread:int) -> dict:
    
    results = {}

    answer_index = random.randint(0, len(some_list))
    answer = some_list[answer_index]

    results["answer"] = answer
    
    choice_indexes = pick_spread(len(some_list), answer_index, num_options, spread)
    
    for i in choice_indexes:
        choice = some_list[i]
        results[f"choice_{i}"] = choice

    return results

#
# Main (Setup)
#
df = pd.read_csv('hindi.csv')
cv_pairs = df.to_dict('records')
mistakes = []

#
# Gameplay Loop
#
while True:
    os.system('cls')

    options = pick_random(cv_pairs, 3, 15)

    all_ans = []
    answer = options["answer"]
    audio_file = f"{answer['trans']}.mp3"

    for k,v in options.items():
        all_ans.append(v)

    random.shuffle(all_ans)

    print("") # new line so letter isn't cut off
    for i,v in enumerate(all_ans):
        hindi = v["hindi"]
        print(f"{i+1}) {hindi}", end="    ")
    

    sound = playsound(f"./mp3/{audio_file}", block=True)
    ans = input(">> \n")
    while ans == "":
        playsound(f"./mp3/{audio_file}", block=True)
        ans = input("\033[F")


    ans_int = int(ans)
    user_ans = all_ans[ans_int - 1]
    if user_ans == answer:
        print(f"Correct! {answer['hindi']} = {answer['trans']}")
        playsound(f"./mp3/{audio_file}", block=True)
    else:
        print(f"Incorrect! {answer['hindi']} = {answer['trans']}")
        playsound(f"./mp3/{audio_file}", block=True)
        playsound(f"./mp3/{audio_file}", block=True)
        mistakes.append(answer)

    cont = input("Continue?")
    if cont == 'q':
        print("Mistakes: ")
        pprint(mistakes)
        sys.exit(0)

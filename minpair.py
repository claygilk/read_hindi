import pandas as pd
from pprint import pprint
import json


def to_bit(bits:str) -> bin:
    return int(bits, 2)

def count_set_bits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

def get_diff(lhs:str, rhs:str):
    
    n = to_bit(lhs) ^ to_bit(rhs)
    count = 0
    while (n):
        count += n & 1
        n >>= 1

    return count


df = pd.read_csv('deva_codes.csv', dtype=str)
codes_raw = df.to_dict('records')

deva_to_code_map = {}
code_to_deva_map = {}


for row in codes_raw:
    code = row["code"]
    deva = row["hindi"]
    code_bits = int(code, 2)
    print(f"{deva} = {code} = {code_bits}")

    code_to_deva_map[code] = deva
    deva_to_code_map[deva] = code


deva_to_dist = {}
dist_to_deva = {}

for this_deva,this_code in deva_to_code_map.items():
    
    this_deva_pairs = {}
    this_deva_dist = {}
    
    
    for that_deva,that_code in deva_to_code_map.items():
        diff = get_diff(this_code, that_code)
        this_deva_pairs.update({that_deva: diff})
        
        dist = this_deva_dist.get(diff, [])
        dist.append(that_deva)
        this_deva_dist.update({diff : dist})

        print(f"{this_deva} vs {that_deva} = {diff}")
    
    deva_to_dist.update({this_deva : this_deva_pairs})
    dist_to_deva.update({this_deva : this_deva_dist})



with open('deva_to_dist.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(deva_to_dist, ensure_ascii=False))

with open('dist_to_deva.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(dist_to_deva, ensure_ascii=False))

ka = "00010000000100000000"
ga = "00110000000100000000"
kha = "01010000000100000000"
gha = "01110000000100000000"
a = "10100000000000000100"
aa = "10100000000000100001"




# get_diff(to_bit(ka), to_bit(a))
# get_diff(to_bit(a), to_bit(aa))

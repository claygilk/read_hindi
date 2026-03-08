from aksharamukha import transliterate
import json

# with open('syllabary_Devanagari.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
cv_pairs = []
with open('c_or_v.csv', 'r', encoding='utf-8') as file:
    for line in file:
        text = line.strip()
        cv_pair = {}
        trans = transliterate.process(src='Devanagari', tgt='HK', txt=text)
        # print(f'{row_count} {hindi} {trans}')
        cv = f"{text},{trans}"
        print(cv)
        cv_pairs.append(cv)


# print(data["compounds"])



# for c in data["compounds"]:
#     cv_pair = {}
#     trans = transliterate.process(src='Devanagari', tgt='HK', txt=c)
#     # print(f'{row_count} {hindi} {trans}')
#     cv_pairs.append({"hindi": c, "trans": trans})

print(cv_pairs)

# cv = {"cv": cv_pairs}

# astring = json.dumps(cv, ensure_ascii=False)
# print(astring)

# with open('cv.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(cv, ensure_ascii=False))

# print(transliterate.process('Devanagari', 'HK', 'धर्म भारत की श्रमण परम्परा से निकला धर्म और दर्शन है', pre_options=['RemoveSchwaHindi']))

# print(transliterate.process('deva', 'taml', 'धर्म भारत की ', param="script_code"))

# print(transliterate.process('hi', 'ur', 'धर्म भारत की ', param="lang_code"))


# print(transliterate.process('hindi', 'kannada', 'धर्म भारत की ', param="lang_name"))

# print(transliterate.process('devanagari', 'granthapandya', 'धर्म'))

# print(transliterate.process('hi', 'pa', 'धर्म भारत की ', param="lang_code"))
# print(transliterate.process('hi-Deva', 'hi-kthi', 'धर्म भारत की ', param="lang_code"))
# print(transliterate.process('hi-Deva', 'mak', 'धर्म भारत की ', param="lang_code"))
# print(transliterate.process('hi-Deva', 'cyrl', 'धर्म भारत की ', param="script_code"))
# print(transliterate.process('sa-Deva', 'ru', 'धर्म भारत की ', param="lang_code"))



## multiple orthographies associated with script example


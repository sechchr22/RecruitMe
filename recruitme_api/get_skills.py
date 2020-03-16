#!/usr/bin/python3
"""
    Github repositories API languages
"""
import sys
import requests
from models.skills import Skill
from models.user import User

if __name__ == "__main__":

    url = "https://api.github.com/users/{}/repos".format(
        sys.argv[1]
    )
    languages = {}
    resp = requests.get(url)

    Relevant_lang = ['Python',
                     'Java',
                     'C',
                     'C++',
                     'JavaScript',
                     'Go',
                     'R',
                     'Swift',
                     'PHP',
                     'C#',
                     'MATLAB',
                    ]
    #try:
    #JSON response
    json_lang = resp.json()

    #get lines per language
    for data in json_lang:
        if data.get('language') is not None:
            rep_name = data.get('name')
            resp_lang = requests.get(data.get('languages_url'))
            lang_count = resp_lang.json()
            for lang in lang_count:
                if lang in languages:
                    languages[lang] += lang_count.get(lang)
                else:
                    languages[lang] = lang_count.get(lang)

            #print('Repository: {}.'.format(rep_name)) 
            #print('Lenguages: {}.'.format(lang_count))
            #print()


    #creating User Obj
    user_obj = User()
    user_obj.name = "Sergio Rueda"
    user_obj.password = "Valen te amo"
    user_obj.email = "lifebysech@gmail.com"
    user_obj.github = "sechchr22"
    user_obj.whatsapp = "3004892618"
    user_obj.save()

    #creating skill obj
    skill_obj = Skill()
    skill_obj.user_id = user_obj.id 

    #print lines of code per language and setting skill obj att
    for l in languages:
        if l in Relevant_lang:
            print("Language: {} {}".format(l, languages[l]))
            if l == 'C++':
                skill_obj.C_plus_plus = languages[l]
            if l == 'C#':
                skill_obj.C_sharp = languages[l]
            else:
                setattr(skill_obj, l, languages[l])

    #saving obj in db
    skill_obj.save()
        
    #except:
        #print("Not a valid JSON")

import json
import string
import emoji

with open("C:\\Users\\Ganesh\\Documents\\Resume Project\\query_classification\\slang.json") as file:
            dict_ = json.load(file)

def slang_convert(text):
    new_text=[]
    for word in text.split():
        if word.lower() in dict_:
            new_text.append(dict_[word.lower()].lower())
        else:
            new_text.append(word)
    return " ".join(new_text)

def remove_punc(txt):
    for i in string.punctuation:
        txt=txt.replace(i,'')
    return txt

def remove_emoji(text):
    return(emoji.demojize(text).replace(':',''))

def preprocessing(query):
    query = str(query)
    if len(query.split(' ')) <=2:
        return "null"
    else:
        query=query.lower()
        query = slang_convert(query).lower()
        query = remove_punc(query)
        query = remove_emoji(query)
    return query
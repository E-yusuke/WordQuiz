import re
import random

file_name='english_01.txt'
class make_dict():
    
    def __init__(self,file_name):
        self.meaning=[]
        self.english_words=[]
        self.file_name=file_name

    def word(self):
        with open(self.file_name, encoding="utf-8") as f:
            data= f.read()

        self.english_words=re.findall('[a-z]+',data)
        ja=re.findall('\n.*\n',data)

        for japanese_words in ja:
            m=re.sub('\n|\t','',japanese_words)
            if m != '':
                self.meaning.append(m)
                
        return dict(zip(self.english_words,self.meaning))
ja=[]
w=make_dict(file_name).word()

for i in range(4):
    en, j=random.choice(list(w.items()))
    ja.append(j)
print(en)
print(ja)

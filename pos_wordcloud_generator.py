import nltk
from random import randrange

nouns='NN'
adverb='RB'
verb='VB'
adjective='JJ'

class PosWordCloudGenerator():
    def __init__(self):
        pass
    def create_wordcloud(self,sentence):
        tokens=nltk.word_tokenize(sentence)
        freqs=[]
        count=0
        for pair in nltk.pos_tag(tokens):
            word=pair[0]
            tag=pair[1]
            s=0
            c1=0
            c2=0
            c3=0
            c4=0
            count=count+1
##            if count>119:
##                break
            if tag.startswith('NN'):
                c1=c1+1
                if c1>2:
                    s=randrange(5,8)
                else:
                    s=randrange(90,100)
                freqs.append({"text":word, "size":s})
            elif tag.startswith('JJ'):
                c2=c2+1
                if c2>2:
                    s=randrange(4,5)
                else:
                    s=randrange(65,80)
                s=randrange(85,95)
                freqs.append({"text":word, "size":s})
            elif tag.startswith('RB'):
                c3=c3+1
                if c3>2:
                    s=randrange(4,5)
                else:
                    s=randrange(45,55)
                s=randrange(45,65)
                freqs.append({"text":word, "size":s})
            elif tag.startswith('VB'):
                c4=c4+1
                if c4>8:
                    s=randrange(4,5)
                else:
                    s=randrange(25,35)
                s=randrange(20,40)
                freqs.append({"text":word, "size":s})
        return freqs

if __name__=="__main__":
    extractor = PosWordCloudGenerator()
    sentence = 'I completely forgot that\n\n I had delicious pasta at the Italian restaurant'
    print extractor.create_wordcloud(sentence)
    
    

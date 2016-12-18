import nltk
from random import randrange
from word_extractor import WordExtractor
##nouns='NN'
##adverb='RB'
##verb='VB'
##adjective='JJ'

class PosWordCloudGenerator():
    def __init__(self):
        pass
    def create_wordcloud(self,sentence):
        nouns=[]
        adverb=[]
        verb=[]
        adjective=[]
        foods=[]
        extractor = WordExtractor()
        st=extractor.extract_words(sentence)
        print len(st)
        for s in st:
            foods.append(s)
        tokens=nltk.word_tokenize(sentence)
        print foods
        freqs=[]
        count=0
        for pair in nltk.pos_tag(tokens):
            word=pair[0]
            tag=pair[1]
            if tag.startswith('NN'):
                count=count+1
                nouns.append(word)
##             freqs.append({"text":word, "size":100})
            elif tag.startswith('JJ'):
                count=count+1
                adjective.append(word)
        wordcount=0
        print count
        big=120
        bw=0
        for word in foods:
            bw=bw+1
            freqs.append({"text":word,"size":big})
            x=big-20
            if x>5:
                big=x
            if x<1:
                break
        rm=nouns+adjective
        tens=0.4*count
        s15=0.25*count
        for word in rm:
            if tens<0 and s15<0:
                freqs.append({"text":word,"size":5})
            elif s15<0 and tens>0:
                freqs.append({"text":word,"size":10})
                tens=tens-1
            elif s15>0:
                s=randrange(15,20)
                freqs.append({"text":word,"size":s})
                s15=s15-1
        return freqs

if __name__=="__main__":
    extractor = PosWordCloudGenerator()
    sentence= "I will admit I am completely biased towards this place. I grew up eating their pizza. Crust is soft and fluffy, not chewy. The cheese is a little thicker than the average new york style pizza place. The sauce has spice but not too much. At some places you need a little milk or water to cool your tongue. Their one downside is that they're not always consistent. Some days its just started to turn golden brown others its over done. Eaten here twicebut only pizza. I do have to say its up there with Napolis or Ailleos as for the pizza. Tonight me and my neighbors were up for some more. Was disappointed when ordering a meatball hoagie to find out they had no meatballs! Pizza places should never run out of certain things. Had gotten a cheese hoagie. Didnt get get why someone would order this, but was told it was good. didnt like. Luckily the pep pizza was great, but.. when u get toward the crust, its all dough. Still kick butt pizza but get rid of the cheese hoagie. According to Urbanspoon (blasphemy I know) their are like 1,100 pizza places in pittsburgh. So what is the best pizza in Pittsburgh. Everyone has an opinion and so here is mine: The best pizza in Pittsburgh is the pie comes from the place in you neighborhood that has quality ingredients, fair prices, and friendly service. Eddie's Pizza Place  is all of these things and since I live in this neighborhood this is my favorite. Decent neighborhood pizza can be found in morningside at eddies pizza haus. The sauce and cheese are perfect, but the crust falls short.  It has a nice texture and overall the pizza isn't greasy, but the crust lacks much flavor. Maybe a little more salt is needed in the dough to compensate? The pizza is decent enough though and merits a try, perhaps it was an off day for Eddies."
##    sentence = 'I completely forgot that\n\n I had delicious pasta at the Italian restaurant'
    print extractor.create_wordcloud(sentence)
    
    

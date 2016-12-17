import nltk

nouns = 'NN'
adverb = 'RB'
verb = 'VB'
adjective = 'JJ'

class PosWordCloudGenerator():
	
	def __init__(self):
		pass

	def create_wordcloud(self, sentence):
		tokens = nltk.word_tokenize(sentence)
		
		freqs = []
		for pair in nltk.pos_tag(tokens):
			word = pair[0]
			tag = pair[1]
			if tag.startswith('NN'):
				freqs.append({"text":word, "size":100})
			elif tag.startswith('JJ'):
				freqs.append({"text":word, "size":80})
			elif tag.startswith('RB'):
				freqs.append({"text":word, "size":50})
			elif tag.startswith('VB'):
				freqs.append({"text":word, "size":30})

		return freqs

if __name__ == "__main__":
	extractor = PosWordCloudGenerator()
	sentence = 'I completely forgot that I had delicious pasta at the Italian restaurant.'
	print extractor.create_wordcloud(sentence)
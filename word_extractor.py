import nltk
from nltk.corpus import wordnet as wn

class WordExtractor:

	def __init__(self):
		self.words = ['food.n.01', 'food.n.02', 'restaurant.n.01', 'dish.n.02',
		'cuisine.n.01', 'fruit.n.01', 'vegetable.n.01', 'meat.n.01',
		'drink.n.01', 'alcohol.n.01', 'inhabitant.n.01']

	def get_hypernyms(self, synset):
	    hypernyms = set()
	    for hypernym in synset.hypernyms():
	        hypernyms |= set(self.get_hypernyms(hypernym))
	    return hypernyms | set(synset.hypernyms())

	def get_hyponyms(self, synset):
	    hyponyms = set()
	    for hyponym in synset.hyponyms():
	        hyponyms |= set(self.get_hyponyms(hyponym))
	    return hyponyms | set(synset.hyponyms())

	def extract_words(self, sentence):

		extracted_words = set()

		# unigrams
		tokens = nltk.word_tokenize(sentence)
		# bigrams
		pairs = [ "_".join(pair) for pair in nltk.bigrams(tokens)]

		for word in self.words:
			synset = wn.synset(word)
			for key in self.get_hyponyms(synset):
				for sentence_word in tokens:
					if str(sentence_word) == str(key.lemma_names()[0]):
						extracted_words.add(sentence_word)
				for pair_word in pairs:
					if str(pair_word) == str(key.lemma_names()[0]):
						extracted_words.add(pair_word)

		return extracted_words

if __name__ == "__main__":
	extractor = WordExtractor()
	sentence = 'I had sushi and salt pork in an Italian restaurant.'
	print extractor.extract_words(sentence)
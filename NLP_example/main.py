# examples derived from https://www.nltk.org

import nltk

# Descargar recursos si no están disponibles
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)
print(tokens)

tagged = nltk.pos_tag(tokens)
print(tagged[0:6])

# examples derived from https://spacy.io/usage/spacy-101
import spacy

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

    for token in doc:
        print(
            token.text,
            token.lemma_,
            token.pos_,
            token.tag_,
            token.dep_,
            token.shape_,
            token.is_alpha,
            token.is_stop,
        )
from collections import Counter
import pygal
import spacy

nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")

twenties = open("twentiesLyricsNLP.txt", "r")

words = twenties.read()
twentiesWords = nlp(words)

def nouncollector(words):
    Nouns = []
    count = 0
    for token in words:
        if token.pos_ == "NOUN":
            count += 1
            Nouns.append(token.lemma_)
    return Nouns

print("TOP TEN NOUNS:")
listNouns = nouncollector(twentiesWords)
noun_freq = Counter(listNouns)
nounTopTen = noun_freq.most_common(10)
print(nounTopTen)

nounBar_chartOver10 = pygal.Bar()
nounBar_chartTopTen = pygal.Bar()

nounBar_chartOver10.title = 'Nouns Used Over 10 Times in Song Lyrics from the 1920s'
nounBar_chartTopTen.title = 'Top 10 Nouns in Songs from the 1920s'
print(nounBar_chartOver10.title)
for n in noun_freq:
    # verb_freq is a dictionary structure, so we return its key and its value:
    print(n, noun_freq[n])
    if noun_freq[n] > 10:
        nounBar_chartOver10.add(n, noun_freq[n])

print(nounBar_chartTopTen.title)
for o in nounTopTen:
    # this is a list of tuples, so we return its values like this:
    print(o[0], o[1])
    nounBar_chartTopTen.add(o[0], o[1])

print(nounBar_chartOver10.render(is_unicode=True))
nounBar_chartOver10.render_to_file('20sNOUNbar_chartOver10.svg')
nounBar_chartTopTen.render_to_file('20sNOUNbar_chartTopTen.svg')







def verbcollector(words):
    Verbs = []
    count = 0
    for token in words:
        if token.pos_ == "VERB":
            count += 1
            # print(count, ": ", token.text, " lemma: ", token.lemma_, " pos: ", token.pos_)
            # don't forget the underscore after token.lemma_ , token.pos_, etc.!
            Verbs.append(token.lemma_)
            #print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    # print(count, ": ", Verbs)
    return Verbs

print("TOP TEN VERBS:")
listVerbs = verbcollector(twentiesWords)
verb_freq = Counter(listVerbs)
topTen = verb_freq.most_common(10)
print(topTen)
lastTen = verb_freq.most_common()[:5:1]

bar_chartOver10 = pygal.Bar()
bar_chartTopTen = pygal.Bar()

bar_chartOver10.title = 'Verbs Used Over 10 Times in Song Lyrics from 1920s'
bar_chartTopTen.title='Top 10 Verbs in Songs from 1920s'
print(bar_chartOver10.title)
for v in verb_freq:
    # verb_freq is a dictionary structure, so we return its key and its value:
    print(v, verb_freq[v])
    if verb_freq[v] > 10:
        bar_chartOver10.add(v, verb_freq[v])

print(bar_chartTopTen.title)
for t in topTen:
    # this is a list of tuples, so we return its values like this:
    print(t[0], t[1])
    bar_chartTopTen.add(t[0], t[1])

print(bar_chartOver10.render(is_unicode=True))
bar_chartOver10.render_to_file('20sVERBbar_chartOver10.svg')
bar_chartTopTen.render_to_file('20sVERBbar_chartTopTen.svg')






def entcollector(words):
    #ent = []
    #count = 0
    Ents = []
    count = 0
    for token in twentiesWords.ents:
        if token.label_ == "GPE":
            count += 1
            print(count, ": ", token.text, token.label_)
            Ents.append(token.lemma_)
            #print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
            # print(count, ": ", token.text, " lemma: ", token.lemma_, " pos: ", token.pos_)
            # don't forget the underscore after token.lemma_ , token.pos_, etc.!
           # Verbs.append(token.lemma_)
            #print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    # print(count, ": ", Verbs)
    return Ents

listEnts = entcollector(twentiesWords)
ent_freq = Counter(listEnts)
entTopTen = ent_freq.most_common(10)
print(entTopTen)
entLastTen = ent_freq.most_common()[:5:1]

bar_chartTopTenEnts = pygal.Bar()
bar_chartTopTenEnts.title='Top 10 Geopolitical Entities Mentioned in Songs from 1920s'

print(bar_chartTopTenEnts.title)
for e in entTopTen:
    # this is a list of tuples, so we return its values like this:
    print(e[0], e[1])
    bar_chartTopTenEnts.add(e[0], e[1])

print(bar_chartTopTenEnts.render(is_unicode=True))
bar_chartTopTenEnts.render_to_file('20sENTITYbar_chartTopTen.svg')



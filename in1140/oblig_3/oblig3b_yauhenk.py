# Del 1
# 1
# Setningen "Norah spiser sushi med pinner" kan ha de følgende tolkningene:
# 1. Norah bruker pinner til å spise sushi.
# 2. Norah spiser sushi som inneholder pinner.

# 2
# Vi kan utvide grammatikken med den følgende regelen:
# NP -> NP PP
# Da vil den representere flertydighet av denne typen.

# 3
# Ja grammatikken er rekursiv. Den inneholder regelen med direkte rekursjon:
# VP -> VP PP
# VP er både i venstre og høyre side av produksjonen.

# Del 2
# 1
# S -> NP VP
# VP -> V NP PP | V NP NP | V NP | V
# PP -> P NP
# NP -> D N | 'Per' | 'Kari' | 'Ola' |'boka' | 'middag'
# V -> 'gir' | 'sover' | 'spiser' | 'finner'
# D -> 'en'
# N -> 'bok'
# P -> 'til'

# 2
# Implemented, see DEMO

# 3
# S -> NP VP
# VP -> V NP PP | V NP NP | V NP | V | V-NP NP | V-No-C
# PP -> P NP
# NP -> D N | 'Per' | 'Kari' | 'Ola' |'boka' | 'middag'
# V -> 'gir' | 'spiser'
# V-NP -> 'finner'
# V-No-C -> 'sover'
# D -> 'en'
# N -> 'bok'
# P -> 'til'

# Del3
# 1. But questions with which committee members taunted bankers appearing as witnesses left little doubt that they will
# recommend passage of it.
# leave#6 (make a possibility or provide opportunity for; permit to be attainable or cause to remain)

# 2. The departure of the Giants and the Dodgers to California left New York with only the Yankees.
# leave#11 (have left or have as a remainder)

# 3. After the coach listed all the boy ’s faults, Hartweger said, “Coach before I leave here, you’ll get to like me”.
# leave#8 (remove oneself from an association with or participation in)

# 4. R. H. S. Crossman, M.P., writing in The Manchester Guardian, states that departures from West Berlin are now
# running at the rate not of 700, but of 1700 a week, and applications to leave have risen to 1900 a week.
# leave#5 (move out of or depart from)

# 5. The house has been swept so clean that contemporary man has been left with no means, or at best with wholly
# inadequate means, for dealing with his experience of spirit.
# leave#3 (act or be so as to become in a specified state)

# Det var vanskelig å annotere setning 3, fordi vi trenger mer kontekst. Det kan være at Hartweger vil enten forlate
# lage eller gå ut fra rommet. Og det er to forskjellige senser. Jeg fant setningen i bredere kontekst og det hjalp meg
# å finne løsning.
# Vi kan også anta at “coach” kan like eller ikke like en ung man bare som en idrettsutøver. I tillegg ”faults” gjelder
# mest sannsynlig ytelsen i et lag eller en konkurranse og så kan vi anta at gutten mener at han vil forlate lage eller
# idrett generelt.

# Det var vanskelig å skille fra hverandre sensene i setninger 1, 5. Og jeg er fortsatt ikke sikker på valget mitt.
# Jeg brukte betydningen til komplementene av ”left” og sammenlignet dem med tolkningen til hver sense.
# I setning 1:
# “little doubt that they will recommend passage of it” = “permit to be attainable”
# “with no means” = “act or be so as to become in a specified state”


##################
# Implementation #
##################

import nltk

# Del 2
# 1, 2
sent_tagged = ['(S (NP Per) (VP (V gir) (NP (D en) (N bok)) (PP (P til) (NP Kari))))',
                '(S (NP Kari) (VP (V gir) (NP Per) (NP boka)))',
                '(S (NP Ola) (VP (V sover)))',
                '(S (NP Kari) (VP (V spiser)))',
                '(S (NP Kari) (VP (V spiser) (NP middag)))',
                '(S (NP Per) (VP (V finner) (NP boka)))',
                '(S (NP Kari) (VP (V sover) (NP boka)))',
                '(S (NP Ola) (VP (V finner)))']

sent = ['Per gir en bok til Kari', 'Kari gir Per boka', 'Ola sover', 'Kari spiser', 'Kari spiser middag',
        'Per finner boka', 'Kari sover boka', 'Ola finner']

sent3 = ['et barn i en vugge sover']


grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP PP | V NP NP | V NP | V  
PP -> P NP
NP -> D N | 'Per' | 'Kari' | 'Ola' |'boka' | 'middag'
V -> 'gir' | 'sover' | 'spiser' | 'finner'
D -> 'en'
N -> 'bok'
P -> 'til'
""")

grammar3 = nltk.CFG.fromstring("""
S -> NP VP
NP -> D N
NP -> NP PP
VP -> V | V NP
VP -> VP PP
PP -> P NP
D -> 'en' | 'et'
N -> 'baby' | 'vindu' | 'vugge'
V -> 'sover'
P -> 'i' | 'ved'
""")


def verify_grammar(grammar, sentences, tagged_sentences):
    for sentence, tagged_sentence in zip(sentences, tagged_sentences):
        sentence = sentence.split()
        rd_parser = nltk.RecursiveDescentParser(grammar)
        for tree in rd_parser.parse(sentence):
            if format(tree) == tagged_sentence:
                print('{} - OK.'.format(tree))
            else:
                print('{} - NOT MATCH'.format(tree))


# Del 2
# 3
grammar_v2 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP PP | V NP NP | V NP | V | V-NP NP | V-No-C
PP -> P NP
NP -> D N | 'Per' | 'Kari' | 'Ola' |'boka' | 'middag'
V -> 'gir' | 'spiser'
V-NP -> 'finner'
V-No-C -> 'sover'
D -> 'en'
N -> 'bok'
P -> 'til'
""")
# Comments:
# V-NP - verb with NP complement
# V-No-C - verb with no complement


def verify_grammar_v2(grammar, sentences):
    accepted = 0
    for position, sentence in enumerate(sent, start=1):
        print('{}.{}. '.format(position, sentence), end='')
        sentence = sentence.split()
        rd_parser = nltk.RecursiveDescentParser(grammar)
        if len(list(rd_parser.parse(sentence))) > 0:
            accepted += 1
            for tree in rd_parser.parse(sentence):
                print('{}.'.format(tree))
        else:
            print('NO MATCH')

    print('\nTotal sentences in input: {}'.format(len(sentences)))
    print('Number of accepted sentences: {}'.format(accepted))


if __name__ == '__main__':

    ########
    # Demo #
    ########

    # Del 2
    # 1, 2
    #print("\nLet's check if grammar tags sentences correctly:")
    #verify_grammar(grammar, sent, sent_tagged)
    #print('The last two sentences are ungrammatical, but we accepted them.\n')

    # 3
    #print('We are checking if the new grammar accepts ungrammatical sentences.')
    #verify_grammar_v2(grammar_v2, sent)
    #print('The last two sentences were not accepted.')
    sent3 ='en baby sover i en vugge ved et vindu'.split()
    rd_parser = nltk.RecursiveDescentParser(grammar3)
    for tree in rd_parser.parse(sent3):
        print(tree)


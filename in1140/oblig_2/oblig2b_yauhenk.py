#############
# Questions #
#############

# Del 1
# 1
# (a) Utfallsrommet – det er en mengde av alle mulige utfall i en tilfeldig prøve eller et tilfeldig eksperiment.
# (b) Betinget sannsynlighet – det er sannsynlighet for en hendelse basert på den andre hendelsen som har allerede skjedd.
# (c) Hendelse – det er en del (en mengde) av utfallsrommet; med andre ord er det en undermengde av utfallsrommet.
#     En hendelse har en viss sannsynlighet.
# (d) Uavhengige hendelser – hvis sannsynligheten av hendelser ikke er påvirket av forekomsten av hverandre,
#     sier vi at hendelsene er uavhengige.
# (e) Uniform distribusjon – det er distribusjon av tilfeldig mengde med en jevn sannsynlighetstetthet;
#     det betyr at alle utfall har lik sannsynlighet.
# (f) Felles sannsynlighet – hvis vi har to tilfeldige hendelser fra et utfallsrom,
#     er felles sannsynlighet en sannsynlighet at begge to hendelsene skjer.

# 2
# Sannsynligheten for alle mulige utfall er summen av sannsynlighetene for hvert mulig utfall i utfallsrommet.
# Sannsynligheten for alle mulige utfall summerer til 1.

# 3
# N-gram – det er en sekvens av N elementer. For eksempel, ”my name”, ”name is”, ”is Yauhen” er en sekvens
# av 2-grammer (bigrammer). Et bigram består av to elementer.

# 4
# P(A|B) = P(B|A)*P(A)/P(B)
# P(A), P(B) - sannsynlighetene av hendelsene A og B, hvor A og B er uavhengige av hverandre.
# P(A|B) – sannsynligheten av A gitt B (betinget sannsynlighet)
# P(B|A) – sannsynligheten av B gitt A (betinget sannsynlighet)
# Vi kan bruke Bayes regelen for å beregne en posterior sannsynlighet. Det er betinget sannsynlighet av A gitt B,
# når A skjer først. For eksempel, i klassen er det 60% gutter, 40% jenter. Normalt får 80% jenter og 70% gutter
# godkjent på oppgaver. Med Bayes reglen kan vi beregne sjansen at en person som fikk godkjent er en gutt.

# 5
# HMM-tagging er prosess for å finne tag-sekvensen som er mest sannsynlig for den gitt inngangssekvensen av tokener.
# HMM modell brukes når man evaluerer samtidig observerte og skjulte hendelser. Under HMM-tagging må man beregne
# sannsynligheten av en tag gitt den forrige taggen og sannsynligheten av et ord å brukes med den gitt taggen.

# 1.2 Del 2
# 1
# Følgende bigrammer forekommer i korpuset:
# ('<s>', 'Truls')
# ('Truls', 'spiller')
# ('spiller', 'piano')
# ('piano', '<\\s>')
# ('<s>', 'Katherine')
# ('Katherine', 'spiller')
# ('spiller', 'ikke')
# ('ikke', 'piano')
# ('piano', '<\\s>')
# ('<s>', 'Ludovico')
# ('Ludovico', 'spiller')
# ('spiller', 'piano')
# ('piano', '<\\s>')

# 2
# P(wn | wn-1) = C(wn-1 wn) / C(wn-1)
# P(wn | wn-1) - Sannsynlighet  av ord 'wn' gitt ord 'wn-1'
# C(wn-1 wn) - antall bigrammen
# C(wn-1) - antall den første unigrammen
#
# Man beregner antall ganger bigrammen forekommer i korpuset.
# Så beregner man antall ganger den første unigrammen fra bigrammen forekommer i korpuset.
# Etterpå deler man antallet bigrammen med antallet den første unigrammen.

# 3
# <s> Katherine spiller piano <\s>
# Vi trenger  følgende bigrammer:
# Bigram: ('<s>', 'Katherine')     Sannsynlighet: 0.33
# Bigram: ('Katherine', 'spiller') Sannsynlighet: 1.0
# Bigram: ('spiller', 'piano')     Sannsynlighet: 0.67
# Bigram: ('piano', '<\\s>')       Sannsynlighet: 1.0
# ('<s>', 'Katherine') forekommer 1 gang. <s> forekommer 3 ganger. 1/3 = 0.33
#
# Sannsynlighet av den hele setningen er: 0.33 * 1.0 * 0.67 * 1.0 = 0.22
#
# Se nedenfor: Implementation 1.2 Del 2

# Del 2
# Tagger for TestSetninger.txt
# [('Samsung', 'NN'), ('has', 'HVZ'), ('unveiled', 'VBD'), ('a', 'AT'), ('virtual', 'JJ'), ('reality', 'NN'),
# ('rig', 'NN'), ('designed', 'VBD'), ('for', 'IN'), ('use', 'NN'), ('with', 'IN'), ('Windows', 'NNS'),
# ('PCs', 'NNS'), ('.', '.')]

# [('HMD', 'NN'), ('Odyssey', 'NN'), ('joins', 'NNS'), ('previously', 'RB'), ('announced', 'VBD'), ('VR', 'NN'),
# ('headsets', 'NNS'), ('and', 'CC'), ('hand', 'NN'), ('controllers', 'NNS'), ('from', 'IN'), ('Dell', 'NN'),
# (',', ','), ('HP', 'NN'), (',', ','), ('Lenovo', 'NN'), (',', ','), ('Acer', 'NN'), ('and', 'CC'), ('Asus', 'NNS'),
# ('to', 'TO'), ('form', 'NN'), ('the', 'AT'), ('launch', 'NN'), ('hardware', 'NN'), ('line-up', 'NN'), ('for', 'IN'),
# ('Microsoft', 'NN'), ("'s", 'NN$'), ('new', 'NN'), ('Mixed', 'VBD'), ('Reality', 'NN'), ('platform', 'NN'), ('.', '.')]

# [('Unlike', 'JJ'), ('earlier', 'NN'), ('PC-based', 'VBD'), ('VR', 'NN'), ('kit', 'NN'), (',', ','), ('the', 'AT'),
# ('new', 'NN'), ('products', 'NNS'), ('are', 'BER'), ('able', 'JJ'), ('to', 'TO'), ('track', 'NN'), ('their', 'PP$'),
# ('wearers', 'NNS'), ("'", 'NN'), ('movements', 'NNS'), ('in', 'IN'), ('a', 'AT'), ('room', 'NN'), ('without', 'NN'),
# ('requiring', 'VBG'), ('additional', 'JJ'), ('external', 'JJ'), ('sensors', 'NNS'), ('.', '.')]

# [('But', 'CC'), ('experts', 'NNS'), ('have', 'HV'), ('questioned', 'VBD'), ('whether', 'NN'), ('the', 'AT'),
# ('market', 'NN'), ('will', 'MD'), ('support', 'NN'), ('so', 'NN'), ('many', 'AP'), ('brands', 'NNS'), ('.', '.')]

# [('Until', 'NN'), ('now', 'NN'), (',', ','), ('HTC', 'NN'), ("'s", 'NN$'), ('Vive', 'NN'), ('and', 'CC'),
# ('Facebook', 'NN'), ("'s", 'NN$'), ('Oculus', 'NNS'), ('Rift', 'NN'), ('have', 'HV'), ('had', 'HVD'), ('most', 'NN'),
# ('of', 'IN'), ('the', 'AT'), ('market', 'NN'), ('in', 'IN'), ('high-end', 'NN'), ('PC-based', 'VBD'), ('VR', 'NN'),
# ('headsets', 'NNS'), ('to', 'TO'), ('themselves', 'VBZ'), ('.', '.')]

# [('But', 'CC'), ('the', 'AT'), ('two', 'NN'), ('firms', 'NNS'), ('had', 'HVD'), ('only', 'RB'), ('sold', 'NN'),
# ('a', 'AT'), ('combined', 'VBD'), ('total', 'JJ'), ('of', 'IN'), ('just', 'NN'), ('over', 'NN'), ('one', 'PN'),
# ('million', 'NN'), ('headsets', 'NNS'), ('by', 'IN'), ('the', 'AT'), ('end', 'NN'), ('of', 'IN'), ('June', 'NN'),
# (',', ','), ('according', 'VBG'), ('to', 'TO'), ('SuperData', 'NN'), ('Research', 'NN'), ('.', '.')]

# [('Both', 'ABX'), ('have', 'HV'), ('cut', 'NN'), ('their', 'PP$'), ('prices', 'VBZ'), ('in', 'IN'), ('recent', 'NN'),
# ('months', 'NNS'), ('in', 'IN'), ('an', 'AT'), ('attempt', 'NN'), ('to', 'TO'), ('stimulate', 'NN'), ('demand', 'NN'),
# ('.', '.')]

# [('By', 'IN'), ('contrast', 'NN'), (',', ','), ('Samsung', 'NN'), ("'s", 'NN$'), ('more', 'NN'), ('basic', 'JJ'),
# ('Gear', 'NN'), ('VR', 'NN'), ('-', '--'), ('which', 'WDT'), ('works', 'NNS'), ('with', 'IN'), ('some', 'JJ'),
# ('of', 'IN'), ('its', 'NNS'), ('smartphones', 'VBZ'), ('-', '--'), ('had', 'HVD'), ('sold', 'NN'), ('more', 'NN'),
# ('than', 'NN'), ('eight', 'NN'), ('million', 'NN'), ('units', 'NNS'), (',', ','), ('according', 'VBG'), ('to', 'TO'),
# ('the', 'AT'), ('same', 'NN'), ('market', 'NN'), ('research', 'NN'), ('.', '.')]

# [('``', '``'), ('VR', 'NN'), ('is', 'BEZ'), ('still', 'NN'), ('a', 'AT'), ('very', 'NN'), ('youthful', 'JJ'),
# ('medium', 'NN'), (',', ','), ('``', '``'), ('commented', 'VBD'), ('Kevin', 'NN'), ('Joyce', 'NN'), (',', ','),
# ('editor-in-chief', 'NN'), ('of', 'IN'), ('the', 'AT'), ('news', 'NNS'), ('site', 'NN'), ('VR', 'NN'),
# ('Focus', 'NNS'), ('.', '.'), ('``', '``')]

# [('There', 'NN'), ("'s", 'NN$'), ('a', 'AT'), ('number', 'NN'), ('of', 'IN'), ('significant', 'NN'),
# ('barriers', 'NNS'), ('to', 'TO'), ('entry', 'NN'), ('-', '--'), ('price', 'NN'), (',', ','), ('lack', 'NN'),
# ('of', 'IN'), ('variety', 'NN'), ('in', 'IN'), ('software', 'NN'), ('collections', 'NNS'), ('etc', 'NN'),
# ('-', '--'), ('all', 'ABN'), ('of', 'IN'), ('which', 'WDT'), ('are', 'BER'), ('slowly', 'RB'), ('being', 'BEG'),
# ('addressed', 'VBD'), ('.', '.')]

# [('But', 'CC'), ('in', 'IN'), ('the', 'AT'), ('short', 'NN'), ('term', 'NN'), (',', ','), ('I', 'PPSS'), ('do', 'DO'),
# ('think', 'NN'), ('we', 'PPSS'), ("'ll", 'NN'), ('see', 'NN'), ('some', 'JJ'), ('of', 'IN'), ('the', 'AT'),
# ('hardware', 'NN'), ('manufacturers', 'NNS'), ('in', 'IN'), ('the', 'AT'), ('current', 'NN'), ('race', 'NN'),
# ('fall', 'NN'), ('before', 'NN'), ('the', 'AT'), ('final', 'JJ'), ('hurdle', 'NN'), ('[', 'NN'), ('since', 'NN'),
# ('some', 'JJ'), (']', 'NN'), ('will', 'MD'), ('want', 'NN'), ('a', 'AT'), ('return', 'NN'), ('on', 'IN'),
# ('their', 'PP$'), ('investment', 'NN'), ('sooner', 'NN'), ('rather', 'NN'), ('than', 'NN'), ('later', 'NN'),
# ('.', '.'), ('``', '``')]

# [('Microsoft', 'NN'), ('hosted', 'VBD'), ('an', 'AT'), ('event', 'NN'), ('in', 'IN'), ('San', 'NN'),
# ('Francisco', 'NN'), ('to', 'TO'), ('mark', 'NN'), ('the', 'AT'), ('release', 'NN'), ('of', 'IN'), ('a', 'AT'),
# ('new', 'NN'), ('version', 'NN'), ('of', 'IN'), ('Windows10', 'NN'), ('on', 'IN'), ('17', 'CD'), ('October', 'NN'),
# ('that', 'CS'), ('supports', 'NNS'), ('new', 'NN'), ('virtual', 'JJ'), ('and', 'CC'), ('augmented', 'VBD'),
# ('reality', 'NN'), ('capabilities', 'VBZ'), ('.', '.')]

# [('The', 'AT'), ('firm', 'NN'), ('uses', 'VBZ'), ('the', 'AT'), ('term', 'NN'), ('``', '``'), ('mixed', 'VBD'),
# ('reality', 'NN'), ('``', '``'), ('to', 'TO'), ('refer', 'NN'), ('to', 'TO'), ('both', 'ABX'), ('VR', 'NN'),
# ('experiences', 'VBZ'), (',', ','), ('which', 'WDT'), ('are', 'BER'), ('based', 'VBD'), ('solely', 'RB'), ('in', 'IN'),
# ('computer-generated', 'VBD'), ('worlds', 'NNS'), (',', ','), ('as', 'CS'), ('well', 'NN'), ('as', 'CS'),
# ('AR', 'NN'), (',', ','), ('which', 'WDT'), ('mixes', 'VBZ'), ('graphics', 'NNS'), ('and', 'CC'), ('real-world', 'NN'),
# ('views', 'NNS'), ('together', 'NN'), ('.', '.')]

# [('Samsung', 'NN'), ("'s", 'NN$'), ('headset', 'NN'), ('was', 'BEDZ'), ('pitched', 'VBD'), ('as', 'CS'), ('a', 'AT'),
# ('premium', 'NN'), ('way', 'NN'), ('to', 'TO'), ('experience', 'NN'), ('VR', 'NN'), (',', ','), ('thanks', 'NNS'),
# ('to', 'TO'), ('it', 'PPS'), ('featuring', 'VBG'), ('higher-resolution', 'NN'), ('OLED', 'NN'), ('(', '('),
# ('organic', 'JJ'), ('light-emitting', 'VBG'), ('diode', 'NN'), (')', ')'), ('displays', 'NNS'), ('than', 'NN'),
# ('the', 'AT'), ('other', 'NN'), ('new', 'NN'), ('kit', 'NN'), ('.', '.')]

# [('It', 'PPS'), ('also', 'NN'), ('has', 'HVZ'), ('a', 'AT'), ('slightly', 'RB'), ('wider', 'NN'),
# ('field-of-view', 'NN'), ('and', 'CC'), ('integrated', 'VBD'), ('headphones', 'VBZ'), ('.', '.')]

# [('However', 'NN'), (',', ','), ('its', 'NNS'), ('$', 'NN'), ('499', 'CD'), ('(', '('), ('£425', 'NN'), (')', ')'),
# ('price', 'NN'), ('makes', 'VBZ'), ('it', 'PPS'), ('more', 'NN'), ('expensive', 'NN'), ('and', 'CC'), ('it', 'PPS'),
# ('will', 'MD'), ('go', 'NN'), ('on', 'IN'), ('sale', 'NN'), ('a', 'AT'), ('month', 'NN'), ('later', 'NN'),
# ('in', 'IN'), ('November', 'NN'), ('.', '.')]

# [('Microsoft', 'NN'), ('is', 'BEZ'), ('also', 'NN'), ('developing', 'VBG'), ('an', 'AT'), ('AR-based', 'VBD'),
# ('headset', 'NN'), ('that', 'CS'), ('does', 'DOZ'), ('not', '*'), ('require', 'NN'), ('a', 'AT'), ('separate', 'NN'),
# ('PC', 'NN'), ('called', 'VBD'), ('the', 'AT'), ('HoloLens', 'NNS'), ('.', '.')]

# [('But', 'CC'), ('a', 'AT'), ('prototype', 'NN'), ('sold', 'NN'), ('to', 'TO'), ('developers', 'NNS'),
# ('costs', 'NNS'), ('£2,719', 'NN'), ('and', 'CC'), ('there', 'NN'), ('was', 'BEDZ'), ('no', 'AT'), ('update', 'NN'),
# ('as', 'CS'), ('to', 'TO'), ('when', 'NN'), ('it', 'PPS'), ('will', 'MD'), ('get', 'NN'), ('a', 'AT'),
# ('mass-market', 'NN'), ('release', 'NN'), ('.', '.')]

# [('One', 'NN'), ('industry-watcher', 'NN'), ('suggested', 'VBD'), ('that', 'CS'), ('consumers', 'NNS'),
# ('tempted', 'VBD'), ('to', 'TO'), ('invest', 'NN'), ('in', 'IN'), ('Microsoft', 'NN'), ('and', 'CC'), ('its', 'NNS'),
# ('partners', 'NNS'), ("'", 'NN'), ('VR', 'NN'), ('tech', 'NN'), ('should', 'MD'), ('wait', 'NN'), ('a', 'AT'),
# ('while', 'CS'), ('before', 'NN'), ('making', 'VBG'), ('a', 'AT'), ('purchase', 'NN'), ('.', '.'), ('``', '``')]

# [('The', 'AT'), ('launch', 'NN'), ('of', 'IN'), ('all', 'ABN'), ('of', 'IN'), ('those', 'NN'), ('head', 'NN'),
# ('mounted', 'VBD'), ('displays', 'NNS'), ('will', 'MD'), ('create', 'NN'), ('a', 'AT'), ('lot', 'NN'), ('of', 'IN'),
# ('competition', 'NN'), ('and', 'CC'), ('possibly', 'RB'), ('price', 'NN'), ('aggressiveness', 'NNS'), ('in', 'IN'),
# ('this', 'NNS'), ('space', 'NN'), ('in', 'IN'), ('the', 'AT'), ('coming', 'VBG'), ('holiday', 'NN'), ('season', 'NN'),
# (',', ','), ('``', '``'), ('Annette', 'NN'), ('Zimmermann', 'NN'), ('from', 'IN'), ('the', 'AT'),
# ('consultancy', 'NN'), ('Gartner', 'NN'), ('told', 'NN'), ('the', 'AT'), ('BBC', 'NN'), ('.', '.'), ('``', '``')]

# [('Until', 'NN'), ('now', 'NN'), ('all', 'ABN'), ('PC', 'NN'), ('vendors', 'NNS'), ('were', 'BED'),
# ('linking', 'VBG'), ('their', 'PP$'), ('high-end', 'NN'), ('devices', 'VBZ'), ('with', 'IN'), ('Oculus', 'NNS'),
# ('or', 'CC'), ('HTC', 'NN'), ('headsets', 'NNS'), ('.', '.')]

# [('With', 'IN'), ('their', 'PP$'), ('own', 'NN'), ('headsets', 'NNS'), ('available', 'JJ'), (',', ','), ('it', 'PPS'),
# ('is', 'BEZ'), ('likely', 'RB'), ('that', 'CS'), ('they', 'PPSS'), ('will', 'MD'), ('focus', 'NNS'), ('on', 'IN'),
# ('promoting', 'VBG'), ('bundles', 'VBZ'), ('with', 'IN'), ('their', 'PP$'), ('own', 'NN'), ('devices', 'VBZ'),
# ('.', '.'), ('``', '``')]

# [('By', 'IN'), ('Leo', 'NN'), ('Kelion', 'NN'), (',', ','), ('Technology', 'NN'), ('desk', 'NN'),
# ('editor', 'NN'), ('.', '.')]

# [('http', 'NN'), (':', ':'), ('//www.bbc.com/news/technology-41491862', 'NN')]

###########
# Feilene #
###########

# 1. Odyssey, Facebook, Windows10
# Taggeren kan ikke finne egennavn. Vi kan ordne det meg tagging alle ord som begynner med en stor bokstav
# og står ikke i begynnelsen av setning med NT-tag. Denne metoden ikke garanterer 100% presisjon.

# 2. this, these, those
# Taggeren har ikke regler for å tagge slike determinativer ”this, these, those” med DT (singular determiner),
# DTS (plural determiner) tagger.
# Merk: Jeg tagger ”that” som Subordinating conjunction (CS) fordi det forekommer oftere som CS enn DT

# 3. to track, to form (VB) vs to developers, to entry price ()
# Vi kunne bruke ”to” som en indikasjon at det neste ordet er ”verb base form” (VB).
# Men på grunn at ”to” er flertydig og det brukes ofte som ”preposition” (IN), ca 41% in Brown korpuset,
# skal gi den slike regelen mange feil.


##################
# Implementation #
##################
# 1.2 Del 2
import nltk
from collections import defaultdict, Counter
from itertools import tee

# Settings
text = ['<s> Truls spiller piano <\s>',
        '<s> Katherine spiller ikke piano <\s>',
        '<s> Ludovico spiller piano <\s>']

test = ['<s> Katherine spiller piano <\s>',]

START_TOKEN = '<s>'
END_TOKEN = '<\\s>'


# The generator that yields tokens from a list of sentences, this is supposed to be plugged into data pip
# after a file reader
def tokens_maker(sentences_lst):
    for sentence in sentences_lst:
        for token in sentence.split():
            yield token


# The generator that yields bigrams from a stream of tokens. It relies on start/stop beacons that indicate
# boundaries of a sentence.
def bigram_maker(tokens):
    token0 = START_TOKEN
    next(tokens)
    for token1 in tokens:
        if token1 in END_TOKEN:
            yield token0, token1
            token0 = START_TOKEN
            next(tokens)
        else:
            yield token0, token1
            token0 = token1


# The function creates a dictionary where key is a bigram, and value is its probability.
def train_model(corpus):
    model = defaultdict(float)
    # We use tee() to replicate the generator that will be consumed twice
    tokens, tokens2 = tee(tokens_maker(corpus))
    bigrams = bigram_maker(tokens)
    # Counting is carried out with a helper class from collections module
    tokens_f = Counter(tokens2)
    bigrams_f = Counter(bigrams)
    # Probability is calculated as the bigram count devided by the count of the first unigram of this bigram
    for key in bigrams_f:
        model[key] = round((bigrams_f[key] / tokens_f[key[0]]), 2)
    return model


# The function calculates probability of a sentence. It takes the bigrams of a sentence and the model (dictionary
# of probabilities) as the input.
def calculate_probability(bigrams, model):
    probability = 1
    # Find bigrams' probability and calculate their product
    for bigram in bigrams:
        print(bigram)
        probability *= model[bigram]
    return round(probability, 2)

###################################################################
# 2

# Settings
brown_train = nltk.corpus.brown.tagged_sents(categories='adventure')
brown_test = nltk.corpus.brown.tagged_sents(categories='fiction')

# Patterns
patterns = [(r'^(?:[Tt]he|[Aa]n?|[Ee]very|[Nn]o)$',
             'AT'),                                     # Determiner E.g.: the, a, an, every, no
            (r'.*(?:ly|wise|ward[s]?)$', 'RB'),         # Adverb E.g.: slowly, forward, clockwise
            (r'^(?:[Aa]nd|[Nn]?[Oo]r|[Bb]ut)$', 'CC'),  # Coordinating conjunction E.g.: and, or, but
            (r'^(?:[Tt]hat|[Ii]f|[Bb]ecause|[Th]ough|'
             r'[Aa]s|[Ww]hile)$', 'CS'),                # Subordinating conjunction E.g. that
            (r'^[Nn]ot$', '*'),                         # Not
            (r'(?:[Aa]ll|[Hh]alf)$', 'ABN'),            # Pre-quantifier E.g.: all, half
            (r'^[Bb]oth$', 'ABX'),                       # Pre-quantifier E.g.: both
            (r'^(?:[Nn]ext|[Ll]atter|[Ll]ast|[Ff]ew|'
             r'[Ss]everal|[Mm]any|[Mm]uch)$', 'AP'),    # Post-determiner E.g.: last, few, next
            (r'.*(?:less|ful|able|ous|like|ish|'
             r'some|al|ary|ic|sque)$', 'JJ'),         # Adjective E.g.: handsome, joyful, delicious, practical
            (r'^[Bb]e$', 'BE'),                         # 'Be'
            (r'^[Ww]ere$', 'BED'),                      # 'Be' simple past, 3rd person, plural
            (r'^[Ww]as$', 'BEDZ'),                      # 'Be' simple past, 3rd person, singular
            (r'^[Bb]eing$', 'BEG'),                     # 'Be' gerund
            (r'^[Aa]m$', 'BEM'),                        # 'Be' present, 1st person, singular
            (r'^[Bb]een$', 'BEN'),                      # 'Be' past participle
            (r'^[Aa]re$', 'BER'),                       # 'Be' present, plural
            (r'^[Ii]s$', 'BEZ'),                        # 'Be' present, 3rd person, singular
            (r'^[Dd]o$', 'DO'),                         # 'Do'
            (r'^[Dd]oes$', 'DOZ'),                      # 'Do' present, 3rd person, singular
            (r'^[Dd]id$', 'DOD'),                       # 'Do' simple past
            (r'^[Hh]ad$', 'HVD'),                       # 'Have' past
            (r'^[Hh]as$', 'HVZ'),                       # 'Have' present, 3rd person
            (r'^[Hh]ave$', 'HV'),                       # 'Have' present, 1-2 person, singular, plural
            (r'^(?:[Oo]f|[Ii]n|[Ff]or|[Oo]n|[Ww]ith|'
             r'[Aa]t|[Bb]y|[Ff]rom|[Uu]p)$', 'IN'),     # Preposition E.g.: of, in, on, with, at, from
            (r'.*ing$', 'VBG'),                         # Gerunds E.g.: snowing
            (r'.*(?:ify)$', 'VB'),                      # Verb E.g.: justify
            (r'^(?:.*ed|said)$', 'VBD'),                # Simple past E.g.: said, visited
            (r'.*es$', 'VBZ'),                          # 3rd singular present E.g.: goes
            (r'^(?:[SsWw]h?ould|[Mm]ust|may|'
             r'[Cc]an|[Ww]ill)$', 'MD'),                        # Modal verbs E.g.: should, would, must
            (r'.*\'s$', 'NN$'),                         # Possessive Nouns E.g.: visitor's
            (r'.*s$', 'NNS'),                           # Plural Nouns E.g.: friends
            (r'^(?:[Ii]t|[Ss]?[Hh]e)$', 'PPS'),         # 3rd. singular nominative pronoun
            (r'^(?:[Ww]e|[Yy]ou|[Tt]hey|I)$','PPSS'),   # Other nominative personal pronoun
            (r'^(?:him|her|us|them|[Mm]e)$', 'PPO'),    # Objective personal pronoun E.g.: him, her, us
            (r'^(?:[Hh]is|[Hh]er|[Tt]heir|[Oo]ur|'
             r'[Ii]ts|[Mm]y|[Yy]our)$', 'PP$'),         # Possessive personal pronoun E.g.: his, her, our
            (r'^(?:(?:[Ee]very|[Ss]ome|[Aa]ny|'
             r'[Nn]o)thing|(?:[Ee]very|[Ss]ome|'
             r'[Aa]ny|[Nn]o)body|(?:[Ee]very|'
             r'[Ss]ome|)one)$', 'PN'),                  # Nominal pronoun E.g.: everything, nobody, someone
            (r'^[Tt]o$', 'TO'),                         # Infinitive marker E.g.: to
            (r'^(?:[Ww]hich|[Ww]hat)(?:ever)?$', 'WDT'),# wh- determiner E.g. what, which
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),            # Cardinal numbers E.g.: 0, 1
            (r'\.$', '.'),                              # Dot
            (r'\,$', ','),                              # Comma
            (r'``$', '``'),                             # Quotation mark
            (r"''$", "''"),                             # Quotation mark
            (r'\?$', '?'),                              # Question mark
            (r'!$', '!'),                               # Exclamation mark
            (r'^-{1,2}$', '--'),                        # Dash
            (r'^\($', '('),                             # Brackets
            (r'^\)$', ')'),                             # Brackets
            (r';$', ';'),                               # Semicolon
            (r'^:$', ':'),                              # Colon
            (r'.*', 'NN')]                              # nouns (default) E.g.: faith

# Initiate tagger
regexp_tagger = nltk.RegexpTagger(patterns)


# Sentence maker. Returns a list with the tokens of one sentence. It uses nltk tokenizers
def make_sentence(filename):
    with open(filename, 'r') as in_file:
        sentences = (nltk.sent_tokenize(line.strip()) for line in in_file if line != '\n')
        for line in sentences:
            for sentence in line:
                yield nltk.word_tokenize(sentence)


# Tagger function, it relies on nltk tagger.
def tag_sentences(sentences_list, tagger):
    for sentence in sentences_list:
        yield tagger.tag(sentence)


########
# DEMO #
########
if __name__ == '__main__':
    # Del 2
    # 1.2
    t = tokens_maker(text)
    b = bigram_maker(t)
    model = train_model(text)
    print('\nAll bigrams and their probability:')
    for i in model:
        print('Bigram: {:25}Probability: {}'.format(str(i), model[i]))

    t2 = tokens_maker(test)
    b2 = bigram_maker(t2)
    print('\bBigrams from the test sentence:')
    print('Probability of the test sentence: {}'.format(calculate_probability(b2, model)))

    # 2
    print('*' * 15)
    print('\nWe are going to evaluate the tagger. It takes a while...')
    print('Success rate for Brown (Adventure): {:.3f}'.format(regexp_tagger.evaluate(brown_train)))
    print('Success rate for Brown (Fiction): {:.3f}'.format(regexp_tagger.evaluate(brown_test)))
    print('*' * 15)
    print('\nThis is the tagged content of testsetninger.txt \n')
    make_sentence('testsetninger.txt')
    for sent in make_sentence('testsetninger.txt'):
        for tagged in tag_sentences([sent], regexp_tagger):
            print(tagged)

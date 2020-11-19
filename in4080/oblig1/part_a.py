import nltk
from nltk.corpus import brown
import numpy as np
import matplotlib.pyplot as plt
from urllib import request
import re
from collections import Counter

# Exercise 1
categories = ['news', 'religion', 'government', 'fiction', 'romance']
words = ['he', 'him', 'she', 'her']

cfd = nltk.ConditionalFreqDist(
    (category, word.lower())
    for category in categories
    for word in brown.words(categories=category)
)

# Exercise 1.A
print('\n# Exercise 1.A')
cfd.tabulate(samples=words)

# Exercise 1.B
print('\n# Exercise 1.B')
for category in categories:
    masc = sum(cfd[category][word] for word in ['he', 'him'])
    fem = sum(cfd[category][word] for word in ['she', 'her'])
    percent_masc = masc / (masc + fem) * 100
    print(f'Category: {category}, M: {masc}, F: {fem} %M: {percent_masc}, %F: {100-percent_masc}', )

# Exercise 1.C
print('\n# Exercise 1.C')
masc = ['he', 'him']
fem = ['she', 'her']
nom = ['he', 'she']
obj = ['him', 'her']
categories_2 = ['masc', 'fem']


def gender_filter(word: str) -> str:
    if word in masc:
        return 'masc'
    elif word in fem:
        return 'fem'
    else:
        return 'none'


cfd_2 = nltk.ConditionalFreqDist((gender_filter(word.lower()), word.lower()) for word in brown.words())

for category in categories_2:
    nom_summary = sum(cfd_2[category][word] for word in nom)
    obj_summary = sum(cfd_2[category][word] for word in obj)
    print(f'Category: {category}, (he, she): {nom_summary}, (him, her): {obj_summary}')


masc_rel_freq = cfd_2['masc']['him'] / sum(cfd_2['masc'][word] for word in masc) * 100
fem_rel_freq = cfd_2['fem']['her'] / sum(cfd_2['fem'][word] for word in fem) * 100

print(f'Relative freq.(%) him to (he + him): {masc_rel_freq}')
print(f'Relative freq.(%) her to (she + her): {fem_rel_freq}')

# Exercise 1.D
print('\nExercise 1.D')


def tag_transformer(tag: str) -> str:
    result = tag

    if '-' in tag:
        result = tag.split('-')[0]

    return result


brown_tagged = nltk.corpus.brown.tagged_words()
cfd_3 = nltk.ConditionalFreqDist((tag_transformer(tag), word.lower()) for word, tag in brown_tagged)

cfd_3.tabulate(conditions=['PP$', 'PP$$', 'PPO', 'PPS'], samples=['he', 'him', 'she', 'her', 'his', 'hers'])

# Exercise 1.E
print('\nExercise 1.E')
rel_PPO_her = cfd_3['PPO']['her'] / (cfd_3['PPO']['her'] + cfd_3['PP$']['her'] + cfd_3['PP$$']['hers'] +
                                     cfd_3['PPS']['she']) * 100

rel_PPS_she = cfd_3['PPS']['she'] / (cfd_3['PPO']['her'] + cfd_3['PP$']['her'] + cfd_3['PP$$']['hers'] +
                                     cfd_3['PPS']['she']) * 100

rel_PPO_his = cfd_3['PPO']['him'] / (cfd_3['PPO']['him'] + cfd_3['PP$']['his'] + cfd_3['PP$$']['his'] +
                                     cfd_3['PPS']['he']) * 100

rel_PPS_he = cfd_3['PPS']['he'] / (cfd_3['PPO']['him'] + cfd_3['PP$']['his'] + cfd_3['PP$$']['his'] +
                                     cfd_3['PPS']['he']) * 100

print(f'Objective forms. M:{rel_PPO_his}, F:{rel_PPO_her}')
print(f'Nominative forms. M:{rel_PPS_he}, F:{rel_PPS_she}')

# Exercise 1.F
print('\nExercise 1.F')
tags = ['PPS', 'PP$', 'PPO', 'PP$$']
f_pron = ['she', 'her', 'her', 'hers']
m_pron = ['he', 'his', 'him', 'his']

# data to plot
n_groups = 4
fem = [cfd_3[tag][word] for tag, word in zip(tags, f_pron)]
masc = [cfd_3[tag][word] for tag, word in zip(tags, m_pron)]

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, masc, bar_width,
alpha=opacity,
color='b',
label='Masculine')

rects2 = plt.bar(index + bar_width, fem, bar_width,
alpha=opacity,
color='r',
label='Feminine')

plt.xlabel('Type of Pronoun')
plt.ylabel('Frequency')
plt.title('Pronouns by type')
plt.xticks(index + bar_width, ('PPS', 'PP\$', 'PPO', 'PP\$\$'))
plt.legend()

plt.tight_layout()
plt.show()

# Exercise 2.A
print('\nExercise 2.A')
url = "https://www.gutenberg.org/files/74/74-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

# Exercise 2.B
print('\nExercise 2.B')

text_start = '“TOM!”'
text_end = 'End of the Project Gutenberg'

# Trim Intro and Outtro
raw = raw[raw.find(text_start):]
raw = raw[:raw.find(text_end)]

# Remove chapter numbers
regex_chapter = re.compile('CHAPTER .*\r')
raw = regex_chapter.sub('', raw)

# Remove conclusion
regex_concl = re.compile('CONCLUSION.*\r')
raw = regex_concl.sub('', raw)

# Exercise 2.C
print('\nExercise 2.C')
# All tokens
tokens = nltk.word_tokenize(raw)

# Remove dot
tokens = [token.replace('.', '') for token in tokens]

# Remove underscore
tokens = [token.replace('_', '') for token in tokens]

# Remove punctuation
pattern_punctuation = re.compile('^\W+$')
tokens = [token for token in tokens if not pattern_punctuation.match(token)]

# Remove empty line
tokens = [token for token in tokens if token != '']

# To lower case
tokens = [token.lower() for token in tokens]

# Exercise 2.D
frq_dist = nltk.FreqDist(tokens)

most_common_20 = frq_dist.most_common(20)

for idx, (word, freq) in enumerate(most_common_20):
    print(f'Pos:{idx}, Token:{word}, Frequency:{freq}')

# Exercise 2.E
data = []
print(len(set(frq_dist.values())))
c = Counter(frq_dist.values())
for i in range(1, 11):
    data.append([i, c[i]])

# 11-50
keys_11_50 = [key for key in c.keys() if 11 <= key <= 50]
sum_11_50 = sum(c[key] for key in keys_11_50)
data.append(['11-50', sum_11_50])

# 51-100
keys_51_100 = [key for key in c.keys() if 51 <= key <= 100]
sum_51_100 = sum(c[key] for key in keys_51_100)
data.append(['51-100', sum_51_100])

# >100
keys_100 = [key for key in c.keys() if key > 100]
sum_100 = sum(c[key] for key in keys_100)
data.append(['>100', sum_100])

for freq, words in data:
    print(f'Frequency: {freq}, No.Words:{words}')

# Exercise 2.F
print('\n Exercise 2.F')


for idx, (word, freq) in enumerate(most_common_20, start=1):
    print(f'Rank: {idx}, R*N: {(idx * freq)}')
    data.append([idx, idx * freq])

# Exercise 2.G
print('\n Exercise 2.G')

x = list(range(1, len(frq_dist) + 1))
y = list(frq_dist.values())
y.sort(reverse=True)


plt.plot(x, y)
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title("Zipf's Law")
plt.show()

x2 = np.log(x)
y2 = np.log(y)
plt.plot(x2, y2)
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title("Zipf's Law - Log Space")
plt.show()

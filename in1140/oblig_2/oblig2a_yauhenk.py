# 1.1
# 1. Ordklasser er kategorier som man bruker til å klassifisere ord basert på felles trekk. Blant slike trekk eller
# kategorier kan jeg nevne morfologiske, syntaktiske og semantiske kriterier.
# 2. På norsk opererer vi med følgende ordklasser: substantiv, verb, adjektiv, adverb, pronomen, preposisjon,
# konjunksjon, subjunksjon, interjeksjon og determinativ.
# 3. Innholdsord har betydning; de betegner objekter, kvaliteter, handlinger, osv.
# Funksjonsord kobler innholdsord sammen og hjelper til å skape større syntaktiske strukturer.
# 4. Bøyning er endring av ord som man gjør for å uttrykke forskjellige grammatiske kategorier, for eksempel,
# kjønn, bestemthet, tall eller tid. Ved bøyning bytter ordet ikke ordklasser. Det er ingen eller liten betydningsendring.
# Avledning er endring av semantiske egenskaper i ord. Ved avledning kan et ord bytte ordklasse.
# Bøyningsmorfemer er vanligvis plassert etter avledningsmorfemer. Mange avledningsmorfemer er ikke produktive.

#1.2
#DT determinative
#NN substantive
#JJ adjektiv
#VB verb
#CC konjunksjon
#PR preposisjon
#PO pronomen
#RB adverb
#SB subjunksjon

[('Politiet', 'NN'), ('ber', 'VB'), ('fortsatt', 'RB'), ('om', 'PR'), ('tips', 'NN'), ('etter', 'PR'), ('et', 'DT'),
 ('stort', 'JJ'), ('våpentyveri', 'NN'), ('i', 'PR'), ('Oslo', 'NN'), ('sentrum', 'NN')]

[('Laks', 'NN'), ('og', 'CC'), ('poteter', 'NN'), ('til', 'PR'), ('middag', 'NN')]

[('Lars', 'NN'), ('sang', 'VB'), ('vakkert', 'RB')]

# 1.3
# 1. Det mest frekvente ordet i Brown er determinativen 'the'
# 2. Den mest frekvente ordklassen i Brown er 'NN'
# 3. Disse ordklassene tilsvarer til ett ord:
# BER-HL, MD*-HL, CS-HL, DT$, FW-DT, AP-TL, UH-TL, VBN-TL-HL, NNS-TL-HL, DT-HL, BE-HL,
# PPSS+HVD, NP-TL-HL, MD+HV, OD-HL, VBD-TL, FW-CC, BEDZ-HL, AP$, NP+BEZ, MD-TL, PN+HVZ,
# ABN-HL, PPS+BEZ-HL, HVD-HL, RB$, FW-AT-HL, DO-HL, PP$-TL, FW-IN-TL, *-HL, PN-HL, PN$,
# BER-TL, TO-TL, BED*, RB+BEZ, VB+PPO, PPSS-HL, HVZ*, FW-IN+NN-TL, FW-IN+AT-TL, JJ-NC, NR$-TL,
# FW-PP$-NC, FW-VB, FW-VB-NC, JJR-NC, NPS$-TL, QL-TL, FW-*, FW-CD, WQL, FW-WDT, WDT+BEZ

# 2
# 1. Når vi sier at det finnes flertydighet i språket, mener vi at det er ord som kan ha flere betydninger eller
# som kan tilhøre forskjellige ordklasser. Et eksempel på norsk er ordet ‘dyr’. Det kan være et adjektiv og bety
# noe som koster mye eller det kan være et substantiv og da betyr det et levende vesen.
# Et eksempel på engelsk er ordet ‘note’. Det kan være et substantiv med flere betydninger, for eksempel, et symbol
# som blir brukt i musikk, et kort notat. Eller så kan ‘note’ fungere som et verb og da betyr det å være oppmerksom på noe.
# 2. 2166 ord i Brown forekommer med mer enn én ordklassetagg.
# 3. Ordene 'to' og 'house' har flest tagger  i Brown-korpuset. Jeg fant at disse ordene forekommer med 7 tagger.
# 'to', {'TO', 'TO-HL', 'IN-TL', 'IN', 'NPS', 'IN-HL', 'TO-TL'
# 'house', {'NN-HL', 'NP', 'NP-TL-HL', 'NN-TL', 'VB', 'NN-TL-HL', 'NN'}
# 4. Ferdig. Se nedenfor.
# 5. Frekvenslisten for ordet 'house' er:
# NN-TL: 68
# NN: 24
# NN-HL: 1
# NP-TL-HL: 1
# NP: 1
# NN-TL-HL: 1
# VB: 1
# Frekvenslisten for ordet 'to' er:
# TO: 1237
# IN: 889
# IN-HL: 5
# TO-HL: 6
# IN-TL: 5
# TO-TL: 1
# NPS: 1



##################
# IMPLEMENTATION #
##################


import nltk

#brown = nltk.corpus.brown.tagged_words(categories='news')
brown = nltk.corpus.brown.tagged_words()

# 1.3
def frequency_counter(input_data, check='word'):
    word_dict = {}

    if check == 'word':
        for i in input_data:
            if i[0].lower() not in word_dict:
                word_dict[i[0].lower()] = 1
            else:
                word_dict[i[0].lower()] += 1

    elif check == 'class':
        for i in input_data:
            if i[1] not in word_dict:
                word_dict[i[1]] = 1
            else:
                word_dict[i[1]] += 1
    return word_dict


# 1.3
def sort_items_by_frequency(input_data, rev=True):
    sorted_input_data = sorted(input_data.items(), key=lambda x: x[1], reverse=rev)
    return sorted_input_data


# 2, 2
def multiple_class_finder(input_data):
    word_dict = {}
    for i in input_data:
        temp_value = set()
        if i[0].lower() not in word_dict:
            temp_key = i[0].lower()
            temp_value.add(i[1])
            word_dict[temp_key] = temp_value
        elif i[0].lower() in word_dict:
            word_dict[i[0].lower()].add(i[1])
    return word_dict


# 2, 2
def count_multiclass_words(input_data):
    multi_class_words = [key for key in input_data if len(input_data[key]) > 1]
    return multi_class_words, len(multi_class_words)


# 2, 3
def sort_items_by_no_of_classes(input_data, rev=True):
    sorted_input_data = sorted(input_data.items(), key=lambda x: len(x[1]), reverse=rev)
    return sorted_input_data


# 2, 4
def freqs(w, brown):
    tag_dict = {}
    for token in brown:
        if w.lower() == token[0].lower() and token[1] in tag_dict:
            tag_dict[token[1]] += 1
        elif w.lower() == token[0].lower() and token[1] not in tag_dict:
            tag_dict[token[1]] = 1
    print('Word "{}" is found with the following tags'.format(w))
    for key, value in tag_dict.items():
        print('{}: {}'.format(key, value))


if __name__ == '__main__':


# 1.3, 1
    print('Output for task 1.3, 1')
    freq_dic_word = frequency_counter(brown, check='word')
    freq_dic_word_sroted = sort_items_by_frequency(freq_dic_word, rev=True)
    print('The most frequent word is "{p[0]}".\nWe found it {p[1]} times.'.format(p=freq_dic_word_sroted[0]))

# 1.3, 2
    print('\nOutput for task 1.3, 2')
    freq_dic_class = frequency_counter(brown, check='class')
    freq_dic_word_class = sort_items_by_frequency(freq_dic_class, rev=True)
    print('The most frequent class is "{p[0]}".\nWe found it {p[1]} times.'.format(p=freq_dic_word_class[0]))

# 1.3, 3
    print('\nOutput for task 1.3, 3')
    print('The least frequent class is "{p[0]}".\nWe found it {p[1]} times.'.format(p=freq_dic_word_class[-1]))

# 2, 2
    print('\nOutput for task 2, 2')
    multi_class_words_dict = multiple_class_finder(brown)
    multi_class_words_list, multi_class_words_count = count_multiclass_words(multi_class_words_dict)
    print('There are {} multiclass words in Brown.'.format(multi_class_words_count))

# 2, 3
    print('\nOutput for task 2, 3')
    multi_class_words_sorted = sort_items_by_no_of_classes(multi_class_words_dict)
    word_with_most_classes = multi_class_words_sorted[0][0]
    no_class_for_word = len(multi_class_words_sorted[0][1])
    print('The word with most classes is "{}".\n'
          'It belongs to the following no. of classes: {}'.format(word_with_most_classes, no_class_for_word))

# 2, 5
    print('\nOutput for task 2, 5')
    freqs('new', brown)

    #freq_dic_class = frequency_counter(brown, check='word')
    #print(sort_items_by_frequency(freq_dic_class, rev=True))
    print(freq_dic_class['JJ'])
    print({item for item in brown if item[1] == 'WDT'})



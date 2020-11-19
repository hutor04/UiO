import re

############
# SETTINGS #
############
input_text = 'ino1.txt'
white_space_tok_out = 'white_space_tokenizer_output.txt'
regex_tok_out = 'regex_tokenizer_output.txt'

# We read the data to a string.
with open(input_text, 'r') as input_file:
    data_in_str = input_file.read()


##################
# IMPLEMENTATION #
##################

# Task 1

# We count all occurrences of 'er' in the input text. The function accepts input text as string, string to search for
# and boolean match_case (the default is True).
def count_er(text, substring='er', match_case=True):
    if not match_case:
        # Convert characters to lower case and count the occurrences of the substring.
        return text.lower().count(substring)
    # Count the occurrences of the substring.
    return text.count(substring)


# We count all occurrences of 'er' in the end of each word.
# The function accepts input text as string, string to search for
# and boolean match_case (the default is True).
def count_ends_er(text, substring='er', match_case=True):
    if not match_case:
        # Convert characters to lower case, create a list with words that end with the substring, then return the
        # length of the list.
        return len([word for word in text.lower().split() if word.endswith(substring)])
    # Create a list with words that end with the substring, then return the length of the list.
    return len([word for word in text.split() if word.endswith(substring)])


# The function creates a list of the last two characters of each word from the input text.
# There's an option to handle the words that actually have less than 2 characters, and we can not
# return 2 characters per word (we then skip words with less than 2 characters).
def last_two_characters_list(text, count_short_words=True):
    if count_short_words:
        # We create a list where we place to last characters of each word regardless of the length of a word.
        return [word[-2:] for word in text.split()]
    else:
        # We create a list where we place to last characters of each word only if a word is 2 or more characters long.
        return [word[-2:] for word in data_in_str.split() if len(word) >= 2]


# This function builds a string delimited with spaces. It accepts a list as the argument.
def list_to_string(list_of_elements):
    return ' '.join(list_of_elements)

# Task 2

# We read the data to a list of lines.
def data_tolist():
    lines = []
    f = open(input_text, 'r')
    for line in f:
        lines.append(line)
    f.close()
    return lines


# We count the number of words.
def count_words(text):
    # A more reasonable solution: return len([word for word in text.split()])
    # This below is implemented as per instructions in the task.
    counter = 0
    for i in text.split():
        counter += 1
    return counter

# Task 3

# We split input text to words (space separated). We write each word to a file from the new line.
def white_space_tokenizer(text):
    words = text.split()
    with open(white_space_tok_out, 'w') as f_out:
        for word in words:
            f_out.write(word + '\n')
    return words


# Here is a set of patterns that we used to tokenize the text, variable names are self-explanatory
pattern_date = '\d{2}\.\d{2}\.\d{4}'
pattern_date_2 = '\d{2}-\d{2}-\d{4}'
pattern_date_3 = '\d{2} [aåA-Å]{3,7} \d{4}'
pattern_time = '\d{2}:\d{2}'
pattern_number = '(?:\d{1,3}[ \.,])?\d{1,3}[ \.,]\d{1,3}'
pattern_phone_no = '[tT][lL][Ff]\.? ?\d{2} ?\d{2} ?\d{2} ?\d{2}'
pattern_co2 = 'CO 2'
pattern_web_address = 'http[s]?:\/\/(?:www\.)?[\w-]{1,121}\.\w{2,24}[\w\/\.]*'
pattern_website_no = '(?:www.)?[\w-]{1,121}\.no'
email = "[\w!#\$%&'\*+\/=\?\^_`\{\|\}~\.]+@[\w-]{1,121}\.[a-zA-Z]{2,3}"
pattern_hyphoned_word = r'\w+-\w+'
pattern_word = '\w+'

# Final pattern, we compile it in advance for multiple reuse and better performance.
PATTERN = re.compile('|'.join([pattern_date, pattern_date_2, pattern_date_3, pattern_time, pattern_phone_no,
                               pattern_co2, pattern_website_no, email, pattern_number, pattern_web_address,
                               pattern_hyphoned_word, pattern_word]))


# This the regex tokenizer.
def regex_tokenizer(text, p):
    # It finds all matches for the pattern
    words = p.findall(text)
    # We write the result to file, each token from new string.
    with open(regex_tok_out, 'w') as f_out:
        for word in words:
            f_out.write(word + '\n')
    return words


####################
# DEMO STARTS HERE #
####################
if __name__ == '__main__':
    # Task 1
    # Count 'er'
    t1_match_case = count_er(data_in_str, match_case=True)
    t1_not_match_case = count_er(data_in_str, match_case=False)
    print('The number of "er" in match case mode is {}.\nThe number of "er" in ignore case mode is {}'.format(t1_match_case,
                                                                                                t1_not_match_case))
    print('-' * 10)

    # Count 'er' in the end
    t1_count_ends_er_match_case = count_ends_er(data_in_str, match_case=True)
    t1_count_ends_er_not_match_case = count_ends_er(data_in_str, match_case=False)

    print('The number of words that end with "er" in match case mode is {}.\n'
          'The number of words that end with "er" in ignore case mode is {}'.format(t1_count_ends_er_match_case,
                                                                                    t1_count_ends_er_not_match_case))
    print('-' * 10)

    # Create a list of last two characters
    t1_last_2_chars_short = last_two_characters_list(data_in_str)
    t1_last_2_chars_long = last_two_characters_list(data_in_str, count_short_words=False)
    sample1 = t1_last_2_chars_short[0:10]
    sample2 = t1_last_2_chars_long[0:10]
    print('Here are some endings including short words {}'.format(sample1))
    print('Here are some endings EXcluding short words {}'.format(sample2))
    print('-' * 10)

    # Convert the list to string
    t1_last_2_chars_short_str = list_to_string(t1_last_2_chars_short)
    t1_last_2_chars_long_str = list_to_string(t1_last_2_chars_long)
    sample2 = t1_last_2_chars_short_str[0:50]
    sample3 = t1_last_2_chars_long_str[0:50]
    print('Here is a sample of the string of last two elements (including short words)\n{}'.format(sample2))
    print('Here is a sample of the string of last two elements (EXcluding short words)\n{}'.format(sample3))
    print('-' * 10)

    # Task 2

    # Read file to the list of lines and output number of lines
    l = data_tolist()
    print("Let's check if we managed to read file to the list of lines.\nThere are {} lines in the text.\n"
          "Here is the first line:\n{}".format(len(l), l[0]))
    print('-' * 10)

    # Count words in file
    no_of_words = count_words(data_in_str)
    print('The number of words (space separated) in text is {}.'.format(no_of_words))

    # Task 3

    # We write words to a file. white_space_tokenizer also returns the list of tokens (space separated)
    ws = white_space_tokenizer(data_in_str)
    sample4 = ws[0:10]
    print('Sample tokens (space separated):\n{}\n'.format(sample4))

    # We run regex tokenizer. It saves the results to file and also returns the list of tokens.
    reg = regex_tokenizer(data_in_str, PATTERN)
    print('The number of tokens (regex) in text is {}.'.format(len(reg)))
    sample5 = reg[0:10]
    print('Sample tokens (regex):\n{}\n'.format(sample5))
    
    # Mistakes and Problems with white-space tokenizer
    # 1. Words include punctuation characters, such as ',', '.' quotation marks etc.
    # 2. The compound words with hyphen are split apart.
    # 3. We need to handle different types of data such as date (different formats),
    # time, URLs, phone numbers, numbers, etc.

    # Remaining issues with regex-tokenizer:
    # Missing out partial dates e.g. 12 desember (add additional regex '\d{2} (?:january|february|etc..)')
    # We do not account for numbers over 999 999 999 (add additional regex)
    # We don't interpret date ranges such as YYYY-YYYY (add additional regex)




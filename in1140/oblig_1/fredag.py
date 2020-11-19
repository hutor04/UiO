import re
import ezgraphics

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
pattern_hyphoned_word = '\w+-\w+'
pattern_word = '\w+'

# Final pattern, we compile it in advance for multiple reuse and better performance.
PATTERN = re.compile(pattern_date + '|' + pattern_date_2 + '|' + pattern_date_3 + '|' + pattern_time + '|' +
                     pattern_phone_no + '|' + pattern_co2 + '|' + pattern_website_no + '|' + email + '|' +
                     pattern_number + '|' + pattern_web_address + '|' + pattern_hyphoned_word + '|' + pattern_word)


# This the regex tokenizer.
def regex_tokenizer(text, p):
    # It finds all matches for the pattern
    words = p.findall(text)
    # We write the result to file, each token from new string.
    with open(regex_tok_out, 'w') as f_out:
        for word in words:
            f_out.write(word + '\n')
    return words


def word_counter():
    all_words = regex_tokenizer(data_in_str, PATTERN)
    set_words = set(all_words)
    dict_words = {key.lower(): 0 for key in set_words}
    for word in all_words:
        if word.lower() in dict_words:
            dict_words[word.lower()] += 1
    return dict_words


def sort_dict(freq_dict, high_freq_first=True):
    return sorted(freq_dict.items(), key=lambda x: x[1], reverse=high_freq_first)


def give_me_rectangles(sorted_freq_list):
    FROM_TOP = 20
    MAX_HEIGHT = 380
    start_x_pos = 100
    start_y_pos = 10
    rectangles = []
    for i in range(5):
        if i != 0:
            x_pos = start_x_pos + 100
            start_x_pos = x_pos
        else:
            x_pos = start_x_pos
        height = round(sorted_freq_list[i][1] / sorted_freq_list[0][1] * MAX_HEIGHT) - FROM_TOP
        width = 50
        y_pos = start_y_pos+(MAX_HEIGHT-height)
        rectangles.append(list((x_pos, y_pos, width, height)))
    return rectangles





freq_dict = word_counter()
sorted_freq_list = sort_dict(freq_dict)
a = give_me_rectangles(sorted_freq_list)

win = ezgraphics.GraphicsWindow(600, 400)
canv = win.canvas()

print(a)
for i in a:
    canv.drawRect(i[0], i[1], i[2], i[3])
win.wait()

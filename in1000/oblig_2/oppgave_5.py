# Task:
# Create a quiz game program. Name the file of the program oppgave_5.py.
# The program must consume an arbitrary number of quiz questions that will
# be used in the quiz.
# Questions are organized as the dictionary of topics, each topic has a list of
# questions, question and answer pairs are placed in tuples, where the 1st
# item is the question, second is the answer.
# The program should let the players choose the topic and ask them questions from
# the selected topic.
# The players should provide answers via keyboard input. The program stores
# answers in strings, thus it doesn't need to convert the input to numerals.
# The program must handle inconsistent capitalization.
# The program must evaluate the responses of the player and tell if they
# were right or wrong.

# The input data, i.e. questions.
questions = {
'geography':[
('What is the capital of Norway? ', 'oslo'),
('How many continents are there in the world? (integers, please) ', '7'),
('Name the highest waterfall in the world? ', 'angel falls')
],
'math':[
('How many is 2 + 2?  (integers, please) ', '4'),
('Who helps you calculate hypotenuse? ', 'pythagor'),
('How many is 10 // 3? (integers, please) ', '3')
]}


# This function prints out the list of available topics, and asks the players
# to select a topic that they like. If the answer is not a valid topic
# it enters the while loop until it gets the right answer.
def choose_topic(quiz_data):
    print('Hi User! Today we have questions about the following topics:')
    topics = {}
    for i, key in enumerate(questions):
        topics[str(i+1)] = key
        print('{}. {}'.format(i+1, key))
    ready = False
    while not ready:
        choice= input('Type in the number of the topic that you prefer: ')
        if choice in topics:
            ready = True
        else:
            print('Looks like there is no topic with such number or you are '
            'typing in text. Have another try.')
    return topics[choice]


# This function loops through the available questions within the selected topic
# and determines if the player was right or wrong.
def quiz_routine(question_set):
    print('Here come the questions!')
    for question in question_set:
        reply = input(question[0]).lower()
        if reply == question[1]:
            print('You got it!')
        else:
            print('Nope, the right aswer is {}.'.format(question[1].title()))
    print('Thank you for playing with us!')


# Main routine of the program
u_choice = choose_topic(questions)
quiz_routine(questions[u_choice])

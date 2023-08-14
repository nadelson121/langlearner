
def language_learning(level):
    # The dictionary contains the Spanish greeting vocabulary for Level 1.
    # Vocabulary Source: https://www.spanishdict.com/guide/greetings-in-spanish
    level_one_greetings = {
        "Hello.": "Hola.",
        "How are you? (formal singular)": "¿Cómo está?",
        "How are you? (formal plural)": "¿Cómo están?",
        "It’s nice to meet you.": "Mucho gusto.",
        "Likewise.": "Igualmente.",
        "Good morning.": "Buenos días.",
        "Good afternoon.": "Buenas tardes.",
        "Good evening.": "Buenas noches."
    }
    # The dictionary contains the Spanish verbs for Level 1.
    # Vocabulary Source: https://www.spanishdict.com/guide/the-100-most-common-spanish-verbs
    level_one_verbs = {
        "to open": "abrir",
        "to look for": "buscar",
        "to change": "cambiar",
        "to give": "dar",
        "to start": "empezar",
        "to form": "formar",
        "to win": "ganar",
        "to speak/talk": "hablar"
    }
    # The dictionary contains the Spanish nouns for Level 2.
    # Vocabulary Source: https://www.spanishpod101.com/blog/2020/06/29/100-most-common-nouns-in-spanish/
    level_two_nouns = {
        "water": "el agua",
        "bread": "el pan",
        "woman": "la mujer",
        "man": "el hombre",
        "doctor (m.)": "el doctor",
        "teacher (f.)": "la maestra",
        "bathroom": "el baño",
        "bed": "la cama"
    }
    # The dictionary contains the Spanish adjectives for Level 2.
    # Vocabulary Source: https://mydailyspanish.com/common-spanish-adjectives/
    level_two_adjective = {
        "boring": "aburrido",
        "low": "bajo",
        "expensive": "caro",
        "thin": "delgado",
        "excited": "emocionado",
        "easy": "fácil",
        "generous": "generoso",
        "beautiful": "hermoso"
    }
    # The dictionary will be used to hold the missed Spanish translations as the key and the question as the value.
    starred = {}
    if level == '1':
        print("Welcome to Spanish Level 1!")
        print("You will be learning basic greetings and verbs, and then you will be tested on your knowledge!")
        print("First, we will start off with basic greetings!")
        print("~~~~~~~~~~~~~~")
        # The loop will run through every key in the "level_one_greetings" dictionary and print out each English
        # greeting with the Spanish translation.
        for i in level_one_greetings:
            print("The Spanish translation for " + "'" + i + "'" + " is " + "'" + level_one_greetings[i] + "'")
            input("Are you ready to move on? Press the 'enter' key if you are! ")
            print("--------------")
        print()
        print("Great! Now that you know all the words for this category, let's test your knowledge!")
        print("Before we begin, please note two important points:")
        print("1. You need to capitalize first letter of the first word of each greeting translation in Spanish")
        print("2. Make sure to have punctuation for each greeting translation in Spanish")
        print("~~~~~~~~~~~~~~")
        # The loop will run through every key in the "level_one_greetings dictionary and print out the question
        # with the key from the dictionary inserted into the respective location.
        for j in level_one_greetings:
            question = "What is the translation of " + "'" + j + "'" + " in Spanish? "
            answer = input(question)
            # The conditionals determine if the user's answer was correct or incorrect, and prints out the
            # appropriate message.
            if answer == level_one_greetings[j]:
                print("You are correct!")
            else:
                print("Incorrect...the correct answer was " + "'" + level_one_greetings[j] + "'...")
                # If the answer was incorrect, the missed Spanish word and question will be added to the "starred"
                # dictionary, and these keys will be accessed after each word was tested once.
                starred[level_one_greetings[j]] = question
            print("--------------")
        if len(starred) > 0:
            # This loop will continue running until the user answers all the questions correctly (ie. when there are no
            # more words to review).
            while len(starred) > 0:
                correct_on_retry = [] # This list will be used to indicate which words were correct on a retry.
                print("Now we will go back to the questions that you missed!")
                # This loop will run through every key in the "starred" dictionary and ask questions with the Spanish
                # words that the user previously missed.
                for k in starred:
                    answer = input(starred[k])
                    # The conditionals determine if the user's answer was correct or incorrect, and prints out the
                    # appropriate message.
                    if answer == k:
                        print("You are correct!")
                        # If the answer was correct, the word is appended to the "correct_on_retry" list. This is
                        # necessary to eventually remove these keys from the "starred" dictionary.
                        correct_on_retry.append(k)
                    else:
                        print("Incorrect...the correct answer was " + "'" + k + "'...")
                    print("--------------")
                # This loop will run through every index in the "correct_on retry" list, and remove the respective
                # keys from the "starred" dictionary.
                for m in range(0, len(correct_on_retry)):
                    starred.pop(correct_on_retry[m])
        print("~~~~~~~~~~~~~~")
        print("Now you learned all of the basic greetings!")
        print("Let's move on to the verbs!")
        print("~~~~~~~~~~~~~~")
        # The loop will run through every key in the "level_one_verbs" dictionary and print out an English
        # verb with the Spanish translation.
        for i in level_one_verbs:
            print("The Spanish translation for " + "'" + i + "'" + " is " + "'" + level_one_verbs[i] + "'")
            input("Are you ready to move on? Press the 'enter' key if you are! ")
            print("--------------")
        print()
        print("Great! Now that you know all the words for this category, let's test your knowledge!")
        print("Before we begin, please note two important points:")
        print("1. Every letter for every verb translation in Spanish must be lowercase")
        print("2. Each verb translation in Spanish needs to be in the infinitive form")
        print("~~~~~~~~~~~~~~")
        # The loop will run through every key in the "level_one_verbs" dictionary and print out the question
        # with the key from the dictionary inserted into the respective location.
        for j in level_one_verbs:
            question = "What is the translation of " + "'" + j + "'" + " in Spanish? "
            answer = input(question)
            # The conditionals determine if the user's answer was correct or incorrect, and prints out the
            # appropriate message.
            if answer == level_one_verbs[j]:
                print("You are correct!")
            else:
                print("Incorrect...the correct answer was " + "'" + level_one_verbs[j] + "'...")
                # If the answer was incorrect, the missed Spanish word and question will be added to the "starred"
                # dictionary, and these keys will be accessed after each word was tested once.
                starred[level_one_verbs[j]] = question
            print("--------------")
        if len(starred) > 0:
            print("--------------")
            # This loop will continue running until the user answers all the questions correctly (ie. when there are no
            # more words to review).
            while len(starred) > 0:
                correct_on_retry = [] # This list will be used to indicate which words were correct on a retry.
                print("Now we will go back to the questions that you missed!")
                # This loop will run through every key in the "starred" dictionary and ask questions with the words
                # that the user previously missed.
                for k in starred:
                    answer = input(starred[k])
                    # The conditionals determine if the user's answer was correct or incorrect, and prints out the
                    # appropriate message.
                    if answer == k:
                        print("You are correct!")
                        # If the answer was correct, the word is appended to the "correct_on_retry" list. This is
                        # necessary to eventually remove these keys from the "starred" dictionary.
                        correct_on_retry.append(k)
                    else:
                        print("Incorrect...the correct answer was " + "'" + k + "'...")
                    print("--------------")
                # This loop will run through every index in the "correct_on retry" list, and remove the respective
                # keys from the "starred" dictionary.
                for m in range(0, len(correct_on_retry)):
                    starred.pop(correct_on_retry[m])
        print("Congratulations on completing level 1 Spanish!")
        print("If you would like to work on this level again or to try level 2, you can restart the program!")
    if level == '2':
        print("Welcome to Spanish Level 2!")
        print("You will be learning nouns and adjectives, and then you will be tested on your knowledge!")
        print("First, we will start off with nouns!")
        print("~~~~~~~~~~~~~~")
        # The loop will run through every key in the "level_two_nouns" dictionary and print out an English
        # verb with the Spanish translation.
        for i in level_two_nouns:
            print("The Spanish translation for " + "'" + i + "'"+ " is " + "'" + level_two_nouns[i] + "'")
            input("Are you ready to move on? Press the 'enter' key if you are! ")
            print("--------------")
        print()
        print("Great! Now that you know all the words for this category, let's test your knowledge!")
        print("Before we begin, please note two important points:")
        print("1. Each letter for every verb translation in Spanish must be lowercase")
        print("2. There must be an article ('el' or 'la') before each noun translation in Spanish")
        print("~~~~~~~~~~~~~~")
        # The loop will run through every key in the "level_two_nouns" dictionary and print out the question
        # with the key from the dictionary inserted into the respective location.
        for j in level_two_nouns:
            question = "What is the translation of " + "'" + j + "'" + " in Spanish? "
            answer = input(question)
            # The conditionals determine if the user's answer was correct or incorrect, and prints out the
            # appropriate message.
            if answer == level_two_nouns[j]:
                print("You are correct!")
            else:
                print("Incorrect...the correct answer was " + "'" + level_two_nouns[j] + "'...")
                # If the answer was incorrect, the missed Spanish word and question will be added to the "starred"
                # dictionary, and these keys will be accessed after each word was tested once.
                starred[level_two_nouns[j]] = question
            print("--------------")
        if len(starred) > 0:
            # This loop will continue running until the user answers all the questions correctly (ie. when there are no
            # more words to review).
            while len(starred) > 0:
                correct_on_retry = [] # This list will be used to indicate which words were correct on a retry.
                print("Now we will go back to the questions that you missed!")
                # This loop will run through every key in the "starred" dictionary and ask questions with the words
                # that the user previously missed.
                for k in starred:
                    answer = input(starred[k])
                    # The conditionals determine if the user's answer was correct or incorrect, and prints out the
                    # appropriate message.
                    if answer == k:
                        print("You are correct!")
                        # If the answer was correct, the word is appended to the "correct_on_retry" list. This is
                        # necessary to eventually remove these keys from the "starred" dictionary.
                        correct_on_retry.append(k)
                    else:
                        print("Incorrect...the correct answer was " + "'" + k + "'...")
                    print("--------------")
                # This loop will run through every index in the "correct_on retry" list, and remove the respective
                # keys from the "starred" dictionary.
                for m in range(0, len(correct_on_retry)):
                    starred.pop(correct_on_retry[m])
        print("~~~~~~~~~~~~~~")
        print("Now you learned all of the nouns!")
        print("Let's move on to the adjectives!")
        print("~~~~~~~~~~~~~~")
        # The loop will run through every key in the "level_two_adjective" dictionary and print out an English
        # adjective with the Spanish translation.
        for i in level_two_adjective:
            print("The Spanish translation for " + "'" + i + "'" + " is " + "'" + level_two_adjective[i] + "'")
            input("Are you ready to move on? Press the 'enter' key if you are! ")
            print("--------------")
        print()
        print("Great! Now that you know all the words for this category, let's test your knowledge!")
        print("Before we begin, please note that each letter for every adjective translation in Spanish must be ")
        print("lowercase")
        print("~~~~~~~~~~~~~~")
        # The loop will run through every key in the "level_two_adjective" dictionary and print out the question
        # with the key from the dictionary inserted into the respective location.
        for j in level_two_adjective:
            question = "What is the translation of " + "'" + j + "'" + " in Spanish? "
            answer = input(question)
            # The conditionals determine if the user's answer was correct or incorrect, and prints out the
            # appropriate message.
            if answer == level_two_adjective[j]:
                print("You are correct!")
            else:
                print("Incorrect...the correct answer was " + "'" + level_two_adjective[j] + "'...")
                # If the answer was incorrect, the missed Spanish word and question will be added to the "starred"
                # dictionary, and these keys will be accessed after each word was tested once.
                starred[level_two_adjective[j]] = question
            print("--------------")
        if len(starred) > 0:
            print("--------------")
            # This loop will continue running until the user answers all the questions correctly (ie. when there are no
            # more words to review).
            while len(starred) > 0:
                correct_on_retry = [] # This list will be used to indicate which words were correct on a retry.
                print("Now we will go back to the questions that you missed!")
                # This loop will run through every key in the "starred" dictionary and ask questions with the words
                # that the user previously missed.
                for k in starred:
                    answer = input(starred[k])
                    # The conditionals determine if the user's answer was correct or incorrect, and prints out the
                    # appropriate message.
                    if answer == k:
                        print("You are correct!")
                        # If the answer was correct, the word is appended to the "correct_on_retry" list. This is
                        # necessary to eventually remove these keys from the "starred" dictionary.
                        correct_on_retry.append(k)
                    else:
                        print("Incorrect...the correct answer was " + "'" + k + "'...")
                    print("--------------")
                # This loop will run through every index in the "correct_on retry" list, and remove the respective
                # keys from the "starred" dictionary.
                for m in range(0, len(correct_on_retry)):
                    starred.pop(correct_on_retry[m])
        print("Congratulations on completing level 2 Spanish!")
        print("If you would like to work on this level again or to try level 1, you can restart the program!")

print("Hello user,")
print("Welcome to SpanStarter, where you can start your journey in learning Spanish!")
print()
print("The Spanish learning path consists of two levels")
print("- Level 1: Greetings and Basic Verbs (type '1')")
print("- Level 2: Nouns and Adjectives (type '2')")
level = input("Which level would you like to try? ")
print("~~~~~~~~~~~~")
while level != '1' and level != '2':
    print("I'm sorry, but", level, "is not a level choice for this application!")
    level = input("Which level would you like to try? ")
language_learning(level)





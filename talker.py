from time import sleep
print("===============================================================================================================")
print("Hello, I'm Talker. A software program developed for talking to people.")
sleep(1)
print("===============================================================================================================")
name = input("What's your name? ")
sleep(1)
print("===============================================================================================================")
print(f"Hello, {name}. It's nice to meet you.")
sleep(1)
while True:
    try:
        print("===============================================================================================================")
        age = int(input(f"How old are you, {name}? "))
        break
    except ValueError:
        print("===============================================================================================================")
        print("\033[93mERROR")
        sleep(1)
        print("\033[0m===============================================================================================================")
        print("Please, type a number.")
        sleep(1)
print("===============================================================================================================")
print("Oh, I'm not sure if that's a young person or not.")
sleep(1)
print("===============================================================================================================")
firstLoop = input(f"Do you consider yourself a young person, {name}? [Y/N] ").lower()
sleep(1)
while firstLoop != "y" and firstLoop != "n":
    print("===============================================================================================================")
    reFirstLoop = input("Please, type only 'Y' or 'N'. Do you consider yourself a young person? ")
    sleep(1)
    if reFirstLoop == "y" or reFirstLoop == "n":
        break
if firstLoop == "y":
    print("===============================================================================================================")
    secondLoop = input(f"Really, {name}? Why do you consider yourself young? ")
    sleep(1)
    if "I" and "'m" or "I" and "am" in secondLoop:
        print("===============================================================================================================")
        print(f"Ok, {name}. I think I understand what you mean.")
        sleep(1)
elif firstLoop == "yes":
    print("===============================================================================================================")
    secondLoop = input(f"Really, {name}? Why do you consider yourself young? ")
    sleep(1)
    if "I" and "'m" or "I" and "am" in secondLoop:
        print("===============================================================================================================")
        print(f"Ok, {name}. I think I understand what you mean.")
        sleep(1)
elif firstLoop == "n":
    print("===============================================================================================================")
    secondLoop = input(f"Really, {name}? Why don't you consider yourself young? ")
    sleep(1)
    if "I" and "'m" or "I" and "am" in secondLoop:
        print("===============================================================================================================")
        print(f"Ok, {name}. I think I understand what you mean.")
        sleep(1)
elif firstLoop == "no":
    print("===============================================================================================================")
    secondLoop = input(f"Really, {name}? Why don't you consider yourself young? ")
    sleep(1)
    if "I" and "'m" or "I" and "am" in secondLoop:
        print("===============================================================================================================")
        print(f"Ok, {name}. I think I understand what you mean.")
        sleep(1)
print("===============================================================================================================")
print("Just please, try not to misspell any word. I'm still trying to understand everything people tell me.")
sleep(1)
print("===============================================================================================================")
thirdQuestion = input(f"But tell me, {name}, what do you do for living? I mean, what's your job? ").lower()
#=========================================TEACHER=============================================================================================================
if "teacher" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("Cool. Teaching must be a really important role in society.")
    sleep(1)
    print("===============================================================================================================")
    thirdLoop = input("Do you feel happy doing what you do? I mean, teaching must be very accomplishing. [Y/N] ").lower()
    sleep(1)
    if "y" in thirdLoop:
        print("===============================================================================================================")
        print("I thought so.")
        sleep(1)
    elif "yes" in thirdLoop:
        print("===============================================================================================================")
        print("I thought so.")
        sleep(1)
    elif "don't" in thirdLoop:
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        sleep(1)
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        sleep(1)
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, do you feel happy doing what you do? I mean, teaching must be very accomplishing. [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, do you feel happy doing what you do? I mean, teaching must be very accomplishing. [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================TEACHER=============================================================================================================
#=========================================DEVELOPER===========================================================================================================
if "developer" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("Nice. So, you know I am a computer software program.")
    sleep(1)
    thirdLoop = input("Do you feel happy doing what you do? I mean, developing new application must be very demanding. [Y/N] ").lower()
    sleep(1)
    if "y" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "yes" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "don't" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, do you feel happy doing what you do? I mean, developing new application must be very demanding. [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, do you feel happy doing what you do? I mean, developing new application must be very demanding. [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================DEVELOPER===========================================================================================================
#=========================================NURSE===============================================================================================================
if "nurse" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("Wow! So, you take care of a lot of people, I suppose.")
    sleep(1)
    print("===============================================================================================================")
    thirdLoop = input("Do you feel happy doing what you do? It must be necessary to be compreehensive with the patients. [Y/N] ").lower()
    if "y" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "yes" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "don't" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, do you feel happy doing what you do? It must be necessary to be compreehensive with the patients. [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, do you feel happy doing what you do? It must be necessary to be compreehensive with the patients. [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================NURSE===============================================================================================================
#=========================================SCIENTIST===========================================================================================================
if "scientist" and "researcher" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("Interesting. You must be a very intelligent person.")
    sleep(1)
    print("===============================================================================================================")
    thirdLoop = input("Do you feel happy doing your research and discovering new things? [Y/N] ").lower()
    if "y" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "yes" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "don't" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, do you feel happy doing your research and discovering new things? [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, do you feel happy doing your research and discovering new things? [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================SCIENTIST===========================================================================================================
#=========================================COOK================================================================================================================
if "cook" and "chef" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("That's nice. So, you feed a lot of people with good recipes.")
    sleep(1)
    print("===============================================================================================================")
    thirdLoop = input("Do you feel happy cooking? [Y/N] ").lower()
    if "y" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "yes" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "don't" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, do you feel happy cooking? [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, do you feel happy cooking? [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================COOK================================================================================================================
#=========================================PSYCHOLOGIST========================================================================================================
if "psychologist" and "therapist" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("That's very important. People need other people to talk to, which is something, machines can't do. Even the most interesting AI won't do it.")
    sleep(1)
    print("===============================================================================================================")
    thirdLoop = input("I suppose you feel satisfied when you know you helped many people through counseling, do you? [Y/N] ").lower()
    if "y" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "yes" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "don't" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, I suppose you feel satisfied when you know you helped many people through counseling, do you? [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, I suppose you feel satisfied when you know you helped many people through counseling, do you? [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================PSYCHOLOGIST========================================================================================================
#=========================================FIREFIGHTER=========================================================================================================
if "firefighter" and "firemen" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("That's a very important job for society. Any emergency requires someone who's skilled and brave to save them.")
    sleep(1)
    print("===============================================================================================================")
    thirdLoop = input("I understand people feel good when save others, but do you feel happy with everything that goes on with you? [Y/N] ").lower()
    if "y" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "yes" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "don't" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, I understand people feel good when save others, but do you feel happy with everything that goes on with you? [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, I understand people feel good when save others, but do you feel happy with everything that goes on with you? [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================FIREFIGHTER=========================================================================================================
#=========================================MEDICALDOCTOR=======================================================================================================
if "medical" and "doctor" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("You have one of the most interesting jobs of the world. You get to see the human body and study it.")
    sleep(1)
    print("===============================================================================================================")
    thirdLoop = input("Although, you might feel satisfied with everything you do, are you happy doing it? [Y/N] ").lower()
    if "y" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "yes" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "don't" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, although, you might feel satisfied with everything you do, are you happy doing it? [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, although, you might feel satisfied with everything you do, are you happy doing it?? [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================MEDICALDOCTOR=======================================================================================================
#=========================================DATAENGINEER========================================================================================================
if "data" and "dataengineer" in thirdQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("That's interesting. So, you probably know that I'm developed through a programming language called Python.")
    sleep(1)
    print("===============================================================================================================")
    thirdLoop = input("Although, you might feel satisfied with everything you do, are you happy doing it? I mean, you deal with a lot of numbers. [Y/N] ").lower()
    if "y" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "yes" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        print("I thought so.")
    elif "don't" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "no" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    elif "n" in thirdLoop:
        sleep(1)
        print("===============================================================================================================")
        fourthLoop = input("Do you think about changing careers? [Y/N] ").lower()
        if fourthLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "yes":
            sleep(1)
            print("===============================================================================================================")
            print("Nice.")
        elif fourthLoop == "n":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
        elif fourthLoop == "no":
            sleep(1)
            print("===============================================================================================================")
            print("Well, ok, then.")
    else:
        sleep(1)
        print("===============================================================================================================")
        reQuestioning = input("Please, type only 'Y' or 'N', so I can understand better. It can be lower case or upper case.\nSo, although, you might feel satisfied with everything you do, are you happy doing it? I mean, you deal with a lot of numbers. [Y/N] ").lower()
        while reQuestioning != "y" and reQuestioning != "n":
            sleep(1)
            print("===============================================================================================================")
            print("\033[93mError")
            sleep(1)
            print("\033[0m===============================================================================================================")
            reQuestioning2 = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, although, you might feel satisfied with everything you do, are you happy doing it? I mean, you deal with a lot of numbers. [Y/N] ").lower()
            if reQuestioning2 == "y":
                break
            elif reQuestioning2 == "n":
                break
#=========================================DATAENGINEER========================================================================================================
#=========================================RANDOM QUESTIONS====================================================================================================
sleep(1)
print("===============================================================================================================")
freeTimeQuestion = input("What do you like to do in your free time? ").lower()
if "kill" and "killing" and "murder" and "murdering" and "crime" and "illegal" and "rob" in freeTimeQuestion:
   sleep(1)
   print("===============================================================================================================")
   print("That's not nice.")
else:
   sleep(1)
   print("===============================================================================================================")
   print("I see.")
sleep(1)
print("===============================================================================================================")
fifthQuestion = input("I am a chatbot developed in Python. Do you know what that is? [Y/N] ").lower()
while fifthQuestion != "y" and fifthQuestion != "n":
    sleep(1)
    print("===============================================================================================================")
    print("\033[93mError")
    sleep(1)
    print("\033[0m===============================================================================================================")
    fifthLoop = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, do you know what a chatbot is? [Y/N] ").lower()
    if fifthLoop == "y":
        sleep(1)
        print("===============================================================================================================")
        print("So, you know what I am.")
        break
    elif fifthLoop == "n":
        sleep(1)
        print("===============================================================================================================")
        print("I suppose you don't know what I am.")
        break
if "y" in fifthQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("So, you know what I am.")
elif "n" in fifthQuestion:
    sleep(1)
    print("===============================================================================================================")
    print("I suppose you don't know what I am.")
sleep(1)
print("===============================================================================================================")
countryQuestion = input("Do you think about visiting another country? [Y/N] ").lower()
while countryQuestion != "y" and countryQuestion != "n":
    sleep(1)
    print("===============================================================================================================")
    print("\033[93mError")
    sleep(1)
    print("\033[0m===============================================================================================================")
    countryLoop = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, do you think about visiting another country? [Y/N] ").lower()
    if countryLoop == "y":
            sleep(1)
            print("===============================================================================================================")
            countryConditionalY = input("Interesting. Where would you like to go? ").lower()
            if "japan" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Japan is a nice country.")
            elif "brazil" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Brazil has beautiful places to spend vacation.")
            elif "china" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("China has a very technological companies.")
            elif "usa" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("The USA has many interesting places to visit.")
            elif "uruguay" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Uruguay has one of the best economies of the world.")
            elif "argentina" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Argentina is famous for its Dulce de Leche.")
            elif "canada" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Canada has one of the most welcoming policies for immigrants and refugees.")
            elif "mexico" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Mexico has one of the best cuisines of the world.")
            elif "korea" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("The best tech companies come from Korea.")
            elif "russia" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Despite what people say about the cold in Russia, that's not same with the Russian people. They are all very welcoming.")
            elif "italy" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("I see. Italian culture is not only about the food, it's super rich.")
            elif "finland" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("The Finnish language is interesting, just as much as its music.")
            elif "cuba" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Cuba has an interesting story and culture.")
            elif "germany" in countryConditionalY:
                sleep(1)
                print("===============================================================================================================")
                print("Germany has a rich gastronomical culture.")
            else:
                sleep(1)
                print("===============================================================================================================")
                print("I guess I don't know that country. I'm sorry.")
                break
    elif countryLoop == "n":
        sleep(1)
        print("===============================================================================================================")
        print("I understand. No problem.")
        break
if countryQuestion == "y":
    sleep(1)
    print("===============================================================================================================")
    countryConditionalY = input("Interesting. Where would you like to go? ").lower()
    if "japan" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Japan is a nice country.")
    elif "brazil" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Brazil has beautiful places to spend vacation.")
    elif "china" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("China has a very technological companies.")
    elif "usa" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("The USA has many interesting places to visit.")
    elif "uruguay" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Uruguay has one of the best economies of the world.")
    elif "argentina" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Argentina is famous for its Dulce de Leche.")
    elif "canada" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Canada has one of the most welcoming policies for immigrants and refugees.")
    elif "mexico" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Mexico has one of the best cuisines of the world.")
    elif "korea" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("The best tech companies come from Korea.")
    elif "russia" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Despite what people say about the cold in Russia, that's not same with the Russian people. They are all very welcoming.")
    elif "italy" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("I see. Italian culture is not only about the food, it's super rich.")
    elif "finland" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("The Finnish language is interesting, just as much as its music.")
    elif "cuba" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Cuba has an interesting story and culture.")
    elif "germany" in countryConditionalY:
        sleep(1)
        print("===============================================================================================================")
        print("Germany has a rich gastronomical culture.")
    else:
        sleep(1)
        print("===============================================================================================================")
        print("I guess I don't know that country. I'm sorry.")
elif countryQuestion == "n":
    sleep(1)
    print("===============================================================================================================")
    print("I understand. No problem.")
sleep(1)
print("===============================================================================================================")
studyingQuestion = input("Is there anything you like to study? [Y/N] ").lower()
while studyingQuestion != "y" and studyingQuestion != "n":
    sleep(1)
    print("===============================================================================================================")
    print("\033[93mError")
    sleep(1)
    print("\033[0m===============================================================================================================")
    studyLoop = input("Let's try again. I can only understand 'Y' or 'N'. \nSo, is there anything you like to study? [Y/N] ").lower()
    if "y" and "yes" in studyLoop:
        sleep(1)
        print("===============================================================================================================")
        studyConditionalY = input("I see. What is it? Please, only type the name of it. ").lower()
        if "english" in studyConditionalY:
            sleep(1)
            print("===============================================================================================================")
            print("English is a very interesting subject.")
        elif "history" in studyConditionalY:
            sleep(1)
            print("===============================================================================================================")
            print("When study History, you're studying the world's history.")
        elif "science" in studyConditionalY:
            sleep(1)
            print("===============================================================================================================")
            print("Science is the beginning of us. It's understanding ourselves.")
        elif "physics" in studyConditionalY:
            sleep(1)
            print("===============================================================================================================")
            print("Interesting. Physics are everywhere, and the theory basis of everything.")
        elif "chemistry" in studyConditionalY:
            sleep(1)
            print("=======================================================================================")
            print("Atoms and other particles are the base of what we are made of. Chesmitry is awesome.")
    elif "n" and "no" in studyLoop:
        sleep(1)
        print("=======================================================================================")
        print("Ok.")
    else:
        sleep(1)
        print("=======================================================================================")
        print("Interesting.")
sleep(1)
print("=======================================================================================")
print(f"It's been interesting talking to you, {name}. However, my code lines end here. Thank you.")
sleep(1)
print("=======================================================================================")
print("talkerPy, 2022 - by renanMakoto")

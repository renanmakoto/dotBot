from time import sleep

def print_separator():
    print("=" * 94)

def ask_yes_no_question(question):
    while True:
        print_separator()
        answer = input(question + " [Y/N] ").lower()
        sleep(1)
        if answer in ['y', 'n']:
            return answer
        else:
            print_separator()
            print("\033[93mERROR\033[0m")
            sleep(1)
            print_separator()
            print("Please, type only 'Y' or 'N'.")

def ask_for_number(question):
    while True:
        print_separator()
        try:
            return int(input(question))
        except ValueError:
            print_separator()
            print("\033[93mERROR\033[0m")
            sleep(1)
            print_separator()
            print("Please, type a number.")
            sleep(1)

def ask_for_string(question):
    print_separator()
    return input(question).lower()

def ask_for_string_with_choices(question, choices):
    while True:
        answer = ask_for_string(question)
        if answer in choices:
            return answer
        print_separator()
        print("\033[93mERROR\033[0m")
        sleep(1)
        print_separator()
        print(f"Please, type one of the following: {', '.join(choices)}.")

def process_job_related_questions(name, job):
    satisfaction = ask_yes_no_question(f"Do you feel happy doing what you do, {job}?")
    if satisfaction == 'y':
        print_separator()
        print("I thought so.")
        sleep(1)
    else:
        career_change = ask_yes_no_question("Do you think about changing careers?")
        if career_change == 'y':
            print_separator()
            print("Nice.")
            sleep(1)
        else:
            print_separator()
            print("Well, ok, then.")
            sleep(1)

def main():
    print_separator()
    print("Hello, I'm Talker. A software program developed for talking to people.")
    sleep(1)
    print_separator()
    name = ask_for_string("What's your name? ")
    sleep(1)
    print_separator()
    print(f"Hello, {name}. It's nice to meet you.")
    sleep(1)
    
    age = ask_for_number(f"How old are you, {name}? ")
    sleep(1)
    print_separator()
    print("Oh, I'm not sure if that's a young person or not.")
    sleep(1)

    is_young = ask_yes_no_question(f"Do you consider yourself a young person, {name}?")
    if is_young == 'y':
        reason = ask_for_string(f"Really, {name}? Why do you consider yourself young? ")
    else:
        reason = ask_for_string(f"Really, {name}? Why don't you consider yourself young? ")
    
    print_separator()
    print(f"Ok, {name}. I think I understand what you mean.")
    sleep(1)
    print_separator()
    print("Just please, try not to misspell any word. I'm still trying to understand everything people tell me.")
    sleep(1)

    job = ask_for_string("What do you do for living? I mean, what's your job? ")
    process_job_related_questions(name, job)
    
    print_separator()
    free_time = ask_for_string("What do you like to do in your free time? ")
    if any(word in free_time for word in ["kill", "killing", "murder", "murdering", "crime", "illegal", "rob"]):
        print_separator()
        print("That's not nice.")
    else:
        print_separator()
        print("I see.")
    sleep(1)
    
    knows_chatbot = ask_yes_no_question("I am a chatbot developed in Python. Do you know what that is?")
    if knows_chatbot == 'y':
        print_separator()
        print("So, you know what I am.")
    else:
        print_separator()
        print("I suppose you don't know what I am.")
    sleep(1)
    
    wants_to_travel = ask_yes_no_question("Do you think about visiting another country?")
    if wants_to_travel == 'y':
        country = ask_for_string_with_choices("Interesting. Where would you like to go?", [
            "japan", "brazil", "china", "usa", "uruguay", "argentina", 
            "canada", "mexico", "korea", "russia", "italy", "finland", "cuba", "germany"
        ])
        country_responses = {
            "japan": "Japan is a nice country.",
            "brazil": "Brazil has beautiful places to spend vacation.",
            "china": "China has very technological companies.",
            "usa": "The USA has many interesting places to visit.",
            "uruguay": "Uruguay has one of the best economies of the world.",
            "argentina": "Argentina is famous for its Dulce de Leche.",
            "canada": "Canada has one of the most welcoming policies for immigrants and refugees.",
            "mexico": "Mexico has one of the best cuisines of the world.",
            "korea": "The best tech companies come from Korea.",
            "russia": "Despite what people say about the cold in Russia, that's not the same with the Russian people. They are all very welcoming.",
            "italy": "I see. Italian culture is not only about the food, it's super rich.",
            "finland": "The Finnish language is interesting, just as much as its music.",
            "cuba": "Cuba has an interesting story and culture.",
            "germany": "Germany has a rich gastronomical culture."
        }
        print_separator()
        print(country_responses.get(country, "I guess I don't know that country. I'm sorry."))
    else:
        print_separator()
        print("I understand. No problem.")
    sleep(1)

    likes_study = ask_yes_no_question("Is there anything you like to study?")
    if likes_study == 'y':
        subject = ask_for_string_with_choices("I see. What is it? Please, only type the name of it.", [
            "english", "history", "science", "physics", "chemistry"
        ])
        study_responses = {
            "english": "English is a very interesting subject.",
            "history": "When studying History, you're studying the world's history.",
            "science": "Science is the beginning of us. It's understanding ourselves.",
            "physics": "Interesting. Physics are everywhere, and the theoretical basis of everything.",
            "chemistry": "Atoms and other particles are the base of what we are made of. Chemistry is awesome."
        }
        print_separator()
        print(study_responses.get(subject, "Interesting."))
    else:
        print_separator()
        print("Ok.")
    sleep(1)

    print_separator()
    print(f"It's been interesting talking to you, {name}. However, my code lines end here. Thank you.")
    sleep(1)
    print_separator()
    print("talkerPy, 2022 - by renanMakoto")

if __name__ == "__main__":
    main()

from nltk.chat.util import Chat, reflections
import operator
import indicoio

indicoio.config.api_key = 'e7541bae2f7fe8e37e4e142d47323add'

gPats = [
    [r"(.*) fine (.*)",
     "That is good"
     ],
    [r"i need (.*)",
     ["Why do you need %1?",
      "Would it really help you to get %1?",
      "Are you sure you need %1?"]],

    [r"Why don't you (.*)",
     ["Do you really think I don't %1?",
      "Perhaps eventually I will %1.",
      "Do you really want me to %1?"]],

    [r"Why can't i (.*)",
     ["Do you think you should be able to %1?",
      "If you could %1, what would you do?",
      "I don't know -- why can't you %1?",
      "Have you really tried?"]],

    [r"I can't (.*)",
     ["How do you know you can't %1?",
      "Perhaps you could %1 if you tried.",
      "What would it take for you to %1?"]],

    [r"I am (.*)",
     ["Did you come to me because you are %1?",
      "How long have you been %1?",
      "How do you feel about being %1?"]],

    [r"I'm (.*)",
     ["How does being %1 make you feel?",
      "Do you enjoy being %1?",
      "Why do you tell me you're %1?",
      "Why do you think you're %1?"]],

    [r"Are you (.*)",
     ["Why does it matter whether I am %1?",
      "Would you prefer it if I were not %1?",
      "Perhaps you believe I am %1.",
      "I may be %1 -- what do you think?"]],

    [r"What (.*)",
     ["Why do you ask?",
      "How would an answer to that help you?",
      "What do you think?"]],

    [r"How (.*)",
     ["How do you suppose?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?"]],

    [r"Because (.*)",
     ["Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If %1, what else must be true?"]],

    [r"(.*) sorry (.*)",
     ["There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],

    [r"Hello(.*)",
     ["Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?"]],

    [r"i think (.*)",
     ["Do you doubt %1?",
      "Do you really think so?",
      "But you're not sure %1?"]],

    [r"(.*) friend(.*)",
     ["Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],

    [r"Yes",
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?"]],

    [r"(.*) computer (.*)",
     ["Are you really talking about me?",
      "Does it seem strange to talk to a computer?",
      "How do computers make you feel?",
      "Do you feel threatened by computers?"]],

    [r"Is it (.*)",
     ["Do you think it is %1?",
      "Perhaps it's %1 -- what do you think?",
      "If it were %1, what would you do?",
      "It could well be that %1."]],

    [r"It is (.*)",
     ["You seem very certain.",
      "If I told you that it probably isn't %1, what would you feel?"]],

    [r"can you (.*)",
     ["What makes you think I can't %1?",
      "If I could %1, then what?",
      "Why do you ask if I can %1?"]],

    [r"Can I (.*)",
     ["Perhaps you don't want to %1.",
      "Do you want to be able to %1?",
      "If you could %1, would you?"]],

    [r"you are (.*)",
     ["Why do you think I am %1?",
      "Does it please you to think that I'm %1?",
      "Perhaps you would like me to be %1.",
      "Perhaps you're really talking about yourself?"]],

    [r"You're (.*)",
     ["Why do you say I am %1?",
      "Why do you think I am %1?",
      "Are we talking about you, or me?"]],

    [r"I don't (.*)",
     ["Don't you really %1?",
      "Why don't you %1?",
      "Do you want to %1?"]],

    [r"I feel (.*)",
     ["Good, tell me more about these feelings.",
      "Do you often feel %1?",
      "When do you usually feel %1?",
      "When you feel %1, what do you do?"]],

    [r"I have (.*)",
     ["Why do you tell me that you've %1?",
      "Have you really %1?",
      "Now that you have %1, what will you do next?"]],

    [r"I would (.*)",
     ["Could you explain why you would %1?",
      "Why would you %1?",
      "Who else knows that you would %1?"]],

    [r"Is there (.*)",
     ["Do you think there is %1?",
      "It's likely that there is %1.",
      "Would you like there to be %1?"]],

    [r"My (.*)",
     ["I see, your %1.",
      "Why do you say that your %1?",
      "When your %1, how do you feel?"]],

    ["You (.*)",
     ["We should be discussing you, not me.",
      "Why do you say that about me?",
      "Why do you care whether I %1?"]],

    ["Why (.*)",
     ["Why don't you tell me the reason why %1?",
      "Why do you think %1?"]],

    ["I want (.*)",
     ["What would it mean to you if you got %1?",
      "Why do you want %1?",
      "What would you do if you got %1?",
      "If you got %1, then what would you do?"]],

    [r"(.*) mother(.*)",
     ["Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does this relate to your feelings today?",
      "Good family relations are important."]],

    [r"(.*) father (.*)",
     ["Tell me more about your father.",
      "How did your father make you feel?",
      "How do you feel about your father?",
      "Does your relationship with your father relate to your feelings today?",
      "Do you have trouble showing affection with your family?"]],

    [r"(.*) child(.*)",
     ["Did you have close friends as a child?",
      "What is your favorite childhood memory?",
      "Do you remember any dreams or nightmares from childhood?",
      "Did the other children sometimes tease you?",
      "How do you think your childhood experiences relate to your feelings today?"]],

    [r"(.*)?",
     ["Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?"]],

    ["quit",
     ["Thank you for talking with me.",
      "Good-bye.",
      "Thank you, that will be $150.  Have a good day!"]],

    [r"(.*)",
     ["Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that %1?",
      "I see.",
      "Very interesting.",
      "%1.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"]]
]


def form():
    print("Kindly fill in the form before proceeding for Therapy")
    name = input("Name: ")
    age = input("Age: ")
    rel_status = input("Relationship Status: ")
    occupation = input("Occupation: ")
    return name, age, rel_status, occupation


def get_keywords(x):
    #Algorithms for breaking down the responses into keywords
    breakdown = []
    word = ""
    for i in x:
        print(i)
        for y in range(0, len(i)):
            if i[y] == " " and y != len(i):
                breakdown.append(word)
                word = ""
            else:
                if i[y] != " " and y == len(i) - 1:
                    word += i[y]
                    breakdown.append(word)
                    word = ""
                else:
                    word += i[y]

    return breakdown


def Treatment():
    pass


def Recommendation(e):
    if(e == 'joy'):
        return print("""
        Find Below some tips to Increasing your Joy Levels

        1.Find joy in the little things. ...
        2.Start each day with a smile. ...
        3.Connect with others. ...
        4.Do what you're most passionate about. ...
        5.Reflect on your blessings and be grateful. ...
        6.Choose to be positive and see the best in every situation. ...
        7.Take steps to enrich your life. ...
        8.Create goals and plans to achieve what you want most...

        Read more about this on https://psychcentral.com/lib/15-ways-to-increase-your-happiness/
        """)

    elif(e == 'anger'):
        return print("""
        Find Below some tips to Managing your Anger

        1.Think before you speak. ...
        2.Once you're calm, express your anger. ...
        3.Get some exercise. ...
        4.Take a timeout. ...
        5.Identify possible solutions. ...
        6.Stick with 'I' statements. ...
        7.Don't hold a grudge. ...
        8.Use humor to release tension.

        Read more about this on https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/anger-management/art-20045434
        """)

    elif(e == 'sadness'): # high sadness levels pass as Depression
        return print("""
        Here are some ways to experience normal sadness in healthy ways and to allow this emotion to enrich your life:

        1. Exercise
        2. Social Support
        3. Nutrition
        4. Sleep
        5. Stress Reduction

        Read more about this on https://www.helpguide.org/articles/depression/depression-treatment.htm
        """)

    elif(e == 'fear'):
        return print("""
        1.Stress management: Limit potential triggers by managing stress levels. Keep an eye on pressures and deadlines,
         organize daunting tasks in to-do lists, and take enough time off from professional or educational obligations.
        2.Relaxation techniques: Certain measures can help reduce signs of anxiety, including deep-breathing exercises,
        long baths, meditation, yoga, and resting in the dark.
        3.Exercises to replace negative thoughts with positive ones: Write down a list of any negative thoughts,
         and make another list of positive thoughts to replace them. Picturing yourself successfully facing and
        conquering a specific fear can also provide benefits
        4.Support network: Talk to a person who is supportive, such as a family member or friend.
         Avoid storing up and suppressing anxious feelings as this can worsen anxiety disorders
        5.Exercise: Physical exertion and an active lifestyle can improve self-image
        and trigger the release of chemicals in the brain that stimulate positive emotions.

        """)


def Detect_Emotion(e):
    Emotions = indicoio.emotion(e)
    detected_emotion = max(Emotions.items(),key=operator.itemgetter(1))[0]
    Recommendation(detected_emotion)



def Therabot():
    print("------------------------------- AI Therapist System (THERABOT) -------------------------------")
    patient_form = form()
    if(int(patient_form[1]) < 18):
        print("We require consent from your Parents to proceed")
    else:
        print()
        print("--------------------- End of Form, Please Proceed to Therapy ----------------------")
        print()
        print("Talk to Therabot by typing in plain English,")
        print('and lower-case letters and punctuation.  Enter "quit" when done.')
        print('=' * 78)
        print("Hi", patient_form[0], ", how are you feeling today?")
        chat = Chat(gPats, reflections, patient_form)
        chat.converse()
        x = chat.get_chat_list()
        # print(x)
        clean_statement = ' '.join(x)
        Detect_Emotion(clean_statement)

if __name__ == "__main__":
    Therabot()


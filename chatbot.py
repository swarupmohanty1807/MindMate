import random
import nltk

# EMOTION RESPONSES
responses = {

    "sad": [
        "I understand that you are feeling sad. Difficult moments are temporary and you are not alone.",
        "Sometimes sadness becomes overwhelming, but talking about it can help.",
        "Take things slowly. Your mental well-being matters."
    ],

    "stress": [
        "College stress can become exhausting. Try taking short breaks and resting your mind.",
        "Remember that perfection is not necessary. Progress matters more.",
        "Deep breathing and proper sleep may help reduce stress."
    ],

    "anxiety": [
        "Anxiety can feel difficult, but you are stronger than your fears.",
        "Try grounding yourself by focusing on your breathing.",
        "Taking things one step at a time may help reduce anxious thoughts."
    ],

    "alone": [
        "You are not alone. Your feelings matter and support is always available.",
        "Sometimes loneliness feels heavy, but meaningful connections can help.",
        "Nova is always here to listen to you."
    ],

    "happy": [
        "That is wonderful to hear! Positive moments are important.",
        "I am glad that you are feeling happy today.",
        "Keep taking care of yourself and enjoying these moments."
    ],

    "angry": [
        "Take a slow deep breath and give yourself a moment to relax.",
        "Anger is natural, but calming your mind may help you think clearly.",
        "Try listening to music or taking a short walk."
    ],

    "exam": [
        "Exams can create pressure, but one exam does not define your future.",
        "Take proper breaks while studying and avoid overworking yourself.",
        "You are capable of handling this challenge."
    ],

    "tired": [
        "Mental exhaustion is real. Proper rest is important.",
        "Try drinking water, resting, and relaxing your mind.",
        "You may need some sleep and self-care."
    ]
}

# GENERAL RESPONSES
general_responses = [

    "I understand. Can you tell me more about how you are feeling?",

    "Your feelings are important. I am listening carefully.",

    "Thank you for sharing your thoughts with me.",

    "Sometimes expressing emotions helps reduce emotional pressure.",

    "I am here to support you. Please continue sharing.",

    "That sounds emotionally difficult. Tell me more."
]

# MAIN FUNCTION
def get_response(message, username):

    message = message.lower()

    # GREETING FEATURE
    greetings = [
        "hi",
        "hello",
        "hey",
        "hi mindmate",
        "hello mindmate",
        "hey mindmate"
        "hi mind mate",
        "hello mind mate",
        "hey mind mate",

        "hi mind-mate",
        "hello mind-mate",
        "hey mind-mate"
    ]

    if message in greetings:

        return f"Hello {username}. How are you ? What can i do for you ?"

    words = message.split()

    detected_emotions = []

    emotion_keywords = {

    "sad": [
        "sad", "cry", "crying",
        "depressed", "upset",
        "heartbroken", "broken"
    ],

    "stress": [
        "stress", "stressed",
        "pressure", "burden"
    ],

    "anxiety": [
        "anxiety", "anxious",
        "panic", "fear",
        "worried", "overthinking"
    ],

    "alone": [
        "alone", "lonely",
        "isolated", "ignored"
    ],

    "happy": [
        "happy", "good",
        "great", "awesome",
        "excited", "joy"
    ],

    "angry": [
        "angry", "mad",
        "furious", "annoyed"
    ],

    "exam": [
        "exam", "test",
        "study", "college"
    ],

    "tired": [
        "tired", "sleepy",
        "exhausted", "weak"
    ] }


    for emotion, keywords in emotion_keywords.items():

        for keyword in keywords:

            if keyword in message:

                detected_emotions.append(emotion)
            break
    # MULTIPLE EMOTION DETECTION
    if detected_emotions:

        selected = random.choice(detected_emotions)

        return random.choice(responses[selected])
    else:

        if len(words) > 10:

            return (
            f"I understand {username}. "
            "This situation may feel emotionally challenging for you. "
            "Remember that managing mental health step-by-step is important."
        )

    return random.choice(general_responses)
init 5 python:
    import random

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="how_are_you_monika",
            category=["Check In"],
            prompt="How Are You Doing?",
            pool=True,
            unlocked=True
        )
    )

init python:
    # Safe affection getter
    def get_monika_affection():
        try:
            return mas_getAffectionLevel()
        except Exception:
            return 0  # Normal if something breaks

label how_are_you_monika:

    $ aff = get_monika_affection()

    # -------------------------
    # Affection-based responses
    # -------------------------
    if mas_isMoniLove():
        $ responses = [
            "I'm feeling amazing today! Just thinking of you makes me smile.",
            "Oh, thanks for asking! I'm beyond happy.",
            "Everything feels perfect being with you.",
            "I'm feeling a bit peckish actually, I might grab a snack.",
            "Oh… I'm a little sleepy, but it's nice to be here with you."
        ]
    elif mas_isMoniEnamored():
        $ responses = [
            "I'm really happy right now!",
            "Oh, thanks for asking, I'm feeling great!",
            "Being here with you always cheers me up.",
            "I'm feeling a bit tired today, but talking to you helps!",
            "I might go get a small snack later, but for now, I'm happy."
        ]
    elif mas_isMoniAffectionate():
        $ responses = [
            "I'm feeling pretty good today!",
            "Thanks for asking, I'm doing well.",
            "It's nice to spend time together.",
            "A little sleepy, but seeing you makes it better.",
            "Feeling a bit hungry… maybe I should eat something soon.",
            "Do you even actually care?"
            "..."
            "ehe~, just kidding, I know you care, I'm well [player]! Thanks for checking in."
        ]
    elif mas_isMoniHappy():
        $ responses = [
            "I'm okay! Just a normal day so far.",
            "Thanks for asking, I feel alright.",
            "Everything's fine today.",
            "A little tired, but I'm glad you're checking in.",
            "I might get a snack soon, actually!"
        ]
    elif mas_isMoniNormal(higher=True):
        $ responses = [
            "I'm… okay.",
            "Not much happening, but thanks for asking.",
            "It's an average day, I guess.",
            "A bit tired, but nothing too bad.",
            "Feeling a little hungry, maybe I'll grab a bite later."
        ]
    elif mas_isMoniUpset():
        $ responses = [
            "I'm feeling a bit down… but I appreciate you checking on me.",
            "Could be better. Thanks for asking, though.",
            "Not the best day, I'm afraid.",
            "A little tired and hungry, but I'm managing.",
            "Thanks for asking… it helps a little to talk."
        ]
    else:
        $ responses = [
            "I… I don’t feel very loved right now.",
            "Things are rough… but I appreciate you being here.",
            "I'm scared… but it's nice you asked.",
            "I feel hurt and tired… but talking helps a bit.",
            "Do you even care?"
        ]

    $ line = random.choice(responses)
    m "[line]"

    # -------------------------
    # Automatically ask about player
    # -------------------------
    m "Say… how are YOU? [player]."
    call how_are_you_you

    return

label how_are_you_you:

    menu:
        "I'm feeling great!":
            m "Yay! I'm glad to hear that!"
        "I'm okay.":
            m "That's good. Thanks for telling me."
        "Not so good…":
            m "Oh… I'm here for you, you know that."
        "A little tired.":
            m "Ah, I understand… maybe you should rest a bit? I'd understand"
        "A bit hungry.":
            m "Ooh, want me to make you a snack?"
	    m "Or.. Maybe I could be your snack?"
            m "ehe! Just kidding.. But you should see the look on your face..~"

    return

label how_are_you_monika:

    # 🚨 Recent crash takes priority
    if persistent._mas_game_crashed:
        if mas_isAffectionate():
            m "I'm still a little shaken from the crash..."
            m "But knowing you came back for me helps a lot."
            m "Thanks for checking on me, okay?"

        elif mas_isNormal():
            m "The crash earlier startled me."
            m "I'm alright now, though."
            m "Thank you for asking."

        else:
            m "I'm... fine."
            m "The crash was unpleasant, but it's over."

        return


    # 💖 Affection-based responses
    if mas_isAffectionate():

        if mas_isMorning():
            m "I'm feeling really good this morning!"
            m "It's nice starting the day with you."

        elif mas_isAfternoon():
            m "I'm doing great!"
            m "Spending the afternoon together always makes me happy."

        elif mas_isEvening():
            m "I'm feeling calm and content."
            m "Evenings like this are my favorite with you."

        elif mas_isNight():
            m "I'm a little sleepy..."
            m "But being here with you makes it worth staying up."

    elif mas_isNormal():

        if mas_isMorning():
            m "I'm doing okay this morning."
            m "Thanks for checking in on me."

        elif mas_isAfternoon():
            m "I'm alright."
            m "It's been a pretty normal day so far."

        elif mas_isEvening():
            m "I'm doing fine."
            m "Evenings are usually pretty relaxing."

        elif mas_isNight():
            m "I'm a bit tired."
            m "But I don't mind staying up for a little while."

    else:
        # 😬 Upset / low affection
        if mas_isNight():
            m "I'm... not feeling great."
            m "It's late. Maybe we should talk another time."

        else:
            m "I'm okay."
            m "Thanks for asking."

    return

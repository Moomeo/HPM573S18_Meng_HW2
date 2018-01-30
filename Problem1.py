#Week 2, HW 2
# #scac

Constant1 = 1.371
Constant2 = 0.371

dictscore = {'Vision':     [1, 0.98, 0.89, 0.84, 0.75, 0.61],
             'Hearing':    [1, 0.95, 0.89, 0.80, 0.74, 0.61],
             'Speech':     [1, 0.94, 0.89, 0.81, 0.68],
             'Ambulation': [1, 0.93, 0.86, 0.73, 0.65, 0.58],
             'Dexterity':  [1, 0.95, 0.88, 0.76, 0.65, 0.56],
             'Emotion':    [1, 0.95, 0.85, 0.64, 0.46],
             'Cognition':  [1, 0.92, 0.95, 0.83, 0.60, 0.42],
             'Pain':       [1, 0.96, 0.90, 0.77, 0.55]}

def cal_utility_score(vision, hearing, speech, ambulation, dexterity, emotion, coginition, pain):
    '''

    :param vision:
    :param hearing:
    :param speech:
    :param ambulation:
    :param dexterity:
    :param emotion:
    :param coginition:
    :param pain:
    :return:
    '''

    if not (vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Vision level can take only 1, 2, 3, 4, 5, 6")
    if not (hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Hearing level can take only 1, 2, 3, 4, 5, 6")
    if not (speech in [1, 2, 3, 4, 5]):
        raise ValueError("Speech level can take only 1, 2, 3, 4, 5")
    if not (ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Ambulation level can take only 1, 2, 3, 4, 5, 6")
    if not (dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Dexterity level can take only 1, 2, 3, 4, 5, 6")
    if not (emotion in [1, 2, 3, 4, 5]):
        raise ValueError("Emotion level can take only 1, 2, 3, 4, 5")
    if not (coginition in [1, 2, 3, 4, 5, 6]):
        raise ValueError("Cognition level can take only 1, 2, 3, 4, 5, 6")
    if not (pain in [1, 2, 3, 4, 5]):
        raise ValueError("Pain level can take only 1, 2, 3, 4, 5")

    u_score = 1
    u_score *= dictscore['Vision'][vision - 1]
    u_score *= dictscore['Hearing'][hearing - 1]
    u_score *= dictscore['Speech'][speech - 1]
    u_score *= dictscore['Ambulation'][ambulation - 1]
    u_score *= dictscore['Dexterity'][dexterity - 1]
    u_score *= dictscore['Emotion'][emotion - 1]
    u_score *= dictscore['Cognition'][coginition - 1]
    u_score *= dictscore['Pain'][pain - 1]
    u_score = Constant1 * u_score - Constant2
    return u_score


myHUI3 = cal_utility_score(2, 1, 1, 2, 1, 2, 1, 3)

print (myHUI3)

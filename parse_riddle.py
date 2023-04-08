import re

def parse(riddle):
    [question, answer] = re.split('[Aa]nswer *- *', riddle)
    question = re.sub('[Rr]iddle *- *', '', question)

    question = question.strip()
    answer = answer.strip()
    return question, answer
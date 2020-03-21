import re

def calculate(question):
    question = question[8:-1].replace(" plus ", "+") \
                       .replace(" minus ", "-") \
                       .replace(" multiplied by ", "*") \
                       .replace(" divided by ", "/")

    if re.match(r'-?\d+[/*+-]', question, flags=0):
        while re.match(r'-?\d+[/*+-]', question, flags=0):
            match = re.match(r'-?\d+[/*+-]-?\d+', question, flags=0)
            if not match:
                raise ValueError("Ill Formed Question")
            else:
                question = question.replace(match.group(), str(int(eval(match.group()))))
    else:
        raise ValueError("Ill Formed Question")
    return int(question)

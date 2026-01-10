def is_perfect_possible(key, answers):
    complete = sum(k != "*" for k in key)
    correct = 0
    incorrect = 0
    for k, answer in zip(key, answers):
        if k == "*":
            continue

        if k != answer:
            incorrect += 1
            continue

        correct += 1

    if correct == complete or incorrect == complete:
        return True

    return False


print(is_perfect_possible(['A', 'B', 'C', '*', '*'], ['A', 'B', 'C', 'D', 'E']))
print(is_perfect_possible(['A', 'B', 'B', '*', '*'], ['A', 'B', 'C', 'A', 'B']))
print(is_perfect_possible(['*', 'A'], ['B', 'B']))

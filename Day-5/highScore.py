scores = [23, 34, 45, 98, 76, 54, 32]
def get_highest_score(list_of_scores):
    highest_score=0
    for score in scores:
        if highest_score < score:
            highest_score = score
    return highest_score

print(get_highest_score(scores))
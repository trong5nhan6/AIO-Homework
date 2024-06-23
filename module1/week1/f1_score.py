def calc_f1_score(tp, fp, fn):
    if isinstance(tp, int) and isinstance(fp, int) and isinstance(fn, int):
        if tp > 0 and fp > 0 and fn > 0:
            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1_score = 2 * (precision * recall) / (precision + recall)
            return precision, recall, f1_score
        else:
            return 'tp and fp and fn must be greater then zero'
    else:
        return 'tp and fp and fn must be int'


print(calc_f1_score('asdhf', 3, 5))
print(calc_f1_score(2, 3, 5))
print(calc_f1_score(-2, 3, 5))

def sort_pos_neg(lst):
    return sorted(lst, key=lambda x: (x < 0, abs(x)))
def answer(intervals):
    ordered_intervals = sorted(intervals, key=lambda i: i[0])
    me_intervals = [ordered_intervals.pop(0)]
    for interval in ordered_intervals:
        if me_intervals[-1][1] < interval[0]:
            me_intervals.append(interval)
        elif me_intervals[-1][1] < interval[1]:
            me_intervals[-1][1] = interval[1]
    f = lambda b: b[1] - b[0]
    return sum(map(f, me_intervals))

print answer([[1, 3], [3, 6]]) # 5
print answer([[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]) # 16

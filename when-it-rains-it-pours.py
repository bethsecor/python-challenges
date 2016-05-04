def answer(heights):
    if len(heights) == 1: return 0
    start = rain_start(heights)
    if start == 0:
        return 0
    else:
        return rain_collect(heights[start:])

def rain_collect(heights):
    next_max = max(heights[1:])
    next_max_i = heights.index(next_max)
    water_total = 0
    while len(heights) > 0:
        print heights[0]
        print next_max
        water_total += sum(map(lambda x: min([heights[0],next_max]) - x, heights[1:next_max_i]))
        print water_total
        heights = heights[next_max_i:]
        if len(heights[1:]) == 0: break
        next_max = max(heights[1:])
        next_max_i = heights.index(next_max)
    return water_total

def rain_start(heights):
    # return (i for i,height in enumerate(heights) if heights[i-1] < height).next()
    start = 0
    for i,height in enumerate(heights):
        if i != 0:
            if heights[i-1] < height:
                start = i
                break
    return start

# print answer([1, 4, 2, 5, 1, 2, 3]) # 5
# print answer([1, 2, 3, 2, 1]) # 0
# print answer([3, 2, 1]) # 0
# print answer([1, 2, 3]) # 0
# print answer([1]) # 0
# print answer([75, 94, 6, 31, 9, 84, 63, 42, 52, 16, 45, 22, 40, 74, 78, 30, 12, 3, 18, 71, 96, 51, 55, 39, 62, 14, 70, 25, 95, 65, 67, 72, 69, 4, 99, 76, 28, 56, 48, 13, 77, 20, 97, 50, 60, 91, 11, 61, 15, 32])
print answer([32, 35, 10, 37, 73, 24, 91, 72, 5, 62, 31, 87, 52, 83, 93, 47, 71, 50, 21, 59, 80, 85, 40, 29, 26, 7, 67, 74, 51, 98, 38, 78, 92, 16, 77, 43, 6, 70, 76, 13, 33, 95, 68, 2, 57, 90, 28, 55, 99, 65])

# import random
# s = random.sample(range(1, 100), 50)
# print s
# print(answer(s))

def answer(x):
    if x < 10:
    	return x
    numbers = list(str(x))
    f = lambda a,b: int(a) + int(b)
    reduced_number = reduce(f, numbers)
    return answer(reduced_number)

print answer(0)
print answer(14)
print answer(1235)

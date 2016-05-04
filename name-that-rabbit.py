def answer(names):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    names_values = {}
    alphabet_to_number = lambda x: alphabet.index(x) + 1
    for name in names:
        names_values[name] = sum(map(alphabet_to_number, list(name)))
    sorted_names = sorted(names_values.items(), key = lambda (k, v): (v, k), reverse=True)
    return map(lambda y: y[0], sorted_names)

print answer(["annie", "bonnie", "liz"]) # ["bonnie", "liz", "annie"]
print answer(["abcdefg", "vi"]) # ["vi", "abcdefg"]

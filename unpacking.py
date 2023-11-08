#unpacking lists
coins = [10,20,30]
# unpack like this *coins

coins2 = {"a":10, "b":20}
# unpack dictionionary **coins2

def yell(*words):
    # uppercased = map(str.upper, words)
    uppercased = [word.upper for word in words]
    print(*uppercased)


# map and filter

students = ['Harry', 'Hermioneone', 'balrog']

griffindor = [{'student': student, 'house': 'griffindor'} for student in students]

print(griffindor)
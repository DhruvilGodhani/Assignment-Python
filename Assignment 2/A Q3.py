String="Dhruvil Godhani"

list = list(filter(lambda x: True if x.lower() in "aeiou" else False, String))

print(list)
String="Dhruvil Godhani 30-10-2003"

list = list(filter(lambda x: True if x in "0123456789" else False, String))

print(list)
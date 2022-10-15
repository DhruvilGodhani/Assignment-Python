list1=[-100, 200, -300, 400, -500, 600, -700]

list2 = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, list1)))

print(list2)

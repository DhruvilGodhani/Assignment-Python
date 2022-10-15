from collections import OrderedDict
def remove_duplicate(sujal):
  return "".join(OrderedDict.fromkeys(sujal))
     
print(remove_duplicate("My Name Is Dhruvil Godhani"))
print(remove_duplicate("Dhruv"))
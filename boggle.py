def file_to_list_of_ints(filename):
   openedFile = open(filename, "r")
   stringList = openedFile.readlines()
   integerList = list(map(int, stringList))
   openedFile.close()
   return integerList

def product(list_of_ints):
   result = 1
   for index in range(0,len(list_of_ints)):
      result = result * list_of_ints[index]
   return result

file_to_list_of_ints("01_data.txt")
integerList = file_to_list_of_ints("01_data.txt")
product(integerList)
print(len(integerList))

#test
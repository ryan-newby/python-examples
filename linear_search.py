myArray = [2, 3, 6, 9, 12, 15, 19]

def search(elm,low,high, myArray):
   index = low
   while(index <= high):
      if myArray[index] == elm:
         return "elm " + str(elm) + " found at index " + str(index) + "!!!"
      else: 
        print("not found at index " + str(index))
        index = index + 1
    
   return "elm not found"

search(12, 0, 6, myArray))

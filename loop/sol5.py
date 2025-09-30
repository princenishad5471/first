input_str=input("give the words for finding duplicates:")

for i in input_str:
   print(i)
   if input_str.count(i)==1:
      print("result:",i)
      #break

def main():
   my_list = [1, 2, 5, 3.14, 8]
   another = my_list.copy()

   my_list += [1,2,3]
   another.append(10)


   print(my_list)
   print(another)

   location = my_list.index(8)
   print(location)

   my_list.insert(0, 20)
   my_list.insert(-0, 333)
   my_list.insert(-1, 22)
   my_list.insert(99, 77)

   my_list.sort()
   my_list.reverse()

   print(my_list)

   #print(min(my_list))
   #print(max(my_list))
   
   two_dlist = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
   ]







   # print(my_list)
   # another = list('hello')
   # print(another)

   # print(my_list[0])
   # my_list[0] = "SALLY"
   # print(my_list)

   # for i in range(len(my_list)):
   #    print(my_list[i])
   #    #my_list[i] = 7
      

   # if 'B' in my_list:
   #    print("FOUND IT")

   # print(my_list)

   for i, elem in enumerate(my_list):
      elem = my_list[i]
      print(i, elem)
      if elem == 'B':
         my_list[i] = 7

   # print(my_list)

   # new_list = my_list * 3
   # print(new_list)

   # my_list = my_list + [2,4,8]
   # print(my_list)

if __name__ == "__main__":
    main()
# Key Points to Remember
# 1) Sets are unordered
# 2) Set elements are unique and duplicates are not allowed.
# 3) Set's are mutable but the elements they contain must be immutable

def main():
   
   my_set = set(["cat", "dog", "kitten", "cat", "dog"])
   another_set = {'mouse', 'mouse', 'potato', 'chicken', 'cat', 'dog'}
   empty_set = {} # set()


   my_set.add("cat")
   my_set.add("parrot")

   print(my_set)
   for item in my_set:
      print(item)

   print(another_set)
   for item in another_set:
      print(item)

   new_set = another_set | my_set 

   print(new_set)
   
   new_set.discard('shark')
   print(new_set)
   my_list = ['cat', 'dog', 'kitten', 'broccoli']
   other_set = my_set.intersection(my_list)
   print(other_set)
   print(my_list)


if __name__ == "__main__":
    main()
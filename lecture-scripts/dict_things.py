# Key Points to Remember
# 1) Dictionaries are "mapping types"
# 2) Dictionaries are ordered by default since Python v3.7

def main():
   my_dict = { 'X': 34,
      'Y': 3.14,
      'Z': [1,2,3],
      0: (3.14, "Billy"),
   }



   another_dict = dict()

   my_funcs = {
         0: main,

   }

   print(my_dict)
   print(my_dict['X'])
   my_dict['X'] = 'Robert'
   print(my_dict)
   print(another_dict)

   for item in my_dict:
      print(my_dict[item])

   for key, value in my_dict.items():
      print(f"key: {key} -- Value: {value}")


   if 'X' in my_dict:
      print("X is a key")

   if 'O' not in my_dict:
      print("O is not here")


   print(my_dict[0])

   # my_funcs[0]()


   my_dict["potato"] = "dinner"
   print(my_dict)
   my_dict.pop("potato")
   print(my_dict)

   print(my_dict.keys())
   print(my_dict.values())






if __name__ == "__main__":
    main()
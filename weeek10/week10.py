# mylist=[ 76, 92.3, "hello", True ,4,76]
# mylist.append("apple")
# mylist.append("76")
# mylist.insert(3, "cat")
# mylist.insert(0,99)
# print(mylist)
#
# print(mylist.index("hello"))
# print(mylist.count("76"))
#
# mylist.remove(76)
# print(mylist)
# (mylist.pop(mylist.index(True)))
# print(mylist)

# def sum_evens(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             sum += number
#     return sum
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_evens(my_list))

# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
# my_list = ["apple", " cat","lemon","pyhton","tiger"]
# print(count_five_letter(my_list))

# def sum_untıl_even(number_list):
#     sum = 0
#     for num in number_list:
#         if num % 2 == 0:
#             break
#         sum += num
#         return sum
#     return sum
# my_list = [1, 2, 3, 4, 5, 6]
# print(sum_untıl_even(my_list))

# def count_untıl_sam(words):
#     count = 0
#     for word in words:
#         count +=1
#         if word == 'sam':
#             break
#     return count
#
# my_list = ["joe", "ali","veli", "sam","sami"]
# print(count_untıl_sam(my_list))

# def replace(s, old,new):
#     pieces = s.split(old)
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#        print("PASSED")
#     else:
#         print("NOT PASSED")
# test(replace('mississippi','i','I'),
#       'mIssIssIppI')

# def find_max_val_in_list(num_list):
#     max_val = num_list[0]
#     for num in num_list:
#         if num > max_val:
#             max_val =num
#
#     return max_val
#
# print(find_max_val_in_list([1,2,3,4,5,6,7,8,9,10]))
# print(find_max_val_in_list([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]))

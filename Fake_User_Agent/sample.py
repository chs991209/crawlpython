# a = input(); b = input()
# # a = input()
# # b = input()
# print('')
#
# print(a+'\n'+ b)
# print('-' * 100)
#
# print(a)
# print(b)
# #
# # str.isalnum()

list_test = [1, 2, 3, 4, 5]
print(len(list_test))

for a in range(len(list_test)):
    print(list_test[a], end=" ")


print("")
for b in range(0, 5):
    print(list_test[b])


print(list_test[0:5])

string = "Hey! What's up bro?"

new_string = "".join(char for char in string if char.isalnum())
print(new_string)

"""
-------------------------------------------
"""


def add_the_num(num1=None, num2=None):
    num1 += num2
    #     return num1
    #
    #
    # print(add_the_num(1, 3))
    print(num1)


add_the_num(1, 3)


shop_list = {"cabbage": 5000, "Daikon": 2000, "Lettuce": 3000}


list_index = []
list_key = []
list_elem = []


#
class DictArgs(
    len_index=None,
):
    for index, (key, elem) in enumerate(shop_list.items()):
        list_index.append(index + 1)
        list_key.append(key)
        list_elem.append(elem)


# for _index, _key, _value in range(len(list_index)):

# html area
material_01 = "Num : {}, Name : {}, Price : {}".format(
    list_index[0], list_key[0], list_elem[0]
)


print(material_01)


# print(str(index) + ' ' + str(key) + ' ' + 'elem')
#
# print("Select Shop_list[1-3] = ")
# goodsIdx = int(input())
# print()

# home = {
#     'p1': 'Seoul',
#     'p2': 'Incheon',
#
#         }
#
# student_01 = home[1]
# print(student_01)

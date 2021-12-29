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
    print(list_test[a], end=' ')


print('')
for b in range(0, 5):
    print(list_test[b])


print(list_test[0:5])

string = "Hey! What's up bro?"

new_string = ''.join(char for char in string if char.isalnum())
print(new_string)
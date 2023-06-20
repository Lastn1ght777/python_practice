# print("Hello World")
# first_name = "Alisher"
# second_name = "Subanov"
# print(f'Привет меня зовут {first_name} {second_name}')
# for i in range(1, 9):
#     print(i)
#
# # Создаём пустой список и в него добавляем строки
# new_list = []
#
#
# def test():
#     while True:
#         word = input("Введите слова:")
#         if (word != "" or word != " " or word.strip()) and word != "q":
#             new_list.append(word)
#             print(new_list)
#         elif word == "q":
#             break
#
#
# test()
# print(new_list)
#
# get_split = "19.06.2023"
# print(get_split.split("."))  # разделяем строку по "." на список ['19', '06', '2023']
# print(get_split[-1])  # берём последний индекс списка 3
# slice_1 = get_split.split(".")
# print(slice_1[::2])  # slice[] start:stop:step
# print(get_split[::2])  # slice
# print(get_split[::-1])  # reverse
# print(get_split[::-1][::-1])  # reverse reverse
# print(get_split[::-1][::-1][::-1])  # reverse reverse reverse
# print(get_split[::-1][::-1][::-1][::-1])  # reverse reverse reverse reverse
# print(get_split[::-1][::-1][::-1][::-1][::-1])  # reverse reverse reverse reverse reverse
# print(get_split[::-1][::-1][::-1][::-1][::-1][::-1])  # reverse reverse reverse reverse reverse reverse
#
# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a, *b = list_a
# print(a)
# print(b)

# x = 10
# while x >= 0:  # До тех пор пока x >= 0
#     print(x)
#     x -= 1  # x = x - 1
# print("Всё!")


t = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # кортэж
print(type(t))  # <class 'tuple'>
print(*t, sep=":", end="!")  # => 1:2:3:4:5:6:7:8:9!

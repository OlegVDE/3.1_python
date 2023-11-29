# удаляем четные элементы
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
delete_list = []
for i in range(len(my_list)-1):
  print(i)
  if i > 0 and i % 2 != 0:
        delete_list.append(i)
for el in delete_list[::-1]:
  my_list.pop(el)
print(my_list)


# печатаем, если более 3х гласных, слова разделены пробелами
stringa = 'привет велосипедист питонист шарпист АРТИСТА'
good_list = []
vowel = ['у','е','ы','а','о','э', 'я', 'и','ю']
for el in stringa.split():
  counter = 0
  for symbol in el:
    if symbol.lower() in vowel:
      counter += 1
  if counter > 2:
    good_list.append(el)
print(good_list)


# находит второй по величине элемент в списке
my_list = [10, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.sort()
print(my_list[-2])
# begin = max(my_list)
# for i in range(len(my_list)):
#   if len(my_list) == 1:
#     print('Обмаан!!! Тут только одно значение!! Фу так делать...')
#     break
#   my_list.remove(begin)
#   if max(my_list) < begin:
#     print(max(my_list))
#     break


# удаляет из списка все дубликаты
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
answer = set(my_list)
print(answer)


# считывает данные из CSV-файла и создает словарь, где ключами являются значения в столбце «Name», а
# значениями — соответствующие им словари с информацией о поле, возрасте и зарплате
import pandas as pd

df = pd.read_csv('example.csv')
data = df.set_index('Name').T.to_dict('dict')
print(data)


# Написать программу, которая запрашивает у пользователя строку и выводит на экран все ее подстроки длиной не менее
# трех символов
text = str(input('введите текст'))
ans = []
for el in text.split():
  if len(el) >= 3:
    ans.append(el)
print(ans)
while True:
 print('Введіть "o", щоб завершити цикл')
 response = input('> ')
 if 'o' in response or 'O' in response:
  break
#######################
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
new_lst = []
for elem in lst1:
 if type(elem) == str:
  new_lst.append(elem)
print(new_lst)
##########################
summ = 0
for i in range(0,2001):
 if i % 2 == 0:
   summ = summ + i
print(summ)
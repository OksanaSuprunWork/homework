def my_funk(x,y):
 if type(x) == int and type(y) == int:
  result = x * y
  print(result)
 elif type(x) == str and type(y) == str:
  result = x + y
  print(result)
 else:
  result = (x,y)
  print(result)
  return result

my_funk(3,5)
my_funk("Ramona","Elli")
my_funk(True,3.8)

def my_funk(x,y):
 if type(x) == int and type(y) == int:
  result = x * y
  print(result)
  return result
 elif type(x) == str and type(y) == str:
  result = x + y
  print(result)
  return result
 else:
  result = (x,y)
  print(result)
  return result
 
my_funk(3,5)
my_funk("6", "Kosta-Rika")
my_funk(True, 5)
x=3
y=0
try:
  print(x/y)
except NameError:
  print("Zmienna nie zdefiniowana") 
except Exception as exp:
  print("Błąd operacji!", exp)
else:
  print("Nie ma błędów")

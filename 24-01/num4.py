s = input()
s2 = "1234567890"
count = 0
for i in range(len(s2)):
  if s2[i] in s:
    count += 1
if count > 0:
  print("Цифра есть")
else:
  print("Цифр нет")

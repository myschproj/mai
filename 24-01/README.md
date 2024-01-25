# Занятие от 24-го числа 

`kakie-to chisla, stroki, kakaya to huynua blyad. mne oni voobshe neinteresny` (c) Oleg Tinkov

---

### Задача 1:

```python
s = str(input())
for x in range(0, len(s), 2):
  print(s[x])
```

### Задача 2:

```python
n = input()
for i in range(-1, -len(s)-1, -1):
  print(s[i])
```

### Задача 3:

```python
s = input()
count = 0
for i in range(len(s)):
  count += int(s[i])
print(count)
```

### Задача 4:

```python
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
```

### Задача 5:

```python
s = input()
count = 0
for i in range(len(s)-1):
  if s[i] == s[i+1]:
    count += 1
print(count)
```

### Задача 6:

```python
s = input()
if s[:] == s[::-1]:
  print("Yes")
else:
  print("No")
```

### Задача 7:

```python
s = input()
print(s*33)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:len(s)-1])
```

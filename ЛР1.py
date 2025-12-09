numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
m = numbers.index(None)
print(f"Индекс пропущенного элемента: {m}")
b = []
for num in numbers:
    if num is not None:
        b.append(num)
total_sum = sum(b)
a = total_sum /( len(b)+ 1 )
print(f"Среднее арифметическое: {a}")
numbers [m] = a
print("Измененный список:",numbers)
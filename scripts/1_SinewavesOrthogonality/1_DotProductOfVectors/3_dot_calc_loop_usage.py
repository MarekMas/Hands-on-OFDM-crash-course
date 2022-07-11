green = [1.23, 2.34]
blue = [2.34, -1.23]

dot_product = 0
for i in range(len(green)):  # i = 0,..len(green)-1
    dot_product += green[i] * blue[i]

print(dot_product)

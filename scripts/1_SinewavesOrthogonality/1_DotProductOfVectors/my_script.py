a = [0.088, 0.088, 0.088, 0.442, 0.530, 0.000, -
     0.530, -0.442, -0.088, -0.088, -0.088]
b = [-0.080, -0.080, -0.080, -0.398, -0.477, -
     0.000, 0.477, 0.398, 0.080, 0.080, 0.080]

dot_product = 0
for i in range(len(a)):
    dot_product += a[i]*b[i]
    print(dot_product)

dot_product = round(dot_product, 6)
print(dot_product)

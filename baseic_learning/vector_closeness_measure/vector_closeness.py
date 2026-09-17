import math

vector_a = [4, 4]
vector_b = [5, 3]

distance = math.sqrt(
    (vector_b[0] - vector_a[0]) ** 2 +
    (vector_b[1] - vector_a[1]) ** 2
)

print(distance)
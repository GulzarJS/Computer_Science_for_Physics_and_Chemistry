import math as mt
import random
import time as t


# Functions for finding area of circle with trapezoid method

# Function to find the angle between radius and the part until to chord
def angle_of_segment(r, a):
    cos_angle = a / r
    angle = mt.acos(cos_angle)

    return angle


# Function to find the length of the chord
def length_of_chord(r, a):
    return 2 * r * mt.sin(angle_of_segment(r, a)).__round__(2)


# Function to find area of trapezoid
def area_trapezoid(a, b, h):
    return ((a + b) / 2) * h


def area_of_circle_trapezoid(r, n):

    h = r / n
    half_area_sum = 0
    chords = list()
    chords.append(r * 2)

    for i in range(1, n):
        chords.append(length_of_chord(r, i * h))

    for i in range(0, n - 2):
        half_area_sum += area_trapezoid(chords[i], chords[i + 1], h)

    area = half_area_sum * 2

    return area.__round__(2)


# Functions for finding area of circle with trapezoid method

def area_of_circle_monte_carlo(radius, n):
    # nb of points which is inside of square. I will show area of circle
    inside = 0

    for i in range(0, n):
        x2 = random.uniform(-1, 1) ** 2
        y2 = random.uniform(-1, 1) ** 2

        if mt.sqrt(x2 + y2) < 1.0:
            inside += 1

    pi = 4 * inside / n
    area = pi * mt.sqrt(radius)
    return area


radius = 1

print("Circle are with Trapezoid Method:")
start = t.time()
print("n = 10 => ", area_of_circle_trapezoid(radius, 10))
end = t.time()
time = end - start
print(time.__round__(8))
start = t.time()
print("n = 100 => ", area_of_circle_trapezoid(radius, 100))
end = t.time()
time = end - start
print(time.__round__(8))
start = t.time()
print("n = 1000 => ", area_of_circle_trapezoid(radius, 1000))
end = t.time()
time = end - start
print(time.__round__(8))

print("Circle are with Monte Carlo Method:")
print("n = 10 => ", area_of_circle_monte_carlo(radius, 10))
print("n = 100 => ", area_of_circle_monte_carlo(radius, 100))
print("n = 1000 => ", area_of_circle_monte_carlo(radius, 1000))
print("n = 10000 => ", area_of_circle_monte_carlo(radius, 10000))
print("n = 100000 => ", area_of_circle_monte_carlo(radius, 100000))

print("\nCONCLUSION: I think that the most efficient method is Trapezoid method with high value of n")





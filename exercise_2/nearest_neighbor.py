import random, math


class Point:
    pass


def generate_point_in_square():
    p = Point()
    p.x = random.random()
    p.y = random.random()
    p.is_in_square = True
    return p


def generate_point_not_in_square():
    p = Point()
    p.x = random.random() + 1
    p.y = random.random() + 1
    p.is_in_square = False
    return p


def generate_point():
    p = Point()
    p.x = random.random() * 2
    p.y = random.random() * 2
    p.is_in_square = None
    return p


def create_learning_set():
    learning_set = []
    for _ in range(100):
        learning_set.append(generate_point_in_square())
    for _ in range(100):
        learning_set.append(generate_point_not_in_square())
    return learning_set


def create_test_set():
    test_set = []
    for _ in range(100):
        test_set.append(generate_point())
    return test_set


def is_in_square(point):
    return point.x < 1 and point.y < 1


def classify(point, learning_set):
    nearest = None
    nearest_distance = 10
    for learn in learning_set:
        distance = math.sqrt((point.x-learn.x)**2+(point.y-learn.y)**2)
        if distance < nearest_distance:
            nearest = learn
            nearest_distance = distance
    return nearest.is_in_square


def evaluate():
    learning_set = create_learning_set()
    test_set = create_test_set()
    correct = 0
    for point in test_set:
        if classify(point, learning_set) == is_in_square(point):
            correct += 1
    return correct


sum = 0
for _ in range(100):
    sum += evaluate()

sum /= 100

print str(sum) + " correct averaged"




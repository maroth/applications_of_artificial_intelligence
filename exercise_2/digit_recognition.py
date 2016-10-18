import wave


class Digit:
    pass



def create_set(path):
    training_set = []
    for num in range(0, 10):
        file_path = "sounds/" + path + "/" + str(num) + ".wav"
        spf = wave.open(file_path, 'r')
        signal = spf.readframes(-1)
        digit = Digit()
        digit.signal = signal
        digit.value = num
        training_set.append(digit)
    return training_set


def distance(d1, d2):
    distance = 0
    for d1_ in d1.signal:
        for d2_ in d2.signal:
            print list(d1_)[0]
            print list(d2_)[0]
    return distance


def classify(point, training_set):
    nearest = None
    nearest_distance = 10
    for learn in training_set:
        d = distance(learn, point)
        if d < nearest_distance:
            nearest = learn
            nearest_distance = distance
    return nearest.value


def evaluate():
    training_set= create_set("train")
    test_set = create_set("test")
    correct = 0
    for point in test_set:
        result = classify(point, training_set)
        print("classified " + str(point.value) + " as " + str(result))
        if str(result) == str(point.value):
            correct += 1
    return correct

print(create_set("test")[0])


sum = 0
tries = 1
for _ in range(tries):
    sum += evaluate()

sum /= tries

print str(sum) + " correct averaged"




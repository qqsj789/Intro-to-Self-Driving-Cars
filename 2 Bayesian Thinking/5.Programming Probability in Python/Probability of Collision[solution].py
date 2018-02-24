def probability_of_collision(car_1, car_2):

    probability = 0.0 # you should change this value based on the directions.

    if car_1 == "L":
        if car_2 == "L":
            probability = 0.5
        elif car_2 == "S":
            probability = 0.25
        else:
            probability = 0.1

    elif car_1 == "S":
        if car_2 == "L":
            probability = 0.25
        elif car_2 == "S":
            probability = 0.02
        else:
            probability = 0.1

    else:
        if car_2 == "L":
            probability = 0.1
        elif car_2 == "S":
            probability = 0.1
        else:
            probability = 0.01


    return probability

def test():
    num_correct = 0

    p1 = probability_of_collision("L", "L")
    if p1 == 0.5:
        num_correct += 1

    p2 = probability_of_collision("L", "R")
    if p2 == 0.1:
        num_correct += 1

    p3 = probability_of_collision("L", "S")
    if p3 == 0.25:
        num_correct += 1

    p4 = probability_of_collision("S", "R")
    if p4 == 0.1:
        num_correct += 1

    print("You got", num_correct, "out of 4 correct")

test()

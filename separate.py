#!/usr/bin/python3

"""
W is a vector of weights
th is a threshold
phi is a classification function
eta is the learning rate (0 <= eta <= 1)
"""

# Threshold ???? (let's try 10, but I want to adjust to see how much it matters)
th = 1

# Initialize weights to 0 (except w0, for cleanliness)
# Note later that each of the tuples has x0 = 1
W = [-th,0,0,0,0]
#W = [-0.8, 0.26, 0.82, -1.04, -0.44]


# Here are the weights after running it once
#W = [-10, -1.9, 0.3, -3.3, -1.2]

# Here are the weights after running it twice
#W = [-10, -3.8, 0.6, -6.6, -2.4]

#W = [-9.2, 1.6, 2.72, -2.86, -1.26]

# Eta ???? (let's try 0.1, but adjust to see how much it matters)
eta = 0.1

def phi(z):
    if z >= 0:
        return 1
    else:
        return -1

def dot(x,w):
    assert len(x) == len(w)
    total = 0
    for i in range(len(x)):
        total += x[i] * w[i]
    return round(total,2)

def setup():
    f = open('iris_two.data')
    data = []
    for line in f:
        split = line.split(',')
        #print(len(split))
        assert len(split) == 5
        a0 = float(split[0])
        a1 = float(split[1])
        a2 = float(split[2])
        a3 = float(split[3])
        cls = split[4].strip()
        tup = (1, a0, a1, a2, a3, cls)
        data.append(tup)
    return data

def train(point):
    global W
    #print(W)
    
    x = point[:5]

    # Compute predicted classification
    predicted = phi(dot(W,x))
    if point[-1] == "Iris-setosa":
        true = 1
    else:
        true = -1

    if true == predicted:
        pass
        #print("Correct!")
    else:
        print("Adjusting weights...")

    for j in range(len(x)):
        # Compute delta for each xj
        delta = eta * (true - predicted) * x[j]

        # Update weights
        W[j] = round(W[j] + delta, 4)

if __name__ == '__main__':
    data = setup()

    # For each training sample, perform the following
    #   Compute predicted classification (either 1 or -1)
    #   Update weights (wj = wj + deltawj)
    #   deltawj = eta(true class - predicted class)* xj

    for i in range(10):
        for point in data:
            train(point)

    print(W)



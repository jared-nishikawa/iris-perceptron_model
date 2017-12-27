# Irises

This was my first foray into machine learning.  I followed a guide to learn about perceptrons and wrote a simple program to separate Iris-setosa from Iris-versicolor samples.

I had read that these two are linearly separable (but not the third), so it seemed like a good first challenge to see if I could separate these two.

Even though I know there are good Python libraries for machine learning, I wanted to write this one from scratch to make sure I understood what was going on.

This model is a simple perceptron model using stochastic gradient descent to update my weights.  It doesn't take very many passes through the data until the weights don't need to be adjusted anymore.

My final weights are:
[-0.8, 0.26, 0.82, -1.04, -0.44]

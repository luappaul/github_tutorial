"""Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with one easy exercise.
    * Submit a Pull-Request on github to practice `git`.

The function below is a skeleton function. The docstring explains what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 1 test ran with success.
"""

import numpy as np


def max_index(X):
    
    if X is None:
        raise ValueError("cannot be None")

    if not isinstance(X, np.ndarray):
        raise ValueError("should be a numpy array")

    if X.ndim != 2:
        raise ValueError("should be 2D")

    max_id = np.unravel_index(np.argmax(X), X.shape)
    return max_id

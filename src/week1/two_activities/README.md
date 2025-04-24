# Numpy activities
This repository contains solutions to two Numpy-based activities. As a beginner in Python, these two activities have been incredibly helpful in solidifying my understanding of fundamental concepts and libraries like Numpy. Here's how each activity has contributed to my learning:

## Activity 1: Basic Numpy array operations( activity_1.py)
- Create Numpy array with intrinsic NumPy array creation functions (e.g. arange), there are also other intrinsic functions like ones, zeros, etc.
- Access the Numpy array's shape attribute, which returns tuple of ints. The elements of the shape tuple give the lengths of the corresponding array dimensions.
- Access the Numpy array's dtype attribute, which returns a data type object that describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted.
- The * operation can be used to multiple every element in a Numpy array by a scalar without using loop.

## Activity 2: 2D Numpy array analysis( activity_2.py )
- Compute the arithmetic mean along the specified axis with numpy.mean function. "axis=0" means along the column and "axis = 1" means working along the row.
- Compute the sum of array elements over a given axis with numpy.sum function. "axis = 1" means working along the row which represents the students. Then use numpy.argmax to return the indices of the maximum values along the axis.
- Accessing a Numpy array by a specific column index can be achieved by indexing. Numpy follows standard 0-based indexing in Python. "scores[:, 2]" returns the 3rd column which represents the 3rd subject. The += operation can be used to add every element in the column to a scalar and save the result to the variable on the left.
- More information about the usage of Numpy can be found on https://numpy.org/doc/stable/

## Overall Benefits
Both activities improved my problem-solving skills and my ability to deal with complex computing tasks efficiently with Numpy.
import numpy as np;

def positive_integers():
    """ 1- Activity : Create a NumPy array of the first 10 positive integers. Then:
            1. Print the array.
            2. Print the shape and data type of the array.
            3. Multiply each element by 2 and print the result.
    """
    # Create a NumPy array of the first 10 positive integers.
    arr = np.arange(1, 11)
    # Print the array.
    print("Created array: ", arr)
    # Print the shape and data type of the array.
    print("Shape: ", arr.shape)
    print("Data type: ", arr.dtype)
    # Multiply each element by 2 and print the result.
    doubled_arr = arr * 2
    print("Doubled array: ", doubled_arr)

if __name__ == '__main__':
    positive_integers()
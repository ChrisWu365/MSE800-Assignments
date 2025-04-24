"""
Tasks:
1. Print the average temperature for a week.
2. Find the highest and lowest temperature recorded.
3. Convert all temperatures to Fahrenheit and print the result.
(Formula: F = C * 9/5 + 32)
4. Identify the days (by index) where the temperature was above 20°C.
"""

import numpy as np

def calctemperature():
    data = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    avg = np.average(data)
    highest = np.amax(data)
    lowest = np.amin(data)
    fahrenheit = data * 9 / 5 + 32
    indices = np.where(data > 20)
    print("The temperature for the week: ", data)

    print(f"1. The average temperature for the week: {avg:.1f}")

    print("2. The highest temperature: %s and the lowest temperature: %s" % (highest, lowest))

    print("3. The Fahrenheit for the week: ", fahrenheit)

    # the index starts from 0 which means the first day of the given week
    print("4. The days (by index) where the temperature was above 20°C: ", indices)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calctemperature()
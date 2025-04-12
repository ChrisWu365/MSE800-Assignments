# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def calctemperature():
    # Use a breakpoint in the code line below to debug your script.
    data = np.array([17,18,19,20,21,22,23])
    avg = np.average(data)
    highest = np.amax(data)
    lowest = np.amin(data)
    fahrenheit = data * 9 / 5 + 32
    indices = np.where(data > 20)
    print("The average temperature for the week: ", avg)
    print("The highest temperature for the week: ", highest)
    print("The lowest temperature for the week: ", lowest)
    print("The Fahrenheit for the week: ", fahrenheit)
    print("The days (by index) where the temperature was above 20°C: ", indices)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calctemperature()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

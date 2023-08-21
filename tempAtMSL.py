# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Revised: 20 Aug 2023
# Description:  Given a temperature (in degrees Celsius), find and return the temperature at Mean Sea Level

def tempAtMSL(temp, alt):
    """
    :param temp:    (float) temperature in degrees Celsius
    :param alt:     (int)   pressure altitude in feet
    :return:        (float) temperature at Mean Sea Level pressure altitude in feet
    """

    return temp + 2 * alt/1000


def main():
    test_temps = tempAtMSL(11.0, 2000)
    print(test_temps)
    return


if __name__ == "__main__":
    main()

# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Created: 3 Sep 2023
# Date Revised: 3 Sep 2023
# Description:  assuming a value has fallen outside of lookup values, determine whether the user would like to use
#               cutoff value in the calculations


def getResponse():
    """
    method to inform the user that values fall outside given table parameters and prompts the user to decide whether
    or not to use cutoff values
    :return: (bool) true or false
    """
    cutoff = input("Would you like to use cutoff values?  Enter 'yes' or 'no'")
    if cutoff.lower() == 'yes' or cutoff.lower() == 'y':
        return True
    elif cutoff.lower() == 'no' or cutoff.lower() == 'n':
        print("process has ended.  Returning to main function.")
        return False
    else:
        print("This response is not understood. Please try again.")



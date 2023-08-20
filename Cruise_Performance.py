# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Revised: 19 Aug 2023
# Description:  Control the Cruise_Performance app and call modules as necessary to
#               get data,
#               perform calculations,
#               save data,
#               return results

from get_data import get_user_data

def main():
    values_at_temp1_alt1_rpm1 = get_user_data()
    print("chickens")
    print(values_at_temp1_alt1_rpm1)
    return

if __name__ == "__main__":
    main()


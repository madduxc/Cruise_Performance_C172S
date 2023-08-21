# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Revised: 19 Aug 2023
# Description:  Greet user and collect input for Temperature, Altitude, and RPM
#               Return values to calling module

def getData():

    # declare variables & initialize
    airplane = "Cessna 172S"            # manually entered airplane type, to be converted to input later
    temp_c = -999                       # fictitious value that must be replaced for function to complete
    alt = -9999                         # fictitious value that must be replaced for function to complete
    rpm = -9999                         # fictitious value that must be replaced for function to complete
    rpm_low = 2100                      # manually entered min rpm value, to be converted to input later
    rpm_high = 2700                     # manually entered max rpm value, to be converted to input later

    # introduce the user to the app
    print("Welcome to the Cruise Performance calculator for the", airplane, ".")
    print("In order to calculate cruise performance, you will need to input Temperature, Altitude, and RPM")

    # get user data
    err_val_alt = 1
    while err_val_alt != 0:
        error_msg = "Altitude must be a number greater than 0.  Please try again"
        alt_input = input("Enter the cruising altitude (in feet): ")
        try:
            alt = int(alt_input)
        except:
            print(error_msg)

        if alt >= 0:
            err_val_alt = 0
        if err_val_alt != 0:
            print(error_msg)
        else:
            break

    err_val_temp = 1
    while err_val_temp != 0:
        error_msg = "Temperature must be a number consistent temperature in Degree Celsius.  Please try again"
        temp_input  = input("Enter the temperature (in degrees Celsius) at this altitude: ")
        try:
            temp_c = float(temp_input)
            err_val_temp = 0
        except:
            print(error_msg)

    err_val_rpm = 1
    while err_val_rpm != 0:
        error_msg = "Engine RPM must be a number between" + str(rpm_low) + " and " + str(rpm_high) + ". Please try again"
        rpm_input = input("Enter the engine RPM for this trip: ")
        try:
            rpm = int(rpm_input)
        except:
            print(error_msg)
        if (rpm >= rpm_low) and (rpm <= rpm_high):
            err_val_rpm = 0
        if err_val_rpm != 0:
            print(error_msg)
        else:
            break

    return [temp_c, alt, rpm]


def main():
    values = getData()
    print(values[0], values[1], values[2])
    return


if __name__ == "__main__":
    main()

Electrical Circuit Calculator

Overview:

This project is a Python-based interactive calculator designed to perform various electrical circuit computations. It provides tools for calculating series/parallel resistances, converting resistor networks between Star (Y) and Delta (Δ) configurations, determining electrical power, and analyzing simple AC circuits.

The program is completely menu-driven and runs in the terminal.

Features:

1. Resistance Calculation
- Series Circuit : Adds resistance directly
- Parallel Circuit: Adds  inverse of input resistances and then inverse the total sum for required answer

2. Star-Delta configurations conversion
-Star to Delta : Equivalent resistances of star in delta form 
-Delta to Star : Equivalent Resistances of delta in star form

3. Power Calculation
Computes electrical power using either:
-P = V2/R
-P = I2R

4. AC circuit Calculation
Handles simple series RLC AC circuits.
-Inductive reactance
-Capacitive reactance	​
-Total impedance (linear sum)
-RMS current

Working:

-Users are provided menu that is accessible at any duration of calculation with the option to end/exit by pressing the required key in terminal.
-For the Series and Parallel resistance calculation a for loop is used for summation . Append is used for adding elemnts to the list
-For star-delta conversions arithmetic algebra is used , error handling is performed for any invalide response
-For Power Calculation and Ac circuit algebra is used for calculation

How to run project:

-Requires python 3.x
-No external Libraries required
-Save the code in a file
{CircuitCalculator_25BCE11055.py}
-Run the script
{python CircuitCalculator_25BCE11055.py}
-Follow the on Screen Commands

For Testing:

Try Inputing values that are not conventional (negative,zero,strings etc) at different sections of the code

"///////////////////FUNCTIONS////////////////////"
def parallel():
    resistance = []
    r = 0
    while True:
        r = int(input("Enter resistance or press 0 to finish: "))
        if r==0:
            break
        if r<0:
            break
        resistance.append(1/r)
        totalresistance = 0
        for i in resistance:
            totalresistance += i
        print(1/totalresistance)
    return(1/totalresistance)
def series():
    resistance2=[]
    r= 0
    while True:
        r = int(input("Enter resistance or press 0 to finish: "))
        if r ==0:
           break
        if r< 0:
            break
        resistance2.append(r)
        totalresistance = 0
        for i in resistance2:
            totalresistance+= i
        print(totalresistance)
    return(totalresistance)
def star2delta():
    "STAR IS Y SHAPED AND DELTA IS TRAINGLE SHAPED"
    print("========================================= REMINDER ==================================================")
    print("STAR IS Y SHAPED AND DELTA IS TRIANGLE SHAPED" \
    " R(ab) refers to the delta equivalent resistance between a and b")
    print("============================================= X =======================================================")
    Ra = int(input("Enter Resistance a :"))
    Rb = int(input("Enter Resistance b :"))
    Rc = int(input("Enter Resistance c :"))
    if Ra <= 0:
        if Rb <=0:
            if Rc <=0:
                print("!!!All values cannot be zero or less than zero!!!")
    R1 = (Ra * Rb + Rb * Rc + Ra * Rc)/(Rc)
    R2 = (Ra * Rb + Rb * Rc + Ra * Rc)/(Rb)
    R3 = (Ra * Rb + Rb * Rc + Ra * Rc)/(Ra)
    print("Resistance in DELTA formation and their respective DELTA conversion are as follows: ")
    print(Ra , Rb , Rc )
    print(R1 , R2 , R3)
def delta2star():
    "STAR IS Y SHAPED AND DELTA IS TRAINGLE SHAPED"
    print("========================================= REMINDER ==============================================")
    print("STAR IS Y SHAPED AND DELTA IS TRIANGLE SHAPED" \
    " R(a) refers to the delta equivalent resistance between 1 and 2")
    print("============================================= X =================================================")
    R1 = int(input("Enter Resistance 1 :"))
    R2 = int(input("Enter Resistance 2 :"))
    R3 = int(input("Enter Resistance 3 :"))
    if R1 <= 0:
        if R2 <=0:
            if R3 <=0:
                print("!!!All values cannot be zero!!!")
    Ra = R1*R2/(R1+R2+R3)
    Rb = R3*R2/(R1+R2+R3)
    Rc = R1*R3/(R1+R2+R3)
    print("Resistance in DELTA formation and their respective STAR conversion are as follows: ")
    print(R1 , R2 , R3 )
    print(Ra , Rb , Rc )
def power():
    choice = input("Voltage or Current for power: v/i ")
    r = float(input("Enter value of resistance: "))
    if choice == 'v':
        voltage= float(input("Enter value of voltage: "))
        power = voltage*voltage/r
    elif choice =='i':
        current = float(input("Enter value of current: "))
        power = current*current*r
    else :
        print("!!!!INVALID CHOICE!!!!")
        power= -1
    print("Power is : ", power)
def acmodule():
    vrms = float(input("Enter rms value of volatge: "))
    if vrms<0:
        print("!!!PLEASE ENTER POSITIVE VALUE!!!")
        return -1
    frequency = float(input("Enter frequency: "))
    if frequency<0:
        print("!!!PLEASE ENTER POSITIVE VALUE!!!")
        return -1
    resistance = float(input("Enter resistance: "))
    if resistance<0:
        print("!!!PLEASE ENTER POSITIVE VALUE!!!")
        return -1
    inductance = float(input("Enter inductance: "))
    if inductance<0:
        print("!!!PLEASE ENTER POSITIVE VALUE!!!")
        return -1
    capacitance = float(input("Enter capacitance: "))
    if capacitance<0:
        print("!!!PLEASE ENTER POSITIVE VALUE!!!")
        return -1
    omega = 2 * 22/7 *frequency
    impedance_r= resistance
    impedance_l= omega*inductance
    impedance_c= 1/(omega*capacitance)
    impedance_total= impedance_c + impedance_l + impedance_r
    i_rms = vrms/impedance_total
    print("Values of impedance(r,l,c,total) and rms current are as follows: ")
    print("R,L,C,TOTAL: " ,impedance_r,impedance_l,impedance_c,impedance_total)
    print("RMS VALUE OF CURRENT: ", i_rms)
    print("ALL VALUES IN THEIR S.I. UNITS")
"///////////////////MAIN PROGRAM/////////////////////"
def main_menu() :
    print("========================== CALCULATOR FOR ELECTRIC CIRCUITS ==========================")
    print("1. RESISTANCE CALCULATION")
    print("2. STAR  / DELTA CONVERSION")
    print("3. POWER CALCULATION")
    print("4. AC CIRCUIT CALCULATION")
    print("PRESS m TO RETURN TO MAIN MENU")
    print("PRESS x TO EXIT")
    option = input("-> ")
    if option == '1' :
        print("1. SERIES ")
        print("2. PARALLEL ")
        inp = input("-> ")
        if inp == '1':
            print(series())
        if inp== '2':
            print(parallel())
        else:
            print("END")
    if option=='2':
        print("1. STAR TO DELTA")
        print("2. DELTA TO STAR ")
        inp = input("-> ")
        if inp =='1' :
            print(star2delta())
        if inp=='2':
            print(delta2star())
        else :
            print("========================================= X ===============================================")
    if option =='3':
        print(power())
    if option=='4':
        print(acmodule())
    if option == 'm':
        print(main_menu())
        return(main_menu())
    if option == 'x':
        print("END")
        return("============================================THANK YOU==========================================")
    else :
            return(main_menu())
print(main_menu())

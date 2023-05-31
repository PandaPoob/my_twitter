import math

def human_format(num):
    
    if num > 9999:
        magnitude = 0
        #while is loop (keeps repeating until condition is falsy)
        #abs() returns the absolute value of the specified number
        while abs(num) >= 1000:
            magnitude += 1
            #Division Assignment: Divides the variable by a value and assigns the result to that variable.
            num /= 1000.0
            #force round down
            roundednum = math.floor(num*10)/10

            #removing number after decimal if it is 0 1
            #The %f formatter is specifically used for formatting float values (numbers with decimals).
            stringn = repr(roundednum)
            if stringn[-1] == "0":
                decimal = '%.0f%s'
            else:
                decimal = '%.1f%s'
            #print(decimal % (num, ['', 'K', 'M', 'B'][magnitude]))
            number = decimal % (roundednum, ['', 'K', 'M', 'B'][magnitude])
        return number

    else:
        return str(num)
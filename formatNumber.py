def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1

        #Division Assignment: Divides the variable by a value and assigns the result to that variable.
        num /= 1000.0
        print(num)
        #removing number after decimal if it is 0
        stringn = repr(num)
        if stringn[-1] == "0":
            decimal = '%.0f%s'
        else:
            decimal = '%.1f%s'
       
        number = decimal % (num, ['', 'K', 'M', 'B'][magnitude])

    return number
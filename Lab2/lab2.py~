# -*- coding: latin-1 -*-

def roman_to_int(romIn):
    runBool = True #runBool = True med gyldig input.
    romIn = romIn.upper() #Konverterer alt til Uppercase.
    value_list = [] #Liste - bokstav -> tall verdi.
    sum = 0
    print romIn
    print runBool
    for char in romIn: #Sjekk for True/False input.
        if char == 'I' or char == 'V' or char == 'X' or char == 'L' or char == 'C' or char == 'D' or char == 'M':
            pass
        else:
            runBool = False
    print runBool
    if runBool == True:
            for char in romIn: #Bokstavenes tall-verdi -> value_list.
                    if char == 'M':
                        value_list.append(1000)
                    elif char == 'D':
                        value_list.append(500)
                    elif char == 'C':
                        value_list.append(100)
                    elif char == 'L':
                        value_list.append(50)
                    elif char == 'X':
                        value_list.append(10)
                    elif char == 'V':
                        value_list.append(5)
                    elif char == 'I':
                        value_list.append(1)
            print value_list
            
            for i, item in enumerate(value_list): #Ser etter negative verdier og legger sammen i sum variabel.
                    print "index: %s, item: %s" %(i, item)
                    try:
                        if item < value_list[i+1]:
                            sum -= item
                        else:
                            sum += item
                    except:
                        sum += item
                        print "Done"
            return sum
    else:
            return "Ikke et gyldig tall"
            

def int_to_roman(number_in_string): #Funksjonen som skal konvertere fra Ti-tall til Romertall
    run = True
    try:
        number_in = int(number_in_string)
    except:
        run = False
    result = []
    
    #Loop som sjekker statements.
    if run == True:
        while number_in > 0:
        
            if number_in >= 1000:
               
                number_in -= 1000
                result.append("M")
                
            elif number_in >= 900:
                number_in -= 900
                result.append("CM")
                
            elif number_in >= 500:
                number_in -= 500
                result.append("D")
                
            elif number_in >= 400:
                number_in -= 400
                result.append("CD")
                
            elif number_in >= 100:
                number_in -= 100
                result.append("C")
                
            elif number_in >= 90:
                number_in -= 90
                result.append("XC")
                
            elif number_in >= 50:
                number_in -= 50
                result.append("L")
                
            elif number_in >= 40:
                number_in -= 40
                result.append("XL")
                
            elif number_in >= 10:
                number_in -= 10
                result.append("X")
            elif number_in >= 9:
                number_in -= 9
                result.append("IX")
            elif number_in >= 5:
                number_in -= 5
                result.append("V")
            elif number_in >= 4:
                number_in -= 4
                result.append("IV")
            elif number_in >= 1:
                number_in -= 1
                result.append("I")
                
        return "".join(result) #Kombinerer resultat.
    else:
        print "Ikke gyldig Input"
        
        

#Konsoll info
def test():
    print 'Test 1: Romertall til Ti-tall'
    print 'Test 2: Ti-tall til Romertall'
    roman_number = raw_input("Skriv inn Romertall med bokstaver mellom I og M: ")
    print roman_to_int(roman_number) #Resultat
    number_in_raw = raw_input("Skriv inn Ti-tall: ")
    print int_to_roman(number_in_raw) #Resultat

test()

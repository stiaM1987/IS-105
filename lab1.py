# -*- coding: utf-8 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#         
#
#
import sys
import psutil
import os
import platform
import gtk


cpu = platform.processor()
kernel = platform.platform()
system = platform.system()


# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Steffen Vetrhus', 'student2': 'Stian Mønsted'}



#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '` 
def ascii_bird():
	
    print   "     \/_" 
    print   "\,   /( ,/"
    print   " \\\' ///"
    print   "  \_ /_/"
    print   "  (./"
    print   "   '` "

print "This is assignment 1"    
print ascii_bird();
# 
#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og 
#					den mest signifikante bit-en er lengst til venstre
def bitAnd(x, y):
	return x & y;	

print "This is assignment 2"
print bitAnd(6, 5);
#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
	return x ^ y

print "This is assignment 3"
print bitXor(4, 5);

#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(x, y):
	return x | y
print "This is assignment 4"
print bitOr(0, 1);

#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
#

#Limitations for this function would be non ascii characters like æøå.
#The argument value of these are longer one so this test will fail.
def ascii8Bin(letter):
	convert = ord(letter)
	return '{0:08b}'.format(convert)

print "This is assignment 5"
print ascii8Bin('H');
# 
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
def transferBin(string): 
	l = list(string) #L = Liste
	for c in l: #For each encounter of C in the list L do the following:
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		print ascii8Bin(c)
		#print "Den binære representasjonen for %s" % c



print "This is assignment 6"
print transferBin("Hi")
#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#			b1.py", l		Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#  

def ascii2hex(bokstav):
	hexb = ord(bokstav)
	toHex = '{0:08x}'.format(hexb)
	return(toHex)

def transferHex(string):
	l = list(string)
	for c in l:
		print ascii2hex(c)		
		print "Den heksadesimale representasjonen for %s" % c

print "This is assignemnt 7"
print transferHex("Hi")

#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
def unicodeBin(character):
	return '{0:08b}'.format(ord(character))

print "Assignment 8"
print unicodeBin('å')
#
# Oppgave 9
#   Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
# 			Brand and model //Not
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU 
# 			Display resolution and size
# 			Operating system
#	
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#	
#	cat /etc/system-release
#	cat /proc/version
#	cat/etc/lib-release
#	uname -a
#	uname -mrs
#	cat/proc/cpuinfo | grep "model-name"	
# 	Or import other modules that can find the information you want like
#	platform
#	gtk



def printSysInfo():
	
	#Returns all mounted disk partitions
	diskInfo = psutil.disk_partitions()
	print diskInfo

	#Returns disk usage statistics about the given path
	diskUsage = psutil.disk_usage('/')
	print diskUsage

	#Return statistics about system memory usage
	memory = psutil.virtual_memory()
	print memory

	#Return system swap memory statistics
	swapMemory = psutil.swap_memory()
	print swapMemory
	
	#Return system CPU times
	cpuTimes = psutil.cpu_times()
	print cpuTimes

	#Return the logical number of CPUs
	cpuCount = psutil.cpu_count()
	print cpuCount

#With the psutil module you can not find information about
#Brand and Model
#Model of CPU
#Display resolution and size
#Operating system

print "This is assignment 9"
print printSysInfo();
print "\nSkjerm info: \n Skjermoppløsning i piksler = %d x %d" % (gtk.gdk.screen_width(),gtk.gdk.screen_height())
print "\nSystem:\n Prosessor type = %s \n Operativsystem = %s \n Distribusjon = %s" % (cpu, system, kernel)

def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	# Skriv her inn passende tester for tarnsferBin og transferHex funksjoner
	# fra oppgavene 6 og 7
	assert unicodeBin('å') == '11100101'
	#Dine egne tester
	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()
		

# Caleb Egbert
# UWYO COSC 1010
# 10/29/24
# HW 02
# Lab Section: 12
# Sources, people worked with, help given to: STEP Tutor
# your
# comments
# here

Morse_Code = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
    'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
    'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
    'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
    'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
    'Z':'--..',' ':' '
}
user_input = input("Write your message: ")

morse_string = ""
for char in user_input.upper():
    morse_string = morse_string + Morse_Code[char] + " "

print(morse_string)
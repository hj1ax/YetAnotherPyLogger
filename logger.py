import sys
import os
os.system("")

reset = "\u001b[0m"

bold =      "\33[1m"
italic =    "\33[3m"
url =       "\33[4m"
blink =     "\33[5m"
underline = "\u001b[4m"
reversed =  "\u001b[7m"

black =     "\u001b[38;5;0m"
gray =      "\u001b[38;5;8m"
red =       "\u001b[38;5;9m"
green =     "\u001b[38;5;10m"
yellow =    "\u001b[38;5;11m"
blue =      "\u001b[38;5;12m"
purple =    "\u001b[38;5;13m"
cyan =      "\u001b[38;5;14m"
white =     "\u001b[38;5;15m"

bg_black =  "\u001b[48;5;0m"
bg_gray =   "\u001b[48;5;8m"
bg_red =    "\u001b[48;5;9m"
bg_green =  "\u001b[48;5;10m"
bg_yellow = "\u001b[48;5;11m"
bg_blue =   "\u001b[48;5;12m"
bg_purple = "\u001b[48;5;13m"
bg_cyan =   "\u001b[48;5;14m"
bg_white =  "\u001b[48;5;15m"


def LOG_ERROR(text):    print(reset + red    + bold + "[-] Error: "   + reset + text + reset)
def LOG_WARNING(text):  print(reset + yellow + bold + "[!] Warning: " + reset + text + reset)
def LOG_INFO(text):     print(reset + blue   + bold + "[?] Info: "    + reset + text + reset)
def LOG_SUCCESS(text):  print(reset + green  + bold + "[+] Success: " + reset + text + reset)

def CUSTOM_COLOR(number):    print(f"\u001b[38;5;{number}m")
def CUSTOM_BG_COLOR(number): print(f"\u001b[48;5;{number}m")


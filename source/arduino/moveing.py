import serial
import keyboard
from colorama import Fore

ser = serial.Serial("COM5", 9600, timeout=1) 

def judge(value_x,value_y):
    if int(value_x) <= 522 and int(value_y)  == 0: 
        print("moving LEFT")
        keyboard.release("w")
        keyboard.release("s")
        keyboard.release("d")
        keyboard.press("a")
        
    if int(value_x) == 1023 and int(value_y) >= 510:
        print("moving stright")
        keyboard.release("a")
        keyboard.release("s")
        keyboard.release("d")
        keyboard.press("w")

    if int(value_x) >= 520 and int(value_y) == 1023:
         print("moving RIGHT")
         keyboard.release("w")
         keyboard.release("a")
         keyboard.release("s")
         keyboard.press("d")

    if int(value_x) == 0 and int(value_y) >= 510:
        print("moving down")
        keyboard.release("w")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.press("s")

    if int(value_x) == 504 and int(value_y) == 516:
        keyboard.release("w")
        keyboard.release("a")
        keyboard.release("s")
        keyboard.release("d")

while True:
    line = ser.readline()  
    if line:  
        str1 = line.decode("ascii").strip()  
        data = list(str1.split(","))
        print(Fore.GREEN+f"X:{data[0]},Y:{data[1]}")
        try: #error対策
            judge(data[0],data[1])
        except IndexError:
             pass
  


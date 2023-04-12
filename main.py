import eel
import turtle
import time
import os
import sys
eel.init("web")
colorValues = {
    1: '#fff',
    2: '#ff0',
    3: '#f0f',
    4: '#f00',
    5: '#ccc',
    6: '#888',
    7: '#880',
    8: '#808',
    9: '#800',
    10: '#0ff',
    11: '#0f0',
    12: '#088',
    13: '#080',
    14: '#00f',
    15: '#008',
    16: '#000'
}
# This function remove spaces and chars that are useless
def clean(array):
    result = []
    for string in array:
        if string != "" and string != " ":
            result.append(string)
    return result

def find_closing_parenthesis(lst, index):
    if lst[index] != "[":
        return -1
    count = 1
    for i in range(index + 1, len(lst)):
        if lst[i] == "[":
            count += 1
        elif lst[i] == "]":
            count -= 1
            if count == 0:
                return i
    return -1



def executeInstruction(i, array):
    if array[i] == "fd" or array[i] == "forward":
        t.fd(float(array[i + 1]))
        i += 1

    elif array[i] == "rt" or array[i] == "right":
        t.rt(float(array[i + 1]))
        i += 1

    elif array[i] == "lt" or array[i] == "left":
        t.lt(float(array[i + 1]))
        i += 1

    elif array[i] == "bk" or array[i] == "backward" or array[i] == "back":
        t.bk(float(array[i + 1]))
        i += 1

    elif array[i] == "color":
        if array[i + 1].isdigit():
            t.color(colorValues[int(array[i + 1])])
        # This means is hexadecimal or string like 'red' or 'blue'
        else:
            t.color(array[i + 1])
            i += 1

    elif array[i] == "setpensize" or array[i] == "pensize":
        if array[i + 1].isdigit():
            t.pensize(float(array[i + 1]))
            i += 1

    elif array[i] == "pu":
        t.pu()

    elif array[i] == "pd":
        t.pd()

    elif array[i] == "repeat":
        if not (array[i + 1].isdigit()):
            print("Falta el numero de repeticiones en el repeat")
        else:
            j = i + 3
            parenthesis = find_closing_parenthesis(array, i + 2)
            repeatArray = array[i+3:parenthesis]
            print(repeatArray)
            r = int(array[i + 1]) - 1
            while r > 0:
                ri = 0
                while ri < len(repeatArray):
                    ri = executeInstruction(ri, repeatArray)
                r -= 1
        i += 2

    else:
        print("Unknown instruction: " + array[i])
    return i + 1


@eel.expose
def stop():
    sys.exit()

@eel.expose
def compile(code):
    eel.writeOnConsole("Compiling...", "warning")
    turtle.Screen()
    turtle.title("Logo compiler output")
    global t
    t = turtle.Turtle()
    array = code.split()
    array = clean(array)
    i = 0
    t.lt(90)
    while i < len(array):
        i = executeInstruction(i, array)
    
    turtle.done()
    sys.exit()
eel.start("index.html")



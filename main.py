import eel
import compiler as cm
import sys
import os
def stop():
    sys.exit()

eel.init('web')


@eel.expose
def execute(code):
    cm.compile(code)
    
eel.start('index.html')
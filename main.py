import eel
import compiler as cm
import sys
import os
def stop():
    sys.exit()

eel.init('web')
eel.start('index.html')

@eel.expose
def execute(code):
    cm.compile(code)
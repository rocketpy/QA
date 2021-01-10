#  A set of Python modules to automate the Microsoft Windows GUI

# PyPi: https://pypi.org/project/pywinauto/
# Docs: https://pywinauto.readthedocs.io/en/latest/

# Getting started guide:  https://pywinauto.readthedocs.io/en/latest/getting_started.html

# pip install pywinauto
# or
# pip install -U pywinauto

from subprocess import Popen
from pywinauto import Desktop
from pywinauto.application import Application


app = Application(backend="uia").start('notepad.exe')

# describe the window inside Notepad.exe process
dlg_spec = app.UntitledNotepad

# wait till the window is really open
actionable_dlg = dlg_spec.wait('visible')

Popen('calc.exe', shell=True)
dlg = Desktop(backend="uia").Calculator
dlg.wait('visible')

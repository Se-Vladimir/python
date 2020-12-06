from tkinter import *
from tkinter.messagebox import askyesno

class ExitSaveChanges:
    def __init__(self, exit_text='Save changes before exit?'):
        self.exit_text = exit_text
        self.result = ''

    def dialog(self):
        self.result = askyesno('', self.exit_text)

    def run(self):
        self.dialog()

if __name__ == '__main__':

    Exit = ExitSaveChanges()

    def save_before_exit():
        Exit.run()

    root = Tk()
    root.protocol('WM_DELETE_WINDOW', save_before_exit)
    root.mainloop()

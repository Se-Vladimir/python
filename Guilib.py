import time
from tkinter import *


class StartMakingRoot:
    '''
    Описание класса:
    Основное tk-окно и все что с ним связано.
    '''
    def __init__(self):
        self.title = 'root'
        self.icon = 'py-blue-trans-out.ico'
        self.makeroot()

    def makeroot(self):
        self.root = Tk()

    def maketitle(self):
        '''
        Примечание:
        Данный метод устанавливает тайтл у основного окна.
        '''
        self.root.title(self.title)

    def endMakingRoot(self):
        self.root.mainloop()

    def parameters(self):
        pass

    def addMenu(self, menu):
        '''
        Примечание:
        "прикручиваем" к root меню оконного типа. Это "стандартное" меню,
        которое отображается полосой, с расположенными на ней выпадающими
        пунктами меню, в верхней части окна.
        '''
        self.root.config(menu=menu)

    def closeall(self):
        self.root.quit()

    def windowCloseClick(self):
        '''
        Примечание:
        Данный метод перехватывает протокол закрытия окна, т.е. когда
        пользователь нажимает на крестик и в момент такого нажатия
        запускает ф-ию root_close_click.
        '''
        self.root.protocol('WM_DELETE_WINDOW', self.root_close_click)

    def root_close_click(self):
        print('closed')
        self.closeall()

    def makeicon(self):
        '''
        Примечание:
        Данный метод устанавливает иконку(значек) основного окна приложения,
        которая отображается в верхней части окна, перед тайтлом и заменяет
        tk-иконку по умолчанию(на которой изображено птичье перо).
        '''
        self.root.iconbitmap(self.icon)

    def returnScreenSize(self):
        '''
        Примечание:
        Данный метод возвращает размер экрана монитора, в виде кортежа
        (ширина, высота).
        '''
        screensize = self.root.maxsize()
        print('scrensize:', screensize)

    def makeWindowSizeAndScreenPosition(self):
        '''
        Пример:
        self.root.geometry('640x480+480+140')

        Метод geometry() задает размер окна и его расположение на экране.
        Первые два параметра определяют ширину и высоту окна.
        Последние два отвечают за «x» и «y» координаты на экране.
        '''
        screensize = self.root.maxsize()
        X = int((screensize[0] / 2) - 320)
        Y = int((screensize[1] / 2) - 300)
        self.root.geometry('640x480'+'+'+str(X)+'+'+str(Y))

    def turnOffWindow(self):
        '''
        Примечание:
        Данный метод сворачивает окно на панель задач windows. Свертывание окна
        происходит мгновенно.
        '''
        self.root.iconify()

    def deleteWindow(self):
        '''
        Примечание:
        Данный метод удаляет окно, так, что оно полностью исчезает
        с экрана монитора.
        '''
        self.root.withdraw()

    def turnOnWindow(self):
        '''
        Примечание:
        Данный метод разворачивает окно из свернутого
        состояния(ф-я turnOffWindow), а также помимо этого он применим к ф-ии
        deleteWindow(удаление окна) - т.е., помимо "развёртывания"
        окна из свернутого состояния, с помощью этого метода можно
        создать заново удаленное окно, которое было удалено с помощью ф-ии
        deleteWindow.
        '''
        self.root.deiconify()

    def makeWindowState(self, state='normal'):
        '''
        Примечание:
        Данный метод устанавливает "статус" окна.
        Статусов у окна может быть четыре:
        1. свернутое окно(окно сворачивается(мгновенно)/открывается в панеле задачь windows):
           state='iconic'
        2. удаленное окно(окно полностью исчезает с экрана): state='withdrawn'
        3. распахнутое на весь экран окно: state='zoomed'
        4. окно с заданными(программистом) настройками,
           либо если настройки не заданы, то с настройками по умолчанию:
           state='normal'
        '''
        self.root.state(state)

    def raiseWindow(self):
        '''
        Примечание:
        Данный метод поднимает окно вверх на экране монитора, относительно
        других окон.
        '''
        self.root.lift()

    def putdownWindow(self):
        '''
        Примечание:
        Данный метод опускает окно вниз на экране монитора, относительно
        других окон.
        '''
        self.root.lower()


class AddWin:
    '''
    Описание класса:
    Неосновные окна-tk и все что с ними связано.
    '''
    def __init__(self):
        '''
        self.parent = Root.root
        self.parent = False
        '''
        self.parent = False
        self.title = 'Toplevel'
        self.icon = 'py-blue-trans-out.ico'
        self.makeToplevel()

    def makeToplevel(self):
        if self.parent:
            self.Toplevel = Toplevel(self.parent)
        else:
            self.Toplevel = Toplevel()

    def addMenu(self, menu):
        '''
        Примечание:
        "прикручиваем" к Toplevel меню оконного типа. Это "стандартное" меню,
        которое отображается полосой, с расположенными на ней выпадающими
        пунктами меню, в верхней части окна.
        '''
        self.Toplevel.config(menu=menu)

    def maketitle(self):
        '''
        Примечание:
        Данный метод устанавливает тайтл у неосновного окна.
        '''
        self.Toplevel.title(self.title)

    def closewin(self):
        '''
        Примечание:
        Данный метод закрывает неосновное окно.
        '''
        self.Toplevel.destroy()

    def windowCloseClick(self):
        '''
        Примечание:
        Данный метод перехватывает протокол закрытия окна, т.е. когда
        пользователь нажимает на крестик и в момент такого нажатия
        запускает ф-ию win_close_click.
        '''
        self.Toplevel.protocol('WM_DELETE_WINDOW', self.win_close_click)

    def win_close_click(self):
        print('Toplevel closed')
        self.closewin()

    def makeicon(self):
        '''
        Примечание:
        Данный метод устанавливает иконку(значек) неосновного окна приложения,
        которая отображается в верхней части окна, перед тайтлом и заменяет
        tk-иконку по умолчанию(на которой изображено птичье перо).
        '''
        self.Toplevel.iconbitmap(self.icon)

    def returnScreenSize(self):
        '''
        Примечание:
        Данный метод возвращает размер экрана монитора, в виде кортежа
        (ширина, высота).
        '''
        screensize = self.Toplevel.maxsize()
        print('scrensize(from Toplevel):', screensize)

    def makeWindowSizeAndScreenPosition(self):
        '''
        Пример:
        self.root.geometry('640x480+480+140')

        Метод geometry() задает размер окна и его расположение на экране.
        Первые два параметра определяют ширину и высоту окна.
        Последние два отвечают за «x» и «y» координаты на экране.
        '''
        screensize = self.Toplevel.maxsize()
        X = int((screensize[0] / 2) - 320)
        Y = int((screensize[1] / 2) - 300)
        self.Toplevel.geometry('640x480'+'+'+str(X)+'+'+str(Y))

    def turnOffWindow(self):
        '''
        Примечание:
        Данный метод сворачивает окно на панель задач windows. Свертывание окна
        происходит мгновенно.
        '''
        self.Toplevel.iconify()

    def deleteWindow(self):
        '''
        Примечание:
        Данный метод удаляет окно, так, что оно полностью исчезает
        с экрана монитора.
        '''
        self.Toplevel.withdraw()

    def turnOnWindow(self):
        '''
        Примечание:
        Данный метод разворачивает окно из свернутого
        состояния(ф-я turnOffWindow), а также помимо этого он применим к ф-ии
        deleteWindow(удаление окна) - т.е., помимо "развёртывания"
        окна из свернутого состояния, с помощью этого метода можно
        создать заново удаленное окно, которое было удалено с помощью ф-ии
        deleteWindow.
        '''
        self.Toplevel.deiconify()

    def makeWindowState(self, state='normal'):
        '''
        Примечание:
        Данный метод устанавливает "статус" окна.
        Статусов у окна может быть четыре:
        1. свернутое окно(окно сворачивается(мгновенно)/открывается в панеле задачь windows):
           state='iconic'
        2. удаленное окно(окно полностью исчезает с экрана): state='withdrawn'
        3. распахнутое на весь экран окно: state='zoomed'
        4. окно с заданными(программистом) настройками,
           либо если настройки не заданы, то с настройками по умолчанию:
           state='normal'
        '''
        self.Toplevel.state(state)

    def raiseWindow(self):
        '''
        Примечание:
        Данный метод поднимает окно вверх на экране монитора, относительно
        других окон.
        '''
        self.Toplevel.lift()

    def putdownWindow(self):
        '''
        Примечание:
        Данный метод опускает окно вниз на экране монитора, относительно
        других окон.
        '''
        self.Toplevel.lower()

    def setWindowFocus(self):
        '''
        Примечание:
        Данный метод устанавливает фокус на окно - таким образом, делая его
        активным(выбранным).
        '''
        self.Toplevel.focus_set()

    def setWindowGrab(self):
        '''
        Примечание:
        Данный метод запрещает доступ к другим окнам, пока открыто данное окно.
        '''
        self.Toplevel.grab_set()

    def waitWindowDestroy(self):
        '''
        Примечание:
        Данный метод заставляет ждать, пока окно не будет уничтожено(закрыто) и
        до этого момента не позволяет закрывать другие окна, хотя и предоставляет
        к ним доступ, в отличие от setWindowGrab.
        '''
        self.Toplevel.wait_window()


class AddFrame(Frame):
    def __init__(self, parent=None):
        '''
        parent = Root.root
        parent = Win1.Toplevel
        '''
        self.parent = parent
        self.makeFrame()

    def makeFrame(self):
        Frame.__init__(self, self.parent)

    def closeall(self):
        '''
        Данный метод должен был служить в качестве аналога Frame.master.atr() из
        библиотеки tkinter. Но смысла делать обращение к quit через Frame, я на
        данный момент не вижу. Моя библиотека обладает достаточной гибкостью,
        чтобы считать этот прием излишним.
        '''
        pass

    def getAccessToUpLevelWinOrRoot(self):
        '''
        Примечание:
        Данный метод должен был служить в качестве аналога self.master.attr() из
        библиотеки tkinter. Но смысла я в нем не вижу, т.к. за счет того что мы
        указываем все атрибуты всех классов в __init__, мы можем обращаться к
        ним напрямую, что делает мою систему более гибкой.
        Например:
        1. Frame.master.title('Spam')
        2. # вместо этого мы просто можем писать из любого места в коде:
        3. Root.title = 'Spam'
        4. Root.maketitle()
        '''
        pass


class AddLabel(Label):
    def __init__(self, parent=None):
        self.parent = parent
        self.text = 'Text'
        self.image = None
        self.bg = '#40E0D0' #цвет фона
        self.fg = '#9370DB' #цвет текста
        self.makeLabel()

    def makeLabel(self):
        Label.__init__(self, self.parent)

    def setConfig(self):
        '''
        Данный метод устанавливает настройки для Label()
        '''
        if self.text != None:
            self.config(text=self.text)
        if self.image != None:
            self.config(image=self.image)
        if self.bg != None:
            self.config(bg=self.bg)
        if self.fg != None:
            self.config(fg=self.fg)


class AddButton(Button):
    def __init__(self, parent=None):
        '''
        command=
            bound_method
            func
            lambda
            exit
            sys.exit
            master.quit
        '''
        self.parent = parent
        self.text = 'Text'
        self.command = None
        self.image = None
        self.bg = '#7B68EE' #цвет фона кнопки
        self.fg = '#B22222' #цвет текста кнопки
        self.makeButton()

    def makeButton(self):
        Button.__init__(self, self.parent)

    def setConfig(self):
        '''
        Данный метод устанавливает настройки для Button()
        '''
        if self.text != None:
            self.config(text=self.text)
        if self.command != None:
            self.config(command=self.command)
        if self.image != None:
            self.config(image=self.image)
        if self.bg != None:
            self.config(bg=self.bg)
        if self.fg != None:
            self.config(fg=self.fg)


class SetPack:
    def __init__(self, widget):
        '''
        side=
            TOP
            BOTTOM
            LEFT
            RIGHT
        expand=
            YES
        fill=
            X
            Y
            BOTH
        anchor=
            CENTER[по умолчанию]
            N
            NE
            NW
            S
            SE
            SW
            E
            W
        padx= [размер отступа(padding) по X]
        pady= [размер отступа(padding) по Y]
        '''
        pass

    def setPack(self):
        self.side = ''
        self.expand = ''
        self.fill = ''
        self.anchor = None
        self.padx = None
        self.pady = None
        if anchor == None:
            self.pack(side=self.side,
                      expand=self.expand,
                      fill=self.fill,
                      padx=self.padx,
                      pady=self.pady)


if __name__ == '__main__':

    def rootConfig():
        #Root.addMenu(menu)
        Root.maketitle()
        Root.windowCloseClick()
        Root.makeicon()
        Root.returnScreenSize()
        Root.makeWindowSizeAndScreenPosition()
        #Root.turnOffWindow()
        #Root.deleteWindow()
        #Root.turnOnWindow()
        Root.makeWindowState()
        #Root.raiseWindow()
        #Root.putdownWindow()

    def winConfig():
        #Win1.addMenu(menu)
        Win1.maketitle()
        #Win1.closewin()
        Win1.windowCloseClick()
        Win1.makeicon()
        Win1.returnScreenSize()
        #Win1.makeWindowSizeAndScreenPosition()
        #Win1.turnOffWindow()
        #Win1.deleteWindow()
        #Win1.turnOnWindow()
        Win1.makeWindowState(state='normal')
        #Win1.raiseWindow()
        #Win1.putdownWindow()
        #Win1.setWindowFocus()
        #Win1.setWindowGrab()
        #Win1.waitWindowDestroy()

    def frameConfig():
        #Frame1.closeall()
        #Frame1.getAccessToUpLevelWinOrRoot()
        SetPack(Frame1)
        SetPack(Frame2)
        SetPack(Frame3)

    def labelConfig():
        Label1.text = 'Label text'
        Label1.bg = '#00CED1'
        Label1.setConfig()
        SetPack(Label1)

    def buttonConfig():
        Button1.setConfig()

    #NoDefaultRoot()
    '''
    tkinter.NoDefaultRoot()
    дает возможность создавать несколько(любое кол-во) КОРНЕВЫХ окно,
    вместо одного - как это определено по умолчанию.
    '''
    Root = StartMakingRoot()
    rootConfig()
    Win1 = AddWin()
    winConfig()
    #Win2 = Win()
    #Win2.maketitle()
    Frame1 = AddFrame(parent=Root.root)
    Frame2 = AddFrame(parent=Win1.Toplevel)
    Frame3 = AddFrame(parent=Win1.Toplevel)
    frameConfig()
    Label1 = AddLabel(parent=Frame1)
    labelConfig()
    Button1 = AddButton(parent=Frame1)
    buttonConfig()
    Root.endMakingRoot()

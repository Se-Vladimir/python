from tkinter import *
from exit_save_changes import ExitSaveChanges
import random
import pickle


class Words:
    def makeSomeOperations(self):
        self.right_answers = {self.test_word1: self.ans_word1,
                              self.test_word2: self.ans_word2,
                              self.test_word3: self.ans_word3,
                              self.test_word4: self.ans_word4,
                              self.test_word5: self.ans_word5}

        self.right_answers_rus = {self.ans_word1: self.test_word1,
                                  self.ans_word2: self.test_word2,
                                  self.ans_word3: self.test_word3,
                                  self.ans_word4: self.test_word4,
                                  self.ans_word5: self.test_word5}

        self.words = [self.word1, self.word2, self.word3, self.word4, self.word5]
        self.words_copy = self.words[:]
        self.test_words = [self.test_word1, self.test_word2, self.test_word3,
                           self.test_word4, self.test_word5]
        self.test_words_copy = self.test_words[:]
        self.ans_words = [self.ans_word1, self.ans_word2, self.ans_word3,
                          self.ans_word4, self.ans_word5]
        self.ans_words_copy = self.ans_words[:]

    def countProgressCheck(self, func):
        if func not in self.count_progress:
            self.count_progress.append(func)
        else: pass

    def words1(self):
        self.countProgressCheck(self.words1)

        self.word1 = "abandon [əˈbandən] отказаться"
        self.word2 = "baby [ˈbābē] ребенок"
        self.word3 = "cab [kab] такси"
        self.word4 = "dad, daddy [dad, dadi] папа, папочка"
        self.word5 = "each [ēCH] каждый"

        self.test_word1 = "отказаться"
        self.test_word2 = "ребенок"
        self.test_word3 = "такси"
        self.test_word4 = "папа, папочка"
        self.test_word5 = "каждый"

        self.ans_word1 = "abandon"
        self.ans_word2 = "baby"
        self.ans_word3 = "cab"
        self.ans_word4 = "dad, daddy"
        self.ans_word5 = "each"

        self.makeSomeOperations()

        self.makeWords()

    def words2(self):
        self.countProgressCheck(self.words1)

        self.word1 = "ability [əˈbilədē] способность"
        self.word2 = "able [ˈābəl] способный"
        self.word3 = "abnormal [abˈnôrməl] ненормальный"
        self.word4 = "aboard [əˈbôrd] на борту"
        self.word5 = "abolish [əˈbäliSH] отменять"

        self.test_word1 = "способность"
        self.test_word2 = "способный"
        self.test_word3 = "ненормальный"
        self.test_word4 = "на борту"
        self.test_word5 = "отменять"

        self.ans_word1 = "ability"
        self.ans_word2 = "able"
        self.ans_word3 = "abnormal"
        self.ans_word4 = "aboard"
        self.ans_word5 = "abolish"

        self.makeSomeOperations()

        self.makeWords()

    def makeWords(self):
        self.word = random.choice(self.words)
        self.Word = self.Canvas1.create_text(225, 80, text=self.word, font=self.font)
        self.words.remove(self.word)

    def nextWord(self):
        self.Canvas1.delete(self.Word)
        if len(self.words) == 0:
            self.words = self.words_copy[:]
            #print(self.test_words)
            self.test(self.text4, self.test_words)
        else:
            self.makeWords()

    def test(self, text, source):
        for wid in (self.Text3, self.canv_window1):
            self.Canvas1.delete(wid)

        self.Text4 = self.Canvas1.create_text(225, 50, text=text, font=self.font)

        for wid in self.downpage_wids:
            if wid == self.Entry1:
                wid.pack(side=LEFT, padx=10, pady=10)
            else: wid.pack(side=LEFT)

        #print(source)
        self.source = source
        #print(self.source)
        self.source_copy = self.source[:]
        self.makeTests()

    def makeTests(self):
        try:
            self.test_word = random.choice(self.source)
        except IndexError:
            pass
        else:
            #print(self.source)
            self.test_Word = self.Canvas1.create_text(225, 80, text=self.test_word, font=self.font)
        #self.test_words.remove(self.test_word) # !!!

    def nextTest(self):
        self.Canvas1.delete(self.test_Word)
        if len(self.source) == 0:
            self.Canvas1.delete(self.Text4)
            self.source = self.source_copy[:]
            if len(self.ans_words) == 0:
                self.ans_words = self.source_copy[:]
            #print('self.source:', self.source)
            #print('ans_words:', self.ans_words)
            for wid in self.downpage_wids:
                wid.pack_forget()
            self.afterTest()
        else:
            self.checkTest()

    def checkTest(self):
        if self.source == self.ans_words:
            self.source_answers = self.right_answers_rus
        else: self.source_answers = self.right_answers

        self.right_answer = self.source_answers[self.test_word]

        self.user_answer = self.Entry1.get()
        self.Entry1.delete(0, END)

        if self.user_answer == self.right_answer:
            pass
        else:
            for word in self.words:
                if self.right_answer in word:
                    self.wrong_answers.append(word)
                    break

        self.source.remove(self.test_word)
        if len(self.source) == 0:
            self.nextTest()
        else: self.makeTests()

    def afterTest(self):
        if len(self.wrong_answers) > 0:
            self.count_afterTest = 0
            self.Text5 = self.Canvas1.create_text(225, 50, text=self.text5, font=self.font)
            self.Canvas1.after(2000, self.badResult)
        else:
            #print(self.count_afterTest)
            if self.count_afterTest == 1:
                self.nextLevel()
            else:
                self.count_afterTest = 1
                self.test('A теперь на русском)', self.ans_words)

    def badResult(self):
        self.Canvas1.delete(self.Text5)

        self.Text7 = self.Canvas1.create_text(225, 50, text=self.text7, font=self.font)
        self.Canvas1.after(2000, self.badResult2)

    def badResult2(self):
        self.Canvas1.delete(self.Text7)

        self.mistakesWork()

        self.Button2_pack(self.nextMistake)

    def nextMistake(self):
        self.Canvas1.delete(self.mistake_Word)

        if len(self.wrong_answers) > 0:
            #print(self.wrong_answers)
            self.mistakesWork()
        else:
            self.Canvas1.delete(self.canv_window1)

            self.Text3 = self.Canvas1.create_text(225, 50, text=self.text3, font=self.font)
            self.Button2_pack(self.nextWord)

            self.count_progress[-1]()

    def mistakesWork(self):
        self.mistake_word = random.choice(self.wrong_answers)
        self.mistake_Word = self.Canvas1.create_text(225, 80, text=self.mistake_word, font=self.font)
        self.wrong_answers.remove(self.mistake_word)

    def nextLevel(self):
        self.count_afterTest = 0

        self.Text6 = self.Canvas1.create_text(225, 50, text=self.text6, font=self.font)
        self.Level += 1
        self.Level_Up(self.Level)
        self.Canvas1.after(2000, self.goodResult)

    def goodResult(self):
        self.Canvas1.delete(self.Text6)

        self.Text3 = self.Canvas1.create_text(225, 50, text=self.text3, font=self.font)
        self.Button2_pack(self.nextWord)

        if len(self.count_progress) == 1:
            self.words2()


class Prog(Words):
    def __init__(self):
        self.start_count = 0
        self.count_progress = []
        self.count_afterTest = 0
        self.Level = 0
        self.Text_Level = 'Deleted'

        self.wrong_answers = []
        self.source = []

        self.font = ('helvetica', 15)
        self.text1 = 'Это программа по изучению слов английского языка.'
        self.text2 = 'Нажмите "File - Start", чтобы начать.'
        self.text3 = 'Запомните следующее слово:'
        self.text4 = 'A теперь тест :)'
        self.text5 = 'Были ошибки. Давайте попробуем еще раз)'
        self.text6 = 'Вы отлично справились! +1 к Уровню.'
        self.text7 = 'Запомните следующие слова:'

        self.root = Tk()
        self.root.state('zoomed')
        self.root.protocol('WM_DELETE_WINDOW', self.deleteWindow)

        # Menu

        WindowMenu = Menu(self.root)
        self.root.config(menu=WindowMenu)

        MenuButton1 = Menu(WindowMenu, tearoff=False)
        MenuButton1.add_command(label='New', command=self.startDropMenuButton)
        MenuButton1.add_command(label='Load', command=self.loadLevel)
        MenuButton1.add_separator()
        MenuButton1.add_command(label='Exit', command=self.deleteWindow)

        WindowMenu.add_cascade(label='File', menu=MenuButton1)

        # uppage_widgets

        frm1 = Frame(self.root)
        frm1.pack(side=TOP, expand=YES, fill=BOTH)
        self.Canvas1 = Canvas(frm1)
        self.Canvas1.config(bg='beige')
        self.Canvas1.pack(expand=YES, fill=BOTH)

        # downpage_widgets

        frm2 = Frame(self.root)
        frm2.pack(side=BOTTOM, fill=X)
        self.Label1 = Label(frm2)
        self.Label1.config(text='Введите перевод слова в поле:', font=self.font)
        self.Label1.pack(side=LEFT)

        self.Entry1 = Entry(frm2)
        self.Entry1.config(width=25, font=self.font)
        self.Entry1.bind('<Return>', self.nextTest)
        self.Entry1.pack(side=LEFT, padx=10, pady=10)

        self.Button1 = Button(frm2)
        self.Button1.config(text='Ввод', font=self.font, command=self.nextTest)
        self.Button1.pack(side=LEFT)

        self.downpage_wids = (self.Label1, self.Entry1, self.Button1)

        for wid in self.downpage_wids:
            wid.pack_forget()

        # operations with Canvas

        self.Text1 = self.Canvas1.create_text(300, 50, text=self.text1, font=self.font)
        self.Text2 = self.Canvas1.create_text(225, 80, text=self.text2, font=self.font)

        self.start_text = (self.Text1, self.Text2)

        self.root.mainloop()

    def startDropMenuButton(self):
        self.start_count += 1

        if self.start_count > 1:
            pass
        else:
            for text in self.start_text:
                self.Canvas1.delete(text)

            self.Level_Up(self.Level)

            self.Text3 = self.Canvas1.create_text(225, 50, text=self.text3, font=self.font)
            self.Button2_pack(self.nextWord)

            self.words1()


    def Button2_pack(self, func):
        self.Button2 = Button(self.Canvas1, text='Далее', font=self.font,
                              command=func)
        self.Button2.pack()
        self.canv_window1 = self.Canvas1.create_window(225, 130, window=self.Button2)

    def Level_Up(self, cur_level):
        self.text_level = 'Your level: %s' % str(cur_level)

        if self.Text_Level != 'Deleted':
            self.Canvas1.delete(self.Text_Level)
            self.Text_Level = self.Canvas1.create_text(1000, 50, text=self.text_level, font=self.font)

        elif self.Text_Level == 'Deleted':
            self.Text_Level = self.Canvas1.create_text(1000, 50, text=self.text_level, font=self.font)

    def Level_Widforget(self):
        self.Canvas1.delete(self.Text_Level)
        self.Text_Level == 'Deleted'

    def deleteWindow(self):
        Exit.run()
        if Exit.result:
            f = open('save', 'wb')
            pickle.dump(self.Level, f)
            f.close()
        self.root.quit()

    def loadLevel(self):
        try:
            f = open('save', 'rb')
        except FileNotFoundError:
            print('Not found!')
        else:
            self.Level = pickle.load(f)
            f.close()


if __name__ == '__main__':
    Exit = ExitSaveChanges(exit_text='Save Your Level before exit?')
    Prog()

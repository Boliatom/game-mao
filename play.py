import pyglet
import tkinter as tk

from winsound import *
import pygame
win = tk.Tk()

win.iconphoto(False, tk.PhotoImage(file="icon.png"))


mus = pyglet.resource.media("sound/music.mp3")
mus.play()


win.title('mya')
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# win.geometry(f'{screen_width}x{screen_height}+0+0')

win.state('zoomed')
win['bg'] = 'black'

def update(index):
    if index > 5:
        index = 0
    label.configure(image=frames[index])
    win.after(180, update, index + 1)

frame1 = tk.PhotoImage(file='menu3/frame_00_delay-0.12s.gif').zoom(2,2)
frame2 = tk.PhotoImage(file='menu3/frame_01_delay-0.12s.gif').zoom(2,2)
frame3 = tk.PhotoImage(file='menu3/frame_02_delay-0.12s.gif').zoom(2,2)
frame4 = tk.PhotoImage(file='menu3/frame_03_delay-0.12s.gif').zoom(2,2)
frame5 = tk.PhotoImage(file='menu3/frame_04_delay-0.12s.gif').zoom(2,2)
frame6 = tk.PhotoImage(file='menu3/frame_05_delay-0.12s.gif').zoom(2,2)
frame7 = tk.PhotoImage(file='menu3/frame_06_delay-0.12s.gif').zoom(2,2)
frame8 = tk.PhotoImage(file='menu3/frame_07_delay-0.12s.gif').zoom(2,2)
frame9 = tk.PhotoImage(file='menu3/frame_08_delay-0.12s.gif').zoom(2,2)
frame10 = tk.PhotoImage(file='menu3/frame_09_delay-0.12s.gif').zoom(2,2)
frame11 = tk.PhotoImage(file='menu3/frame_10_delay-0.12s.gif').zoom(2,2)
frame12 = tk.PhotoImage(file='menu3/frame_11_delay-0.12s.gif').zoom(2,2)
frame13 = tk.PhotoImage(file='menu3/frame_12_delay-0.12s.gif').zoom(2,2)
frame14 = tk.PhotoImage(file='menu3/frame_13_delay-0.12s.gif').zoom(2,2)
frame15 = tk.PhotoImage(file='menu3/frame_14_delay-0.12s.gif').zoom(2,2)
frame16 = tk.PhotoImage(file='menu3/frame_15_delay-0.12s.gif').zoom(2,2)
frames = [frame1, frame2, frame3, frame4, frame5, frame6,frame7, frame8, frame9, frame10, frame11, frame12,frame13, frame14, frame15, frame16]

label = tk.Label(win, width=1000, borderwidth=0)
label.pack(pady=125)
update(0)


class Playsound:
    pass
    command = lambda: Playsound("sound/music.mp3", SND_FILENAME)




def switch_windows():
    win.withdraw()
    pygame.init()
    win2 = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("meo")
    icon_image = pygame.image.load("icon.png")
    pygame.display.set_icon(icon_image)
    a = 0
    b = 0
    c = 0
    v = 0
    q = 0
    def prolog(c):
        prolog1 = ['Куда направляешься?', 'Тебе нечего тут делать',
                   'У тебя есть шанс уйти, просто нажми [ESC]', 'Эй, почему ты не уходишь?', 'Стой, стой, стой','Возможно,ты меня не понял, но тебе правда лучше уйти',
                   '...','Тебе не понравится тут..', 'Даю последний шанс',
                   'Ладно, я понял тебя',
                   'Тогда...(нажмите [C]- чтобы включить свет)']

        win2.fill('black')
        pygame.display.update()
        f1 = pygame.font.SysFont('Segoe print', 30)
        if type(prolog1[c]) == str:
            tx3 = f1.render(prolog1[c], True, (255,250,240))
            win2.blit(tx3, (400, 500))

        else:
            tx3 = f1.render(prolog1[c][0], True, (255,250,240))
            win2.blit(tx3, (400, 500))
        pygame.display.update()

        c += 1
        return c


    def dialog2(b):
        prolog3 = [('Думаю, так и вправду лучше','(теперь для продолжения нажмите на [E])'), 'Нравится?', 'Смотри, на меня похож',
                   ('Ну прям вылитый я, такой же милый и прищуренный,','только белого цвета'), ('Думаю, побуду с ним чуть подольше','(нажмите на [ESC] для выхода)') ]
        win2.fill('black')
        pin2 = pygame.image.load('cute.png')
        win2.blit(pin2, (590, 170))
        sl_2 = pygame.image.load('sl_2.png')
        win2.blit(sl_2, (800, 270))
        pygame.display.update()
        pygame.time.delay(1000)
        font2 = pygame.font.SysFont('Segoe print', 17)
        font3 = pygame.font.SysFont('Adobe Gothic Std', 40)
        spc4 = font2.render('НАЖМИТЕ [E] - чтобы продолжить', True, (255, 250, 240))
        win2.blit(spc4, (1517, 960))
        spc5 = font3.render('---------------------------------------------', True, ('red'))
        win2.blit(spc5, (1505, 1005))
        f5 = pygame.font.SysFont('Segoe print', 30)

        if type(prolog3[b]) == str:
            tx3 = f5.render(prolog3[b], True, (255, 250, 240))
            win2.blit(tx3, (575, 900))
        elif len(prolog3[b]) == 2:
            text3 = f5.render(prolog3[b][0], True, (255, 250, 240))
            win2.blit(text3, (575, 900))
            text3 = f5.render(prolog3[b][1], True, (255, 250, 240))
            win2.blit(text3, (570, 950))
        elif len(prolog3[b]) == 3:
            text3 = f5.render(prolog3[b][0], True, (255, 250, 240))
            win2.blit(text3, (570, 950))
            text3 = f5.render(prolog3[b][1], True, (255, 250, 240))
            win2.blit(text3, (570, 950))
            text3 = f5.render(prolog3[b][2], True, (255, 250, 240))
            win2.blit(text3, (570, 1000))
        else:
            tx3 = f5.render(prolog3[b][0], True, (255, 250, 240))
            win2.blit(tx3, (570, 900))
        pygame.display.update()
        b += 1
        return b

    def dialog(a):
        prolog2 = ['БУ (теперь для продолжения нажмите на [C])', ('А я тебя предупреждал.','У тебя всё еще есть выбор выйти (нажмите на [ESC] для выхода)'),
                   '...', 'Ладно, твоё дело',
                   ('Тут мрачновато немного, но лично меня всё устраивает.', 'Со временем привыкаешь к данной обстановке'),
                   '...', 'Я вижу по твоему лицу, что тебе не нравится...', 'Боже, не смотри так',
                   ('Ладно-Ладно, могу сменить фон на что то "более привлекательное",',' но на что не скажу'),
                   ('Выбор за тобой:',' [E] - сменить картинку','[C]- оставить всё как есть'), 'Удивительно, ты решил оставить такую жутковатую картину...',
                   'Правда не хочешь?',
                   ('Даю последний шанс',' [E] - сменить картинку','[C]- оставить всё как есть'),'Ну ладно, мне не столь важно (нажмите на [ESC] для выхода)']

        win2.fill('black')
        pin1 = pygame.image.load('pin1.png')
        win2.blit(pin1, (590, 170))
        sl_1 = pygame.image.load('sl_1.png')
        win2.blit(sl_1, (590, 170))
        pygame.display.update()
        pygame.time.delay(1000)
        font2 = pygame.font.SysFont('Segoe print', 17)
        font3 = pygame.font.SysFont('Adobe Gothic Std', 40)
        spc = font2.render('НАЖМИТЕ [C] - чтобы продолжить', True, (255, 250, 240))
        win2.blit(spc, (1517,960))
        spc1 = font3.render('---------------------------------------------', True, ('red'))
        win2.blit(spc1, (1505,1005))
        f1 = pygame.font.SysFont('Segoe print', 30)


        if type(prolog2[a]) == str:
            tx3 = f1.render(prolog2[a], True, (255, 250, 240))
            win2.blit(tx3, (560, 800))
        elif len(prolog2[a]) == 2:
            text3 = f1.render(prolog2[a][0], True, (255, 250, 240))
            win2.blit(text3, (560, 800))
            text3 = f1.render(prolog2[a][1], True, (255, 250, 240))
            win2.blit(text3, (555, 850))
        elif len(prolog2[a]) == 3:
            text3 = f1.render(prolog2[a][0], True, (255, 250, 240))
            win2.blit(text3, (555, 800))
            text3 = f1.render(prolog2[a][1], True, (255, 250, 240))
            win2.blit(text3, (555, 850))
            text3 = f1.render(prolog2[a][2], True, (255, 250, 240))
            win2.blit(text3, (555, 900))
        else:
            tx3 = f1.render(prolog2[a][0], True, (255, 250, 240))
            win2.blit(tx3, (600, 800))
        pygame.display.update()

        a += 1
        return a
    def pasxalka(v):
        win2.fill('black')
        pas1 = [('Ой','(теперь для продолжения нажмите на [B])'), '(нажмите на [ESC] для выхода)']
        pasxalka1 = pygame.image.load('pasxalka.jpg')
        win2.blit(pasxalka1, (590, 170))
        font2 = pygame.font.SysFont('Segoe print', 17)
        font3 = pygame.font.SysFont('Adobe Gothic Std', 40)
        spc4 = font2.render('НАЖМИТЕ [B] - чтобы продолжить', True, (255, 250, 240))
        win2.blit(spc4, (1517, 960))
        spc5 = font3.render('---------------------------------------------', True, ('red'))
        win2.blit(spc5, (1505, 1005))
        f1 = pygame.font.SysFont('Segoe print', 30)
        if type(pas1[v]) == str:
            tx3 = f1.render(pas1[v], True, (255, 250, 240))
            win2.blit(tx3, (560, 800))
        elif len(pas1[v]) == 2:
            text3 = f1.render(pas1[v][0], True, (255, 250, 240))
            win2.blit(text3, (560, 800))
            text3 = f1.render(pas1[v][1], True, (255, 250, 240))
            win2.blit(text3, (555, 850))
        elif len(pas1[v]) == 3:
            text3 = f1.render(pas1[v][0], True, (255, 250, 240))
            win2.blit(text3, (555, 800))
            text3 = f1.render(pas1[v][1], True, (255, 250, 240))
            win2.blit(text3, (555, 850))
            text3 = f1.render(pas1[v][2], True, (255, 250, 240))
            win2.blit(text3, (555, 900))
        else:
            tx3 = f1.render(pas1[v][0], True, (255, 250, 240))
            win2.blit(tx3, (600, 800))
        pygame.display.update()

        v += 1
        return v

    def dialog4(q):
        pin1 = pygame.image.load('pin1.png')
        win2.blit(pin1, (590, 170))
        sl_1 = pygame.image.load('sl_1.png')
        win2.blit(sl_1, (590, 170))
        pygame.display.update()
        i = { 'Неизвестная аномалия' : ' Вы не знаете эту аномалию'}
        f3 = pygame.font.SysFont('Segoe print', 20)
        text3 = f3.render('Неизвестная аномалия' + ' - ' + i.get('Неизвестная аномалия'), True, (255, 250, 240))
        win2.blit(text3, (600, 750))
        q += 1
        return q
    while True:

        font1 = pygame.font.SysFont('Segoe print', 17)
        spc =  font1.render('НАЖМИТЕ [SPACE] - чтобы продолжить', True, (255,250,240))
        win2.blit(spc,(1517,1000))
        esc = font1.render('НАЖМИТЕ [ESC] - чтобы выйти', True, (255, 250, 240))
        win2.blit(esc, (1517, 1040))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_SPACE:
                    win2.fill('black')
                    pygame.display.update()
                    c = prolog(c)
                elif event.key == pygame.K_c:
                    pygame.time.delay(200)
                    win2.fill('black')

                    pygame.display.update()
                    a = dialog(a)
                elif event.key == pygame.K_e:
                    pygame.time.delay(200)
                    win2.fill('black')

                    pygame.display.update()
                    b = dialog2(b)
                elif event.key == pygame.K_b:
                    pygame.time.delay(200)
                    win2.fill('black')

                    pygame.display.update()
                    v = pasxalka(v)
                elif event.key == pygame.K_z:
                    q = dialog4(q)


        pygame.display.update()





btn1 = tk.Button(win,
                 text='НАЧАТЬ ИГРУ',
                 width=15,
                 borderwidth=0,
                 background="#8B2500",
                 activebackground='#d7704b',
                 relief="flat",
                 font=('Segoe print', 25),
                 command= switch_windows)

btn1.place(relx=0.42, rely=0.45)


win.mainloop()
pyglet.app.run()



switch_windows()






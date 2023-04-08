from tkinter import *
import tkinter.font
import tkinter.messagebox as msgbox
import time
import os
root = Tk()
root.geometry("500x200")
root.title("Minecraft Regedit tweaker - by Kidon")
ReachCheck=tkinter.IntVar()
KBCheck=tkinter.IntVar()
ComboCheck=tkinter.IntVar()

def Ok_Pressed():
    global ReachCheck,KBCheck,ComboCheck
    time.sleep(2)
    if (ReachCheck.get() == True):
        print("Reach")
        os.system("regedit.exe /s \"%temp%\\OPReach.reg\"")

    if (KBCheck.get() == True):
        print("KB")
        os.system("regedit.exe /s \"%temp%\\NoKB.reg\"")

    if (ComboCheck.get() == True):
        print("Combo")
        os.system("regedit.exe /s \"%temp%\\BIGLatency.reg\"")

    msgbox.showinfo("완료!","적용되었습니다. 컴퓨터를 껐다 키는걸 추천드립니다.")
    root.destroy()


os.system("curl https://raw.githubusercontent.com/BAtchfiler0/-/main/Auto%20Reg%20%231%20No%20KB.reg>\"%temp%\\NoKB.reg\"")
os.system("curl https://raw.githubusercontent.com/BAtchfiler0/-/main/Auto%20Reg%20%232%20OP%20Reach.reg>\"%temp%\\OPReach.reg\"")
os.system("curl https://raw.githubusercontent.com/BAtchfiler0/-/main/Auto%20Reg%20%233%20BIG%20Latency.reg>\"%temp%\\BIGLantency.reg\"")

font=tkinter.font.Font(family="맑은 고딕", size=20)

Regedit = Label(root, text="Minecraft Regedit tweaker!", font=font)

Regedit.pack()
ck1 = Checkbutton(root, text="Increase Reach 리치 증가", variable=ReachCheck)
ck1.pack()
ck2 = Checkbutton(root, text="Reduce Knockback 넉백 감소", variable=KBCheck)
ck2.pack()
ck3 = Checkbutton(root, text="Smooth Combo 콤보율 상승", variable=ComboCheck)
ck3.pack()
okbtn = Button(root, text="적용", command=Ok_Pressed)
okbtn.pack()

root.mainloop()
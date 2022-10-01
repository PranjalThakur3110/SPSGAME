from ast import Global, Lambda
from cProfile import label
from email.policy import strict
from gc import freeze
from importlib.metadata import files
from logging import root
from multiprocessing.pool import TERMINATE
from random import Random
from textwrap import fill, wrap
import textwrap
from tkinter import *
from tkinter import font
from tkinter.tix import COLUMN
from turtle import color, st
from PIL import ImageTk,Image
import random
from tkinter import messagebox



#MAKING THE MAIN WINDOW HERE
root=Tk()
root.title('SPSGAME')
root.iconbitmap('icon.ico')
root.config(bg="white")
root.attributes('-fullscreen',True)




# MAKING FRAME FOR PLAYERINFO
frame_player=LabelFrame(root,text="USER`S INFO",padx=20,bg="light pink",relief='raised',font=("",20))
frame_player.grid(row=0,column=0,padx=10,pady=10,ipadx=80,sticky=W)

# MAKING FRAME FOR GAME BUTTONS
frame_btn= LabelFrame(root,text="Stone Paper Scissors Game",padx=20,bg="light pink",relief='raised',font=("",20))
frame_btn.grid(row=1,column=0,padx=20,pady=10)

#MAKING FRAME FOR SCORES OF THE GAME
frame_score=LabelFrame(root,text="Your Score",padx=200,bg="light pink",relief='raised',font=("",20))
frame_score.grid(row=1,column=1,padx=10,pady=10,sticky=N,columnspan=2)
img_score=Image.open('score.jpg').resize((200,100))
score_img=ImageTk.PhotoImage(img_score)
scoreimg_label=Label(frame_score,image=score_img).grid(row=0,column=0)



#PLAYER INFORMATION HERE
player_name=Label(frame_player,text="Pranjal Thakur",bd=1,bg="light pink",padx=0,pady=1,font=("",10))
player_name.grid(row=0,column=0,columnspan=2,ipadx=10,sticky=W)



#DECLARING VARIABLES FOR SCOPE
label1=Label(frame_btn)
status=Label(frame_btn)
score=0
scorelabel=Label(frame_score)
scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
scorelabel.grid(row=1,column=0,padx=30,pady=10)


def Game(player):

    #1 FOR STONE
    #2 FOR PAPER
    #3 FOR SCISSORS
    global label1
    global status
    global score
    global scorelabel

    sample = [1,2,3]
    msg = ""
    st=""
    com=random.choice(sample)
    if player==1 and com==1: 
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        msg="MATCH DRAWN"
        st="You both chose Stone"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10)
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1,)
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)

        
        
        
    elif player==2 and com==2:
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        msg="MATCH DRAWN"
        st="You both chose Paper"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10)
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1)
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)

        


    elif player==3 and com==3:
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        msg="MATCH DRAWN"
        st="You both chose Scissors"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10)
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1)
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)


        
    elif player==1 and com==2:
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        score=score-1
        msg="YOU LOSE"
        st="You chose Stone and Computer chose Paper"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10)
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1)
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)

        
    
    
    elif  player==1 and com==3:
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        score=score+2
        msg="YOU WIN"
        st="You chose Stone and Computer chose Scissors"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10)
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1) 
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)

        

    elif player==2 and com==1:
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        score=score+2
        msg="YOU WIN"
        st="You chose Paper and Computer chose Stone"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10)
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1)
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)

    
    elif player==2 and com==3:
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        score=score-1
        msg="YOU LOSE"
        st="You chose Paper and Computer chose Scissors"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10)
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1)
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)

        
    elif player==3 and com==1:
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        score=score-1
        msg="YOU LOSE"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10)
        st="You chose Scissors and Computer chose Stone"
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1)
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)

    
    elif player==3 and com==2:
        label1.destroy()
        status.destroy()
        scorelabel.destroy()
        score=score+2
        msg="YOU WIN"
        label1=Label(frame_btn,text=msg,bg="light pink",font=("",10))
        label1.grid(row=1,column=1,padx=10,pady=10) 
        st="You chose Scissors and Computer chose Paper" 
        status= Label(frame_btn, text=st,bg="light pink",font=("",10),anchor=CENTER)
        status.grid(row=2,column=1)
        scorelabel=Label(frame_score,text=score,bg="light pink",relief='flat',font=("",50))
        scorelabel.grid(row=1,column=0,padx=10,pady=10, columnspan=3)

        





#TAKING IMAGE AND MAKING BUTTON FOR STONE 
img_st=Image.open('rock.jpg').resize((200,200))
st_img=ImageTk.PhotoImage(img_st)
button_st= Button(frame_btn,image=st_img,borderwidth=2,bg="white",command=lambda: Game(1),relief="raised").grid(row=0,column=0,padx=30,pady=10)


#TAKING IMAGE AND MAKING BYUTTON FOR PAPER
img_paper= Image.open('paper.jpg').resize((200,200),Image.ANTIALIAS)
paper_img=ImageTk.PhotoImage(img_paper)
button_paper=Button(frame_btn,image=paper_img,borderwidth=2,bg="white",command=lambda: Game(2),relief="raised").grid(row=0,column=1,padx=30,pady=10)


#TAKING IMAGE AND MAKING BUTTON FOR SCISSORS
img_sci=Image.open('scissors.jpg').resize((200,200),Image.ANTIALIAS)
sci_img=ImageTk.PhotoImage(img_sci)
button_scissors=Button(frame_btn,image=sci_img,borderwidth=2,bg="white",command=lambda: Game(3),relief="raised").grid(row=0,column=3,padx=30,pady=10)






#EXIT BUTTON FUNCTION
def Terminate():
    decision=messagebox.askyesno("ATTENTION!!!","ARE YOU SURE YOU WANT TO EXIT?")
    if decision==1:
        root.destroy()

#EXIT BUTTON HERE
button_exit= Button(frame_btn,text='EXIT', command=Terminate,bg="red",fg="white", padx=20,pady=10,font="lucida")
button_exit.grid(row=3,column=1,ipadx=10,sticky=S)


root.mainloop()









## different types of message boxes=== showinfo,showwaring,showerror,askokcancel,askyesno,askquestion
##IMPORT FILEDIALOG FROM TKINTER TO MAKE DIALOG BOXES AND IMPORT OTHER FILES IN THE PROJECT
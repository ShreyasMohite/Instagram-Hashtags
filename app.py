from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox


class Tags:
    def __init__(self,root):
        self.root=root
        self.root.title("Instagram HashTags")
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        p=PhotoImage(file="hash.png")
        self.root.iconphoto(False,p)


        tags=StringVar()


        def on_enter1(e):
            but_tag['background']="black"
            but_tag['foreground']="cyan"  
        def on_leave1(e):
            but_tag['background']="SystemButtonFace"
            but_tag['foreground']="SystemButtonText"

        def on_enter2(e):
            but_erase['background']="black"
            but_erase['foreground']="cyan"  
        def on_leave2(e):
            but_erase['background']="SystemButtonFace"
            but_erase['foreground']="SystemButtonText"



        def erase():
            text.delete('1.0',"end")
            tags.set("Select Any Tag")

        
        def gettag():
            try:
                if tags.get()=="Select Any Tag":
                    tkinter.messagebox.showerror("Error","Please Select Any tag")
                else:
                    text.delete('1.0',"end")
                    with open(f"tags/{tags.get()}.txt") as f:
                        text.insert("end",f.read()+"\t")

                    
            except Exception as e:
                print(e)




#========================frame==============================
        mainframe=Frame(self.root,width=500,height=500,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,heigh=200,relief="ridge",bd=3,bg="gray33")
        firstframe.place(x=0,y=0)


        secondframe=Frame(mainframe,width=494,heigh=295,relief="ridge",bd=3,bg="black")
        secondframe.place(x=0,y=200)



#==========================================================================================#

        select_state=["popular","amazing","animal","art","beautiful","cats","couplegoals","cute","dogs","family",\
        "fashion","file","follow","food","friendship","girls","happy","hbd","instragram","like","love","music",\
        "nature","photography","picoftheday","selfie","smile","style"]
        select_state_combo=Combobox(firstframe,values=select_state,font=('arial',14),width=23,state="readonly",justify="center",textvariable=tags)
        select_state_combo.set("Select Any Tag")
        select_state_combo.place(x=100,y=30)
         
        but_tag=Button(firstframe,width=14,text="Tags",font=('times new roman',14),cursor="hand2",command=gettag)
        but_tag.place(x=50,y=150)
        but_tag.bind("<Enter>",on_enter1)
        but_tag.bind("<Leave>",on_leave1)

        but_erase=Button(firstframe,width=14,text="Erase",font=('times new roman',14),cursor="hand2",command=erase)
        but_erase.place(x=290,y=150)
        but_erase.bind("<Enter>",on_enter2)
        but_erase.bind("<Leave>",on_leave2)


#============================================================#

        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,width=52,height=15,yscrollcommand=scol.set,font=("times new roman",13),wrap="word")
        text.place(x=0,y=0)
        scol.config(command=text.yview)



if __name__=="__main__":
    root=Tk()
    Tags(root)
    root.mainloop()
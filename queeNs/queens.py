from tkinter import *
from tkinter import messagebox as tkMessageBox
from PIL import ImageTk ,Image

root=Tk()
root.geometry("480x505")

board=[]        #store button object
queens=[]       #queenimage
res=[]          #result array main
res = [0.5 for i in range(12)]
size=StringVar()
size.set("8x8")
colors=[["#7D945D","#EEEED5","#444","#222"],
["#C18A6C","#EEEED5","#151007","#300A00"],["#4B7399","#EEEED5","#14426E","#83acd4"]]
queens.append(ImageTk.PhotoImage(Image.open ("qb.png")))
queens.append(ImageTk.PhotoImage(Image.open ("q2.png")))
queens.append(ImageTk.PhotoImage(Image.open ("q3.png")))
queens.append(ImageTk.PhotoImage(Image.open ("qw.png")))
theme,N,phase,X,Y=0,8,0,0,0


def setTheme(x):
    global phase
    global theme
    theme,phase=x,0
    for i in range(9):          #iterate through whole board to change theme
        for j in range(9):
            board[i][j].mode=0
            butColor(i,j)
    #changing background and other buttons colors
    root.config(bg=colors[theme][3])
    dropdown.config(bg=colors[theme][1])
    Classic.config(bg=colors[theme][2],fg=colors[theme][1])
    Wood.config(bg=colors[theme][2],fg=colors[theme][1])
    Aqua.config(bg=colors[theme][2],fg=colors[theme][1])

def setsize(event):
    #When we select a size from dropdown menu this funtion is
    #called and sets N and the window size of program
    global N
    if size.get()=="5x5":
        root.geometry("300x325")
        N=5
    elif size.get()=="6x6":
        root.geometry("360x385")
        N=6
    elif size.get()=="7x7":
        root.geometry("420x445")
        N=7
    elif size.get()=="8x8":
        root.geometry("480x505")
        N=8
    elif size.get()=="9x9":
        root.geometry("540x565")
        N=9
    elif size.get()=="10x10":
        root.geometry("600x625")
        N=10

def butColor(i,j):
    # this function is used to change color of buttons based
    # also make the queen icon visible or invisible(depending on mode)
    if board[i][j].mode:
        if (i+j)%2:
            board[i][j].but.config(image=queens[3])
        else:
            board[i][j].but.config(image=queens[theme])
        return
    board[i][j].but.config(bg=colors[theme][(i+j)%2])
    board[i][j].but.config(image='')

def togg(i,j):
    #when you press any square(button) on the board this fucntion called
    #this starts the algorithm or resets the board based on phase value
    global phase,X,Y
    if phase:
        setTheme(theme)
        phase=0
    else:
        if ((board[i][j]).mode==0):
            (board[i][j]).mode=1
            butColor(i,j)
        else:
            (board[i][j]).mode=0
            butColor(i,j)
        #we initialized first queen now we will call solver function
        phase,X,Y=1,i,j
        res[i]=j
        #solver function called which stores result in res[] array
        #two cases soln found and not found
        if solver(0):
            print("\n\nOne solution for N={} is".format(N))
            for i in range(N):
                print(res[i],end=' ')
                board[i][res[i]].mode=1
                butColor(i,res[i])
        else:
            print('\nNo sol')
            tkMessageBox.showinfo("Solution Not found", "{} Queens cannot be placed with this initial configuration".format(N))

def solver(row):
    if row==N:
        return True
        #traversed whole board successfully and reached Nth row which means
        #all N queens placed so soln found
    if row==X:
        return solver(row+1)
        #skip Xth row since queen already placed(starting queen pos)
    else:
        #traverse kth row to find safe position for queen
        for i in range(N):
            #initialize safe flag to true and below we check whether the posn is safe
            #if even one unsafe condition then set flag=false
            flag=True
            for p in range(1,1+row):
                #we check vertically above, diagonally left&right(updirection) 
                #if any queen is present
                if res[row-p]==i or res[row-p]==i+p or res[row-p]==i-p:
                    flag=False #queen present so unsafe so set flag=false
                    break
            if res[X]==i or res[X]==i+X-row or res[X]==i+row-X:
                #this is for checking the initially placed queen safe or not
                flag=False
            if flag:
                #safe square so we add it to result array
                res[row]=i
                if solver(row+1):
                    #recursively call solver and if the deeper iterations
                    #have a solution then return true to above iteration
                    return True
        return False    #traversed whole row didnt find safe position return false
    

class square:
    #this is the button object which contains i and j cordinates of button
    #and the button widget. it is of class square
    def __init__(self,but,i,j,mode):
        self.i=i
        self.j=j
        self.mode=mode
        self.but=Button(root,text="",width=60,height=60,borderwidth=0,relief = "flat",command=lambda: togg(self.i,self.j))
        self.but.place(x=j*60,y=25+60*i)        #cordinates of button(i,j) width and height are 60

#in the below chunk we just create the buttons and place it in the
#window with the help of grid()
root.title("N Queen")
dropdown=OptionMenu(root,size,"5x5","6x6","7x7","8x8","9x9",command=setsize)
dropdown.config(width=6,borderwidth=0,relief="flat")
Classic=Button(text="Classic",width=11,command=lambda: setTheme(0))
Wood=Button(text="Wood",width=11,command=lambda: setTheme(1))
Aqua=Button(text="Aqua",width=11,command=lambda: setTheme(2))
dropdown.grid(row=0,column=0)
Classic.grid(row=0,column=1)
Wood.grid(row=0,column=2)
Aqua.grid(row=0,column=3)

for i in range(10):
    col=[]
    for j in range(10):
        x=square(i,i,j,0)   ##Passing random value for but and color
        col.append(x)
    board.append(col)

setTheme(0)                 #initialize board theme

root.mainloop()

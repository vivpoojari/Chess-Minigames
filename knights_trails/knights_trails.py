from tkinter import *

root=Tk()
board=[]
colors=[["black","white","#444","#222"],
["black","#DDCC66","#200900","#300A00"],["#808B92","#DACABA","#607082","#EEDDD2"]]
theme=1
inputnum=0
ycoord=0
xcoord=0
ycoordend=0
xcoordend=1
xxx=0

def setTheme(x):
    global theme
    theme=x
    print("Theme is now- ",end="")
    print(theme)
    for i in range(8):
        for j in range(8):
            butColor(i,j)
    root.config(bg=colors[theme][3])
    themeLabel.config(bg=colors[theme][1])
    BW.config(bg=colors[theme][2],fg=colors[theme][1])
    Wood.config(bg=colors[theme][2],fg=colors[theme][1])
    Porc.config(bg=colors[theme][2],fg=colors[theme][1])

def butColor(i,j):
    if board[i][j].mode:
        (board[i][j]).but.config(bg="orange")
        return
    board[i][j].but.config(bg=colors[theme][(i+j)%2])

def togg(i,j):
    print("I and J are")
    print(i)
    print(j)
    global inputnum
    global xcoord
    global ycoord
    global xcoordend
    global ycoordend
    global xxx
    if inputnum==0:
        xxx=0
        ycoord=i
        xcoord=j
        inputnum=1
        print(inputnum)
    elif inputnum==1:
        ycoordend=i
        xcoordend=j
        n=64
        TheQueue = Queue()
        position=indexes(xcoord,ycoord)
        TheQueue.addtoq(position)
        dx=[1,2,2,1,-1,-2,-2,-1]
        dy=[2,1,-1,-2,-2,-1,1,2]
        visited=[0]*n
        flow=0
        way=[-1]*n
        finalpath=[0]*n
        way[int(ycoord)*8+int(xcoord)]=10


        while TheQueue.size()>0:
            current=TheQueue.removefromq()
            print(current.i,current.j)
            visited[(int(current.j))*8+int(current.i)]=1
            for r in range(8):
                if (int(current.i)+dx[r])<8 and (int(current.i)+dx[r])>=0 and (int(current.j)+dy[r])<8 and (int(current.j)+dy[r])>=0:
                    if (int(current.i)+dx[r])==int(xcoordend) and (int(current.j)+dy[r])==int(ycoordend):
                        endpoint=indexes(int(current.i)+dx[r],int(current.j)+dy[r])
                        print(endpoint.i,endpoint.j)
                        flow=1
                        way[(int(current.j)+dy[r])*8+int(current.i)+dx[r]]=r
                        break
                    elif visited[(int(current.j)+dy[r])*8+int(current.i)+dx[r]]==0:
                        inserter=indexes(int(current.i)+dx[r],int(current.j)+dy[r])
                        print(inserter.i,inserter.j,"q")
                        TheQueue.addtoq(inserter)
                        visited[(int(current.j)+dy[r])*8+int(current.i)+dx[r]]=1
                        way[(int(current.j)+dy[r])*8+int(current.i)+dx[r]]=r
            if flow==1:
                break


        visited[(int(endpoint.j))*8+int(endpoint.i)]=1
        for l in range(8):
            print(visited[l*8:l*8+8])
        res=0
        for lant in range(64):
            if visited[lant]==1:
                res=res+1
        print(res)
        print(way)
        checker=indexes(xcoordend,ycoordend)
        while way[int(checker.j)*8+int(checker.i)]!=10:
          finalpath[int(checker.j)*8+int(checker.i)]=1
          print(way[int(checker.j)*8+int(checker.i)])
          if way[int(checker.j)*8+int(checker.i)]==0:
            checker.i=int(checker.i)-1
            checker.j=int(checker.j)-2
          elif way[int(checker.j)*8+int(checker.i)]==1:
            checker.i=int(checker.i)-2
            checker.j=int(checker.j)-1
          elif way[int(checker.j)*8+int(checker.i)]==2:
            checker.i=int(checker.i)-2
            checker.j=int(checker.j)+1
          elif way[int(checker.j)*8+int(checker.i)]==3:
            checker.i=int(checker.i)-1
            checker.j=int(checker.j)+2
          elif way[int(checker.j)*8+int(checker.i)]==4:
            checker.i=int(checker.i)+1
            checker.j=int(checker.j)+2
          elif way[int(checker.j)*8+int(checker.i)]==5:
            checker.i=int(checker.i)+2
            checker.j=int(checker.j)+1
          elif way[int(checker.j)*8+int(checker.i)]==6:
            checker.i=int(checker.i)+2
            checker.j=int(checker.j)-1
          elif way[int(checker.j)*8+int(checker.i)]==7:
            checker.i=int(checker.i)+1
            checker.j=int(checker.j)-2

        finalpath[int(ycoord)*8+int(xcoord)]=1

        for y in range(8):
            print(finalpath[y*8:y*8+8])

        for ab in range(64):
            if finalpath[ab]==1:
                (board[int(ab/8)][int(ab%8)]).mode=1
                butColor(int(ab/8),int(ab%8))
        inputnum=2
        print(inputnum,"hehe")
    elif inputnum==2:
        for a in range(8):
            for b in range(8):
                board[a][b].mode=0
                butColor(a,b)
        inputnum=0
        xxx=1
    #abcdefgh
    if ((board[i][j]).mode==0) and inputnum!=2 and xxx==0:
        (board[i][j]).mode=1
        butColor(i,j)
    #elif ((board[i][j]).mode==1 and (i+j)%2):
        #(board[i][j]).mode=0
       # butColor(i,j)
    #else:
       # (board[i][j]).mode=0
       # butColor(i,j)
    print("During toggle theme was - ",end="")
    
class square:
    def __init__(self,but,i,j,mode):
        self.i=i
        self.j=j
        self.mode=mode
        self.but=Button(root,text="",width=6,height=3,command=lambda: togg(self.i,self.j))
        self.but.grid(row=i+1,column=j)

root.title("Knight's Trails")
themeLabel=Button(text="Theme",width=14,state="disabled")
BW=Button(text="B&W",width=14,command=lambda: setTheme(0))
Wood=Button(text="Wood",width=14,command=lambda: setTheme(1))
Porc=Button(text="Porcelain",width=14,command=lambda: setTheme(2))
themeLabel.grid(row=0,column=0,columnspan=2)
BW.grid(row=0,column=2,columnspan=2)
Wood.grid(row=0,column=4,columnspan=2)
Porc.grid(row=0,column=6,columnspan=2)

for i in range(8):
    col=[]
    for j in range(8):
        x=square(i,i,j,0)   ##Passing random value for but and color
        col.append(x)
    board.append(col)

setTheme(1)

class Queue:

    def __init__(self):
        self.queue = list()

    def addtoq(self,dataval):
# Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False

    def removefromq(self):
        if(len(self.queue)>0):
            return self.queue.pop()
        return False

    def size(self):
        return len(self.queue)


class indexes:
    def __init__(self,i,j):
        self.i=i
        self.j=j

#bfs code

    

root.mainloop()

"""
import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
root = tk.Tk()

frame = ScrollableFrame(root)

for i in range(2000):
    ttk.Label(frame.scrollable_frame, text=str(i)).pack()

frame.pack()
root.mainloop()
"""
"""
from tkinter import *
w = Tk()
w.geometry('650x400')

c=Canvas(w,bg="gray94",height=750,width=650)
c.config(scrollregion=c.bbox("all"))
c.pack(expand=YES,fill=BOTH)

scr=Scrollbar(c)
scr.pack(side=RIGHT,fill=Y)

c.config(yscrollcommand=scr.set)
scr.config(command=c.yview)

l2 = ['KA', 'NY']
lst = []
for i in range(10000):
    button1 = Button(c, text=str(i))
    lst += [c.create_window(0,i*160, window=button1)]
   
for i in range(30):
    c.coords(lst[i],0,i*100)




c.configure(scrollregio=c.bbox("all"))

w.mainloop()

"""
"""
 class Elemento(Canvas):
            
            def __init__(self,Tabela,livro,posx,posy,color,ID):              
                
                livro.Set_Autor(str(ID))
                #get master
                self.__Frame = Tabela.Get_ScrollFrame()
                self.__Canvs = Tabela.Get_Canvas()
                self.__Frame.update_idletasks()
                #info
                self.__Color = color
                self.__ColorSelected = "light blue"
                self.__Livro = livro
                self.__TxtsId_dic  = {}
                self.__id = ID
                self.__Suspended = False
                #Dimenções
                self.__pad= 4
                self.__posx = posx
                self.__posy = posy
                self.__h = Tabela.Get_Elemento_Height()
                self.__w = self.__Canvs.winfo_width()     
                                
                super().__init__(self.__Frame,width=self.__Canvs.winfo_width(), height=80,highlightthickness=0,bg=self.__Color)
                                
                #elementos (Estado,image,infotable)                
                self.__Rect_Estado_id = self.create_rectangle(self.__posx,0,self.__posx+20,self.__posy+self.__h,tags=("Estado"),fill="light green",outline="",width=0)
                self.__Rect_Image_id = self.create_rectangle(self.__posx+20+self.__pad,0+self.__pad,self.__posx+120-self.__pad,0+(self.__h-self.__pad),tags=("Image",),fill="Gray",outline="",width=0)
                
                self.Comfigurar(altura=self.__h)
                self.Refresh_Texts()
                
                self.place(x=self.__posx,y=self.__posy,width=self.__w, height=self.__h)
                self.bind("<Enter>",self.Mouse_in)
                self.bind("<Leave>",self.Mouse_out)
                                
            def Get_id(self):
                return self.__id
             
            def Get_livro(self):
                return self.__Livro    
            
            def Get_Position(self):
                return (self.__posx,self.__posy)
                        
            def Set_Position(self,pos=None):
                if pos==None:
                    pos = (self.__posx,self.__posy)
                else:
                    self.__posx = pos[0]
                    self.__posy = pos[1]

            def Suspend(self):
                self.__Suspended = True
                self.place_forget()
                
            def Unsuspend(self,pos=None):
                if pos!=None:
                    self.place(x=pos[0],y=pos[1],width=self.__w, height=self.__h)
                    self.__Suspended = False
                else:
                    self.place(x=self.__posx,y=self.__posy,width=self.__w, height=self.__h)
                    self.__Suspended = False
                    
            def IsSuspended(self):
                return self.__Suspended            

            def Comfigurar(self,color=None,image=None,altura=None):
                
                if color != None:
                    self.configure(bg=color)
                if image != None:
                    pass
                
                if altura != None or altura>=80:    
                
                    self.delete("TEXTOS")
                    self.__h = int(altura)     
                   
                    tempdic = self.__Livro.Get_Basic_Info()
                    tempkeylist = list(tempdic.keys())  
                    i=0
                    lim = 0
                    stepy = Settings.Get("Tab_Font_2")["T"] 
                    
                    while (i==0 or i < lim) and i<len(tempdic):
                                                                    
                        txtTITLE = self.create_text(self.__posx+130,5+i*stepy,text=tempkeylist[i]+':',fill=Settings.Get("Tab_Font_2")["FG"],\
                                                font=(Settings.Get("Tab_Font_2")["Font"],Settings.Get("Tab_Font_2")["T"],"bold"),\
                                                justify=LEFT,anchor=NW,tags="TEXTOS")
                        
                        dimentions = self.bbox(txtTITLE)                        
                        x = abs(dimentions[2]-dimentions[0])+5
                        y = abs(dimentions[3]-dimentions[1])
                        
                        txtTEXT = self.create_text((self.__posx+130+x,5+i*stepy),text=tempdic[tempkeylist[i]],fill=Settings.Get("Tab_Font_2")["FG"],\
                                                font=(Settings.Get("Tab_Font_2")["Font"],Settings.Get("Tab_Font_2")["T"],"italic"),\
                                                justify=LEFT,anchor=NW,tags="TEXTOS")
                        
                        self.__TxtsId_dic[tempkeylist[i]] = {"Title":txtTITLE,"Text":txtTEXT}

                        if i==0:
                            stepy = y                           
                            lim = round((self.__h-10)/stepy)   
                            
                        i+=1
                    
                    self.place_configure(height=self.__h)
                    self.coords(self.__Rect_Estado_id,self.__posx,0,self.__posx+20,0+self.__h)
                    self.coords(self.__Rect_Image_id,self.__posx+20+self.__pad,0+self.__pad,self.__posx+120-self.__pad,0+(self.__h-self.__pad))
                    
                    del(tempdic,tempkeylist,lim,stepy)
                            
            def Refresh_Texts(self,font=None):
                
                self.__Canvs.update_idletasks()
                self.__w = self.__Canvs.winfo_width()
                dic = self.__Livro.Get_Basic_Info()
                
                if font!=None:
                    self.Comfigurar(altura=self.__h)
                                                 
                for key in self.__TxtsId_dic:
                    
                    dimentions = self.bbox(self.__TxtsId_dic[key]["Text"])
                    x = abs(dimentions[2]-dimentions[0])
                    carateres = round((self.__w-220) / (x/len(self.itemcget(self.__TxtsId_dic[key]["Text"],"text")) ))                    
            
                    if carateres < len(dic[key]):
                        self.itemconfigure(self.__TxtsId_dic[key]["Text"],text=dic[key][:carateres-3]+"...")
                    else:
                        self.itemconfigure(self.__TxtsId_dic[key]["Text"],text=dic[key])
                        
            def Mouse_in(self,event=None):    
                self.itemconfigure(self.__Rect_Estado_id,fill="light green")
                self.configure(bg=self.__ColorSelected,highlightthickness=3)

            def Mouse_out(self,event=None):
                self.configure(bg=self.__Color,highlightthickness=0)
                
            def Event_ONclick(self,event):
                pass
            
            def ONResize(self):
                
                self.__Canvs.update_idletasks()
                self.__w = self.__Canvs.winfo_width()
                self.place_configure(width=self.__w, height=self.__h)  
                self.Refresh_Texts()  
                """

#----------------------------------------------
"""
 class Tabela(Frame):
        
        NumeroAtivos = 0
        __NumeroTotal = 0
        
        def __init__(self,x,y,Master,relwidth=0.625,relheight=1):
                       
            self.__Master = Master
            self.__Master.update_idletasks()
            
            self.__x = 0
            self.__y = y
            self.__relwidth = relwidth
            self.__relheight = relheight

            self.__w = self.__relwidth*Master.winfo_width()
            self.__h = self.__relheight*Master.winfo_height()
            
            super().__init__(Master,width=self.__w,height=self.__h,bg=Settings.Get("Lyt_Clrs_Tebela")["Top_BG"],borderwidth=0)            

            self.place_configure(x=self.__x,y=self.__y,relwidth=self.__relwidth,relheight=self.__relheight)
            #Colunas
            self.columnconfigure(0,weight=0, pad=0)
            self.columnconfigure(1,weight=0, minsize=20, pad=0)
            self.columnconfigure(2,weight=0, minsize=100, pad=0)
            self.columnconfigure(3,weight=1, minsize=100, pad=0)
            #linhas
            self.rowconfigure(0,weight=0,minsize=30, pad=0)
            self.rowconfigure(1,weight=1, pad=0)
            
            #ScrollFrame e scrollbar                      
            self.__Canvas = Canvas(self,width=self.__w-20, height=self.__h,highlightthickness=0,bg="pink")      
            self.__ScrollBar = Scrollbar(self, orient="vertical", command=self.__Canvas.yview)             
            self.__ScrollFrame = Frame(self)
            self.__ScrollFrame.bind("<Configure>", self.On_Scrollbar_change)    
            self.__Canvas.create_window((0,0), window=self.__ScrollFrame, anchor="nw")                          
            self.__Canvas.config(yscrollcommand=self.__ScrollBar.set)            
            self.__Canvas.grid(row=1,column=1, columnspan=3, sticky="NSEW")
            self.__ScrollBar.grid(row=0,rowspan=2,column=0,sticky="NSEW" ) 
            
            self.__Canvas.bind("<Configure>", self.On_Resize)
            
            #Desins
            self.__lb_fantasma = Label(self,bg= Settings.Get("Lyt_Clrs_Tebela")["Top_BG"])
            self.__lb_fantasma.grid(row=0,column=1,sticky="NSEW")
            
            self.__lb_Imagem = Label(self,text="Imagem",\
                                      font=(Settings.Get("Tab_Font_1")["Font"],Settings.Get("Tab_Font_1")["T"]),\
                                      bg= Settings.Get("Lyt_Clrs_Tebela")["Top_BG"],\
                                      fg= Settings.Get("Tab_Font_1")["FG"],\
                                      justify=CENTER)  
            self.__lb_Imagem.grid(row=0,column=2,sticky="NSEW")
            
            self.__lb_MaisInfo = Label(self,text="Informações",\
                                      font=(Settings.Get("Tab_Font_1")["Font"],Settings.Get("Tab_Font_1")["T"]),\
                                      bg= Settings.Get("Lyt_Clrs_Tebela")["Top_BG"],\
                                      fg= Settings.Get("Tab_Font_1")["FG"],\
                                      justify=CENTER) 
            self.__lb_MaisInfo.grid(row=0,column=3,sticky="NSEW")
            
            self.__lst_OrdemDosEementos = [] 
            self.__lst_Visiveis = []
            self.__lst_NotVisiveis = []
            self.__dic_id_pos = {}
            self.__Last_id = 0
            self.__focuspos = 0
            self.__Canvas_Heitgh = self.__h
            self.__Element_Height= 160
            self.__LastIndice = -1
       
        def Get_Elemento_Height(self):
            return self.__Element_Height    

        def Get_NumeroElementos(self):
            return len(self.__List)
        
        def Get_Elementos(self):
            return self.__List
    
        def Get_ScrollFrame(self):
            return self.__ScrollFrame
        
        def Atualizar_listas(self):
            
            #update para não haver numeros errados
            self.__ScrollFrame.update_idletasks()
            self.__Canvas.update_idletasks()  
            
            #calcular quantos se pode mostar
            q = ceil(self.__Canvas.winfo_height()/self.__Element_Height) + 2
            print(q,"--------")
            yview_inicio = ceil((self.__Canvas.yview()[0]*self.__ScrollFrame.winfo_height())/self.__Element_Height - 1)
            
            if yview_inicio < 0:
                yview_inicio = 0
            
            if q >= len(self.__lst_OrdemDosEementos):
                print(self.__lst_Visiveis)
                self.__lst_Visiveis = self.__lst_OrdemDosEementos[:q]
                self.__lst_NotVisiveis = []
            else:
                self.__lst_Visiveis = self.__lst_OrdemDosEementos[yview_inicio:yview_inicio+q]
                self.__lst_NotVisiveis = self.__lst_OrdemDosEementos[:yview_inicio] + self.__lst_OrdemDosEementos[yview_inicio+q:]
                print(self.__lst_Visiveis,yview_inicio,yview_inicio+q,)
                
        def Get_Canvas(self):
            return self.__Canvas        
        
        def Atualizar_Posições(self,inicio,lastpos={}):
            
            for idd in self.__lst_OrdemDosEementos[inicio:fim]:
                
                elemento = self.__dic_id_pos[str(idd)]["Elemento"]
                
                if str(idd) not in lastpos:
                    lastpos[str(idd)] = elemento.Get_Position()[1]-self.__Element_Height

                b = elemento.Move_DownToTop(topos=lastpos[str(idd)],incremento=10) 

            if not b:
                self.after(10, lambda inicio=inicio,lastpos=lastpos: self.Atualizar_Posições(inicio,lastpos) )    
            print("--------------------------------------")
                 
        def Novo_Elemento(self,livro): 

            Cria uma nova linha na tabela return o id do elemento livro. 

            
            self.__Canvas.update_idletasks()
            self.__Last_id += 10
            self.__focuspos += self.__Element_Height
            self.__ScrollFrame.configure(width=self.__Canvas.winfo_width(),height=self.__focuspos,bg="Black")
            elemento = self.Elemento(Tabela=self,livro=livro,posx=0,posy=self.__focuspos-self.__Element_Height,color="yellow",ID=self.__Last_id)        
            elemento.ONResize()            
            self.__LastIndice += 1 
            self.__dic_id_pos[str(self.__Last_id)] = {"Elemento":elemento,"Pos":self.__LastIndice}
            self.__lst_OrdemDosEementos += [elemento]
        
            return self.__Last_id
            
        def Novos_Elementos(self,livro):
            

            Cria uma nova linha para cada livro no argumento (lista/tuplo)livros:
            Retorna os respetivos ids

            
            for i in range(206):
                self.Novo_Elemento(livro)
                
        def Remover_Elemento(self,Elementoid=None,ElementoPos=None):              
            
            self.Atualizar_Posições(inicio=ElementoPos)
            
        def On_Resize(self,event):    
            self.Atualizar_listas()
            for elemento in self.__lst_Visiveis:
                elemento.ONResize()            

        def On_Scrollbar_change(self,event):
            self.__Canvas.configure(scrollregion=self.__Canvas.bbox("all"))
            self.Atualizar_listas()
            for elemento in self.__lst_Visiveis:
                elemento.ONResize()  
            
            """
"""
from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title("PythonGuides")

tv = ttk.Treeview(ws, columns=(1, 2, 3), show='headings', height=8)
tv.pack()

tv.heading(1, text="name")
tv.heading(2, text="eid")
tv.heading(3, text="Salary")

def update_item():
    selected = tv.focus()
    temp = tv.item(selected, 'values')
    sal_up = float(temp[2]) + float(temp[2]) * 0.05
    tv.item(selected, values=(temp[0], temp[1], sal_up))

tv.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00))
tv.insert(parent='', index=1, iid=1, values=("anil", "e12", 120000.00))
tv.insert(parent='', index=2, iid=2, values=("ankit", "e13", 41000.00))
tv.insert(parent='', index=3, iid=3, values=("Shanti", "e14", 22000.00))

Button(ws, text='Increment Salary', command=update_item).pack()

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

ws.mainloop()
"""

from tkinter import * 
  
  
root = Tk()  
root.geometry("400x300") 
  
v1 = DoubleVar()
  
def show1():  
      
    sel = "Horizontal Scale Value = " + str(v1.get())
    l1.config(text = sel, font =("Courier", 14))  
  
  
s1 = Scale( root, variable = v1, 
           from_ = 1, to = 100, 
           orient = HORIZONTAL)   
  
l3 = Label(root, text = "Horizontal Scaler")
  
b1 = Button(root, text ="Display Horizontal", 
            command = show1, 
            bg = "yellow")  
  
l1 = Label(root)
  
  
s1.pack(anchor = CENTER) 
l3.pack()
b1.pack(anchor = CENTER)
l1.pack() 
  
root.mainloop()

        """
        self.MainFrame.columnconfigure(0,minsize=470,weight=1)
        self.MainFrame.columnconfigure(1,minsize=30,weight=0)
        self.MainFrame.columnconfigure(2,minsize=300,weight=1)
        
        self.MainFrame.rowconfigure(1,minsize=30,weight=0)
        self.MainFrame.rowconfigure(0,weight=1)
        
       # barra = MyWidgets.Progress_Bar(Janela_principal,1000,650,steps=5)
        
       
        

        
        gG = MyWidgets.Tabela(0,0,self.MainFrame)
        gG.grid(row=0,column=0,sticky=NSEW)
        f = Livro(1234,title="O Barco do mar Barnco a b c d e f g h i j k l m n o p q r s ç t u v w x y z 1234456789123456789123456789123456789 ",autor="Rui Abril")
      
       # MyWidgets.Janela_Adicionar(Janela_principal,gG)
       # MyWidgets.Frame_Adicionar(Janela_principal,gG).pack(fil=BOTH,expand=True)
       # MyWidgets.Frame_FichaTecnica(Janela_principal,tabela=gG,livro=f).place(x=0,y=0,width=300,height=600)
        MyWidgets.Frame_InformaçõesTabela(self.MainFrame,gG).grid(row=0,rowspan=2,column=2,sticky=NSEW)
       # MyWidgets.Janela_Frame_FichaTecnica(Janela_principal,tabela=gG,livro=f)
        gG.Novos_Elementos(f)
        
        MyWidgets.MenuBarVertical(self.MainFrame).grid(row=0,column=1,sticky=NSEW)
        MyWidgets.BarraDePrucura(self.MainFrame).grid(row=1,column=0,columnspan=2,sticky=NSEW)
        #MyWidgets.Zoom_Bar(self.MainFrame,40,140,10).place(x=100,y=50)

        Atualizar cores quando remover

        
        
        def fff():
           # gG.Atualizar_listas()
           # gG.Mover_Elementos(ids=range(10,200,10),mode="paraCima",x=-250,y=80,delta=True,stepy=20,time=10)
            #gG.Remover_Elemento(20)
            gG.Remover_Elementos((50,60,70,80,90),sty=20,)
           # gG.MoveViewTo(80)
            
        
        Button(Janela_principal,text="clica",command=fff).place(x=1000,y=600)        
        
        
        """

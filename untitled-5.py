from tkinter import ttk
import tkinter as tk

x=500

root = tk.Tk()

canvas = tk.Canvas(root, width=550, height=550)
canvas.create_oval(10, 50, 20, 20, fill="red")
canvas.grid(row=0, column=1)

scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroll_y.grid(row=0, column=0, sticky="ns")

canvas.configure(yscrollcommand=scroll_y.set)



def dd(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def ff():
    canvas.create_rectangle(0, 700, 20, 750, fill="red")

f = tk.Button(root,command=ff)
f.grid(row=0, column=1)

canvas.configure(scrollregion=canvas.bbox("all"))
root.bind("<Configure>",dd)

root.mainloop()

#--------------------------------------------------------------------
"""
self.__Master = Master
            
            Master.update_idletasks()
            
            self.__Frame = Frame(Master,width=0.625*Master.winfo_width(),height=Master.winfo_height(),bg="pink")   
            
            self.__Frame.place(x=0,y=0,relwidth=0.625,relheight=1)
            self.__frm_Top = Frame(self.__Frame,bg=Settings.Get("Lyt_Clrs_Tebela")["Top_BG"])
            self.__frm_Top.place(x=0,y=0,relwidth=1,height=40)
            
            self.__lb_NLivros = Label(self.__frm_Top,text="Número\nDe Livros",\
                                      font=(Settings.Get("Font_Text1")["Font"],Settings.Get("Font_Text1")["T"]),\
                                      bg= Settings.Get("Lyt_Clrs_Tebela")["Top_BG"],\
                                      fg= Settings.Get("Font_Text1")["FG"],\
                                      justify=CENTER)  
            
            self.__lb_Imagem = Label(self.__frm_Top,text="Imagem",\
                                      font=(Settings.Get("Font_Text1")["Font"],Settings.Get("Font_Text1")["T"]),\
                                      bg= Settings.Get("Lyt_Clrs_Tebela")["Top_BG"],\
                                      fg= Settings.Get("Font_Text1")["FG"],\
                                      justify=CENTER)   
            
            self.__lb_MaisInfo = Label(self.__frm_Top,text="Informações",\
                                      font=(Settings.Get("Font_Text1")["Font"],Settings.Get("Font_Text1")["T"]),\
                                      bg= "pink",\
                                      fg= Settings.Get("Font_Text1")["FG"],\
                                      justify=CENTER)    
            
            self.__frm_Top.update_idletasks()           
            self.__lb_NLivros.place(x=0,y=0,width=80,height=40)
            self.__lb_Imagem.place(x=80,y=0,width=150,height=40)
            self.__lb_MaisInfo.place(x=230,y=0,width=self.__frm_Top.winfo_width()-230,height=40) 
        
            self.__scrollbar = Scrollbar(Master, width=20, bg="Gray", orient= "vertical")
            self.__scrollbar.pack( side = LEFT, fill = Y )
            
            self.__Canvas = Canvas(self.__Frame,bg="yellow",width=0.625*Master.winfo_width(),height=Master.winfo_height(), yscrollcommand = self.__scrollbar.set )
            self.__scrollbar.config(command= self.__Canvas.yview )
            
            self.__Canvas.place(x=0,y=40, relwidth=1, height=Master.winfo_height()-40 )
            
            self.__Canvas.configure(scrollregion=self.__Canvas.bbox("all"))
            
            self.__Canvas.create_rectangle(30,30,50,50,fill = "Blue")
                                             
            
            self.__frm_Top.bind("<Configure>",self.__OnResize_frm_top)
            
        def New_Livro(self):
            pass
    
            
        def __OnResize_frm_top(self,event):
        
            
            self.__lb_MaisInfo.place_forget()
            self.__lb_MaisInfo.place(x=230,y=0,width=self.__frm_Top.winfo_width()-230,height=40) 
            
            self.__Canvas.place_forget()
            self.__Canvas.place(x=0,y=40,relwidth=1,height=self.__Master.winfo_height()-40)
            

"""
self.__Frame.columnconfigure(0,weight=0,minsize=2,pad=0)
self.__Frame.columnconfigure(1,weight=0,minsize=50,pad=0)
self.__Frame.columnconfigure(2,weight=1,pad=0)

self.__Frame.rowconfigure(0,minsize=4,pad=0)
self.__Frame.rowconfigure((1,2,3,4),pad=0)
self.__Frame.rowconfigure(5,weight=1,pad=0)
self.__Frame.rowconfigure(6,minsize=2,pad=0)

self.__lb_Titulo = Label(self.__Frame,text="Titulo",\
                          font=(Settings.Get("Font_Text2")["Font"],Settings.Get("Font_Text2")["T"]),\
                          bg= self.__Color,\
                          fg= Settings.Get("Font_Text2")["FG"],\
                          justify=CENTER) 
self.__lb_Titulo.grid(row=1,column=1,sticky="NSEW")

self.__lb_TituloLivro = Label(self.__Frame,text=livro.Get_Title(),\
                          font=(Settings.Get("Font_Text3")["Font"],Settings.Get("Font_Text3")["T"],"italic"),\
                          bg= self.__Color,\
                          fg= Settings.Get("Font_Text3")["FG"],\
                          justify=LEFT) 
self.__lb_TituloLivro.grid(row=1,column=2,sticky="W")
      
self.__lb_Autor = Label(self.__Frame,text="Autor",\
                          font=(Settings.Get("Font_Text2")["Font"],Settings.Get("Font_Text2")["T"]),\
                          bg= self.__Color,\
                          fg= Settings.Get("Font_Text2")["FG"],\
                          justify=CENTER)  
self.__lb_Autor.grid(row=2,column=1,sticky="NSEW")

self.__lb_Autorlivro = Label(self.__Frame,text=livro.Get_Autor(),\
                          font=(Settings.Get("Font_Text3")["Font"],Settings.Get("Font_Text3")["T"],"italic"),\
                          bg= self.__Color,\
                          fg= Settings.Get("Font_Text3")["FG"],\
                          justify=CENTER)  
self.__lb_Autorlivro.grid(row=2,column=2,sticky="W")                

self.__lb_MaisInfo = Label(self.__Frame,text="Informações",\
                          font=(Settings.Get("Font_Text1")["Font"],Settings.Get("Font_Text1")["T"]),\
                          bg= self.__Color,\
                          fg= Settings.Get("Font_Text2")["FG"],\
                          justify=CENTER) 
self.__lb_MaisInfo.grid(row=5,column=1,sticky="NSEW")
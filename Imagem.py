from tkinter import *
from PIL import Image, ImageTk

class EditImage(Toplevel):
        
    """
    Abre uma nova janela onde se pode editar uma imagem 
    """
    def __init__(self,master,image_path):
        
        super().__init__(master)
        
        self.title("Editar Imagem")
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()                 
        
        self.geometry("500x500+{}+{}".format((screen_width-400)//2,(screen_height-600)//2))
        self.minsize(500,500)
        self.resizable(width =False,height=False)
        self.configure(background="white")  
        self.attributes('-topmost',True)
                
        #botoes guardar e cancelar
        Button(self,command = self.concluir ,text="Concluir").place(x=260,y=465,width=100,height=25)
        Button(self,command = self.cancelar ,text="Cancelar").place(x=150,y=465,width=100,height=25) 
        
        #canvas
        self.canvas = Canvas(self,highlightthickness=2,highlightbackground="black")
        self.canvas.place(x=10,y=5,width=480,height=450)
        
        self.image_path = image_path
        self.image_ori = Image.open(image_path)
        
        if self.image_ori.width < 300 or self.image_ori.height < 270:
            self.image_temp = self.image_ori.resize((300,270))  
            self.image_ori = self.image_temp
            self.image_in = self.image_ori
            self.img = ImageTk.PhotoImage(self.image_temp )
        else:
            self.image_in = self.image_ori
            self.img = ImageTk.PhotoImage(self.image_ori)
            
        self.image_resize = self.image_in
            
        self.Id = self.canvas.create_image(240, 225, anchor=CENTER,image=self.img) 
        self.canvas.tag_bind(self.Id ,"<B1-Motion>",self.ON_MOVE_PRESS)
        self.canvas.tag_bind(self.Id ,"<Button-1>",self.ON_PRESS)   
        
        self.canvas.create_rectangle(90,90,390,360,fill=None ,outline="red",width=2)
        
        #botões Mover, Resize e Crop
        self.b_Move = Button(self,command = self.Mover ,text="Mover")
        self.b_Move.place(x=12,y=428,width=50,height=25)
        self.B_b_Move = False
        
        self.b_Resize = Button(self,command = self.Resize ,text="Resize")
        self.b_Resize.place(x=64,y=428,width=50,height=25) 
        self.B_b_Resize = False        
        
        self.b_crop = Button(self,command = self.Crop ,text="Crop")
        self.b_crop.place(x=116,y=428,width=50,height=25)    
        
        self.b_reset = Button(self,command = self.Reset,text="Reset")
        self.b_reset.place(x=168,y=428,width=50,height=25) 
        
        self.MousePos = (0,0)
        
    def ON_PRESS(self,event):
        
        self.MousePos = ( event.x , event.y )    
    
    def ON_MOVE_PRESS(self,event):
        
        if self.B_b_Move:
            
            pos = self.canvas.coords(self.Id)
             
            aresta_cima = (pos[1]+event.y-self.MousePos[1]) - self.image_in.height/2
            aresta_baixo = (pos[1]+event.y-self.MousePos[1]) + self.image_in.height/2 
            aresta_esquerda = (pos[0] + event.x - self.MousePos[0]) - self.image_in.width/2 
            aresta_direita = (pos[0] + event.x - self.MousePos[0]) + self.image_in.width/2                   
            
            #centro 240, 225
            # E90,D390,C90,B360
            # CMB EMD
            # Meio direita 
            #canto superior direito
            if (aresta_cima >= 90) and (aresta_direita <= 390):               
                self.canvas.coords( self.Id, (390-self.image_in.width/2 , 90+self.image_in.height/2) )
            #canto superior esquerdo
            elif (aresta_cima >= 90) and (aresta_esquerda >= 90):                
                self.canvas.coords( self.Id, (90+self.image_in.width/2 , 90+self.image_in.height/2) )
            #canto inferior direito
            elif (aresta_baixo <= 360) and (aresta_direita <= 390):             
                self.canvas.coords( self.Id, (390-self.image_in.width/2 , 360-self.image_in.height/2) )
            #canto inferior esquerdo
            elif (aresta_baixo <= 360) and (aresta_esquerda >= 90):                
                self.canvas.coords( self.Id, (90+self.image_in.width/2 , 360-self.image_in.height/2) )            
            # Meio Direita
            elif aresta_direita <= 390 :            
                self.canvas.coords( self.Id, (390-self.image_in.width/2  , pos[1]+event.y-self.MousePos[1]) )
            # Meio esquerda
            elif aresta_esquerda >= 90 :            
                self.canvas.coords( self.Id, (90 + self.image_in.width/2 , pos[1]+event.y-self.MousePos[1]) )
            # Cima Meio
            elif aresta_cima >= 90: #self.image_in.height/2 + 450 :
                self.canvas.coords( self.Id, (pos[0]+event.x-self.MousePos[0] , 90 + self.image_in.height/2) )
            # Baixo Meio
            elif aresta_baixo <= 360 :    
                self.canvas.coords( self.Id, (pos[0]+event.x-self.MousePos[0] , 360 - self.image_in.height/2) )
            # Meio Meio 
            else:
                self.canvas.coords( self.Id, (pos[0]+event.x-self.MousePos[0] , pos[1]+event.y-self.MousePos[1]) )
            
            self.MousePos = ( event.x , event.y )
     
        elif self.B_b_Resize:
            
            pos = self.canvas.coords(self.Id)
             
            aresta_cima = (pos[1]+event.y-self.MousePos[1]) - self.image_in.height/2
            aresta_baixo = (pos[1]+event.y-self.MousePos[1]) + self.image_in.height/2 
            aresta_esquerda = pos[0] - self.image_in.width/2 
            aresta_direita = pos[0] + self.image_in.width/2                   
           
            delta_y = event.y-self.MousePos[1]
            delta_x = event.x-self.MousePos[0]
            w = self.image_in.width 
            h = self.image_in.height
            
            if w+delta_x <= 300:
                new_w = 300
            else:
                new_w = w+delta_x
                
            if h+delta_y <= 270:
                new_h = 270
            else:
                new_h = h+delta_y 
                
            self.image_temp = self.image_resize.resize((new_w,new_h)) 
            
            #centro 240, 225
            # E90,D390,C90,B360
            # CMB EMD
            # Meio direita 
            #canto superior direito            
            if (aresta_cima >= 90) and (aresta_direita <= 390):               
                self.canvas.coords( self.Id, (390-self.image_temp.width/2 , 90+self.image_temp.height/2) )
            #canto superior esquerdo
            elif (aresta_cima >= 90) and (aresta_esquerda >= 90):                
                self.canvas.coords( self.Id, (90+self.image_temp.width/2 , 90+self.image_temp.height/2) )
            #canto inferior direito
            elif (aresta_baixo <= 360) and (aresta_direita <= 390):             
                self.canvas.coords( self.Id, (390-self.image_temp.width/2 , 360-self.image_temp.height/2) )
            #canto inferior esquerdo
            elif (aresta_baixo <= 360) and (aresta_esquerda >= 90):                
                self.canvas.coords( self.Id, (90+self.image_temp.width/2 , 360-self.image_temp.height/2) )            
            # Meio Direita
            elif aresta_direita <= 390 :            
                self.canvas.coords( self.Id, (390-self.image_temp.width/2  , pos[1]+event.y-self.MousePos[1]) )
            # Meio esquerda
            elif aresta_esquerda >= 90 :            
                self.canvas.coords( self.Id, (90 + self.image_temp.width/2 , pos[1]+event.y-self.MousePos[1]) )
            # Cima Meio
            elif aresta_cima >= 90: #self.image_in.height/2 + 450 :
                self.canvas.coords( self.Id, (pos[0]+event.x-self.MousePos[0] , 90 + self.image_in.height/2) )
            # Baixo Meio
            elif aresta_baixo <= 360 :    
                self.canvas.coords( self.Id, (pos[0]+event.x-self.MousePos[0] , 360 - self.image_in.height/2) )
            # Meio Meio 

            self.image_in = self.image_temp
            self.img = ImageTk.PhotoImage(self.image_temp)
            self.canvas.itemconfig(self.Id,image=self.img)

            self.MousePos = ( event.x , event.y )
            
    def Reset(self):
        
        self.image_resize = self.image_ori
        self.image_in = self.image_ori
        self.img = ImageTk.PhotoImage(self.image_ori)
        self.canvas.itemconfig(self.Id,image=self.img)
        self.canvas.coords(self.Id,(240,225))
        
    def Mover(self):
        
        self.B_b_Move = not self.B_b_Move
        
        if self.B_b_Move:  
            
            self.b_Move.configure(relief=SUNKEN,background="light grey")
            
            self.B_b_Resize = False
            self.b_Resize.configure(relief=RAISED,background="#f0f0f0")
                     
        else: 
            
            self.b_Move.configure(relief=RAISED,background="#f0f0f0")
        
    def Resize(self):
        
        self.B_b_Resize = not self.B_b_Resize
        
        if self.B_b_Resize:  
            
            self.b_Resize.configure(relief=SUNKEN,background="light grey")
            
            self.B_b_Move = False
            self.b_Move.configure(relief=RAISED,background="#f0f0f0")
                        
        else: 
            
            self.b_Resize.configure(relief=RAISED,background="#f0f0f0")        
        
    def Crop(self):
        
        self.B_b_crop = True
 
        self.B_b_Move = False
        self.b_Move.configure(relief=RAISED,background="#f0f0f0")
            
        self.B_b_crop = False
        self.b_crop.configure(relief=RAISED,background="#f0f0f0")               
                        
        pos = self.canvas.coords(self.Id)
        left_x = int(pos[0]-self.image_in.width/2)
        left_y = int(pos[1]-self.image_in.height/2)
        
        if left_x >= 0:
            x = 90 - left_x
        else:
            x = -left_x + 90
            
        if left_y >= 0:
            y = 90 - left_y
        else:
            y = -left_y + 90        

        self.image_temp = self.image_in.crop((x, y,x+300,y+270))
        self.image_in = self.image_temp
        self.img = ImageTk.PhotoImage(self.image_temp)
        self.canvas.itemconfig(self.Id,image=self.img)   
        self.canvas.coords(self.Id,(240,225))      
        
        self.image_resize = self.image_in
    
    def concluir(self):        
        pass
        
    def cancelar(self):
        self.destroy()



main = Tk()
main.geometry("600x600+300+300")
EditImage(main,"tt.png")
main.mainloop()


 
        """
        self.Frm = Frame(Barra,width=400, height=20, bg="red")  
        
        Canvas_WinfoText = Label(Frm,text="Infodfgasdgasdgasdgdsg1234567890gasdgasdgasdgdsg12345678901234567",wraplength=380, justify="center",background="red")
        Canvas_WinfoText.place(x=20,y=0)        
        
        Canvas_WinfoIcon = Canvas(self.Frm, width=20, height=20, bg="blue" ,highlightthickness=0, highlightbackground="blue")              
        Canvas_WinfoIcon.place(x=0,y=0)        
        
        Frm.place(relx=0.25,y=2)
        
        
        
    def RedesenharBarra(self,Bool,Master):
        
        print(Bool)
                
        if Master == self.frm_Barra:
            
            if Bool: 
                self.frm_Barrinha.config(width=300)
                self.Canvas_WinfoText.config(wraplength=260) 
                self.Canvas_WinfoText.update_idletasks()
            else:
                self.frm_Barrinha.config(width=400)
                self.Canvas_WinfoText.config(wraplength=380)
                self.Canvas_WinfoText.update_idletasks()

    
    @classmethod  
    def CommandConfigimage(cls,Menu,Comando,Image=None):
        Menu.configure(takefocus=Comando,image=Image)
    """
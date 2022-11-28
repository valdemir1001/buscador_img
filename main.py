from tkinter import *
import customtkinter
from cores import *

root = Tk()

class Application(Cor):
    def __init__(self,master=None):
        self.root = root
        self.tela()
        self.colorir()
        self.fontes()
        self.add_frames()
        self.label()
        root.mainloop()
        
    def tela(self):
        self.root.title('Buscador de Imagens')
        self.root.geometry('1200x1000+10+10')
        self.root.configure(background='gray')
        
    def gerador_de_frames(self,root_frame,bordaltura,radio,borda_cor,bg_cor,fg_cor,x,y,w,h):
        self.frame = customtkinter.CTkFrame(root_frame,
                                    border_width=bordaltura,
                                    corner_radius=radio,
                                    border_color=borda_cor,
                                    bg_color=bg_cor,
                                    fg_color= fg_cor
                                    ).place(relx=x,rely=y,relwidth=w,relheight=h)
        return self.frame
    
    def add_frames(self):
        # Frame 1 Main
        self.frame_1 = self.gerador_de_frames(self.root,2,20,'black',self.fundo,'white',0.01,0.01,0.98,0.20)
        # Frame 2 Main
        self.frame_2 = self.gerador_de_frames(self.root,2,20,'black',self.fundo,'red',0.01,0.22,0.57,0.77)
        # Frame 3 Main
        self.frame_3 = self.gerador_de_frames(self.root,2,20,'black',self.fundo,'green',0.59,0.22,0.40,0.77)
        
        
    def gerador_de_label(self,frame,texto,texto_fonte,fg,texto_cor,x,y,w,h):
        # Label 1
        self.labels = customtkinter.CTkLabel(frame, 
                                  text=texto.upper(), 
                                  width=900,
                                  compound=CENTER, 
                                  relief=RAISED, 
                                  text_font=texto_fonte, 
                                  fg=fg,
                                  text_color=texto_cor
                                  ).place(relx=x, rely=y, relwidth=w, relheight=h)
        
        return self.labels
    
    def label(self):
        self.label_titulo = self.gerador_de_label(self.frame_2,'gerador de imagens',self.arial_50,'#cfd5e1','red',0.02,0.05,0.80,0.1)
        
  
        self.label_titulo_2 = self.gerador_de_label(self.frame_3,'gerador de imagens',self.arial_50,'#cfd5e1','red',0.02,0.05,0.80,0.1)
        self.bt = Button(self.frame_3,text='botao').place(relx=0.05,rely=0.05,relwidth=0.10,relheight=0.05)
            
    
    
Application()
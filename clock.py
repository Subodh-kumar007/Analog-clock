from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
class clock:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        title=Label(self.root,text="Analog Clock",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)
        self.lbl=Label(self.root,bg="white",bd=20,relief=RAISED)
        self.lbl.place(x=450,y=150,height=400,width=400)
        self.working()

    def clock_image(self,hr,mint,secn):
        cloks=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(cloks)
        #=======for clock Image======>
        bg=Image.open("cl.jpg")
        bg=bg.resize((300,300),Image.Resampling.LANCZOS)
        cloks.paste(bg,(50,50))
        origin=200,200
        
        #formula t rotate the clock
        #angle_in_radians= angle_in_degrees * math.pi/180
        #line_length=100
        #center_x= 250
        #center_y= 250
        #end_x= center_x + line_length * math.sin(angle_in_radians)
        #end_y= center_y + line_length * math.cos(angle_in_radians)
        #=========hour line image===========>
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        #=========Min line image===========>
        draw.line((origin,200+80*sin(radians(mint)),200-80*cos(radians(mint))),fill="blue",width=3)
        #=========Sec line image===========>
        draw.line((origin,200+110*sin(radians(secn)),200-110*cos(radians(secn))),fill="red",width=4)
        draw.ellipse((195,195,210,210),fill="black")
        cloks.save("new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        mint=(m/60)*360
        secn=(s/60)*360
        self.clock_image(hr,mint,secn)
        #self.img=Image.open("images/new.png")
        self.img=ImageTk.PhotoImage(file="new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
#=======Main==============>
root=Tk()
obj=clock(root)
root.mainloop()

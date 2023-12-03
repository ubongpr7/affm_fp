from math import pi,radians
import threading
import time
from flet import *

class AnimatedBox(UserControl):
    def __init__(self,page:Page,border_color,bg_color,rotate_angle,duration,clockwise):
        super().__init__()
        self.border_color=border_color
        self.bg_color=bg_color
        self.page=page
        self.rotate_angle=rotate_angle
        self.duration=duration
        self.clockwise=clockwise
        

    def build(self):
        return Container(
                width=40,
                height=40,
                border=border.all(2.5,self.border_color),
                bgcolor=self.bg_color,
                rotate=transform.Rotate(
                     self.rotate_angle,
                    alignment.center
                ),
                animate_rotation=animation.Animation(700,'easeInOut')
            )
    def did_mount(self):
        self.running=True
        self.tasker=threading.Thread(target=self.animate_box, daemon=True,args=())
        self.tasker.start()


    def will_unmount(self):
        self.running=False
        
                
    def animate_box(self):
        count=0
        clockwise_= 1 / 2
        ant_clock_wise= - 1 * 2
        while self.running :
        
            if count>=0 and count<=4 : 
                if self.clockwise==True:

                    self.rotate =transform.Rotate(clockwise_ ,alignment.center)

                    clockwise_ +=1 / 2
                    count +=1
                    time.sleep(self.duration)
                    self.update() 
                elif self.clockwise==False:    

                    self.rotate =transform.Rotate(ant_clock_wise ,alignment.center)

                    ant_clock_wise -= 1 / 2
                    count+=1
                    time.sleep(self.duration)
                    self.update()  

            if count>=5 and count<=10  :
                if self.clockwise:
                    clockwise_ -=1 / 2

                    self.rotate =transform.Rotate(clockwise_ ,alignment.center)

                    clockwise_-=1 / 2
                    count+=1
                    time.sleep(self.duration)
                    self.update() 
                elif self.clockwise==False:    
                    ant_clock_wise +=1 / 2

                    self.rotate =transform.Rotate(ant_clock_wise ,alignment.center)

                    ant_clock_wise+=1 / 2
                    count+=1
                    time.sleep(self.duration)
                    self.update() 
            if count==11:
                count=0
                



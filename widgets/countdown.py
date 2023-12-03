import flet as fl
from flet import *
import time,threading
class CountDown(fl.UserControl):
    def __init__(self, seconds,text_info,t_align=None):
        self.text_info=text_info
        self.seconds=seconds
        self.t_align=t_align
        super().__init__()
    def count_down(self):
        while self.seconds!=-1 and self.running:
            mins,secs=divmod(self.seconds,60)
            self.text.value=f'{self.text_info}'+ '{:02d}:{:02d}'.format(mins,secs)
            self.update()
            time.sleep(1)
            self.seconds-=1
            if self.seconds==0:
                self.text.value=f'{self.text_info}'
            
        
    def build(self):
        self.text=Text(color=colors.PRIMARY,text_align='center',size=9)
        return self.text
    def did_mount(self):
        self.running=True
        self.tasker=threading.Thread(target=self.count_down, daemon=True,args=())
        self.tasker.start()


    def will_unmount(self):
        self.running=False
     
from math import pi
from flet import *
import requests

from config.utils import *
from base.app_bar_widget import  *
from widgets.auth_widgets import *
from base.base_ import *
from widgets.buttons_widget import column_set, image_address1 
from widgets.text_widget import *
from config.utils import project_



class  HomePage(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()
        self.page=page
        self.route=f'/{project_}/{routed}'
        self.auth_=auth_
        self.navigation_bar=NavBottom(selfed=self)
        self.bgcolor=colors.SECONDARY_CONTAINER
        self.appbar=LernOnAppBar(selfed=self)
        self.updateables=[]
        self.student_review=ResponsiveRow(controls=[MediumTitleText(text="What our students are saying",font_family='heading')] )
        self.teacher_review=ResponsiveRow(controls=[MediumTitleText(text="Teachers' Review",font_family='heading')], )

        self.large_=MediumTitleText(text='2 million+ registered Students',font_family='heading',color=colors.PRIMARY,boldness=None)
        self.large_left=MediumTitleText(text='11,000+ registered Schools ',font_family='heading',color=colors.PRIMARY,boldness=None)
        self.large_.text_align='center'
        self.left_col=Container(
            border_radius=20,
            border=border.all(0.8,colors.PRIMARY_CONTAINER),
            col=column_set(small_phone=12,land_scape_phone=3),

            padding=10,
            
        content=Column(
            horizontal_alignment='center',

            controls=[
                self.large_left,
                
                SmallTitleText(text="Embrace technology, avoid waste of resources, be more productive with little resources and effort",text_align='end',font_family='styled'),

                Icon(icons.ARROW_DOWNWARD,color=colors.SECONDARY_CONTAINER),
                ElevatedButton(content=SmallTitleText(color='blue',text='Register your school',font_family='styled',boldness='400'))

            ]
        )
        )
        
        self.right_col=Container(
            border_radius=20,
            border=border.all(0.8,colors.PRIMARY_CONTAINER),
            col=column_set(small_phone=12,land_scape_phone=3),

            padding=10,
            
        content=Column(
            horizontal_alignment='center',

            controls=[
                self.large_,
                SmallTitleText(text="Stop wasting time and resouces on crude approach to learning. Simplify the learning process while stillachieving your goals .",text_align='end',font_family='styled'),
                Icon(icons.ARROW_DOWNWARD,color=colors.SECONDARY_CONTAINER),
                ElevatedButton(content=SmallTitleText(color='blue',text='Join Us',font_family='styled',boldness='400'))

            ]
        )
        )
        
        self.center_col1=Column(
            col=column_set(small_phone=12,land_scape_phone=3+3),
            alignment='center',
            horizontal_alignment='center',
            controls=[
            
           
            ]
        )
        
        self.my_row=ResponsiveRow(
                expand=True,
                # col=4+2,
                controls=[
                   self.right_col,
                   self.center_col1,
                   self.left_col,
                        
                        ]
                    )
        self.responsive_size=[]
                      
        self.scroll='adaptive'
        self.main_container=Container(
            # gradient=LinearGradient(
            #     colors=[colors.PRIMARY_CONTAINER,'blue',colors.BLUE_300,colors.SECONDARY,],
            #     stops=[0.2,.7,0.8,1],
            #     begin=alignment.top_left,
            #     # end=Alignment(0.4,1),
            #     tile_mode=GradientTileMode.MIRROR,
            #     rotation=pi/3,

            #     ),
                
                padding=10,               
            content=self.my_row
        )

        self.controls =[     
            self.main_container,
            self.student_review,
            Container(bgcolor=colors.SECONDARY_CONTAINER,content=self.teacher_review)
        ]
        self.slides=[]
        self.i=0
        self.back_=IconButton(icon=icons.ARROW_BACK_IOS,tooltip='previous',icon_color=colors.BLUE,on_click=self.prev_slide)

        self.next_=IconButton(icon=icons.ARROW_FORWARD_IOS,tooltip='next',icon_color=colors.BLUE,on_click=self.next_slide)
        self.slide_=[]
        
    def did_mount(self):
        self.running=True
            
        self.tasker_1=threading.Thread(target=self.bg_task, daemon=True,args=())
        self.tasker_1.start()
        self.tasker_2=threading.Thread(target=self.show_slides, daemon=True,args=())
        self.tasker_2.start()
        
    def will_unmount(self):
        self.running=False
    
    def user_review(self,rating,message,reviewer,profile):
        stars=Row(spacing=0,alignment='center')
        if rating>3:
            color_=colors.GREEN
        else:
            color_=colors.YELLOW

        for i in range(rating):
            stars.controls.append(Icon(icons.STAR,color=color_,size=14))
        return Container(

             gradient=LinearGradient(
                colors=[colors.ON_PRIMARY,colors.PRIMARY_CONTAINER,colors.PRIMARY_CONTAINER,colors.ON_SECONDARY,],
                stops=[0.5,.7,0.8,.9],
                begin=alignment.top_left,
                # end=Alignment(0.4,1),
                tile_mode=GradientTileMode.MIRROR,
                rotation=pi/3,

                ),
                # blend_mode=BlendMode.EXCLUSION,
           
            border=border.all(0.8,colors.PRIMARY_CONTAINER),
            border_radius=20,
            padding=10,
            col=column_set(small_phone=4+2,land_scape_phone=4,desktop=3),
            content=Column(
            controls=[
                stars,
                MediumBodyText(text=message,text_align='start',color=colors.PRIMARY),
                Row(
                    controls=[TextButton(content=MediumBodyText(text=reviewer,color=colors.PRIMARY),),])
            ]

                )

            )
    
    def bg_task(self):
        if is_authenticated(self=self):
            self.drawer=LeftSideBar(selfed=self)

        for i in range(4):
            self.student_review.controls.append(self.user_review(rating=1+i,message='I love LernOn, it is the best platform for learning',reviewer='Ubong Prosper',profile='Link to profile'))
        self.student_review.update()    

    def show_slides(self):
        
        for i in range(4,11):
            self.slides.append(self.slide_show(some_='LernOn Edu Solutions',sub_title='Learning should be fun and exciting ',image_name=f'affm{i}',slides=len(self.slides)))
        
        while self.running:
            
            for i in range(len(self.slides)):
                self.i=i    
                self.center_col1.controls=[
                        self.slides[self.i],
                        ]


                if self.i==len(self.slides)-1:
                    self.next_.tooltip='Last'
                    self.next_.disabled=True
                    self.next_.icon_color=colors.PRIMARY


                else:
                    self.next_.tooltip='Next'
                    self.next_.disabled=False
                    self.next_.icon_color=colors.BLUE

                if self.i ==0:
                    self.back_.icon_color=colors.PRIMARY

                    self.back_.tooltip='First'
                    self.back_.disabled=True

                    
                else:
                    self.back_.tooltip='Previous'
                    self.back_.disabled=False
                    self.back_.icon_color=colors.BLUE
            
                self.center_col1.update()

                time.sleep(15)
        
    def slide_show(self,some_ , image_name,slides,sub_title):
        slide_btn=Row(alignment='center',spacing=0)
        for i in range(slides):
            slide_btn.controls.append(IconButton(icon=icons.DONUT_SMALL,icon_size=10,icon_color=colors.PRIMARY))
            # self.slide.update()  

        return Container(
            height=300,
            image_src=image_address1(name=image_name),
            image_fit=ImageFit.FIT_WIDTH,
            border=border.all(0.8,colors.PRIMARY_CONTAINER),
            border_radius=20,
            padding=20,
            content=ResponsiveRow(

                vertical_alignment='center',
                
                controls=[
                    Row(height=50),
                   Container(
                       padding=20,
                        border=border.all(0.8,colors.PRIMARY_CONTAINER),
                        # border_radius=20,
                       height=150,

                        bgcolor=colors.with_opacity(opacity=0.7,color=colors.PRIMARY_CONTAINER),
                       content=Row(
                        alignment=MainAxisAlignment.CENTER,

                      controls=[
                          
                    PageHeading_3(main_title=some_,main_size=20,sub_size=12,sub_title=sub_title,bg_color=colors.SECONDARY_CONTAINER,text_color=colors.PRIMARY),
                    # Row(height=25),
                          
                      ] 
                   ) ,
                
                   ),
                   
                    # Container(
                    #     bgcolor=colors.with_opacity(color=colors.PRIMARY_CONTAINER,opacity=0.3),
                    # content=slide_btn,
                    # ),

                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls= [
                            self.back_,
                            self.next_,


                    ]),
                    
                    
                ],
            )
        )   
    
    def prev_slide(self,e):
        
        self.i -=1
        self.center_col1.controls=[
            self.slides[self.i],
                        ]
        
        self.center_col1.update()
        
        if self.i==len(self.slides)-1:
            self.next_.tooltip='Last'
            self.next_.disabled=True
            self.next_.icon_color=colors.PRIMARY
            self.center_col1.update()


        else:
            self.next_.tooltip='Next'
            self.next_.disabled=False
            self.next_.icon_color=colors.BLUE
            self.center_col1.update()

        if self.i ==0:
            self.back_.icon_color=colors.PRIMARY

            self.back_.tooltip='First'
            self.back_.disabled=True
            self.center_col1.update()

            
        else:
            self.back_.tooltip='Previous'
            self.back_.disabled=False
            self.back_.icon_color=colors.BLUE
            self.center_col1.update()

    def next_slide(self,e):
        if self.i<len(self.slides):

            self.i +=1
        else:
            pass
        self.center_col1.controls=[
            self.slides[self.i],
                        ]
        
        if self.i==len(self.slides)-1:
            self.next_.tooltip='Last'
            self.next_.disabled=True
            self.next_.icon_color=colors.PRIMARY
            self.center_col1.update()


        else:
            self.next_.tooltip='Next'
            self.next_.disabled=False
            self.next_.icon_color=colors.BLUE
            self.center_col1.update()

        if self.i ==0:
            self.back_.icon_color=colors.PRIMARY

            self.back_.tooltip='First'
            self.back_.disabled=True
            self.center_col1.update()

            
        else:
            self.back_.tooltip='Previous'
            self.back_.disabled=False
            self.back_.icon_color=colors.BLUE
            self.center_col1.update()

       
        
        self.center_col1.update()

    def logout_user(self,e):
        logout_user(self=self) 

           

from flet import *

class PageHeading_2(UserControl):
    def __init__(self,main_title,main_size, sub_title,sub_size,bg_color,text_color,):
        super().__init__()
        self.main_title=main_title
        self.bg_color=bg_color
        self.sub_title=sub_title
        self.text_color=text_color
        self.main_size=main_size
        self.sub_size=sub_size

    def build(self):
        return Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=5,
            controls=[
                Text(value=self.main_title, color=self.text_color, size=self.main_size,weight='bold'),
                Text(
                    value=self.sub_title,
                    size=self.sub_size,
                    weight='bold',
                    color=self.text_color,
                    font_family='styled'
                )
            ]

        )


class PageHeading_3(ResponsiveRow):
    def __init__(self,main_title,main_size, sub_title,sub_size,bg_color,text_color,):
        super().__init__()
        self.main_title=main_title
        self.bg_color=bg_color
        self.sub_title=sub_title
        self.text_color=text_color
        self.main_size=main_size
        self.sub_size=sub_size
        self.expand=1
        # self.height=200 

    
        self.controls=[ 
            
                
                Text(value=self.main_title, color=self.text_color, size=self.main_size,weight='bold',text_align='center'),
                    
               
                Text(
                    value=self.sub_title,
                    size=self.sub_size,
                    weight='bold',
                    color=self.text_color,
                    font_family='styled',
                    text_align='center'
                )
            

        ]

    
    
class LargeDisplayText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.DISPLAY_LARGE
        self.weight=boldness
        self.size=50
        self.font_family=font_family
        self.color=color
        self.text_align=text_align

            
class MediumDisplayText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.DISPLAY_MEDIUM
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align


class SmallDisplayText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.DISPLAY_SMALL
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align


class LargeHeadlineText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.HEADLINE_LARGE
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align


class MediumHeadlineText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.HEADLINE_MEDIUM
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align


class LargeTitleText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.TITLE_LARGE
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align
        self.text_align=text_align

            
            
class MediumTitleText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.TITLE_MEDIUM
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align
            
class SmallTitleText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.TITLE_SMALL
        self.weight=boldness
        self.font_family=font_family
        self.color=color
            
class LargeLabelText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.text_align=text_align
        self.value=text
        self.style=TextThemeStyle.LABEL_LARGE
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align


            
class MediumLabelText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.text_align=text_align
        self.value=text
        self.style=TextThemeStyle.LABEL_MEDIUM
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align

            
            
class SmallLabelText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.text_align=text_align
        self.value=text
        self.text_align=text_align
        self.style=TextThemeStyle.LABEL_SMALL
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align

            
class LargeBodyText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.BODY_LARGE
        self.text_align=text_align
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align

            
class MediumBodyText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.value=text
        self.style=TextThemeStyle.BODY_MEDIUM
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align
            
            
class SmallBodyText(Text):
    def __init__(self, text='',boldness=None,font_family=None,color=colors.PRIMARY,text_align='center'):
        super().__init__()
        self.text_align=text_align
        self.value=text
        self.style=TextThemeStyle.BODY_SMALL
        self.weight=boldness
        self.font_family=font_family
        self.color=color
        self.text_align=text_align

            
            

            
            

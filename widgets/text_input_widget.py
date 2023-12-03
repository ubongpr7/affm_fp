from flet import *


def code_verifier(code):
    password=code.value
    if len(password)!=0:
        
            try:
                
                int(password)

                code.error_text=''

                code.valid=True

                code.update()
            except:
                code.error_text=f'Numbers  only'
                code.value=""
                code.update()
   
class NumberInput(TextField):
    def __init__(self,type=None,field_hint=None,prefix_=None,suffix=None,col=None):
        super().__init__()
        self.hint_text=field_hint
        self.type=type
        self.valid=False
        self.prefix_text=prefix_
        self.suffix_text=suffix        
        self.width=150     
        self.color=colors.PRIMARY
        self.border_color='transparent'
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.cursor_color=colors.PRIMARY
        self.text_size=12,
        self.col=col
        self.content_padding=5
        self.text_align=TextAlign.CENTER
        self.hint_style=TextStyle(size=12,color=colors.PRIMARY,)
        self.on_change=self.validators        
            
    def validators(self,e):
        
        if self.type=='num':
            return code_verifier(code=self)
                
        
class ReadonlyTextInput(TextField):
    def __init__(self,type,value,):
        super().__init__()
        self.type=type
        self.valid=False
        self.value=value
        self.read_only=True

        
        self.width=150     
        self.color=colors.PRIMARY
        self.border_color='transparent'
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.cursor_color=colors.PRIMARY
        self.text_size=12,
        self.content_padding=5
        self.text_align=TextAlign.CENTER
        self.hint_style=TextStyle(size=12,color=colors.PRIMARY,)
        self.on_change=self.validators        
            
    def validators(self,e):
        
        if self.type=='read':
            # return code_verifier(code=self)
            pass
                
        
class TextInput(TextField):
    def __init__(self,type,field_hint,prefix_=None,suffix=None,tooltip=None,col=None):
        super().__init__()
        self.hint_text=field_hint
        self.type=type
        self.valid=False
        self.prefix_text=prefix_
        self.suffix_text=suffix 
        self.tooltip=tooltip
        self.col=col       

        self.multiline=True
        self.width=150     
        self.color=colors.PRIMARY
        self.border_color='transparent'
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.cursor_color=colors.PRIMARY
        self.text_size=12,
        self.content_padding=5
        # self.text_align=TextAlign.CENTER
        self.hint_style=TextStyle(size=12,color=colors.PRIMARY,)
        self.on_change=self.validators        
            
    def validators(self,e):
        
        if self.type=='text':
            # return code_verifier(code=self)
            pass
                
        

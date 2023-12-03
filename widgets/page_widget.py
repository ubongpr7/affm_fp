from flet import *

def sections_container(self,controls,bgcolor=colors.SECONDARY_CONTAINER,border=None,border_radius=20,padding=20):
        return Container(
            bgcolor=bgcolor,
            border=border,
            padding=padding,
            
            border_radius=border_radius,
            col=12,
            content=ResponsiveRow(
                controls=controls
            )
        )      

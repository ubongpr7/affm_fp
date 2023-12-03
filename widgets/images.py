from flet import *

def width_fitted_image(src):
    return Image(
            src=src,
            fit=ImageFit.FIT_WIDTH,
        )
def height_fitted_image(src):
    return Image(
            src=src,
            fit=ImageFit.FIT_HEIGHT,
        )
def container_fitted_image(src):
    return Image(
            src=src,
            fit=ImageFit.CONTAIN,
        )
def affm_logo(selfed):
    if selfed.page.client_storage.get('logo'):
        return selfed.page.client_storage.get('logo')
    else:
        return  'images/logos/lernon_logowl.svg'
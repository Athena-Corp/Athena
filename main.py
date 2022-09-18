from PySimpleGUI import *
from config import ATHENA_THEME, FONT, FONT_NAME
from time import sleep

LOOK_AND_FEEL_TABLE['Athena'] = ATHENA_THEME
theme('Athena')

layout = [
    [VPush()],
    [Push(), Text('Athena', font=(FONT_NAME, 26)), Text('by Athena Corp.', font=(FONT_NAME, 12, 'bold'), text_color='grey'), Push()],
    [HSeparator()],
    [Button('DÉMARRER', expand_x=True, key='START')],
    [VPush()]
]
window = Window('Athena', layout, font=FONT, size=(1000, 500))

while True:
    event, values = window.read()
    if event in (WIN_CLOSED, 'Cancel'):
        break
    if event == 'START':

        # EFFET FONDU
        for _ in range(100):
            window.alpha_channel -= .01
            sleep(.01)

window.close()

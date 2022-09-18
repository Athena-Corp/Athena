from PySimpleGUI import *

from config import ATHENA_THEME, FONT_NAME, FONT


LOOK_AND_FEEL_TABLE['Athena'] = ATHENA_THEME
theme('Athena')

state = {
    'Module1': False,
    'Module2': False,
    'Module3': True,
    'Module4': False,
    'Module5': False,
    'Module6': True
}

modules = []
for m, is_on in state.items():
    modules.append(
        [Text(m, pad=(45, 0)), Push(), Button(' ' * 25, key=m, button_color=('green', 'red')[state[m]]),
         Button(image_filename='images/settings.png', image_subsample=7, k=f'{m}_settings'.lower())])

layout = [
    [Push(), Text('Modules', font=(FONT_NAME, 25, 'bold')), Push()],
    [HSeparator()],
    [Column(modules, scrollable=True, vertical_scroll_only=True, size=(500, 300))]
]
window = Window('Athena', layout, font=FONT, use_custom_titlebar=True, keep_on_top=True)
while True:
    event, values = window.read()
    if event in (WIN_CLOSED, 'Cancel'):
        break
    if event in state.keys():
        state[event] = not state[event]
        window[event].update(button_color=('green', 'red')[state[event]])


window.close()

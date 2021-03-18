#!usr/bin/python
import os
if __name__ == '__main__':
    res = os.popen('xinput list | grep -i Touchpad').read()
    touchpad_id = res.split('id=')[1].split('\t')[0]
    res = os.popen('xinput --list-props {} | grep -i middle'.format(touchpad_id)).read()
    setting_val = res.split('Emulation Enabled (')[1].split(')')[0]
    os.system('xinput --set-prop {} {} 1'.format(touchpad_id, setting_val))
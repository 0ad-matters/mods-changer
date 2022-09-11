import time
import subprocess
import re
# mod.enabledmods
whynot = "boonGUI-with-working-hardcoded-beepIdle" 
whynot += " whynot autociv-2021-0824 HostEnhanced better_summary_charts" #  customrating0.25.2

KateGUIv5 = "boonGUI-with-working-hardcoded-beepIdle HostEnhanced autociv-KateGUIv5 better_summary_charts customrating0.25.2"  # 

StarGUI7 = "StarGUI7 boonGUI-with-working-hardcoded-beepIdle"  # customrating0.25.2

plus = "boonGUI-with-working-hardcoded-beepIdle" 
plus += "10ad cartographymode customrating0.25.2"

# whynot dog is little (normal size)
# KateGUIv5 dog also small ?
# StarGUI7 dog very small. good to see :) 

choices = [ KateGUIv5, whynot, StarGUI7, plus ]
retCode, choice = dialog.list_menu(choices, title="Choose mods", message="good luck ;)", default=None,  geometry="800x400" )
if retCode == 0:
    # keyboard.send_keys("" + choice)
    clipboard.fill_clipboard( choice )

    kate = "kate"
    userCfg = "~/snap/0ad/current/.config/0ad/config/user.cfg"

    with open (userCfg, 'r+' ) as f:
        content = f.read()
        f.truncate(0)
        f.write(re.sub('^mod\.enabledmods[^\n]+', r'mod.enabledmods = "mod public ' + choice + '"', content, flags = re.M))
        #f.truncate()
        f.close()

    # p2 = subprocess.Popen( [ kate, userCfg ] ) # works 22-0911_1150-40

    p3 = subprocess.Popen(['killall' ,'main']) # works :) 22-0911_1153-11

    if window.wait_for_exist(': fish',0):
        window.activate(': fish')
    else:
        window.activate(': fish') # sometimes needet 22-02-15_0725-2545
        window.activate(': bash')
        time.sleep(0.1)        
        winClass = window.get_active_class()
        if winClass != 'konsole.konsole':
            window.activate(' : ')
    time.sleep(.4)

    keyboard.send_keys("killall main; 0ad >/dev/null 2>&1 & pwd; <enter>")

    time.sleep(.5)
    window.resize_move('0 A.D.', xOrigin=1908, yOrigin=-27, width=1922, height=1089, matchClass=False)

    time.sleep(.5)
    window.resize_move('0 A.D.', xOrigin=1908, yOrigin=-27, width=1922, height=1089, matchClass=False)
    



from ahk import AHK,  Hotkey

ahk = AHK(executable_path="D:\Program Files\AutoHotkey\AutoHotkey.exe")

key_combo = '#q' # Define an AutoHotkey key combonation
script = 'MsgBox, win+q' # Define an ahk script
hotkey = Hotkey(ahk, key_combo, script) # Create Hotkey
hotkey.start()  #  Start listening for hotkey
# hotkey.stop() 停止脚本
#
key_combo = '#w' # Define an AutoHotkey key combonation
script = 'Send, ^a' # Define an ahk script
hotkey = Hotkey(ahk, key_combo, script) # Create Hotkey
hotkey.start()  #  Start listening for hotkey


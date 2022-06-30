from  ahk import  AHK

ahk = AHK(executable_path="D:\Program Files\AutoHotkey\AutoHotkey.exe")

ahk.mouse_move(x=100, y=100, blocking=True)  # Blocks until mouse finishes moving (the default)
ahk.mouse_move(x=150, y=150, speed=10, blocking=True) # Moves the mouse to x, y taking 'speed' seconds to move
print(ahk.mouse_position)  #  (150, 15j0)

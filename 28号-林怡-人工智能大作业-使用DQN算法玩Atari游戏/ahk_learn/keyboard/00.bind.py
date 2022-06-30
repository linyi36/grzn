from ahk import AHK

ahk = AHK(executable_path="D:\Program Files\AutoHotkey\AutoHotkey.exe")

ahk.type('hello, world!')  # Send keys, as if typed (performs ahk string escapes)
ahk.send_input('Hello`, World{!}')  # Like AHK SendInput, must escape strings yourself!
ahk.key_state('Control')  # Return True or False based on whether Control key is pressed down
ahk.key_state('CapsLock', mode='T')  # Check toggle state of a key (like for NumLock, CapsLock, etc)
ahk.key_press('a')  # Press and release a key
ahk.key_down('Control')  # Press down(but do not release) Control key
ahk.key_wait('a', timeout=3)  # Wait up to 3 seconds for the "a" key to be pressed. NOTE: This throws
                              # a TimeoutError if the key isn't pressed within the timeout window
ahk.key_up('Control')  # Release the key

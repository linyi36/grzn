from ahk import AHK

ahk = AHK(executable_path="D:\Program Files\AutoHotkey\AutoHotkey.exe")

ahk.sound_play('C:\\path\\to\\sound.wav')  # Play an audio file
ahk.sound_beep(frequency=440, duration=1000)  # Play a beep for 1 second (duration in microseconds)
ahk.get_volume(device_number=1)  # Get volume of a device
ahk.set_volume(50, device_number=1)  # Set volume of a device
ahk.sound_get(device_number=1, component_type='MASTER', control_type='VOLUME') # Get sound device property
ahk.sound_set(50, device_number=1, component_type='MASTER', control_type='VOLUME') # Set sound device property
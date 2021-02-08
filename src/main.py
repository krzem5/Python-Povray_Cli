import subprocess
import os



EXE_FILE_PATH="D:\\K\\Downloads\\povray\\povray\\windows\\vs10\\bin64\\povconsole64.exe"



with open("./__tmp.ini","w") as f:
	f.write("Width=960\nHeight=540\n")
subprocess.run([EXE_FILE_PATH,"C:\\Users\\aleks\\AppData\\Local\\Temp\\__povray\\include","__tmp.ini","C:\\Users\\aleks\\AppData\\Local\\Temp\\__povray\\scenes\\subsurface\\subsurface.pov","out.png"])

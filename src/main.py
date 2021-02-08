import subprocess
import os



EXE_FILE_PATH="D:\\K\\Downloads\\povray\\povray\\windows\\vs10\\bin64\\povconsole64.exe"



with open("./__tmp.ini","w") as f:
	f.write("Library_Path=C:\\Users\\aleks\\AppData\\Local\\Temp\\__povray\\include\nWidth=200\nHeight=200\nOutput_File_Name=__out.tmp\nDisplay=true\nInput_File_Name=C:\\Users\\aleks\\AppData\\Local\\Temp\\__povray\\scenes\\subsurface\\subsurface.pov\nOutput_To_File=true\n")
subprocess.run([EXE_FILE_PATH,"__tmp.ini"])

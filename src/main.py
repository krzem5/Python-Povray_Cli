import subprocess
import os



with open("./__tmp.ini","w") as f:
	f.write("Library_Path=C:\\Users\\aleks\\AppData\\Local\\Temp\\__povray\\include\nWidth=200\nHeight=200\nOutput_File_Name=__out.tmp\nInput_File_Name=C:\\Users\\aleks\\AppData\\Local\\Temp\\__povray\\scenes\\subsurface\\subsurface.pov\nOutput_To_File=true\n")
subprocess.run(["D:\\K\\Downloads\\povray\\povray\\windows\\vs10\\bin64\\povconsole64.exe","__tmp.ini"])
os.remove("__tmp.ini")

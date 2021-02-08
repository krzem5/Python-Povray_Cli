import subprocess
import os
import ctypes



EXE_FILE_PATH="D:\\K\\Downloads\\povray\\povray\\windows\\vs10\\bin64\\povconsole64.exe"
GENERIC_READ=0x80000000



with open("./__tmp.ini","w") as f:
	f.write("Width=400\nHeight=400\nOutput_File_Name=__out.tmp\n")
# p=subprocess.Popen([EXE_FILE_PATH,"C:\\Users\\aleks\\AppData\\Local\\Temp\\__povray\\include","__tmp.ini","C:\\Users\\aleks\\AppData\\Local\\Temp\\__povray\\scenes\\subsurface\\subsurface.pov"])
fh=ctypes.windll.kernel32.CreateFileW("__out.tmp.pov-state",GENERIC_READ,FILE_SHARE_READ,NULL,OPEN_EXISTING,FILE_FLAG_OVERLAPPED|FILE_FLAG_NO_BUFFERING,NULL)
ctypes.windll.kernel32.CloseHandle(fh)

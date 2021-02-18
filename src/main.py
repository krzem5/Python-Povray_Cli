import atexit
import ctypes
import ctypes.wintypes
import os
import subprocess
import sys
import tkinter
import time
import threading
from PIL import Image,ImageTk



BUFFER_SIZE=2048
IGNORE_TIME=0.05
RENDER_SIZE=(960,540)



FILE_ACTION_MODIFIED=3
FILE_FLAG_BACKUP_SEMANTICS=0x2000000
FILE_FLAG_OVERLAPPED=0x40000000
FILE_LIST_DIRECTORY=1
FILE_NOTIFY_CHANGE_LAST_WRITE=0x10
FILE_NOTIFY_CHANGE_LAST_WRITE=0x10
FILE_SHARE_DELETE=0x4
FILE_SHARE_READ=0x1
FILE_SHARE_WRITE=0x2
INFINITE=0xffffffff
INVALID_HANDLE_VALUE=0xffffffffffffffff
MAX_PATH=260
OPEN_EXISTING=3
WAIT_OBJECT_0=0



ctypes.wintypes.ULONG_PTR=ctypes.POINTER(ctypes.wintypes.DWORD)
ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO=type("CONSOLE_SCREEN_BUFFER_INFO",(ctypes.Structure,),{"_fields_":[("dwSize",ctypes.wintypes._COORD),("dwCursorPosition",ctypes.wintypes._COORD),("wAttributes",ctypes.wintypes.WORD),("srWindow",ctypes.wintypes.SMALL_RECT),("dwMaximumWindowSize",ctypes.wintypes._COORD)]})
ctypes.wintypes.FILE_NOTIFY_INFORMATION=type("FILE_NOTIFY_INFORMATION",(ctypes.Structure,),{"_fields_":[("NextEntryOffset",ctypes.wintypes.DWORD),("Action",ctypes.wintypes.DWORD),("FileNameLength",ctypes.wintypes.DWORD),("FileName",ctypes.wintypes.WCHAR*MAX_PATH)]})
ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME=type("OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME",(ctypes.Structure,),{"_fields_":[("Offset",ctypes.wintypes.DWORD),("OffsetHigh",ctypes.wintypes.DWORD)]})
ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME=type("OVERLAPPED_DUMMYUNIONNAME",(ctypes.Union,),{"_fields_":[("_0",ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME),("Pointer",ctypes.wintypes.LPVOID)],"_anonymous_":["_0"]})
ctypes.wintypes.OVERLAPPED=type("OVERLAPPED",(ctypes.Structure,),{"_fields_":[("Internal",ctypes.wintypes.ULONG_PTR),("InternalHigh",ctypes.wintypes.ULONG_PTR),("_0",ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME),("hEvent",ctypes.wintypes.HANDLE)],"_anonymous_":["_0"]})
ctypes.wintypes.PCONSOLE_SCREEN_BUFFER_INFO=ctypes.POINTER(ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO)
ctypes.wintypes.LPOVERLAPPED=ctypes.POINTER(ctypes.wintypes.OVERLAPPED)
ctypes.wintypes.LPOVERLAPPED_COMPLETION_ROUTINE=ctypes.c_void_p
ctypes.wintypes.LPSECURITY_ATTRIBUTES=ctypes.c_void_p
ctypes.windll.kernel32.CloseHandle.argtypes=(ctypes.wintypes.HANDLE,)
ctypes.windll.kernel32.CloseHandle.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.CreateEventW.argtypes=(ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.BOOL,ctypes.wintypes.BOOL,ctypes.wintypes.LPCWSTR)
ctypes.windll.kernel32.CreateEventW.restype=ctypes.wintypes.HANDLE
ctypes.windll.kernel32.CreateFileW.argtypes=(ctypes.wintypes.LPCWSTR,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.HANDLE)
ctypes.windll.kernel32.CreateFileW.restype=ctypes.wintypes.HANDLE
ctypes.windll.kernel32.FillConsoleOutputAttribute.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.WORD,ctypes.wintypes.DWORD,ctypes.wintypes._COORD,ctypes.wintypes.LPDWORD)
ctypes.windll.kernel32.FillConsoleOutputAttribute.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.FillConsoleOutputCharacterA.argtypes=(ctypes.wintypes.HANDLE,ctypes.c_char,ctypes.wintypes.DWORD,ctypes.wintypes._COORD,ctypes.wintypes.LPDWORD)
ctypes.windll.kernel32.FillConsoleOutputCharacterA.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.GetConsoleScreenBufferInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PCONSOLE_SCREEN_BUFFER_INFO)
ctypes.windll.kernel32.GetConsoleScreenBufferInfo.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.GetStdHandle.argtypes=(ctypes.wintypes.DWORD,)
ctypes.windll.kernel32.GetStdHandle.restype=ctypes.wintypes.HANDLE
ctypes.windll.kernel32.ReadDirectoryChangesW.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPVOID,ctypes.wintypes.DWORD,ctypes.wintypes.BOOL,ctypes.wintypes.DWORD,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPOVERLAPPED,ctypes.wintypes.LPOVERLAPPED_COMPLETION_ROUTINE)
ctypes.windll.kernel32.ReadDirectoryChangesW.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.ResetEvent.argtypes=(ctypes.wintypes.HANDLE,)
ctypes.windll.kernel32.ResetEvent.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetConsoleCursorPosition.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes._COORD)
ctypes.windll.kernel32.SetConsoleCursorPosition.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.WaitForSingleObject.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD)
ctypes.windll.kernel32.WaitForSingleObject.restype=ctypes.wintypes.DWORD



def run(fp):
	def _render(b,td,fp):
		def _run_r(b,td,fp):
			ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
			dt=""
			if (os.path.exists(f"{fp[:-3]}ini")):
				with open(f"{fp[:-3]}ini","r") as f:
					dt=f.read()
			with open(f"{td}/__tmp.ini","w") as f:
				f.write(f"{dt}\nLibrary_Path={b}/bin/lib/include\nWidth={RENDER_SIZE[0]}\nHeight={RENDER_SIZE[1]}\nOutput_File_Name={td}/__out.png\nInput_File_Name={fp}\nOutput_To_File=true\nVerbose=false\nWarning_Console=false\nDebug_Console=false\nRender_Console=false\nStatistic_Console=false\n")
			o=subprocess.run([f"{b}/bin/pov.exe",f"{td}/__tmp.ini"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.strip().replace(b"\r\n",b"\n")[:-14]
			os.remove(f"{td}/__tmp.ini")
			if (os.path.exists(f"{td}/__out.png")):
				r.geometry(f"{RENDER_SIZE[0]}x{RENDER_SIZE[1]}+{w-RENDER_SIZE[0]}+{h-RENDER_SIZE[1]}")
				img=Image.open(f"{td}/__out.png")
				img=img.resize((w//4,h//4))
				r._im=ImageTk.PhotoImage(image=img)
				img.close()
				os.remove(f"{td}/__out.png")
			else:
				r.geometry(f"{RENDER_SIZE[0]}x{RENDER_SIZE[1]}+{w}+{h}")
				sys.__stdout__.write(str(o,"utf-8"))
		thr=threading.Thread(target=_run_r,args=(b,td,fp),kwargs={})
		thr.daemon=True
		thr.start()
	def _read_dc(fp):
		fp=os.path.abspath(fp)
		d="/".join(fp.replace("\\","/").split("/")[:-1])
		f=fp[len(d)+1:]
		b=os.path.abspath("/".join(__file__.replace("\\","/").split("/")[:-1])+"/../")
		td=os.path.abspath((os.getenv("TEMP") if os.getenv("TEMP") else os.getenv("TMP"))).replace("\\","/")
		_render(b,td,fp)
		dh=ctypes.windll.kernel32.CreateFileW(d,FILE_LIST_DIRECTORY,FILE_SHARE_READ|FILE_SHARE_WRITE|FILE_SHARE_DELETE,0,OPEN_EXISTING,FILE_FLAG_BACKUP_SEMANTICS|FILE_FLAG_OVERLAPPED,0)
		if (dh!=INVALID_HANDLE_VALUE):
			atexit.register(lambda:ctypes.windll.kernel32.CloseHandle(dh))
			bf=ctypes.create_string_buffer(BUFFER_SIZE)
			ov=ctypes.wintypes.OVERLAPPED()
			ov.hEvent=ctypes.windll.kernel32.CreateEventW(0,True,False,None)
			ig_tm=0
			dt=ctypes.wintypes.FILE_NOTIFY_INFORMATION()
			while (True):
				ctypes.windll.kernel32.ReadDirectoryChangesW(dh,bf,BUFFER_SIZE,False,FILE_NOTIFY_CHANGE_LAST_WRITE,ctypes.byref(ctypes.wintypes.DWORD()),ctypes.byref(ov),0)
				if (ctypes.windll.kernel32.WaitForSingleObject(ov.hEvent,INFINITE)==WAIT_OBJECT_0):
					ctypes.windll.kernel32.ResetEvent(ov.hEvent)
					if (ig_tm>time.time()):
						continue
					ig_tm=time.time()+IGNORE_TIME
					i=0
					while (True):
						ctypes.memmove(ctypes.addressof(dt),bf[i:],min(ctypes.sizeof(dt),len(bf)-i))
						if (dt.Action==FILE_ACTION_MODIFIED and dt.FileName[:dt.FileNameLength//ctypes.sizeof(ctypes.wintypes.WCHAR)]==f):
							_render(b,td,fp)
						if (dt.NextEntryOffset==0):
							break
						else:
							i=dt.NextEntryOffset
	def _render_loop():
		if (r._im is not None):
			c.delete(tkinter.ALL)
			c.create_image(0,0,image=r._im,anchor=tkinter.NW)
			r._t_im=r._im
			r._im=None
		r.after(1000//60,_render_loop)
	sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
	ho=ctypes.windll.kernel32.GetStdHandle(-11)
	ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
	ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
	ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
	ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
	thr=threading.Thread(target=_read_dc,args=(fp,),kwargs={})
	thr.daemon=True
	thr.start()
	r=tkinter.Tk()
	r.attributes("-topmost",True)
	r.resizable(False,False)
	r.overrideredirect(True)
	r.bind("<Escape>",lambda _:r.destroy())
	w=r.winfo_screenwidth()
	h=r.winfo_screenheight()
	r.geometry(f"{RENDER_SIZE[0]}x{RENDER_SIZE[1]}+{w}+{h}")
	c=tkinter.Canvas(r,width=RENDER_SIZE[0],height=RENDER_SIZE[1],highlightthickness=0,background="#000000",cursor="tcross")
	c.pack()
	r.update_idletasks()
	r._im=None
	r.after(1000//60,_render_loop)
	r.mainloop()



run(sys.argv[1])

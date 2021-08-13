import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from playsound import playsound

class ExtractAudio:
	def settings(self):
		self.root.geometry('400x250')
		self.root.resizable(False,False)
		self.root.title(self.title)
		self.root.config(bg='skyblue')


	def ask_dir(self):
		self.dir = fd.askdirectory(title='Choise your Dir')
		self.btn_dir.configure(text=self.dir)


	def ask_file(self):
		self.file = fd.askopenfile(title='Choise your Video',filetypes=[("Video files","*.mp4;*.avi")])
		self.btn_file_dialog.configure(text=self.file.name.split('/')[-1])
	

	def items(self):
		self.label = Label(self.root,text='Choise your video to extract',font=('Abscissa',15,'bold'),bg='skyblue')
		self.label_path = Label(self.root,text='Select Your Directory you want to get the audio',font=('Abscissa',15,'bold'),bg='skyblue')
		self.btn_file_dialog = Button(self.root,text='Choise File',command=self.ask_file,font=('Abscissa',12,'bold'),border=2,borderwidth=5) 
		self.btn_dir = Button(self.root,text='Choise Directory',command=self.ask_dir,font=('Abscissa',12,'bold'),border=2,borderwidth=5) 
		self.btn_extract = Button(self.root,text='Extract Audio',command=self.extract,font=('Abscissa',12,'bold'),border=2,borderwidth=5) 


	def pack_items(self):
		self.label.grid(row=0,column=0,padx=5,pady=5,sticky='W')
		self.btn_file_dialog.grid(row=1,column=0,padx=5,pady=5,sticky='W')
		self.label_path.grid(row=2,column=0,padx=5,pady=5,sticky='W')
		self.btn_dir.grid(row=3,column=0,padx=5,pady=5,sticky='W')
		self.btn_extract.grid(row=4,column=0,padx=5,pady=5,sticky='W')

	def extract(self):
		if not (self.file and self.dir):
			messagebox.showerror('Error','Choise file and directory')
		else:
			path = self.file.name.replace('/','\\')
			filname = path.split('\\')[-1]
			name = filname.split('.mp4')[0]
			the_clip = mp.VideoFileClip(r'{}'.format(path))
			if self.dir.endswith('/'):
				real_file_name = self.dir + name
			else:
				real_file_name = self.dir +'\\'+ name
			real_file_name = real_file_name.replace('/','\\') + '.mp3'
			print(real_file_name)
			the_clip.audio.write_audiofile(r'{}'.format(real_file_name))
			action = messagebox.showinfo(title='Done',message="The auido extracted in {} file".format(real_file_name))
			# if action:
			# 	playsound(real_file_name)

	def __init__(self,title):
		self.file = None
		self.dir = None
		self.root = Tk()
		self.title = title
		self.settings()
		self.items()
		self.pack_items()


	def __call__(self):
		self.root.mainloop()



instance = ExtractAudio('Extract Audio from Video')
if __name__ == '__main__':
	instance()

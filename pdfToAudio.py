import PyPDF2
from gtts import gTTS
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk

text = ""
window = Tk()
window.title("AudiobookAI")
window.geometry('145x210')

def pdf_():
	global text
	filelocation = askopenfilename()
	book = open(filelocation, 'rb')
	pdfreader = PyPDF2.PdfFileReader(book)
	for pagenum in range(pdfreader.numPages):
		pageObj = pdfreader.getPage(pagenum)
		text += pageObj.extractText()
	book.close()


def audio_():
	tts = gTTS(text = text, lang = 'en')
	tts.save("audio.mp3")



tab_control = ttk.Notebook(window)
tab2 = Frame(tab_control)
tab_control.add(tab2, text='PDF')



label1 = Label(tab2, text = "Select a pdf file", font = ("Arial", 15),background = 'white')
label1.grid(row = 0, column = 0, sticky=E+W)

button1 = Button(tab2, text = "Open",command = pdf_)
button1.grid(pady = 10,row = 4)
button1 = Button(tab2, text = "Convert",command =audio_)
button1.grid(pady = 10,row = 5)

button1 = Button(tab2, text = "Close",command = window.quit)
button1.grid(pady = 10,padx=10,row = 6, column = 0)




tab_control.grid(row = 0, column = 0)
window.mainloop()


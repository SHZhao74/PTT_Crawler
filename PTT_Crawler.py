# -*- coding: utf-8 -*-
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

import os
import ttk
import time
class TweetGUI(Frame):
	"""docstring for ClassName"""
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		#self.drawBackground() #todo

	def drawBackground(self):
		bg = Canvas(self,width=300,height=300)
		#image = PhotoImage("twitter-breaking.jpeg")
		image = Image.open("twitter-breaking.jpeg") 
		#ImageTk.PhotoImage(image)
		bg.create_image(300, 300, image=image)
		#bg = Label(self, compound = 'bottom', image = image)
		
		#
		bg.pack()
	def createWidgets(self):
		'''Search field'''
		#self.inputText          = Label(self)
		#self.inputText["text"]  = "Search:"
		#self.inputText.grid(row =0, column=0)
		self.inputField        = Entry(self,bd=2)
		self.inputField['width'] = 10
		self.inputField.focus() #let the entry can be typed directly 
		
		self.search            = Button(self,text ="Search",command = self.searchMethod)
		self.search["command"] = self.searchMethod
		#self.search.pack()
		
		''' parameter field'''
		WEIGHT = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
		interesVar = StringVar(self,'0.5')
		self.interestLabel          = Label(self)
		self.interestLabel["text"]  = "Interesting:"

		#self.interestField          = apply(OptionMenu, (self, interesVar) + tuple(WEIGHT))
		self.interestField          = ttk.Combobox(self,textvariable=interesVar,values = WEIGHT,width='6')
		self.interestField.state(['readonly'])
		self.interestField.bind('<<ComboboxSelected>>', self.paraMethod) #set command
		
		self.diversityLabel         = Label(self)
		self.diversityLabel["text"] = "Diversity : " + str(1-float(self.interestField.get())) + " (1-Interesting)"
		
		'''Output result field'''
		self.outputLabel          = Label(self, text="Search Result",justify = CENTER)
		self.outputField          = Text(self,bd=4)
		self.outputField['width'] = 45

		'''Typesetting '''
		self.inputField.grid(row     = 0, column = 0)
		self.search.grid(row         = 0, column = 1, sticky='W')
		self.interestLabel.grid(row  = 1, column = 0, sticky='W')
		self.interestField.grid(row  = 1, column = 1, sticky='W')
		self.diversityLabel.grid(row = 1, column = 2, sticky='W')
		self.outputLabel.grid(row    = 2, column = 2, sticky='W')
		self.outputField.grid(row    = 3, column = 0,padx=5,pady=5,sticky='W',columnspan=3)


	def cppAnalsis(self):
		cmd = "./temp"
		t1  = time.time()
		os.system(cmd)
		t2  = time.time()
		self.outputField.insert(INSERT,'Spand ' + str(t2-t1) +"sce\n")

	def searchMethod(self):
		self.outputField.delete(0.0,END)#clear all text
		self.userinput = self.inputField.get()
		self.outputLabel["text"] = 'Search ' + self.userinput + ' Result'
		#self.outputField.insert(INSERT,"FUCK")
		
		'''call function to gather tweets '''
		
		self.outputField.insert(INSERT,'Searching \"' + self.userinput+"\"...\n")
		TwitterStream.doSearch(self,self.userinput)
		
		'''write weight value to .txt'''
		f    = open('weight.txt','w')
		f.write(self.interestField.get()+"\n")
		temp = str(1-float(self.interestField.get()))
		#print str(1-float(temp))
		f.write(temp)
		f.close()

		'''call c++ program to analsis'''
		self.outputField.insert(INSERT,'Analysing...')


		while (open('signal.ini','r').read() == '0'):
			pass
		self.cppAnalsis()
		
		

		'''read analsis result and display'''
		while (open('signal.ini','r').read() == '0'):pass
		rank = open('rank.txt','r')
		tmp  = rank.read()
		self.outputField.delete(0.0,END)#clear all text
		self.outputField.insert(INSERT,tmp+'\n')
		rank.close()
		open('signal.ini','w').write('0')
	def paraMethod(self,wtf):#I don't know why it must have 2 arguments
		self.diversityLabel["text"]  = "Diversity : " + str(1-float(self.interestField.get())) + " (1-Interesting)"
	
	
if __name__ == '__main__':
	root = Tk()
	root.title("PTT Crawler")
	app  = TweetGUI(master=root)
	app.mainloop()
		
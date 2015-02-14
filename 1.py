import wx
import os


new_autho=[]



class main_window(wx.Frame) :
	def __init__(self,parent,id) :
		wx.Frame.__init__(self,parent,id,'',size=(500,500),style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX)
		panel=wx.Panel(self,-1)
		panel.SetBackgroundColour(wx.Colour(220,220,250))
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
		font.SetPointSize(20)
		training_button=wx.Button(panel,label="Training",pos=(90,120),size=(300,100))
		training_button.SetBackgroundColour(wx.Colour(200,250,200))
		training_button.SetFont(font)
		self.Bind(wx.EVT_BUTTON, self.show_training_window, training_button)
		testing_button=wx.Button(panel,label="Testing",pos=(90,250),size=(300,100))
		testing_button.SetBackgroundColour(wx.Colour(200,250,200))
		testing_button.SetFont(font)
		self.Bind(wx.EVT_BUTTON, self.show_testing_window, testing_button)
		status_bar=self.CreateStatusBar()
		menubar=wx.MenuBar()
		file_menu=wx.Menu()
		tools_menu=wx.Menu()
		help_menu=wx.Menu()
		quit = wx.MenuItem(file_menu, wx.NewId(), '&Quit\tCtrl+Q')
		exit_img=wx.Bitmap('icons/exit_ico.png')
		quit.SetBitmap(exit_img)
		file_menu.AppendItem(quit)
		self.Bind(wx.EVT_MENU, self.close_window, id=quit.GetId())
		training = wx.MenuItem(help_menu, wx.NewId(), '&Training')
		tools_menu.AppendItem(training)
		testing_menu=wx.Menu()
		test1=wx.MenuItem(testing_menu, wx.NewId(), 'Binary Testing')
		test2=wx.MenuItem(testing_menu, wx.NewId(), 'One versus All Testing')
		self.Bind(wx.EVT_MENU, self.show_testing_window, id=test1.GetId())
		self.Bind(wx.EVT_MENU, self.show_testing_window, id=test2.GetId())
		self.Bind(wx.EVT_MENU, self.show_training_window, id=training.GetId())
		testing_menu.AppendItem(test1)
		testing_menu.AppendItem(test2)
		tools_menu.AppendMenu(wx.NewId(),'Testing',testing_menu)
		help_topics = wx.MenuItem(help_menu, wx.NewId(), '&Help Topics')
		help_topics.SetBitmap(wx.Bitmap('icons/help_ico.jpg'))
		help_menu.AppendItem(help_topics)
		about = wx.MenuItem(help_menu, wx.NewId(), '&About')
		help_menu.AppendItem(about)
		self.Bind(wx.EVT_MENU, self.show_about_window, id=about.GetId())
		menubar.Append(file_menu,"File")
		menubar.Append(tools_menu,"Tools")
		menubar.Append(help_menu,"Help")
		self.SetMenuBar(menubar)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		font.SetPointSize(30)
		appname=wx.StaticText(panel,-1,"Authorship Predictor",(10,30),(460,-1),wx.ALIGN_CENTER)
		appname.SetFont(font)
		appname.SetForegroundColour(wx.Colour(250,100,150))
		self.Centre()


	def close_window(self,event) :
		self.Close()

	
	def show_about_window(self,event) :
		about_frame=about_window(parent=None,id=0)
		about_frame.Show()


	def show_training_window(self,event) :
		training_frame=training_window(parent=None,id=1)
		training_frame.Show()


	def show_testing_window(self,event) :
		testing_frame=testing_window(parent=None,id=1)
		testing_frame.Show()





class about_window(wx.Frame) :
	def __init__(self,parent,id) :
		wx.Frame.__init__(self,parent,id,'About',size=(400,400),style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		panel1=wx.Panel(self)
		font.SetPointSize(30)
		appname=wx.StaticText(panel1,-1,"About",(10,30),(360,-1),wx.ALIGN_CENTER)
		appname.SetFont(font)
		appname.SetForegroundColour('blue')
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		font.SetPointSize(10)
		appname=wx.StaticText(panel1,-1,"Automatic Authorship Predictor Version : 1.0.0.1",(10,100),(360,-1),wx.ALIGN_CENTER)
		appname.SetFont(font)
		font.SetPointSize(15)
		appname.SetForegroundColour('red')
		appname=wx.StaticText(panel1,-1,"Authors",(10,140),(360,-1),wx.ALIGN_CENTER)
		appname.SetFont(font)
		appname=wx.StaticText(panel1,-1,"---------------------",(10,165),(360,-1),wx.ALIGN_CENTER)
		appname=wx.StaticText(panel1,-1,"Anjana.R\nDeepika.M\nNithin.P\nPanchami Raj.B\nRanjana.V",(10,190),(360,-1),wx.ALIGN_CENTER)
		appname.SetFont(font)






class training_window(wx.Frame) :
	def __init__(self,parent,id) :
		self.author_list=[]
		self.novel_list=[]
		self.numberOfAuthors=0
		self.authors=[]
		wx.Frame.__init__(self,parent,id,'Training..!!!!!',size=(600,600),style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX)
		self.panel=wx.Panel(self)
		self.panel.SetBackgroundColour(wx.Colour(220,220,250))
		font1 = wx.Font(10, wx.DEFAULT, wx.NORMAL,wx.FONTWEIGHT_NORMAL)
		font1.SetPointSize(12)
		add_author_button=wx.Button(self.panel,label="Add New Author",pos=(190,90),size=(200,30))
		add_author_button.SetFont(font1)
		self.Bind(wx.EVT_BUTTON, self.show_add_author, add_author_button)
		self.authorNameText=wx.StaticText(self.panel,-1,"Author Name\t : ",pos=(20,150),size=(30,50))
		self.authorNameText.SetFont(font1)
		self.authorNameChoices=wx.Choice(self.panel,-1,pos=(155,150),size=(290,30),choices=self.author_list)
		self.authorNameChoices.SetSelection(0)
		self.novelNameText=wx.StaticText(self.panel,-1,"Novel Name\t : ",pos=(20,200),size=(30,50))
		self.novelNameText.SetFont(font1)
		self.novelNameChoices=wx.Choice(self.panel,-1,pos=(155,200),size=(290,30))
		self.novelNameChoices.SetSelection(0)
		self.novelPrev=wx.TextCtrl(self.panel,-1,"",pos=(50,260),size=(500,200),style=wx.TE_READONLY)
		self.novelPrev.SetInsertionPoint(0)
		start_training_button=wx.Button(self.panel,label="Start Training",pos=(150,500),size=(300,40))
		start_training_button.SetFont(font1)
		self.Bind(wx.EVT_BUTTON, self.start_training_dialog, start_training_button)
		self.numberAuthors=wx.StaticText(self.panel,-1,"Number Of Authors Selected : "+str(self.numberOfAuthors),(120,30),(360,-1),wx.ALIGN_CENTER)
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		font.SetPointSize(15)
		self.numberAuthors.SetFont(font)
		self.Bind(wx.EVT_CLOSE, self.close_all)


	def close_all(self,event) :
		try :
			self.new_author_frame.Destroy()
			self.Destroy()
		except :
			self.Destroy()


	def show_add_author(self,event) :
		try :
			tmp=self.new_author_frame.GetSize()
		except :
			self.new_author_frame=self.select_new_author_window(parent=None,id=1)
			self.new_author_frame.Show()
			self.new_author_frame.Bind(wx.EVT_CLOSE, self.add_new_author,self.new_author_frame)


	def add_new_author(self,event) :
		try :
			global new_autho
			if len(new_autho)>=3 and len(new_autho[-1])>0 :
				self.numberOfAuthors+=1
				self.authors.append(new_autho)
				#print new_autho[0::-1]
				self.novel_list.append(new_autho[1:-1])
				self.author_list.append(new_autho[-1])
				self.authorNameChoices.SetItems(self.author_list)
				self.authorNameChoices.SetSelection(0)
				#print self.novel_list
				self.novelNameChoices.SetItems(self.novel_list[self.authorNameChoices.GetSelection()])
				self.novelNameChoices.SetSelection(0)
				self.Refresh()
			self.new_author_frame.Destroy()
			self.numberAuthors.SetLabel("Number Of Authors Selected : "+str(self.numberOfAuthors))
		except :
			self.new_author_frame.Destroy()
			


	def start_training_dialog(self,event) :
		if self.numberOfAuthors==0 :
			box=wx.MessageDialog(None,"Please input atleast one author details..!!!",'Alert',wx.OK)
			answer=box.ShowModal()
			box.Destroy()
		else :
			box=wx.MessageDialog(None,"Start Training..!!???",'Alert',wx.YES_NO)
			answer=box.ShowModal()
			box.Destroy()
			if answer==wx.ID_YES :
				print "Training Started with data!!!!","\n",self.authors
				## Place to call the training Function!!!!!!!
				box=wx.MessageDialog(None,"Training Started!!!",'Alert',wx.OK)
				answer=box.ShowModal()
				box.Destroy()



	class select_new_author_window(wx.Frame) :
		new_author=[]
		author_name=""
		
		
		def __init__(self,parent,id) :
			self.new_author=[]
			wx.Frame.__init__(self,parent,id,'Add New Author..!!!!!',size=(500,200),style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX)
			panel=wx.Panel(self)
			panel.SetBackgroundColour(wx.Colour(220,220,250))
			font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
			font.SetPointSize(12)
			font1 = wx.Font(10, wx.DEFAULT, wx.NORMAL,wx.FONTWEIGHT_NORMAL)
			font1.SetPointSize(12)
			self.authorText=wx.StaticText(panel,-1,"Author Name  \t :",pos=(8,30),size=(130,25))
			self.authorText.SetFont(font1)
			self.nameText=wx.TextCtrl(panel,-1,"Enter name of author...!!",pos=(150,30),size=(300,-1))
			self.nameText.SetInsertionPoint(0)
			select_novels_button=wx.Button(panel,label="Select Novels",pos=(8,70),size=(130,25))
			select_novels_button.SetFont(font1)
			self.Bind(wx.EVT_BUTTON, self.show_select_novels, select_novels_button)
			self.novelText=wx.TextCtrl(panel,-1,"",pos=(150,70),size=(300,-1))#,style=wx.TE_READONLY)
			self.novelText.Bind(wx.EVT_LEFT_DOWN, self.show_select_novels)
			self.novelText.SetInsertionPoint(0)
			ok_button=wx.Button(panel,label="OK",pos=(150,120),size=(100,40))
			ok_button.SetFont(font1)
			self.Bind(wx.EVT_BUTTON, self.return_new_author, ok_button)
		
		
		def show_select_novels(self,event) :
			wcd = 'Text Files (*.txt)|*.txt'
			open_dlg = wx.FileDialog(self, message='Choose Novels', defaultDir=os.getcwd(), defaultFile='',wildcard=wcd, style=wx.OPEN|wx.CHANGE_DIR|wx.MULTIPLE)
			ans=open_dlg.ShowModal()
			open_dlg.Destroy()
			self.new_author=[]
			novels=""
			novels+=open_dlg.GetDirectory()
			self.new_author.append(open_dlg.GetDirectory())
			for i in range(len(open_dlg.GetFilenames())) :
				novels+=open_dlg.GetFilenames()[i]
				novels+=","
				self.new_author.append(open_dlg.GetFilenames()[i])

			self.novelText.SetValue(novels)
		
		
		def return_new_author(self,event) :
			self.new_author.append(self.nameText.GetValue())
			global new_autho
			new_autho=self.new_author
			self.Close()









class testing_window(wx.Frame) :
	
	
	def __init__(self,parent,id) :
		self.author_list=open("author_list.txt","r").readlines()
		self.testing_novel=[]
		self.novel1=[]
		wx.Frame.__init__(self,parent,id,'Testing..!!!!!',size=(480,400),style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX)
		panel = wx.Panel(self)
		panel.SetBackgroundColour(wx.Colour(220,220,250))
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
		font.SetPointSize(12)
		self.test1=wx.RadioButton(panel, -1, 'One versus all testing',pos=(20,20),size=(220,50), style=wx.RB_GROUP)
		self.test1.SetFont(font)
		self.test2=wx.RadioButton(panel, -1, 'Binary testing',pos=(20,55),size=(220,50))
		self.test2.SetFont(font)
		self.Bind(wx.EVT_RADIOBUTTON, self.disable_choices, self.test1)
		self.Bind(wx.EVT_RADIOBUTTON, self.enable_choices, self.test2)
		font1 = wx.Font(10, wx.DEFAULT, wx.NORMAL,wx.FONTWEIGHT_NORMAL)
		font1.SetPointSize(12)
		select_novels_button=wx.Button(panel,label="Select a Novel",pos=(8,120),size=(130,25))
		select_novels_button.SetFont(font1)
		self.Bind(wx.EVT_BUTTON, self.show_select_novel, select_novels_button)
		self.novelText=wx.TextCtrl(panel,-1,"",pos=(150,120),size=(300,-1))
		self.novelText.Bind(wx.EVT_LEFT_DOWN, self.show_select_novel)
		self.novelText.SetInsertionPoint(0)
		self.author1Text=wx.StaticText(panel,-1,"Select Author 1 \t : ",pos=(20,180),size=(30,50))
		self.author1Text.SetFont(font1)
		self.author1Choices=wx.Choice(panel,-1,pos=(155,180),size=(290,50),choices=self.author_list)
		self.author1Choices.SetSelection(0)
		self.author2Text=wx.StaticText(panel,-1,"Select Author 2 \t : ",pos=(20,220),size=(30,50))
		self.author2Text.SetFont(font1)
		self.author2Choices=wx.Choice(panel,-1,pos=(155,220),size=(290,50),choices=self.author_list)
		self.author2Choices.SetSelection(1)
		self.author2Choices.Disable()
		self.author1Choices.Disable()
		start_test_button=wx.Button(panel,label="Start Test",pos=(170,280),size=(130,40))
		start_test_button.SetFont(font1)
		self.Bind(wx.EVT_BUTTON, self.start_test_dialog, start_test_button)


	def start_test_dialog(self,event) :
		if self.test2.GetValue() and self.author2Choices.GetSelection()==self.author1Choices.GetSelection()  :
			box=wx.MessageDialog(None,"Please select two different authors...!!!",'Alert',wx.OK)
			answer=box.ShowModal()
			box.Destroy()
		elif len(self.novel1) <2 :
			box=wx.MessageDialog(None,"Please select a novel..!!!!!",'Alert',wx.OK)
			answer=box.ShowModal()
			box.Destroy()
		else :
			box=wx.MessageDialog(None,"Start testing of the novel..!!!",'Alert',wx.YES_NO)
			answer=box.ShowModal()
			box.Destroy()
			if answer==wx.ID_YES :
				self.testing_novel=[]
				self.testing_novel.append(self.test2.GetValue())
				self.testing_novel.append(self.novel1)
				print "Testing Started with data!!!!","\n",self.testing_novel
				## Place to call the testing Function!!!!!!!
				box=wx.MessageDialog(None,"Test Started!!!",'Alert',wx.OK)
				answer=box.ShowModal()
				box.Destroy()



	def disable_choices(self,event) :
		self.author1Choices.Disable()
		self.author2Choices.Disable()


	def enable_choices(self,event) :
		self.author1Choices.Enable()
		self.author2Choices.Enable()


	def show_select_novel(self,event) :
		wcd = 'Text Files (*.txt)|*.txt'
		open_dlg = wx.FileDialog(self, message='Choose a Novel', defaultDir=os.getcwd(), defaultFile='',wildcard=wcd, style=wx.OPEN|wx.CHANGE_DIR)
		ans=open_dlg.ShowModal()
		open_dlg.Destroy()
		if open_dlg.GetFilename()!="" :
			self.novel1=[]
			novels=""
			novels+=open_dlg.GetDirectory()
			novels+=open_dlg.GetFilename()
			self.novel1.append(open_dlg.GetDirectory())
			self.novel1.append(open_dlg.GetFilename())
			self.novelText.SetValue(novels)





def main() :
	app=wx.App()
	frame=main_window(parent=None,id=-1)
	frame.Show()
	app.MainLoop()




if __name__=='__main__' :
	main()

from tkinter import *
from db import Mydb
from tkinter import messagebox
from NLP import NLPclass

class NLPapp:
    def __init__(self):
        #nlpclass ka obj
        self.nlp = NLPclass()
        # Mydb ka obj
        self.database = Mydb()

        # login ka GUI code
        self.root = Tk()
        self.root.title("NLP app")
        self.root.geometry("350x600")
        self.root.configure(bg='#C4D7EF')
        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root , text="NLPapp" , bg = "#C4D7EF" ,fg='black')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root ,text="enter email" )
        label1.pack(pady=(10,10))

        self.input_email = Entry(self.root , width='50')
        self.input_email.pack(pady=(10,10))

        label2=Label(self.root , text="enter password")
        label2.pack(pady=(10,10))

        self.input_password = Entry(self.root, width=30 , show='*')
        self.input_password.pack(pady=(10,10))

        button_login = Button(self.root , text="Login",command=self.perform_login)
        button_login.pack(pady=(10,10))

        label3 = Label(self.root , text="Not a member")
        label3.pack(pady=(70,10))

        button_signup = Button(self.root,text="sign up",width=40,height=2,command=self.register_gui)
        button_signup.pack(pady=(10,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root , text="NLPapp" , bg = "#C4D7EF" ,fg='black')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root , text="new menmber \n register here")
        label0.pack(pady=(10,10),ipady=4)

        label1 = Label(self.root , text="enter name")
        label1.pack(pady=(10,10))

        self.input_name = Entry(self.root,width=30)
        self.input_name.pack(pady=(10,10))
        
        label2 = Label(self.root ,text="enter email" )
        label2.pack(pady=(10,10))

        self.input_email = Entry(self.root , width='50')
        self.input_email.pack(pady=(10,10))

        label3=Label(self.root , text="create password")
        label3.pack(pady=(10,10))

        self.input_password = Entry(self.root, width=30 , show='*')
        self.input_password.pack(pady=(10,10))

        button_register = Button(self.root , text="Register" , command=self.perform_registration)
        button_register.pack(pady=(10,10))

        button_login = Button(self.root , text="logn now" , command=self.login_gui)
        button_login.pack(pady=(10,10))

        
    def perform_registration(self):
        #just fetching the data
        name = self.input_name.get()
        email = self.input_email.get()
        password = self.input_password.get()
        response = self.database.add_data(email,name, password)
        if response:
            messagebox.showinfo('success','Registration successful ! you can now login')
        else:
            messagebox.showinfo('error','email already exist')
    
    def perform_login(self):
        #matching the data in database

        email = self.input_email.get()
        password = self.input_password.get()
        response = self.database.check_data(email,password)
        if response:
            self.home_gui()
        else:
            messagebox.showinfo('error','wrong email or password')

    def home_gui(self):
        self.clear()
        heading_home = Label(self.root,text="NLP home", bg = "#C4D7EF" ,fg='black')
        heading_home.pack(pady=(10,10),ipady=5)
        heading_home.configure(font=('verdana',24,'bold'))

        button_ner = Button(self.root,text="NER(Entity Extraction)",width=30,height=3,command=self.ner_gui)
        button_ner.pack(pady=(10,30))

        button_sentiment = Button(self.root,text="Sentiment Analysis",width=30,height=3,command=self.sentiment_gui)
        button_sentiment.pack(pady=(10,30))

        button_language_detection = Button(self.root,text="Language Detection",width=30,height=3,command=self.title_detection_gui)
        button_language_detection.pack(pady=(10,30))


    def ner_gui(self):
        self.clear()
        heading_home = Label(self.root,text="Entity Extraction", bg = "#C4D7EF" ,fg='black')
        heading_home.pack(pady=(10,10),ipady=5)
        heading_home.configure(font=('verdana',24,'bold'))

        para = Label(self.root,text="Text")
        para.pack(pady=(10,10))

        self.input_para = Entry(self.root,width=50)
        self.input_para.pack(pady=(10,10),ipady=10)
        
        entity = Label(self.root,text="Entity")
        entity.pack(pady=(10,10))

        self.input_entity = Entry(self.root,width=30)
        self.input_entity.pack(pady=(10,10))

        button_ner= Button(self.root,text="Analyze",width=20,height=2,command=self.perform_ner)
        button_ner.pack(pady=(10,10))
        
        self.ner_result = Label(self.root,text='',bg = "#C4D7EF" )
        self.ner_result.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()
        heading_home = Label(self.root,text="Sentiment Analysis", bg = "#C4D7EF" ,fg='black')
        heading_home.pack(pady=(10,10),ipady=5)
        heading_home.configure(font=('verdana',24,'bold'))

        text = Label(self.root,text="Text")
        text.pack(pady=(10,10))

        self.input_text = Entry(self.root,width=50)
        self.input_text.pack(pady=(10,10),ipady=10)

        button_ner= Button(self.root,text="Analyze",width=20,height=2,command=self.perform_sentiment_analysis)
        button_ner.pack(pady=(10,10))
        
        self.sa_result = Label(self.root,text='',bg = "#C4D7EF" )
        self.sa_result.pack(pady=(10,10))

    def title_detection_gui(self):
        self.clear()
        heading_home = Label(self.root,text="Heading Detection", bg = "#C4D7EF" ,fg='black')
        heading_home.pack(pady=(10,10),ipady=5)
        heading_home.configure(font=('verdana',24,'bold'))

        text = Label(self.root,text="Text")
        text.pack(pady=(10,10))

        self.input_passage = Entry(self.root,width=50)
        self.input_passage.pack(pady=(10,10),ipady=10)

        button_ner= Button(self.root,text="Analyze",width=20,height=2,command=self.perform_title_detection)
        button_ner.pack(pady=(10,10))
        
        self.heading_result = Label(self.root,text='',bg = "#C4D7EF" )
        self.heading_result.pack(pady=(10,10))
    
    def perform_ner(self):
        para = self.input_para.get()
        entity = self.input_entity.get()
        response=self.nlp.ner(para,entity)
        self.ner_result['text'] = response
    
    def perform_sentiment_analysis(self):
        text = self.input_text.get()
        response = self.nlp.sentiment_analysis(text)
        self.sa_result['text'] = response

    def perform_title_detection(self):
        text = self.input_passage.get()
        response = self.nlp.title_gen(text)
        self.heading_result['text'] = response



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

nlp = NLPapp()
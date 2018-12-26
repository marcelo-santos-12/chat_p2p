from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Login(Screen):

    def __init__ (self,**kwargs):
        super (Login, self).__init__(**kwargs)
    
        box1 = BoxLayout()
        label1 = Label(text="Tela de Login")
        button1 = Button(text="Next", on_press=self.changer)
        box1.add_widget(label1)
        box1.add_widget(button1)
        self.add_widget(box1)

    def changer(self,*args):
        self.manager.current = 'chat'

class Chat(Screen):

    def __init__(self,**kwargs):
        super (Chat, self).__init__(**kwargs)
        
        box1 = BoxLayout()
        label1 = Label(text="Tela do chat")
        button1 = Button(text="Back", on_press=self.changer)
        box1.add_widget(label1)
        box1.add_widget(button1)
        self.add_widget(box1)

    def changer(self,*args):
        self.manager.current = 'login'

class TestApp(App):

        def build(self):
            screenmanager = ScreenManager()
            tela1 = Login(name='login')
            tela2 = Chat(name='chat')
            screenmanager.add_widget(tela1)
            screenmanager.add_widget(tela2)
            return screenmanager

if __name__ == '__main__':
    TestApp().run()

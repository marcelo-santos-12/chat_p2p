# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from teste_cliente_servidor import Server_Cliente
import threading

class TelaInicial(GridLayout):
   def __init__(self, **kwargs):
      super(TelaInicial, self).__init__(**kwargs)
      self.cols = 1
      self.label_rec = Label(text='Mensagem Recebida...')
      self.label_send = Label(text='Mensagem Enviada...')
      self.add_widget(self.label_rec)
      self.add_widget(self.label_send)
      self.write_msg = TextInput(multiline=False)
      self.add_widget(self.write_msg)
      self.button_send = Button(text='Enviar', on_release = self.envia_msg)
      self.add_widget(self.button_send)

      self.obj = Server_Cliente()
      self.is_server = False
      self.obj.init_client('192.168.1.6')
      th = threading.Thread(target = self.print_msg_return)
      th.start()

   def print_msg_return(self):
      while True:
         self.label_rec.text = self.obj.recebe_msg(self.is_server)

   def envia_msg(self, button):
      self.label_send.text = self.write_msg.text
      self.write_msg.text = ""
      self.obj.envia_msg(self.label_send.text, self.is_server)
      
class MyApp(App):
   def build(self):
      return TelaInicial()

if __name__ == '__main__':
   MyApp().run()

# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import teste_cliente_servidor as scv

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
      self.button_send = Button(text='Enviar', on_release = self.msg_enviar)
      self.add_widget(button_send)

      self.obj = scv.Server_Cliente('192.168.1.7', 5000, '192.168.1.7', 5000)
      
      try:
         self.obj.init_cliente()
         self.label_rec.text = "Conectado"
         self.conexao = True

      except:
         self.label_rec.text = "Falha na comunicação com o Servidor"

   def msg_enviar(self, button):
      self.label_send.text = self.write_msg.text
      self.write_msg.text = ""
      self.obj.envia_msg(self.write_msg.text)

   def msg_recebida(self):
      self.label_rec.text = self.obj.recebe_msg()

class MyApp(App):
   def build(self):
      return TelaInicial()

if __name__ == '__main__':
   MyApp().run()

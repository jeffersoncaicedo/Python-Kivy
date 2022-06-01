from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.utils import platform

from time import strftime
from datetime import datetime

import os

Config.set('graphics', 'width', 1366)
Config.set('graphics', 'height', 720)


class GridMain(GridLayout):
    fechatext = StringProperty("")

    def __init__(self):
        super(GridMain, self).__init__()
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
            app_folder = os.path.dirname(os.path.abspath(__file__))
            PATH = "/storage/emulated/0/Movies"
        Clock.schedule_interval(self.fecha, 1)

    def fecha(self, dt):
        ahora = datetime.now()
        meses = ("Ene.", "Feb.", "Mar.", "Abr.", "May.", "Jun.", "Jul.", "Ago.", "Sep.", "Oct.", "Nov.", "Dic.")
        dia = ahora.day
        mes = meses[ahora.month - 1]
        anio = ahora.year
        self.fechatext = "{} de {} del {}".format(dia, mes, anio) + "           " + strftime("%X")


class MainApp(App):
    def build(self):
        return GridMain()


if __name__ == "__main__":
    MainApp().run()

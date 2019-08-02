from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import winsound
from __init__.py import *


winsound.PlaySound("Project-Song2", winsound.SND_ASYNC)

kv = Builder.load_file("File.kv")


class WindowManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class ScheduleScreen(Screen):
    pass


class BookScreen(Screen):
    pass


class TicketScreen(Screen):
    name1 = ObjectProperty(None)
    cnic = ObjectProperty(None)
    contact = ObjectProperty(None)
    journey = ObjectProperty(None)
    standard = ObjectProperty(None)
    economy = ObjectProperty(None)
    luxury = ObjectProperty(None)

    def reset(self):
        self.cnic.text = ""
        self.name1.text = ""
        self.contact.text = ""
        self.journey.text = ""
        with open("database.txt", "a+") as file:
            file.write("\n")
            file.write("\n")

    def submit1(self):
        with open("database.txt", "a+") as file:
            with open("voucher.txt", "w") as voucher:

                if self.name1.text != "":
                    file.write("Name: ")
                    file.write(self.name1.text)
                    file.write('\n')
                    voucher.write("Name: ")
                    voucher.write(self.name1.text)
                    voucher.write('\n')

                    if self.cnic.text != "":
                        file.write("CNIC: ")
                        file.write(self.cnic.text)
                        file.write('\n')
                        voucher.write("CNIC: ")
                        voucher.write(self.cnic.text)
                        voucher.write('\n')

                        if self.contact.text != "":
                            file.write("Contact: ")
                            file.write(self.contact.text)
                            file.write('\n')
                            voucher.write("Contact: ")
                            voucher.write(self.contact.text)
                            voucher.write('\n')

                            if self.journey.text != "":
                                file.write("Train Name: ")
                                file.write(self.journey.text)
                                file.write('\n')
                                voucher.write("Train Name: ")
                                voucher.write(self.journey.text)
                                voucher.write('\n')

                                if self.standard.active:
                                    file.write('Class: Standard')
                                    file.write('\n')
                                    voucher.write('Class: Standard')
                                    voucher.write('\n')
                                    self.reset()

                                elif self.economy.active:
                                    file.write('Class: Economy')
                                    file.write('\n')
                                    voucher.write('Class: Economy')
                                    voucher.write('\n')
                                    self.reset()

                                elif self.luxury.active:
                                    file.write('Class: Luxury')
                                    file.write('\n')
                                    voucher.write('Class: Luxury')
                                    voucher.write('\n')
                                    self.reset()


class VoucherScreen(Screen):
    with open("voucher.txt") as f:

        voucher = f.read()


class PromotionScreen(Screen):
    pass


class AdminScreen(Screen):
    namee = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != '':
            if self.password.text != '':
                self.reset()

    def reset(self):
        self.password.text = ""
        self.namee.text = ""


class ResInfoScreen(Screen):

    with open("database.txt") as f:
        info = f.read()


class MainApp(App):

    def build(self):
        return WindowManager()


if __name__ == "__main__":
    MainApp().run()

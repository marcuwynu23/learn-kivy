import sys
from kivymd.app import MDApp
from kivy.lang import Builder
from app.drawer import NavigationDrawer, ContentNavigationDrawer


class DemoApp(MDApp):
  def build(self):
      return Builder.load_file("kivy/main.kv")


if __name__ == '__main__':
	DemoApp().run()
from kivy.uix.boxlayout import BoxLayout

class NavigationDrawer(BoxLayout):
	def __init__(self,**kwargs):
	  super().__init__(**kwargs)

	def toggle_nav_drawer(self):
	  print("Hello World!")
	
	def logout(self):
	  sys.exit(0)

class ContentNavigationDrawer(BoxLayout):
	pass

import tkinter as tk
from Calendar_widget import Calendar
class Control:
	def __init__(self, parent):
		self.parent = parent
		self.choose_btn = tk.Button(self.parent, text='Choose', command=self.popup)
		self.show_btn = tk.Button(self.parent, text='Show Selected', command=self.print_selected_date)
		self.choose_btn.grid()
		self.show_btn.grid()
		self.data = {}
	
	def popup(self):
		child = tk.Toplevel()
		cal = Calendar(child, self.data)
	
	def print_selected_date(self):
		print(self.data)
		data_Formatted = "{day}-{month}-{year}".format(day=self.data['day_selected'],month=self.data['month_selected'],year=self.data['year_selected'])
		return (data_Formatted)
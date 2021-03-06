from easy_tk import EasyTkObject
from views.ViewDecorator import widget_decorator
from tkinter import Label,Button,Entry
from tkinter.ttk import Progressbar

class BaseView(EasyTkObject):
    frame_path = ""

    def __init__(self):
        super(BaseView,self).__init__()
        self.dimensions = ""
        self.frame_to_raise = ""
        self.name = type(self).__name__
    
    def set_controller(self,controller):
        self.controller = controller
    
    def adding_complete_widgets(self,root,widget):
        self.easy.add_complete_widget(root)
        self.easy.add_complete_widget(widget)

    def set_model(self, model):
        self.model = model

    def method_part(self):
        pass

    def frame_part(self):
        self.set_font()
        self.style_all_buttons()
    
    def set_font(self):
        for i in self.easy.all_widgets:
            for j in [Label,Button,Entry,Progressbar]:
                try:
                    if isinstance(self.easy.all_widgets.get(i).get(), j):
                        self.easy.all_widgets.get(i).get()["font"] = ('Minion Pro SmBd', 18, '')
                        break
                except:
                    continue
    
    @widget_decorator
    def create_widgets(self):
        self.open_file(self.frame_path)
        self.reading_from_json()

    def tkraise(self):
        self.get("root").geometry(self.dimensions)
        self.get("root").update()
        self.get(self.frame_to_raise).tkraise()
    
    def style_all_buttons(self):
        for i in self.easy.all_widgets:
            if i.startswith("Button"):
                self.get(i)["relief"] = "solid"
                self.get(i)["borderwidth"] = 2
                self.get(i)["bg"] = "#dedcdc"
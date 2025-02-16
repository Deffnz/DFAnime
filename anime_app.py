from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class NavBar(BoxLayout):
    def __init__(self, toggle_menu, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = 80
        self.padding = [10, 10]
        self.spacing = 10
        self.pos_hint = {'top': 1}
        
        with self.canvas.before:
            Color(0.125, 0.125, 0.125, 1)  # Серый 20
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.logo = Image(source="df.png", size_hint=(None, None), size=(50, 50))
        self.title = Label(text="Anime App", color=(1, 1, 1, 1), font_size=20)
        self.menu_button = Button(text="☰", size_hint=(None, None), size=(50, 50))
        self.menu_button.bind(on_release=toggle_menu)
        
        self.add_widget(self.logo)
        self.add_widget(self.title)
        self.add_widget(self.menu_button)
    
    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class SideMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = None
        self.width = Window.width * 0.2
        self.height = Window.height - 80  # Исключаем навбар
        self.pos = (-self.width, 80)  # Прячем за левым краем
        self.orientation = 'vertical'
        
        with self.canvas.before:
            Color(0.15, 0.15, 0.15, 1)  # Серый 19
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        self.add_widget(Label(text="Меню", color=(1, 1, 1, 1)))
        self.add_widget(Button(text="Опция 1"))
        self.add_widget(Button(text="Опция 2"))
        self.add_widget(Button(text="Опция 3"))
    
    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
    
    def toggle(self, instance):
        print("Меню нажато")
        new_x = 0 if self.pos[0] < 0 else -self.width
        print(f"Перемещение меню в: {new_x}")
        anim = Animation(pos=(new_x, self.pos[1]), duration=0.3)
        anim.start(self)

class MainApp(App):
    def build(self):
        Window.size = (430, 932)
        root = FloatLayout()
        
        with root.canvas.before:
            Color(0.07, 0.07, 0.07, 1)  # Серый 18
            root.rect = Rectangle(size=Window.size, pos=root.pos)
        
        root.bind(size=self.update_rect, pos=self.update_rect)
        
        self.side_menu = SideMenu()
        self.navbar = NavBar(self.side_menu.toggle)
        
        root.add_widget(self.navbar)
        root.add_widget(Widget(size_hint_y=None, height=Window.height - 80))  # Для заполнения
        root.add_widget(self.side_menu)
        
        return root
    
    def update_rect(self, instance, *args):
        instance.rect.size = instance.size
        instance.rect.pos = instance.pos

if __name__ == "__main__":
    MainApp().run()

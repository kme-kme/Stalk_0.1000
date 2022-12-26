from kivy.app import App
from kivy.lang import Builder
import keyboard as keyb
import time

time.sleep(5)
class ServiceApp(App):
    n=1
    while n<<30:
        n+=1
        keyb.write('...')
        time.sleep(1)



if __name__ == '__main__':
    ServiceApp().run()
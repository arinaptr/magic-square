import numpy as np
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.config import Config


class ABC:
    abc = 1


inc = ABC()
kol = ABC()
ord = ABC()
funi = ABC()
funj = ABC()
funarr = ABC()


class MainWindow(Screen, BoxLayout):
    passw = ObjectProperty(None)

    def pressed(self):
        if self.passw.text != "" and int(self.passw.text) > 0 and int(self.passw.text) <= 40:
            order = int(self.passw.text)
            ord.abc = order
            a = (order * (order ** 2 + 1)) / 2
            kol.abc = a
            print(a)

    def delete(self):
        self.passw.text = ""

    def min_sum(self):
        snd = self.manager.get_screen("second")
        snd.show()


class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show(self):
        name = str(kol.abc)
        print(name)
        inc.abc = 1
        self.ids.size_label.text = f"Минимальная сумма \n          равнa {name}"
        self.ids.size_label.font_size = 30
        self.ids.label_change.text = f"\nCумма равна {name}"

    def delete1(self):
        self.ids.size_label.text = ""
        self.ids.label_change.text = ""
        self.slider_label.text = "Увеличение \n  суммы в"

    def slide_it(self, *args):
        self.slider_label.text = str(int(args[1]))
        self.slider_label.font_size = str(int(args[1]) * 5)

    def change(self):
        print(self.slider_label.text)
        if self.slider_label.text != "Увеличение \n  суммы в" and int(self.slider_label.text) >= 2:
            name = kol.abc
            incr = int(self.slider_label.text)
            inc.abc = incr
            name = name * incr
            name = str(name)
            print(name)
            self.ids.label_change.text = f"\nCумма равна {name}"

    def count(self):
        n = int(inc.abc)
        print(n)
        order = int(ord.abc)
        print(order)

        if order % 2 == 0:
            # двумерная матрица, все записи которой равны 0
            arr = [[(order * y) + x + 1 for x in range(order)] for y in range(order)]
            # Изменение значения элементов массива в фиксированном месте (n*n+1)-arr[i][[j]
            # Углы порядка (order/4)*(order/4)
            # Верхний левый угол
            for i in range(0, order // 4):
                for j in range(0, order // 4):
                    arr[i][j] = (order * order + 1) - arr[i][j];
            # верхний правый угол
            for i in range(0, order // 4):
                for j in range(3 * (order // 4), order):
                    arr[i][j] = (order * order + 1) - arr[i][j];
            # левый нижний угол
            for i in range(3 * (order // 4), order):
                for j in range(0, order // 4):
                    arr[i][j] = (order * order + 1) - arr[i][j];
            # правый нижний угол
            for i in range(3 * (order // 4), order):
                for j in range(3 * (order // 4), order):
                    arr[i][j] = (order * order + 1) - arr[i][j];
            # центр матрицы (order/2, order/2)
            for i in range(order // 4, 3 * (order // 4)):
                for j in range(order // 4, 3 * (order // 4)):
                    arr[i][j] = (order * order + 1) - arr[i][j];
            # result
            for i in range(order):
                for j in range(order):
                    print('%4d ' % (arr[i][j] * n), end=" ")
                print()

        else:
            mid = order // 2
            arr = np.zeros((order, order))
            i = 0
            j = mid
            for k in range(1, order * order + 1):
                arr[i][j] = k
                p = i
                i = i - 1
                q = j
                j = j + 1

                if i < 0:
                    i = order - 1

                if j > order - 1:
                    j = 0

                if arr[i][j] != 0:
                    j = q
                    i = p + 1

            for i in range(order):
                print("", end="")
                for j in range(order):
                    print("%4d" % (arr[i][j] * n), end="")
                print()
                for k in range(1, 6 * order + 1):
                    print("", end="")
                print()
        funi.abc = i
        funj.abc = j
        funarr.abc = arr

    def next(self):
        i = int(funi.abc)
        j = int(funj.abc)
        arr = funarr.abc
        order = int(ord.abc)
        n = int(inc.abc)
        s = self.manager.get_screen("third")
        # s.layout=GridLayout(cols=1, spacing=10, size_hint_y=None)
        # s.layout.bind(minimum_height=s.layout.setter('height'))
        for i in range(order):
            for j in range(order):
                s.ids.print_label.text += ("%8d" % (arr[i][j] * n))
            s.ids.print_label.text += "\n\n"
        if order <= 9:
            s.ids.print_label.font_size = 30
        else:
            s.ids.print_label.font_size = (200 / order)
        # s.root=ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        # s.root.add_widget(s.layout)
        # return s.root


class ThirdWindow(Screen):
    def delete2(self):
        self.ids.print_label.text = ""
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     i = int(funi.abc)
    #     j = int(funj.abc)
    #     arr = funarr.abc
    #     order = int(ord.abc)
    #     n = int(inc.abc)
    #     for i in range(order):
    #         for j in range(order):
    #             self.print_label.text += ("%6d" % (arr[i][j] * n))

    # self.add_widget(Label(text=""))


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()

    # print_label:print_label
    # Button:
    #     text: "print"
    #     spacing: 10
    #     size_hint: 0.5,0.5
    #     on_press:
    #         root.display()
    # Label:
    #     id:print_label

    # def __init__(self, **kwargs):
    #
    #     super(ThirdWindow, self).__init__(**kwargs)
    #     i = int(funi.abc)
    #     j = int(funj.abc)
    #     arr = funarr.abc
    #     order = int(ord.abc)
    #     n = int(inc.abc)
    #     for i in range(order):
    #         for j in range(order):
    #             self.print_label.text += ("%6d" % (arr[i][j] * n))
    #         self.print_label.text += "\n\n"

    # def display(self):
    #     print("third window")
    #     i = int(funi.abc)
    #     j = int(funj.abc)
    #     arr = funarr.abc
    #     order = int(ord.abc)
    #     n = int(inc.abc)
    #     for i in range(order):
    #         for j in range(order):
    #             self.ids.print_label.text+= ("%6d" % (arr[i][j] * n))
    #         self.ids.print_label.text += "\n\n"

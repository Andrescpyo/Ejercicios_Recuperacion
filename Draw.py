import tkinter as tk
from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def dibujar(self, canvas, punto1, punto2):
        pass


class Circulo(Figura):
    def dibujar(self, canvas, punto1, punto2):
        x1, y1 = punto1
        x2, y2 = punto2
        radio = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        canvas.create_oval(x1 - radio, y1 - radio, x1 + radio, y1 + radio)


class Triangulo(Figura):
    def dibujar(self, canvas, punto1, punto2):
        x1, y1 = punto1
        x2, y2 = punto2
        lado1 = abs(x2 - x1)
        lado2 = abs(y2 - y1)
        hipotenusa = math.sqrt(lado1 ** 2 + lado2 ** 2)
        punto3 = (x1, y1 + lado2)  # Calcula el tercer punto del triángulo rectángulo
        canvas.create_polygon(x1, y1, x2, y1, punto3[0], punto3[1], fill="", outline="black")


class Rectangulo(Figura):
    def dibujar(self, canvas, punto1, punto2):
        x1, y1 = punto1
        x2, y2 = punto2
        canvas.create_rectangle(x1, y1, x2, y2)


class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()
        self.figura_actual = None
        self.punto1 = None

        self.circulo_button = tk.Button(self, text="Círculo", command=self.seleccionar_circulo)
        self.circulo_button.pack(side=tk.LEFT)
        self.triangulo_button = tk.Button(self, text="Triángulo", command=self.seleccionar_triangulo)
        self.triangulo_button.pack(side=tk.LEFT)
        self.rectangulo_button = tk.Button(self, text="Rectángulo", command=self.seleccionar_rectangulo)
        self.rectangulo_button.pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.obtener_punto)

    def seleccionar_circulo(self):
        self.figura_actual = Circulo()

    def seleccionar_triangulo(self):
        self.figura_actual = Triangulo()

    def seleccionar_rectangulo(self):
        self.figura_actual = Rectangulo()

    def obtener_punto(self, event):
        if self.figura_actual is not None:
            if self.punto1 is None:
                self.punto1 = (event.x, event.y)
            else:
                punto2 = (event.x, event.y)
                self.figura_actual.dibujar(self.canvas, self.punto1, punto2)
                self.punto1 = None


if __name__ == "__main__":
    app = InterfazGrafica()
    app.mainloop()
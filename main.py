import tkinter as tk
import threading
import random
import time

class TemperaturaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface de Temperatura e Umidade")

        self.temperatura_img = tk.PhotoImage(file="temperatura.png")  
        self.umidade_img = tk.PhotoImage(file="umidade.png")

        self.temperatura_img = self.temperatura_img.subsample(2, 2)
        self.umidade_img = self.umidade_img.subsample(2, 2)  

        self.temperatura_label = tk.Label(root, image=self.temperatura_img)
        self.temperatura_label.grid(row=0, column=0, padx=10, pady=10)

        self.umidade_label = tk.Label(root, image=self.umidade_img)
        self.umidade_label.grid(row=0, column=1, padx=10, pady=10)

        self.temperatura_atual_label = tk.Label(root, text="", fg="red", font=("Arial", 15))
        self.temperatura_atual_label.grid(row=1, column=0, padx=10, pady=5)

        self.umidade_atual_label = tk.Label(root, text="", fg="blue", font=("Arial", 15))
        self.umidade_atual_label.grid(row=1, column=1, padx=10, pady=5)

        self.thread_temperatura = threading.Thread(target=self.atualizar_temperatura)
        self.thread_umidade = threading.Thread(target=self.atualizar_umidade)
        self.thread_temperatura.daemon = True  
        self.thread_umidade.daemon = True
        self.thread_temperatura.start()
        self.thread_umidade.start()

    def atualizar_temperatura(self):
        while True:
            temperatura = random.uniform(20, 30)
            
            self.root.after(0, self.atualizar_interface_temperatura, temperatura)
            time.sleep(5)

    def atualizar_umidade(self):
        while True:
            umidade = random.uniform(40, 60)

            self.root.after(0, self.atualizar_interface_umidade, umidade)
            time.sleep(3)

    def atualizar_interface_temperatura(self, temperatura):
        self.temperatura_atual_label.config(text=f"{temperatura:.2f} °C")

    def atualizar_interface_umidade(self, umidade):
        self.umidade_atual_label.config(text=f"{umidade:.2f}%")

def main():
    root = tk.Tk()
    app = TemperaturaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
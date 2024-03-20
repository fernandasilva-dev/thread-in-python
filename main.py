import tkinter as tk
import threading

class Temperatura_interface:
    def __init__(self,root):
        self.root = root
        self.root.title("Interface de Temperatura")

        self.temperatura_label = tk.Label(root, text = "Temperatura")
        self.temperatura_label.pack()

        self.imagem = tk.PhotoImage(file="temperatura.png")
        self.imagem_label = tk.Label(root, image=self.imagem)
        self.imagem_label.pack()

        self.temperatura_atual_label = tk.Label(root, text = "")
        self.temperatura_atual_label.pack()

        self.thread = threading.Thread(target=self.atualizar_temperatura)
        self.thread.daemon = True
        self.thread.start()

    def atualizar_temperatura(self):
        while True:
            temperatura = float(input(""))
            
            self.root.after(0,self.atualizar_interface, temperatura)

    def atualizar_interface(self, temperatura):
        self.temperatura_atual_label.config(text=f"{temperatura:.2f} ºC")

def main():
    root = tk.Tk()
    app = Temperatura_interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
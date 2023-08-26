import tkinter as tk
from professor import ProfessorApp
from validar_presenca import ValidarPresencaApp

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Inicial")

        self.validar_button = tk.Button(root, text="Validar Presença de Aluno", command=self.validar_presenca)
        self.validar_button.pack()

        self.professor_button = tk.Button(root, text="Professor", command=self.abrir_professor)
        self.professor_button.pack()

    def validar_presenca(self):
        self.root.destroy()  # Fechar a tela inicial
        root_validar = tk.Tk()
        app_validar = ValidarPresencaApp(root_validar)
        root_validar.mainloop()

    def abrir_professor(self):
        self.root.destroy()  # Fechar a tela inicial
        root_professor = tk.Tk()
        app_professor = ProfessorApp(root_professor)
        root_professor.mainloop()

def main():
    root = tk.Tk()
    tela_inicial = TelaInicial(root)
    root.mainloop()

if __name__ == "__main__":
    main()

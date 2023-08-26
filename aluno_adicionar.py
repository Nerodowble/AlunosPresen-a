import tkinter as tk
from tkinter import messagebox

class AdicionarAlunoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adicionar Aluno")

        self.name_label = tk.Label(root, text="Nome do Aluno:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.class_label = tk.Label(root, text="Classe:")
        self.class_label.pack()

        self.class_entry = tk.Entry(root)
        self.class_entry.pack()

        self.submit_button = tk.Button(root, text="Adicionar Aluno", command=self.adicionar_aluno)
        self.submit_button.pack()

    def adicionar_aluno(self):
        nome_aluno = self.name_entry.get()
        classe_aluno = self.class_entry.get()

        if nome_aluno and classe_aluno:
            with open("alunos.txt", "a", encoding="utf-8") as presenca_file:
                presenca_file.write(f"{nome_aluno} - {classe_aluno}\n")
            messagebox.showinfo("Aluno Adicionado", f"Aluno {nome_aluno} adicionado à lista de presença!")
            self.name_entry.delete(0, tk.END)
            self.class_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos!")

def main():
    root = tk.Tk()
    app = AdicionarAlunoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

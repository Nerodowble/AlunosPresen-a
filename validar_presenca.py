import tkinter as tk
from tkinter import messagebox
from unidecode import unidecode

class ValidarPresencaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Validação de Presença")

        self.name_label = tk.Label(root, text="Nome do Aluno:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.class_label = tk.Label(root, text="Classe:")
        self.class_label.pack()

        self.class_entry = tk.Entry(root)
        self.class_entry.pack()

        self.submit_button = tk.Button(root, text="Validar Presença", command=self.validate_presence)
        self.submit_button.pack()

    def validate_presence(self):
        nome_aluno = self.name_entry.get()
        classe_aluno = self.class_entry.get().lower()  # Converte para minúsculas

        aluno_presente = False
        with open("alunos.txt", "r", encoding="utf-8") as file:
            for line in file:
                nome, classe = line.strip().split(" - ")
                if self.normalize_text(nome_aluno) in self.normalize_text(nome) and classe_aluno == classe.lower():
                    aluno_presente = True
                    break

        if aluno_presente:
            with open("alunos_presenca.txt", "a", encoding="utf-8") as presenca_file:
                presenca_file.write(f"{nome_aluno} - {classe_aluno}\n")

            messagebox.showinfo("Presença Validada", f"Presença de {nome_aluno} validada com sucesso!")
        else:
            messagebox.showwarning("Aluno Não Encontrado", "Aluno não encontrado na lista!")

    def normalize_text(self, text):
        return unidecode(text).lower()

def main():
    root = tk.Tk()
    app = ValidarPresencaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
from aluno_adicionar import AdicionarAlunoApp  # Importa o script para adicionar alunos

class ProfessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Acesso do Professor")

        self.senha_label = tk.Label(root, text="Senha do Professor:")
        self.senha_label.pack()

        self.senha_entry = tk.Entry(root, show="*")
        self.senha_entry.pack()

        self.acessar_button = tk.Button(root, text="Acessar", command=self.acessar)
        self.acessar_button.pack()

    def acessar(self):
        senha = self.senha_entry.get()
        if senha == "123":  # Substitua pela senha real
            self.root.destroy()
            root_professor_view = tk.Tk()
            app_professor_view = ProfessorViewApp(root_professor_view)
            root_professor_view.mainloop()
        else:
            messagebox.showwarning("Acesso Negado", "Senha incorreta!")

class ProfessorViewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualização do Professor")

        self.atualizar_button = tk.Button(root, text="Atualizar Página", command=self.atualizar_pagina)
        self.atualizar_button.pack()

        self.header_label = tk.Label(root, text="Selecione uma Classe:")
        self.header_label.pack()

        self.classes_listbox = tk.Listbox(root)
        self.classes_listbox.pack()

        self.alunos_label = tk.Label(root, text="ALUNOS:")
        self.alunos_label.pack()

        self.alunos_frame = tk.Frame(root)
        self.alunos_frame.pack()

        self.carregar_classes()
        self.classes_listbox.bind("<<ListboxSelect>>", self.carregar_alunos)

        self.limpar_button = tk.Button(root, text="Limpar Lista de Presença", command=self.limpar_presenca)
        self.limpar_button.pack()

        self.adicionar_aluno_button = tk.Button(root, text="Adicionar Aluno", command=self.adicionar_aluno)
        self.adicionar_aluno_button.pack()

    def carregar_classes(self):
        try:
            with open("alunos.txt", "r", encoding="utf-8") as file:
                alunos = file.readlines()
                classes = set()
                for aluno in alunos:
                    _, classe = aluno.strip().split(" - ")
                    classes.add(classe)
                for classe in sorted(classes):
                    self.classes_listbox.insert(tk.END, classe)
        except FileNotFoundError:
            messagebox.showinfo("Nenhum Aluno", "Nenhum aluno validou a presença ainda.")

    def carregar_alunos(self, event):
        selected_class = self.classes_listbox.get(self.classes_listbox.curselection())
        self.limpar_alunos_frame()
        
        try:
            with open("alunos.txt", "r", encoding="utf-8") as file:
                alunos = file.readlines()
                alunos_da_classe = [aluno.strip().split(" - ") for aluno in alunos if aluno.strip().endswith(selected_class)]

                for nome, _ in alunos_da_classe:
                    aluno_frame = tk.Frame(self.alunos_frame)
                    aluno_label = tk.Label(aluno_frame, text=nome)
                    
                    # Verifica se o aluno está na lista de presença
                    if self.aluno_presente(nome, selected_class):
                        check_label = tk.Label(aluno_frame, text="✓")
                        check_label.pack(side=tk.RIGHT)
                    
                    aluno_label.pack(side=tk.LEFT)
                    aluno_frame.pack()
        except FileNotFoundError:
            messagebox.showinfo("Nenhum Aluno", "Nenhum aluno cadastrado na classe selecionada.")

    def aluno_presente(self, nome, classe):
        try:
            with open("alunos_presenca.txt", "r", encoding="utf-8") as file:
                for line in file:
                    aluno, classe_presenca = line.strip().split(" - ")
                    if aluno == nome and classe_presenca == classe:
                        return True
        except FileNotFoundError:
            pass
        return False

    def limpar_presenca(self):
        selected_class = self.classes_listbox.get(self.classes_listbox.curselection())
        try:
            with open("alunos_presenca.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open("alunos_presenca.txt", "w", encoding="utf-8") as file:
                for line in lines:
                    nome, classe = line.strip().split(" - ")
                    if classe != selected_class:
                        file.write(line)
            messagebox.showinfo("Lista Limpa", f"Lista de presença para {selected_class} foi limpa.")
        except FileNotFoundError:
            pass

    def adicionar_aluno(self):
        adicionar_aluno_window = tk.Toplevel(self.root)
        adicionar_aluno_app = AdicionarAlunoApp(adicionar_aluno_window)

    def atualizar_pagina(self):
        self.root.destroy()  # Destruir a janela atual
        root_professor_view = tk.Tk()
        app_professor_view = ProfessorViewApp(root_professor_view)
        root_professor_view.mainloop()

    def limpar_alunos_frame(self):
        for widget in self.alunos_frame.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    app = ProfessorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

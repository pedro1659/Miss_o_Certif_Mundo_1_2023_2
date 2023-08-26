import os
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import datetime
import locale
import pandas as pd


class MatrizSoDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação Matriz SoD")

        self.tabControl = ttk.Notebook(self.root)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("Treeview", rowheight=25, font=("Arial", 10))

        self.style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        self.style.map("Treeview", background=[("alternate", "#f2f2f2")])

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tab5 = ttk.Frame(self.tabControl)
        self.tab6 = ttk.Frame(self.tabControl)
        self.tab7 = ttk.Frame(self.tabControl)
        self.tab8 = ttk.Frame(self.tabControl)
        self.tab9 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text="Cadastro de Sistema")
        self.tabControl.add(self.tab2, text="Consulta de Sistemas")
        self.tabControl.add(self.tab3, text="Cadastro dos Perfis de Acesso")
        self.tabControl.add(self.tab4, text="Consulta dos Perfis de Acesso")
        self.tabControl.add(self.tab5, text="Cadastro da Matriz SoD")
        self.tabControl.add(self.tab6, text="Consulta da Matriz SoD")
        self.tabControl.add(self.tab7, text="Cadastro dos Usuários e Perfis")
        self.tabControl.add(self.tab8, text="Consulta dos Usuários e Perfis")
        self.tabControl.add(self.tab9, text="Excluir Dados")

        self.tabControl.pack(expand=1, fill="both")

        self.criar_conteudo_aba1()
        self.criar_conteudo_aba2()
        self.criar_conteudo_aba3()
        self.criar_conteudo_aba4()
        self.criar_conteudo_aba5()
        self.criar_conteudo_aba6()
        self.criar_conteudo_aba7()
        self.criar_conteudo_aba8()
        self.criar_conteudo_aba9()

    def formatar_data_hora(self, data):
        locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
        data_obj = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        data_formatada = data_obj.strftime("%d %b %Y %H:%M:%S")
        return data_formatada

    def criar_conteudo_aba1(self):
        label = tk.Label(self.tab1, text="Cadastro de Sistemas")
        label.pack(padx=10, pady=10)

        codigo_label = tk.Label(self.tab1, text="Código do Sistema (chave primária):")
        codigo_label.pack(padx=10, pady=5)
        self.codigo_entry = tk.Entry(self.tab1)
        self.codigo_entry.pack(padx=10, pady=5)

        nome_label = tk.Label(self.tab1, text="Nome do Sistema:")
        nome_label.pack(padx=10, pady=5)
        self.nome_entry = tk.Entry(self.tab1)
        self.nome_entry.pack(padx=10, pady=5)

        adicionar_button = tk.Button(
            self.tab1, text="Adicionar Sistema", command=self.adicionar_sistema
        )
        adicionar_button.pack(padx=10, pady=10)

    def adicionar_sistema(self):
        codigo = self.codigo_entry.get()
        nome = self.nome_entry.get()

        if not codigo or not nome:
            tk.messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        data_adicao = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.salvar_em_csv(codigo, nome, data_adicao)
        data_adicao_formatada = self.formatar_data_hora(data_adicao)
        self.tree_consulta.insert(
            "", tk.END, values=(data_adicao_formatada, codigo, nome)
        )
        self.codigo_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)

    def salvar_em_csv(self, codigo, nome, data_adicao):
        with open("./sistema.csv", "a", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow([data_adicao, codigo, nome])

    def criar_conteudo_aba2(self):
        label = tk.Label(self.tab2, text="Consulta de Sistemas")
        label.pack(padx=10, pady=10)

        self.tree_consulta = ttk.Treeview(
            self.tab2, columns=("DataAdicao", "Codigo", "Nome"), show="headings"
        )
        self.tree_consulta.heading("#1", text="Data de Adição")
        self.tree_consulta.heading("#2", text="Código")
        self.tree_consulta.heading("#3", text="Nome")
        self.tree_consulta.column("#1", width=150)
        self.tree_consulta.column("#2", width=100)
        self.tree_consulta.column("#3", width=150)
        self.tree_consulta.pack(padx=10, pady=10)

        self.carregar_dados_csv()

    def criar_conteudo_aba3(self):
        label = tk.Label(self.tab3, text="Cadastro dos Perfis de Acesso")
        label.pack(padx=10, pady=10)

        codigo_label = tk.Label(self.tab3, text="Código do Sistema (chave primária):")
        codigo_label.pack(padx=10, pady=5)
        self.codigo_entry_perfil = tk.Entry(self.tab3)
        self.codigo_entry_perfil.pack(padx=10, pady=5)

        nome_label = tk.Label(self.tab3, text="Nome do Perfil (chave primária):")
        nome_label.pack(padx=10, pady=5)
        self.nome_entry_perfil = tk.Entry(self.tab3)
        self.nome_entry_perfil.pack(padx=10, pady=5)

        descricao_label = tk.Label(self.tab3, text="Descrição detalhada do perfil:")
        descricao_label.pack(padx=10, pady=5)
        self.descricao_entry_perfil = tk.Entry(self.tab3)
        self.descricao_entry_perfil.pack(padx=10, pady=5)

        adicionar_button = tk.Button(
            self.tab3, text="Adicionar Perfil", command=self.adicionar_perfil
        )
        adicionar_button.pack(padx=10, pady=10)

    def criar_conteudo_aba4(self):
        label = tk.Label(self.tab4, text="Consulta dos Perfis de Acesso")
        label.pack(padx=10, pady=10)

        self.tree_perfil_consulta = ttk.Treeview(
            self.tab4,
            columns=("Data de Adição", "Código", "Nome", "Descrição"),
            show="headings",
        )
        self.tree_perfil_consulta.heading("#1", text="Data de Adição")
        self.tree_perfil_consulta.heading("#2", text="Código")
        self.tree_perfil_consulta.heading("#3", text="Nome")
        self.tree_perfil_consulta.heading("#4", text="Descrição")
        self.tree_perfil_consulta.column("#1", width=150)
        self.tree_perfil_consulta.column("#2", width=100)
        self.tree_perfil_consulta.column("#3", width=150)
        self.tree_perfil_consulta.column("#4", width=300)
        self.tree_perfil_consulta.pack(padx=10, pady=10)

        self.carregar_dados_perfil_csv()

    def adicionar_perfil(self):
        codigo = self.codigo_entry_perfil.get()
        nome = self.nome_entry_perfil.get()
        descricao = self.descricao_entry_perfil.get()

        if not codigo or not nome or not descricao:
            tk.messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        data_adicao = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")
        self.salvar_perfil_em_csv(codigo, nome, descricao, data_adicao)
        self.tree_perfil_consulta.insert(
            "",
            tk.END,
            values=(data_adicao, codigo, nome, descricao),
        )

        self.codigo_entry_perfil.delete(0, tk.END)
        self.nome_entry_perfil.delete(0, tk.END)
        self.descricao_entry_perfil.delete(0, tk.END)

    def salvar_perfil_em_csv(self, codigo, nome, descricao, data_adicao):
        with open("./perfil.csv", "a", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow([data_adicao, codigo, nome, descricao])

    def carregar_dados_perfil_csv(self):
        try:
            with open("./perfil.csv", "r", encoding="utf-8") as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
                next(leitor)
                for linha in leitor:
                    data_adicao, codigo, nome, descricao = linha
                    if (
                        data_adicao.strip()
                        and codigo.strip()
                        and nome.strip()
                        and descricao.strip()
                    ):
                        self.tree_perfil_consulta.insert(
                            "", tk.END, values=(data_adicao, codigo, nome, descricao)
                        )
        except FileNotFoundError:
            pass

    def carregar_dados_csv(self):
        try:
            with open("./sistema.csv", "r", encoding="utf-8") as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
                next(leitor)
                for linha in leitor:
                    data_adicao, codigo, nome = linha
                    if data_adicao.strip() and codigo.strip() and nome.strip():
                        data_adicao_formatada = self.formatar_data_hora(data_adicao)
                        self.tree_consulta.insert(
                            "", tk.END, values=(data_adicao_formatada, codigo, nome)
                        )
        except FileNotFoundError:
            pass

    def criar_conteudo_aba5(self):
        label = tk.Label(self.tab5, text="Cadastro da Matriz SoD")
        label.pack(padx=10, pady=10)

        codigo_sistema1_label = tk.Label(
            self.tab5, text="Código do Sistema 1 (chave primária):"
        )
        codigo_sistema1_label.pack(padx=10, pady=5)
        self.codigo_sistema1_entry = tk.Entry(self.tab5)
        self.codigo_sistema1_entry.pack(padx=10, pady=5)

        nome_perfil1_label = tk.Label(
            self.tab5, text="Nome do Perfil 1 (chave primária):"
        )
        nome_perfil1_label.pack(padx=10, pady=5)
        self.nome_perfil1_entry = tk.Entry(self.tab5)
        self.nome_perfil1_entry.pack(padx=10, pady=5)

        codigo_sistema2_label = tk.Label(
            self.tab5, text="Código do Sistema 2 (chave primária):"
        )
        codigo_sistema2_label.pack(padx=10, pady=5)
        self.codigo_sistema2_entry = tk.Entry(self.tab5)
        self.codigo_sistema2_entry.pack(padx=10, pady=5)

        nome_perfil2_label = tk.Label(
            self.tab5, text="Nome do Perfil 2 (chave primária):"
        )
        nome_perfil2_label.pack(padx=10, pady=5)
        self.nome_perfil2_entry = tk.Entry(self.tab5)
        self.nome_perfil2_entry.pack(padx=10, pady=5)

        adicionar_perfis_button = tk.Button(
            self.tab5,
            text="Adicionar Perfis Conflitantes",
            command=self.adicionar_perfis_conflitantes,
        )
        adicionar_perfis_button.pack(padx=10, pady=10)

    def adicionar_perfis_conflitantes(self):
        codigo_sistema1 = self.codigo_sistema1_entry.get()
        nome_perfil1 = self.nome_perfil1_entry.get()
        codigo_sistema2 = self.codigo_sistema2_entry.get()
        nome_perfil2 = self.nome_perfil2_entry.get()

        if (
            not codigo_sistema1
            or not nome_perfil1
            or not codigo_sistema2
            or not nome_perfil2
        ):
            tk.messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        self.salvar_matriz_sod_em_csv(
            codigo_sistema1, nome_perfil1, codigo_sistema2, nome_perfil2
        )
        self.codigo_sistema1_entry.delete(0, tk.END)
        self.nome_perfil1_entry.delete(0, tk.END)
        self.codigo_sistema2_entry.delete(0, tk.END)
        self.nome_perfil2_entry.delete(0, tk.END)

        self.tree_matriz_sod_consulta.insert(
            "",
            tk.END,
            values=(codigo_sistema1, nome_perfil1, codigo_sistema2, nome_perfil2),
        )

    def salvar_matriz_sod_em_csv(
        self, codigo_sistema1, nome_perfil1, codigo_sistema2, nome_perfil2
    ):
        with open("./matriz_sod.csv", "a", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(
                [codigo_sistema1, nome_perfil1, codigo_sistema2, nome_perfil2]
            )

    def criar_conteudo_aba6(self):
        label = tk.Label(self.tab6, text="Consulta da Matriz SoD")
        label.pack(padx=10, pady=10)

        self.tree_matriz_sod_consulta = ttk.Treeview(
            self.tab6,
            columns=(
                "Data de Adição",
                "Código Sistema 1",
                "Nome Perfil 1",
                "Código Sistema 2",
                "Nome Perfil 2",
            ),
            show="headings",
        )
        self.tree_matriz_sod_consulta.heading("#1", text="Datade Adição")
        self.tree_matriz_sod_consulta.heading("#2", text="Código Sistema 1")
        self.tree_matriz_sod_consulta.heading("#3", text="Nome Perfil 1")
        self.tree_matriz_sod_consulta.heading("#4", text="Código Sistema 2")
        self.tree_matriz_sod_consulta.heading("#5", text="Nome Perfil 2")
        self.tree_matriz_sod_consulta.column("#1", width=150)
        self.tree_matriz_sod_consulta.column("#2", width=150)
        self.tree_matriz_sod_consulta.column("#3", width=100)
        self.tree_matriz_sod_consulta.column("#4", width=150)
        self.tree_matriz_sod_consulta.column("#5", width=100)
        self.tree_matriz_sod_consulta.pack(padx=10, pady=10)

        self.carregar_dados_matriz_sod_csv()

    def carregar_dados_matriz_sod_csv(self):
        try:
            with open("./matriz_sod.csv", "r", encoding="utf-8") as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
                for linha in leitor:
                    codigo_sistema1, nome_perfil1, codigo_sistema2, nome_perfil2 = linha
                    if (
                        codigo_sistema1.strip()
                        and nome_perfil1.strip()
                        and codigo_sistema2.strip()
                        and nome_perfil2.strip()
                    ):
                        self.tree_matriz_sod_consulta.insert(
                            "",
                            tk.END,
                            values=(
                                codigo_sistema1,
                                nome_perfil1,
                                codigo_sistema2,
                                nome_perfil2,
                            ),
                        )
        except FileNotFoundError:
            pass

    def criar_conteudo_aba7(self):
        label = tk.Label(self.tab7, text="Cadastro dos Usuários e Perfis")
        label.pack(padx=10, pady=10)

        cpf_label = tk.Label(self.tab7, text="CPF do Usuário (chave primária):")
        cpf_label.pack(padx=10, pady=5)
        self.cpf_entry = tk.Entry(self.tab7)
        self.cpf_entry.pack(padx=10, pady=5)

        codigo_sistema_label = tk.Label(
            self.tab7, text="Código do Sistema (chave primária):"
        )
        codigo_sistema_label.pack(padx=10, pady=5)
        self.codigo_sistema_entry = tk.Entry(self.tab7)
        self.codigo_sistema_entry.pack(padx=10, pady=5)

        nome_perfil_label = tk.Label(self.tab7, text="Nome do Perfil (chave primária):")
        nome_perfil_label.pack(padx=10, pady=5)
        self.nome_perfil_entry = tk.Entry(self.tab7)
        self.nome_perfil_entry.pack(padx=10, pady=5)

        adicionar_cadastro_button = tk.Button(
            self.tab7,
            text="Adicionar Cadastro de Usuário e Perfil",
            command=self.adicionar_cadastro,
        )
        adicionar_cadastro_button.pack(padx=10, pady=10)

    def adicionar_cadastro(self):
        cpf = self.cpf_entry.get()
        codigo_sistema = self.codigo_sistema_entry.get()
        nome_perfil = self.nome_perfil_entry.get()

        if not cpf or not codigo_sistema or not nome_perfil:
            tk.messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        perfil_existente = None

        for item in self.tree_cadastro_consulta.get_children():
            if self.tree_cadastro_consulta.item(item, "values")[2] == nome_perfil:
                perfil_existente = self.tree_cadastro_consulta.item(item, "values")[2]
                break

        if perfil_existente:
            tk.messagebox.showwarning("Aviso", "Cadastro já existe")
        else:
            if self.verificar_cpf_perfil_conflito(cpf, nome_perfil):
                tk.messagebox.showwarning("Aviso", "Perfil em conflito")
            else:
                self.salvar_cadastro_em_csv(cpf, codigo_sistema, nome_perfil)
                self.tree_cadastro_consulta.insert(
                    "", tk.END, values=(cpf, codigo_sistema, nome_perfil)
                )
                self.cpf_entry.delete(0, tk.END)
                self.codigo_sistema_entry.delete(0, tk.END)
                self.nome_perfil_entry.delete(0, tk.END)

    def salvar_cadastro_em_csv(self, cpf, codigo_sistema, nome_perfil):
        with open("./cadastro.csv", "a", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow([cpf, codigo_sistema, nome_perfil])

    def carregar_dados_cadastro_csv(self):
        try:
            with open("./cadastro.csv", "r", encoding="utf-8") as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
                for linha in leitor:
                    cpf, codigo_sistema, nome_perfil = linha
                    if cpf.strip() and codigo_sistema.strip() and nome_perfil.strip():
                        self.tree_cadastro_consulta.insert(
                            "", tk.END, values=(cpf, codigo_sistema, nome_perfil)
                        )
        except FileNotFoundError:
            pass

    def criar_conteudo_aba8(self):
        label = tk.Label(self.tab8, text="Consulta dos Usuários e seus Perfis")
        label.pack(padx=10, pady=10)

        self.tree_cadastro_consulta = ttk.Treeview(
            self.tab8,
            columns=("Data de Adição", "CPF", "Código do Sistema", "Nome do Perfil"),
            show="headings",
        )
        self.tree_cadastro_consulta.heading("#1", text="Data de Adição")
        self.tree_cadastro_consulta.heading("#2", text="CPF")
        self.tree_cadastro_consulta.heading("#3", text="Código do Sistema")
        self.tree_cadastro_consulta.heading("#4", text="Nome do Perfil")
        self.tree_cadastro_consulta.column("#1", width=150)
        self.tree_cadastro_consulta.column("#2", width=150)
        self.tree_cadastro_consulta.column("#3", width=150)
        self.tree_cadastro_consulta.column("#4", width=200)
        self.tree_cadastro_consulta.pack(padx=10, pady=10)

        self.carregar_dados_cadastro_csv()

    def verificar_conflitos(self, codigo_sistema, nome_perfil):
        for item in self.tree_matriz_sod_consulta.get_children():
            values = self.tree_matriz_sod_consulta.item(item, "values")
            if values[0] == codigo_sistema and values[1] == nome_perfil:
                return True
        return False

    def verificar_cpf_perfil_conflito(self, cpf, nome_perfil):
        for item in self.tree_cadastro_consulta.get_children():
            if self.tree_cadastro_consulta.item(item, "values")[0] == cpf:
                perfil_usuario = self.tree_cadastro_consulta.item(item, "values")[2]
                if self.verificar_conflito_matriz_sod(nome_perfil, perfil_usuario):
                    return True
        return False

    def verificar_conflito_matriz_sod(self, nome_perfil1, nome_perfil2):
        try:
            with open("./matriz_sod.csv", "r", encoding="utf-8") as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
                for linha in leitor:
                    if (nome_perfil1 in linha) and (nome_perfil2 in linha):
                        return True
        except FileNotFoundError:
            pass
        return False

    def criar_conteudo_aba9(self):
        label = tk.Label(self.tab9, text="Excluir Dados")
        label.pack(padx=10, pady=10)

        excluir_button = tk.Button(
            self.tab9,
            text="Excluir Todos os Dados",
            command=self.excluir_todos_os_dados,
        )
        excluir_button.pack(padx=10, pady=10)

    def excluir_todos_os_dados(self):
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            "Todos os dados serão excluídos. Tem certeza que deseja efetuar a exclusão?",
        )

        if resposta:
            arquivos_csv = [
                "./sistema.csv",
                "./perfil.csv",
                "./matriz_sod.csv",
                "./cadastro.csv",
            ]

            for arquivo in arquivos_csv:
                self.excluir_dados_csv(arquivo)

            self.limpar_arvore_consulta(self.tree_consulta)
            self.limpar_arvore_consulta(self.tree_perfil_consulta)
            self.limpar_arvore_consulta(self.tree_matriz_sod_consulta)
            self.limpar_arvore_consulta(self.tree_cadastro_consulta)

    def excluir_dados_csv(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)

    def limpar_arvore_consulta(self, tree):
        for item in tree.get_children():
            tree.delete(item)


def main():
    root = tk.Tk()
    app = MatrizSoDApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

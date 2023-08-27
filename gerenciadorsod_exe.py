"""App para genrenciar uma matriz SoD"""

import os
import locale
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import datetime


class MatrizSoDApp:
    """Responsável por criar a interface gráfica e gerenciar os diferentes aspectos da matriz SoD"""

    # Por padrão eu normalmente prefiro utilizar menos atributos para uma classe,
    # porém tentei minimizar o código que já está extenso e deixar tudo em um lugar só.
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação Matriz SoD")

        self.tabcontrol = ttk.Notebook(self.root)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("Treeview", rowheight=25, font=("Arial", 10))

        self.style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        self.style.map("Treeview", background=[("alternate", "#f2f2f2")])

        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        self.tab1 = ttk.Frame(self.tabcontrol)
        self.tab2 = ttk.Frame(self.tabcontrol)
        self.tab3 = ttk.Frame(self.tabcontrol)
        self.tab4 = ttk.Frame(self.tabcontrol)
        self.tab5 = ttk.Frame(self.tabcontrol)
        self.tab6 = ttk.Frame(self.tabcontrol)
        self.tab7 = ttk.Frame(self.tabcontrol)
        self.tab8 = ttk.Frame(self.tabcontrol)
        self.tab9 = ttk.Frame(self.tabcontrol)

        self.tabcontrol.add(self.tab1, text="Cadastro de Sistema")
        self.tabcontrol.add(self.tab2, text="Consulta de Sistemas")
        self.tabcontrol.add(self.tab3, text="Cadastro dos Perfis de Acesso")
        self.tabcontrol.add(self.tab4, text="Consulta dos Perfis de Acesso")
        self.tabcontrol.add(self.tab5, text="Cadastro da Matriz SoD")
        self.tabcontrol.add(self.tab6, text="Consulta da Matriz SoD")
        self.tabcontrol.add(self.tab7, text="Cadastro dos Usuários e Perfis")
        self.tabcontrol.add(self.tab8, text="Consulta dos Usuários e Perfis")
        self.tabcontrol.add(self.tab9, text="Excluir Dados")

        self.tabcontrol.pack(expand=1, fill="both")

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
        """Formata data e hora"""
        # Utilizado na Treeview, abas 2, 4, 6, 8.
        locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
        data_obj = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        data_formatada = data_obj.strftime("%d %b %Y %H:%M:%S")
        return data_formatada

    def criar_conteudo_aba1(self):
        """Aba Cadastro de Sistema"""
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
        """Botão Adicionar Sistema"""
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
        """Salva os dados inseridos na aba1 através adicionar_sistema em sistema.csv."""
        csv_path = os.path.join(self.script_dir, "sistema.csv")
        with open(csv_path, "a", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow([data_adicao, codigo, nome])

    def criar_conteudo_aba2(self):
        """Aba Consulta de Sistema"""
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
        """Aba Cadastro dos Perfis"""
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
        """Aba Consulta dos Perfis de Acesso"""
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
        """Botão Adicionar Perfil"""
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
        """Salva os dados inseridos na aba3 através adicionar_perfil em perfil.csv."""
        csv_path = os.path.join(self.script_dir, "perfil.csv")
        with open(csv_path, "a", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow([data_adicao, codigo, nome, descricao])

    def carregar_dados_perfil_csv(self):
        """Carrega os dados inseridos em perfil.csv ao iniciar o programa"""
        try:
            csv_path = os.path.join(self.script_dir, "perfil.csv")
            with open(csv_path, "r", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    data_adicao, codigo, nome, descricao = linha
                    if (
                        data_adicao.strip()
                        and codigo.strip()
                        and nome.strip()
                        and descricao.strip()
                    ):
                        self.tree_perfil_consulta.insert(
                            "",
                            tk.END,
                            values=(data_adicao, codigo, nome, descricao),
                        )
        except FileNotFoundError:
            pass

    def carregar_dados_csv(self):
        """Carrega os dados inseridos em sistema.csv ao iniciar o programa"""
        try:
            csv_path = os.path.join(self.script_dir, "sistema.csv")
            with open(csv_path, "r", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)
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
        """Aba Cadastro da Matriz SoD"""
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
        """Botão Adicionar Perfil"""
        codigo_sistema1 = self.codigo_sistema1_entry.get()
        nome_perfil1 = self.nome_perfil1_entry.get()
        codigo_sistema2 = self.codigo_sistema2_entry.get()
        nome_perfil2 = self.nome_perfil2_entry.get()

        if not (codigo_sistema1 and nome_perfil1 and codigo_sistema2 and nome_perfil2):
            tk.messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        data_adicao = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.salvar_matriz_sod_em_csv(
            codigo_sistema1, nome_perfil1, codigo_sistema2, nome_perfil2
        )
        self.tree_matriz_sod_consulta.insert(
            "",
            tk.END,
            values=(
                data_adicao,
                codigo_sistema1,
                nome_perfil1,
                codigo_sistema2,
                nome_perfil2,
            ),
        )

        self.codigo_sistema1_entry.delete(0, tk.END)
        self.nome_perfil1_entry.delete(0, tk.END)
        self.codigo_sistema2_entry.delete(0, tk.END)
        self.nome_perfil2_entry.delete(0, tk.END)

    def salvar_matriz_sod_em_csv(
        self, codigo_sistema1, nome_perfil1, codigo_sistema2, nome_perfil2
    ):
        """Salva os dados inseridos na aba5 através adicionar_perfis_conflitantes
        em matriz_sod.csv."""
        data_adicao = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        csv_path = os.path.join(self.script_dir, "matriz_sod.csv")
        with open(csv_path, "a", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(
                [
                    data_adicao,
                    codigo_sistema1,
                    nome_perfil1,
                    codigo_sistema2,
                    nome_perfil2,
                ]
            )

    def criar_conteudo_aba6(self):
        """Aba Consulta da Matriz SoD"""
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
        """Carrega os dados inseridos em matriz_sod.csv ao iniciar o programa"""
        try:
            csv_path = os.path.join(self.script_dir, "matriz_sod.csv")
            with open(csv_path, "r", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    if len(linha) == 5:
                        (
                            data_adicao,
                            codigo_sistema1,
                            nome_perfil1,
                            codigo_sistema2,
                            nome_perfil2,
                        ) = linha
                        if (
                            data_adicao.strip()
                            and codigo_sistema1.strip()
                            and nome_perfil1.strip()
                            and codigo_sistema2.strip()
                            and nome_perfil2.strip()
                        ):
                            self.tree_matriz_sod_consulta.insert(
                                "",
                                tk.END,
                                values=(
                                    data_adicao,
                                    codigo_sistema1,
                                    nome_perfil1,
                                    codigo_sistema2,
                                    nome_perfil2,
                                ),
                            )
        except FileNotFoundError:
            pass

    def criar_conteudo_aba7(self):
        """Aba Cadastro dos usuários e Perfis"""
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
        """Botão Adicionar Cadastro de Usuário e Perfil"""
        cpf = self.cpf_entry.get()
        codigo_sistema = self.codigo_sistema_entry.get()
        nome_perfil = self.nome_perfil_entry.get()

        if not cpf or not codigo_sistema or not nome_perfil:
            tk.messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        perfil_existente = None

        for item in self.tree_cadastro_consulta.get_children():
            if self.tree_cadastro_consulta.item(item, "values")[3] == nome_perfil:
                perfil_existente = self.tree_cadastro_consulta.item(item, "values")[3]
                break

        if perfil_existente:
            tk.messagebox.showwarning("Aviso", "Cadastro já existe")
        else:
            if self.verificar_cpf_perfil_conflito(cpf, nome_perfil):
                tk.messagebox.showwarning("Aviso", "Perfil em conflito")
            else:
                data_adicao = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.salvar_cadastro_em_csv(
                    cpf, codigo_sistema, nome_perfil, data_adicao
                )
                self.tree_cadastro_consulta.insert(
                    "", tk.END, values=(data_adicao, cpf, codigo_sistema, nome_perfil)
                )
                self.cpf_entry.delete(0, tk.END)
                self.codigo_sistema_entry.delete(0, tk.END)
                self.nome_perfil_entry.delete(0, tk.END)

    def salvar_cadastro_em_csv(self, cpf, codigo_sistema, nome_perfil, data_adicao):
        """Salva os dados inseridos na aba6 através de adicionar_cadastro em cadastro.csv."""
        csv_path = os.path.join(self.script_dir, "cadastro.csv")
        with open(csv_path, "a", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow([data_adicao, cpf, codigo_sistema, nome_perfil])

    def carregar_dados_cadastro_csv(self):
        "Carrega os dados inseridos em cadastro.csv ao iniciar o programa."
        try:
            csv_path = os.path.join(self.script_dir, "cadastro.csv")
            with open(csv_path, "r", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    data_adicao, cpf, codigo_sistema, nome_perfil = linha
                    if (
                        data_adicao.strip()
                        and cpf.strip()
                        and codigo_sistema.strip()
                        and nome_perfil.strip()
                    ):
                        self.tree_cadastro_consulta.insert(
                            "",
                            tk.END,
                            values=(data_adicao, cpf, codigo_sistema, nome_perfil),
                        )
        except FileNotFoundError:
            pass

    def criar_conteudo_aba8(self):
        """Aba Consulta dos usuários e seus Perfis"""
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
        """Verifica se usuário já está cadastrado."""
        for item in self.tree_matriz_sod_consulta.get_children():
            values = self.tree_matriz_sod_consulta.item(item, "values")
            if values[1] == codigo_sistema and values[2] == nome_perfil:
                return True
        return False

    def verificar_cpf_perfil_conflito(self, cpf, nome_perfil):
        """Verifica se há conflito de perfis, utilizando-se de lógica estabelecida
        em verificar_conflito_matriz_sod"""
        for item in self.tree_cadastro_consulta.get_children():
            if self.tree_cadastro_consulta.item(item, "values")[1] == cpf:
                perfil_usuario = self.tree_cadastro_consulta.item(item, "values")[3]
                if self.verificar_conflito_matriz_sod(nome_perfil, perfil_usuario):
                    return True
        return False

    def verificar_conflito_matriz_sod(self, nome_perfil1, nome_perfil2):
        """Verifica se há conflitos consultando matriz_sod.csv e verificando se
        nome_perfil1 e nome_perfil2 está na mesma linha"""
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
        """Aba Excluir Dados"""
        label = tk.Label(self.tab9, text="Excluir Dados")
        label.pack(padx=10, pady=10)

        excluir_button = tk.Button(
            self.tab9,
            text="Excluir Todos os Dados",
            command=self.excluir_todos_os_dados,
        )
        excluir_button.pack(padx=10, pady=10)

    def excluir_todos_os_dados(self):
        """Mensagem de confirmação de exclusão de dados"""
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            "Todos os dados serão excluídos. Tem certeza que deseja efetuar a exclusão?",
        )

        if resposta:
            arquivos_csv = [
                "sistema.csv",
                "perfil.csv",
                "matriz_sod.csv",
                "cadastro.csv",
            ]

            for arquivo in arquivos_csv:
                csv_path = os.path.join(self.script_dir, arquivo)
                self.excluir_dados_csv(csv_path)

            self.limpar_arvore_consulta(self.tree_consulta)
            self.limpar_arvore_consulta(self.tree_perfil_consulta)
            self.limpar_arvore_consulta(self.tree_matriz_sod_consulta)
            self.limpar_arvore_consulta(self.tree_cadastro_consulta)

    def excluir_dados_csv(self, csv_path):
        """Apaga os dados dos arquivos .csv"""
        if os.path.exists(csv_path):
            os.remove(csv_path)

    def limpar_arvore_consulta(self, tree):
        """Apaga os dados da Treeview das abas de consulta (2, 4, 6 e 8)"""
        for item in tree.get_children():
            tree.delete(item)

    # O método não está sendo usado mais, utilizei para limpar o cache e
    # evitar erros enquanto testava o programa.
    def cleanup_temporary_files(self):
        """Limpa os arquivos temporários"""
        temp_files = ["sistema.csv", "perfil.csv", "matriz_sod.csv", "cadastro.csv"]
        for file_name in temp_files:
            file_path = os.path.join(self.script_dir, file_name)
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    pass
                os.remove(file_path)


def main():
    """Ponto de entrada do app, dificil explicar, muito importante."""
    root = tk.Tk()
    app = MatrizSoDApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

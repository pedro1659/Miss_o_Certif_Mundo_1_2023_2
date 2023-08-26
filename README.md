# Miss_o_Certif_Mundo_1_2023_2
Projeto referente a missão de certificação do Mundo 1 - Dev Full Stack

O projeto requer que o usuario disponha de uma IDE funcional com python instalado.
O projeto foi desenvolvido usando o VSCode como IDE.
Também serao necessarias as seguintes bibliotecas para seu funcionamento:
import os
import sys
import locale
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import datetime
import pandas as pd
Note que algumas dessas bibliotecas ja vem embutidas com o python.

O programa também ja esta pronto para ser convertido em um .exe. Sugiro o cx_Freeze, que também requer instalaçao.


Explicações do que é o projeto:

O projeto consiste em um simples programa ou aplicação(.exe) para gerenciamento de Segregação de Funções; ao ser iniciado o programa disponibilizará ao usuario uma interface com abas para adição de dados e a consulta dos dados adicionados e também a verificação de conflitos entre os diferentes perfis de usuarios adicionados (se necessário), o objetivo do programa é:

Cadastrar sistemas com seus respectivos códigos e nomes.
Consultar esses sistemas em uma aba diferente.

Cadastrar perfis de acesso com seus respectivos código do sistema, nome do perfil e descrição detalhada do perfil.
Consultar perfis de acesso em uma aba diferente.

Cadastrar dados na matriz sod, com seus respectivos código do sistema1 e código do sistema, nome do perfil1 e nome do perfil2, onde o cadastro indicará quais perfis serão conflitantes.
Consultar perfis conflitantes em uma aba diferente.

Cadastrar os usuarios e seus perfis com seus respectivos CPF,código do sistema e nome do perfil.
Consultar o perfil de usuario adicionado em uma aba diferente.
Na aba cadastro de usuarios e seus perfis, o usuario consegue fazer as seguintes verificações:
Se o perfil de usuario(CPF) sendo adicionado não constar na aba consulta dos usuarios, significa que o perfil pode ser adicionado, o perfil será adicionado.
Se o perfil de usuario(CPF) sendo adicionado constar na aba consulta dos usuarios, e for identico, um aviso será exibido e não será possivel adicionar o usuario.
Se o perfil de usuario(CPF) sendo adicionado constar na aba consulta dos usuarios, mesmo que o código de sistema dado seja diferente mas o nome do perfil sendo adicionado constar na aba consulta da matriz sod, signica que há conflito um aviso será exibido, e não será possivel adicionar esse usuario.

Explicado a fundo a função de analisar perfis em conflito:
A verificação de conflitos é feita utilizando os dados do perfil já adicionados na aba de consulta dos usuarios e perfis e fazendo a verificação por cpf e nome de perfil de usuario, isso significa que um usuario já adicionado pode ser adicionado novamente desde que os nomes de perfis sendo atribuidos ao usuario nao estejam cadastrados na matriz sod, indicando que há conflitos.                                    

import pandas as pd # type: ignore


class ProcessadorCSV: # a classe diferente da função cria uma instância, ou seja, ela passa a existir, diferente da função que começa e termina.
    def __init__(self, arquivo_csv): # Metodo de inicialização ou metodo construtor
        self.arquivo_csv = arquivo_csv
        self.df = None

    def carregar_csv(self):
        # Carregar o arquivo csv em um DataFrame
        self.df = pd.read_csv(self.arquivo_csv)

    def remouver_celulas_vazias(self):
        # Verificar e remouver celulas vazias
        self.df = self.pd.dropna()

    def filtrar_por_estado(self, estado):
        # Filtrar linhas pela coluna estado
        self.df = self.df[self.df['estado'] == estado]

    def processar(self, estado):
        # Carrega CSV, remover celulas vazias e filtrar por estado
        self.carregar_csv()
        self.remouver_celulas_vazias()
        self.filtrar_por_estado()

        return self.df
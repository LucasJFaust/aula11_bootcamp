import pandas as pd # type: ignore

class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError("Métodos extrair_dados deve ser implementado nas classes filhas.")

    def tranformar_dados(self, dados):
        raise NotImplementedError("Métodos tranformar_dados deve ser implementado nas classes filhas.")

    def carregar_dados(self, dados_transformados):
        raise NotADirectoryError("Métodos carregar_dados deve ser implementado nas classes filhas.")

    def executar_etl(self):
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.tranformar_dados(dados_extraidos)
        self.carregar_dados(dados_transformados)

class ETLCSV(ETLProcess):
     def extrair_dados(self):
         return pd.read_csv(self.fonte_dados)

     def tranformar_dados(self, dados):
         # Exemplo simples de transformação: converter todas as letras em maiúsculas
         return dados.applymap(lambda x: x.upper() if isinstance(x, str) else x)

     def carregar_dados(self, dados_transformados):
         # Aqui você pode implementar a lógica para carregar os dados transformados para onde desejar
         print("Dados transformados")
         print(dados_transformados)


class ETLExcel(ETLProcess):
    def __init__(self, fonte_dados):
        super().__init__(fonte_dados) # O "super" nos da o direito dentro dessa classe de acessar um método da classe anterior a ela, ou seja a classe pai dela.

    def extrair_dados(self):
        return super().extrair_dados()

    def tranformar_dados(self, dados):
        return "dados transformados" # Caso a gente não queira usar o método da classe anterior é só alterar a linha.

# Exemplo de uso
if __name__ == "__main__":
    fonte_csv = 'dados.csv' # Substitua 'dados.csv' pelo caminho do seu arquivo csv
    etl_csv = ETLCSV(fonte_csv)
    etl_csv.executar_etl()
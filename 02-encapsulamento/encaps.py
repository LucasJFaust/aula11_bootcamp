import os
import sqlite3
import psycopg2


class BancoDeDados:
    def __init__(self, tipo_banco):
        self.tipo_banco = tipo_banco
        self.conexao = None

    def conectar(self):
        if self.tipo_banco =="sqlite":
            try:
                nome_arquivo = os.getenv('NOME_ARQUIVO_SQLITE')
                self.conexao = sqlite3.connect(nome_arquivo)
                print("Conexão SQLite estabelecida com sucesso!")
            except sqlite3.Error as e:
                print("Erro ao conectar ao SQLite: ", e)
        elif self.tipo_banco == 'postgre':
            try:
                host = os.getenv('HOST_PG')
                porta = os.getenv('PORTA_PG')
                banco = os.getenv('BANCO_PG')
                usuario = os.getenv('USUARIO_PG')
                senha = os.getenv('SENHA_PG')
                self.conexao = psycopg2.connect(
                    host=host,
                    port=porta,
                    database=banco,
                    user=usuario,
                    password=senha
                )
                print("Conexão PostgreSQL estabelecida com sucesso!")
            except psycopg2.Error as e:
                print("Erro ao conectar ao PostgreSQL: ", e)
        else:
            print("Tipo de banco de dados não suportado")

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            if self.tipo_banco == 'sqlite':
                print("Conexão SQLite fechado")
            elif self.tipo_banco == 'postgre':
                print("Conexão PostgreSQL fechada")

    def executar_query(self, query):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            self.conexao.commit()
            print("Query executada com sucesso!")
        except (sqlite3.Error, psycopg2.Error) as e:
            print("Erro ao executar query: ", e)


# Exemplo de uso
if __name__ == '__main__':
    tipo_banco = os.getenv('TIPO_BANCO') # sqlite ou postgre

    banco = BancoDeDados(tipo_banco)
    banco.conectar()

    # Exemplo de criação de tabela
    create_table_query = """
CREATE TABLE IF NOT EXISTE usuarios (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
"""
    banco.executar_query(create_table_query)

    # Exemplo de iserção de dados
    insert_query = """
    INSERT INTO usuarios (nome,email) VALUES
    ('João', 'joao@exemplo.com'),
    ('Maria', 'maria@exemplo.com');
    """
    banco.executar_query(insert_query)

    banco.desconectar()


test = BancoDeDados('SQLite')

test.conectar()

test.executar_query()

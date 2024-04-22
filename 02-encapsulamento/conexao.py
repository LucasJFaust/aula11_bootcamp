from .sqlite import BancoDeDadosSQLite
from .postgree import BancoDeDadosPost
from .encaps import BancoDeDados


# SQL Lite

nome_arquivo = "exemplo.db"
banco_sql = BancoDeDadosSQLite(nome_arquivo)
banco_sql.conectar()

# Inserindo dados na tabela:
insert_query = """
INSERT INTO usuarios (nome,email) VALUES
('João', 'joao@exemplo.com'),
('Maria', 'maria@exemplo.com');
"""

banco_sql.executar_query(insert_query)

banco_sql.desconectar()


# POSTGRE



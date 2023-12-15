import psycopg2

# Conexão com o servidor primário
primary_conn = psycopg2.connect(
    dbname='nome_do_banco_de_dados',
    user='seu_usuario',
    password='sua_senha',
    host='endereço_do_servidor_primário'
)

# Criar um cursor para executar comandos SQL
primary_cursor = primary_conn.cursor()

# Habilitar a replicação no servidor primário
primary_cursor.execute('SELECT pg_create_physical_replication_slot(%s)', ('slot_replicacao',))
primary_conn.commit()

# Consultar dados no servidor primário
primary_cursor.execute('SELECT * FROM sua_tabela')
rows = primary_cursor.fetchall()
for row in rows:
    print(row)

# Conexão com o servidor secundário
secondary_conn = psycopg2.connect(
    dbname='nome_do_banco_de_dados',
    user='seu_usuario',
    password='sua_senha',
    host='endereço_do_servidor_secundário'
)

# Criar um cursor para executar comandos SQL no servidor secundário
secondary_cursor = secondary_conn.cursor()

# Consultar dados replicados no servidor secundário
secondary_cursor.execute('SELECT * FROM sua_tabela')
replicated_rows = secondary_cursor.fetchall()
for row in replicated_rows:
    print(row)

# Fechar conexões
primary_cursor.close()
primary_conn.close()
secondary_cursor.close()
secondary_conn.close()
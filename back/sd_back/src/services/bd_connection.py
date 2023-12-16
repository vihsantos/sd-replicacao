import psycopg2


class BDConnection:

    def __init__(self):
        connectionA = psycopg2.connect(
            dbname='pedidos',
            user='vih',
            password='123456',
            host='localhost',
            port='5432'
        )
        connectionB =psycopg2.connect(
            dbname='pedidos',
            user='vih',
            password='123456',
            host='localhost',
            port='5433'
        )
        self.conn = self.connection(connectionA, connectionB)
    def connection(self, connection1, connection2):
        with connection1.cursor() as cursor:
            cursor.execute("SELECT pg_is_in_recovery()")
            result = cursor.fetchone()
            if result[0] is True:
                return connection1
            else:
                return connection2

    def addPedido(self, pedido):
        query = "INSERT INTO PEDIDO(DESCRICAO) VALUES (%s)"
        self.conn.cursor.execute(query, pedido)
        self.conn.commit()

    def getPedidos(self):
        query = 'SELECT * FROM PEDIDO'
        self.conn.cursor.execute(query)
        rows = self.conn.cursor.fetchall()
        return rows

    def deletePedido(self, id):
        query = f'DELETE FROM PEDIDO WHERE ID = {id}'
        self.conn.cursor.execute(query)
import psycopg2

try:

    conn = psycopg2.connect(

        host='localhost',

        port=5432,

        dbname='postgres',

        user='odoo',

        password='odoo'

    )

    print("✅ Conexión establecida correctamente.")

    conn.close()

except Exception as e:

    print("❌ Error de conexión:", e)
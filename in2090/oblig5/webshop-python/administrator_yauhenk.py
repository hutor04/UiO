import psycopg2

# MERK: Må kjøres med Python 3

user = 'yauhenk' # Sett inn ditt UiO-brukernavn ("_priv" blir lagt til under)
pwd = 'eaCh2ay5oh' # Sett inn passordet for _priv-brukeren du fikk i en mail

connection = \
    "dbname='" + user + "' " +  \
    "user='" + user + "_priv' " + \
    "port='5432' " +  \
    "host='dbpg-ifi-kurs.uio.no' " + \
    "password='" + pwd + "'"


def administrator():
    conn = psycopg2.connect(connection)
    
    ch = 0
    while (ch != 3):
        print("-- ADMINISTRATOR --")
        print("Please choose an option:\n 1. Create bills\n 2. Insert new product\n 3. Exit")
        ch = int(input("Option: "))

        if (ch == 1):
            make_bills(conn)
        elif (ch == 2):
            insert_product(conn)


def make_bills(conn):
    cur = conn.cursor()

    print('-- BILLS --')

    username = input('Username: ')

    if username == '':
        sub_query = ''
    else:
        sub_query = f"username LIKE '{username}' AND"

    query = f"SELECT bills.name, bills.address, SUM(bills.ordersum) as total " \
            f"FROM " \
            f"(SELECT ws.users.uid, ws.users.name, address, ws.orders.oid, ws.orders.num * ws.products.price as ordersum " \
            f"FROM ws.users " \
            f"INNER JOIN ws.orders ON ws.users.uid = ws.orders.uid " \
            f"INNER JOIN ws.products ON ws.orders.pid = ws.products.pid " \
            f"WHERE {sub_query} payed = 0) " \
            f"AS bills " \
            f"GROUP BY bills.name, bills.address;"

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print('--- Bill ---')
        print(f'Name: {row[0]}\nAddress: {row[1]}\nTotal due: {row[2]}')
        print(' ')

    cur.close()


def _get_category_id(conn, name):
    cur = conn.cursor()
    cat_q = f"SELECT cid FROM ws.categories WHERE name LIKE '{name}';"
    cur.execute(cat_q)
    cat_rows = cur.fetchall()
    cur.close()

    if len(cat_rows) > 0:
        return cat_rows[0][0]
    else:
        return None


def _insert_category(conn, name):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO ws.categories(name) VALUES ('{name}') RETURNING cid;")
    conn.commit()
    rows = cur.fetchall()
    cur.close()
    return rows[0][0]


def insert_product(conn):
    print('-- INSERT NEW PRODUCT --')
    product_name = input('Product name: ')
    product_price = input('Price: ')
    category_name = input('Category: ')
    description = input('Dedcription: ')

    cat_id = _get_category_id(conn, category_name)
    if cat_id is None:
        cat_id = _insert_category(conn, category_name)

    cur = conn.cursor()

    cur.execute(f"INSERT INTO ws.products(name, price, cid, description) VALUES ('{product_name}', {product_price},"
                f"{cat_id}, '{description}')")

    conn.commit()
    cur.close()

    print(f'New product {product_name} inserted.')


if __name__ == "__main__":
    administrator()

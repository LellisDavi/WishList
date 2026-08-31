import sqlite3

banco = sqlite3.connect('database/wishlist.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS categoria (" \
"id integer PRIMARY KEY AUTOINCREMENT," \
" nome text," \
" tipo text)")

cursor.execute("CREATE TABLE IF NOT EXISTS item (" \
"id integer PRIMARY KEY AUTOINCREMENT," \
" nome text," \
" preco double," \
" categoria_id integer," \
" status text," \
" FOREIGN KEY (categoria_id) REFERENCES categoria(id))")

banco.commit()
banco.close()
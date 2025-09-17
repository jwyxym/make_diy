import sqlite3
import subprocess
import shutil
conn = sqlite3.connect('../card/cards.cdb')
cursor = conn.cursor()
cursor.execute("select * from datas,texts where datas.id=texts.id")
rows = cursor.fetchall()
conn.close()

conn = sqlite3.connect('./cards.cdb')
cursor = conn.cursor()
cursor.execute("CREATE TABLE texts(id integer primary key,name text,desc text,str1 text,str2 text,str3 text,str4 text,str5 text,str6 text,str7 text,str8 text,str9 text,str10 text,str11 text,str12 text,str13 text,str14 text,str15 text,str16 text);")
cursor.execute("CREATE TABLE datas(id integer primary key,ot integer,alias integer,setcode integer,type integer,atk integer,def integer,level integer,race integer,attribute integer,category integer);")
conn.commit()
conn.close()
shutil.copy2('./cards.cdb', '../fantoccini/cards.cdb')
i = 0
j = 0
conn = None
while True:
    if j >= 20 or len(rows) <= i:
        if not conn is None:
            conn.close()
            conn = None
        shutil.copy2('../fantoccini/cards.cdb', '../web/src/static/')
        subprocess.run(["cargo", "run"], cwd='../fantoccini')
        shutil.copy2('./cards.cdb', '../fantoccini/cards.cdb')
        j = 0
    if len(rows) <= i:
        break

    if conn is None:
        conn = sqlite3.connect('../fantoccini/cards.cdb')
    cursor = conn.cursor()
    row = rows[i]
    cursor.execute(f"INSERT OR REPLACE INTO datas VALUES({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]});")
    query = """
        INSERT OR REPLACE INTO texts VALUES(
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """
    values = (
        row[11], row[12], row[13], row[14], row[15],
        row[16], row[17], row[18], row[19], row[20],
        row[21], row[22], row[23], row[24], row[25],
        row[26], row[27], row[28], row[29]
    )
    cursor.execute(query, values)
    conn.commit()
    i += 1
    j += 1
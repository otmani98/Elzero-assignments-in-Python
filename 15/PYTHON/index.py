import sqlite3

db = sqlite3.connect("elzero.db")

cr = db.cursor()

cr.execute("create table if not exists users (id integer UNIQUE, name text UNIQUE, birth date UNIQUE,email text UNIQUE)")

try :
    cr.execute("insert into users (id, name, birth, email) values (1, 'Tarek', '2066-12-12', 'uio@gma.con')")
    cr.execute("insert into users (id, name, birth, email) values (2, 'Ahmed', '2059-12-12', 'ghjyu@gma.con')")
    cr.execute("insert into users (id, name, birth, email) values (3, 'Mohamed', '2057-12-12', 'ghj@gma.con')")
    cr.execute("insert into users (id, name, birth, email) values (4, 'TRy', '2056-12-12', 'sdf@gma.con')")
    cr.execute("insert into users (id, name, birth, email) values (5, 'Dry', '2055-12-12', 'tsdf@gma.con')")
except :
    pass

db.commit()

cr.execute("select * from users order by id desc limit 1")

print(cr.fetchall()[0])


id_user = input("Enter the Number of user:").strip()

try :
    cr.execute("select * from users where id=?", id_user)

except sqlite3.ProgrammingError:
    print("User Not Found.")

else :
    info = cr.fetchone()
    print(f"ID => {info[0]}, Name => {info[1]}, Date Of Birth => {info[2]}, Email => {info[3]}")

finally :
    db.close()
'''
Created on 2021. 7. 22.

@author: pc356
'''

import sqlite3

def createTable():
    # connection 객체 생성
    conn = sqlite3.connect('systemServer.db') # isolation_level = None 생략
    
    # cursor 생성
    c = conn.cursor()
    c.execute('''
        create table if not exists table1
        (id text primary key,
        name text,
        age text,
        gender text,
        bloodtype text,
        remark text)
    ''')
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

# insert할 매개 변수    
def insertData(id, name, age, gender, bloodtype, remark):
    conn = sqlite3.connect('systemServer.db')
    
    c = conn.cursor()
    c.execute('''
        insert into table1(id, name, age, gender, bloodtype, remark)
        values(?, ?, ?, ?, ?, ?)
    ''',(id, name, age, gender, bloodtype, remark))# 매개 변수를 질의문에 넣는 방법
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def insertManyData(tupleData):
    conn = sqlite3.connect('systemServer.db')
    
    c = conn.cursor()
    c.executemany('''
        table1(id, name, age, gender, bloodtype, remark)
        values(?, ?, ?, ?, ?, ?)
    ''',tupleData)# 매개 변수를 질의문에 넣는 방법
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def selectAll():
    conn = sqlite3.connect('systemServer.db')

    c = conn.cursor()
    c.execute('select * from table1')
    
    rows = c.fetchall()
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    return rows

    pass

def select(key):
    conn = sqlite3.connect('systemServer.db')
    
    c = conn.cursor()
    c.execute('select * from table1 where id = ?',(key,)) # key - tuple 형식, 유의
    
    row = c.fetchone()
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    return row
    
    pass

# vo는 dict로 만들어서 보냄
def update(vo): # vo는 tuple 형식임
    conn = sqlite3.connect('systemServer.db')
    
    c = conn.cursor()
    c.execute('''
        update table1 set name = ?, age = ?, gender = ?, bloodtype = ?, remark = ? where id = ?
    ''',vo) # vo - tuple 형식(dict일 경우 복잡함.), 유의
    
     # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def delete(key):
    conn = sqlite3.connect('systemServer.db')
    
    c = conn.cursor()
    res = c.execute('''delete from table1 where id = ?''',(key,)) # key - tuple 형식, 유의
    
     # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass
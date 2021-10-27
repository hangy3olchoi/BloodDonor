'''
Created on 2021. 7. 22.

sqliteCRUD Test

@author: pc356
'''

import sqlite3
from main import sqliteCRUD_HW

if __name__ == '__main__':
    # table 만들기
    sqliteCRUD_HW.createTable()
    
    # 자료 하나 입력하기
    sqliteCRUD_HW.insertData('100', '최한결', '32', '남성', 'Rh+ B','특이사항 없음')
    #
    # # 여러 자료를 동시에 입력하기
    # t_data = (
    #     ('ygs','유관순','1234','삼월하늘'),
    #     ('lss','이순신','1234','한산섬'),
    #     ('ysd','윤선도','1234','지국총')
    # )
    # sqliteCRUD.insertManyData(t_data)
    #
    # sqliteCRUD.selectAll()
    # sqliteCRUD.select('hgd')
    # sqliteCRUD.update(('홍길동','1237','동서번쩍','hgd')) # update시 질의문의 물음표 순서에 맞추어 tuple 형식으로 작성할 것!
    # sqliteCRUD.delete('hgd')
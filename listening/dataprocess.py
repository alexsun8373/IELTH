#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sqlite3
import re
import sys
#reload(sys)
sys.setdefaultencoding('utf8')

def creat_database(db_name,table_name,array):
    conn = sqlite3.connect(db_name)
    conn.text_factory = str
    c = conn.cursor()
    # create table
    c.execute("CREATE TABLE "+ table_name +" (id integer primary key,org text,act text,comments text, error_mark integer,remembered integer)")
    c.executemany("INSERT INTO " + table_name + " VALUES (?,?,?,?,?,?)", array)
    conn.commit()
    for row in c.execute('SELECT * FROM ' + table_name + ' ORDER BY id'):
        print(row)
    conn.close


def add_table(db_name, table_name, list_ele):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # create table
    c.execute("CREATE TABLE " + table_name + " (id integer primary key,org text,act text,comments text, error_mark integer,remembered integer)")
    c.executemany("INSERT INTO " + table_name + " VALUES (?,?,?,?,?,?)", list_ele)
    for row in c.execute('SELECT * FROM ' + table_name + ' ORDER BY id'):
        print(row)
    conn.commit()
    conn.close


def delete_table(db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    # DELETE table
    c.execute("DROP TABLE " + table_name)

    conn.commit()
    conn.close

def show_tables(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ' + table_name + ' WHERE error_mark=? AND remembered=?',(1,0))
    results = cursor.fetchall()
    G_DB_ROW_LENGTH = len(results)
    conn.close

# function: process a sentence to recreate 2 sentences
# input:    a sentence
# output1:  what I have write
# output2:  The standardized one
def sentence_check(sentence):
    global array,number

    if number == 37:
        print("debug")
    #value = re.findall(r'[(](.*?)[)]', sentence)
    value = re.split('[()]', sentence)
    if not '(' in sentence:#right
        org = sentence
        act = ''
        comments = ''
        error_mark = 0
    else:
        org = ''
        act = ''
        for l in value:
            if "#" in l:
                act = act + ' ' + re.findall(r'\s(.+)[/]', l)[0]
                org = org + ' ' + re.findall(r'[/](.+)', l)[0]
            else:
                act = act + l
                org = org + l
        error_mark = 1

    array.append((number,unicode(org),unicode(act),unicode(''),error_mark,1))
    #array.append((number, org, act, '', error_mark, 1))

    #array.append()
    #array.append('')#comments
    #array.append()

    #print(array)

if __name__ == '__main__':
    file_name = 'l1_t13.txt'
    table_name = file_name[:-4]
    array=[]
    number = 0
    file = open(file_name,'r')
    for line in open(file_name):
    	#print(line)
        if(not len(line.replace('\r','').replace('\n',''))):
            continue
    	sentence_check(line.replace('\r','').replace('\n',''))
        number = number + 1
        print(number)
    #delete_table("listentothis.db",table_name)
    add_table("listentothis.db",table_name,array)
    show_tables("listentothis.db",table_name)
import sqlite3
import re
def count_title():
    field_list = select_column('title')
    for title in field_list:
        for name in create_permanent_concil_list():
            match_list =re.findall(name, title)
            


def select_column(field):
    # print(field)
    conn = sqlite3.connect("data.sqlite")
    cur = conn.cursor() 
    cur.execute("select " + field + " from article")
    field_list =[]
    for line in cur:
        field_list.append(line[0])
    cur.close()
    conn.close()
    return field_list


def create_permanent_concil_list():
    return ('习近平','李克强','张德江','俞正声','刘云山','王岐山','张高丽')


if __name__=='__main__':
    # print (create_permanent_concil_list())
    # select_column("title')
    count_title()
    # for i in field_list:
    #     print (i)
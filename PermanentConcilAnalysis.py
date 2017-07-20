import sqlite3
import re
def count_name_title():
    field_list = select_column('title')
    count_result = create_council_dic(create_permanent_concil_list())
    for title in field_list:
        for name in count_result.keys():
            match_list =re.findall(name, title)
            count = count_result[name]
            count_result[name] = count + len(match_list)
    print("Name in title counts: ", count_result)    
            

def create_council_dic(name_list):
    count_result = {}
    for name in name_list:
        count_result[name]= 0
    return count_result

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
    count_name_title()
    # for i in field_list:
    #     print (i)
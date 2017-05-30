
import re
import sqlite3

# Фунція для пошуку значень та підготовка до занесення в БД.

def email(data):
    data_set = []
    all_pattern = re.compile('^From ([\w\.]+@[\w\.]+) [A-Z][a-z]{2}\s([A-Z][a-z]{2})', re.M)
    emails_pattern = re.compile('^From ([\w\.]+@[\w\.]+) [A-Z][a-z]{2}\s[A-Z][a-z]{2}', re.M)
    data_all = all_pattern.findall(data)
    emails = emails_pattern.findall(data)
    lats_date_all = {email:date for email,date in data_all}
    

    for i in set(emails):
        #print i, emails.count(i), lats_date_all[i]
        
        data_set.append((i, emails.count(i), lats_date_all[i]))
    return data_set

if __name__ == "__main__":
    data = open('mbox.txt').read()
    up = email(data)
    print 'up', up

    # Cтворення файлу БД, її таблиці, та заповнення даними.

    conn = sqlite3.connect('exam_3.sqlite')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS DATA")
    cur.execute("CREATE TABLE DATA (email TEXT, count INTEGER, date TEXT)")
    for email, count, date in up:
        cur.execute("INSERT INTO DATA (email,date,count) VALUES (?,?,?)",(email,date,count))
        
      
    conn.commit()
    sqlstr = 'SELECT email, count, date FROM DATA Order BY date, count DESC, DATA.date, DATA.count LIMIT 10 '
    
    for elements in cur.execute(sqlstr) :
        print elements
        

    cur.close()
   
    conn.close()

import sys
import sqlite3 
def read(x):
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    c. execute('''Select cosx from cosines where x= ?''', (x,))
    a = c.fetchone()
    conn.commit()
    conn.close()
    return a[0]
   
if __name__=="__main__":
    x = float(sys.argv[1])
    a = read(x)
    print(a)

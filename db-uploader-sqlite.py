import sqlite3

urls = ["<insert links>"] 

connection = sqlite3.connect("linkdrop")

connection.execute("CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY, url STRING, used BOOL);")

insert_query = ("INSERT INTO links (id, url, used)" 
                "VALUES (:id, :url, :used);")

for i, url in enumerate(urls):
  author_parameters = {
          'id': i,
          'url': url,
          'used': False
      }
  
  connection.execute(insert_query, author_parameters)

connection.commit()
connection.close()




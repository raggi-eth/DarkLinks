from replit import web
import sqlite3
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index_sqlite():
  connection = sqlite3.connect("linkdrop")

  result = connection.execute("UPDATE links SET used = true WHERE id in (SELECT id FROM links WHERE used == false LIMIT 1) RETURNING url").fetchone()

  connection.commit()
  connection.close()

  if not result:
    return('Dispenser is out of NFTs')
  else:
    return redirect(result[0], code=302, Response=None)

@app.route("/used-links")
def links():
  connection = sqlite3.connect("linkdrop")

  result = connection.execute("SELECT * FROM links WHERE used == true").fetchall()

  connection.commit()
  connection.close()

  if result:
    return result

web.run(app, debug=True)
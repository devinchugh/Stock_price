from flask import Flask, render_template

import os
import requests
import urllib.parse

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)




def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = "pk_fc6f5ddb92a3402db06c38afd053fe19"
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

# Custom filter
app.jinja_env.filters["usd"] = usd    


@app.route("/", methods=["GET", "POST"])
def index():
    # connect withe the myTable database
    connection = sqlite3.connect("myTable.db", check_same_thread=False)

    # cursor object
    crsr = connection.cursor()
    if request.method == "POST":
         sym = request.form.get("symbol")
        # execute the command to fetch all the data from the table emp
         crsr.execute("SELECT * FROM names")

        # store all the fetched data in the ans variable
         data = crsr.fetchall()
         chk=1
         for name in data:
             if str(name[1])==str(sym):
                 chk=0
                 

         if chk:
              crsr.execute("INSERT INTO names(symbol) values(?)",(sym,))
         redirect("/")
         



    

# execute the command to fetch all the data from the table emp
    crsr.execute("SELECT * FROM names")

# store all the fetched data in the ans variable
    data = crsr.fetchall()

    prices=[]
    for name in data:
        item=lookup(name[1])
        prices.append(item)

    connection.commit()
  
    # Close the connection
    connection.close()
    return render_template("index.html", prices=prices)



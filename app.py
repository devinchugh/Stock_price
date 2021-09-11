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



@app.route("/", methods=["GET", "POST"])
def index():
    #if request.method == "POST":
    return render_template("index.html")
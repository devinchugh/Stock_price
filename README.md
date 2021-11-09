# Stock_price
This will do the basic task of showing the Stock Prices for the stocks-added.

Video Explaining Project: https://youtu.be/CK5WG3NKcVw

My project is all about solving the problem for those people who wish to monitor real-time stock prices of some particular stocks. 
It uses an API from IEX Cloud to get the prices for stock added. It also have a backend to store the stocks name added by user and the user can also delete the stocks when needed.

The project mainly uses Flask for backend and sqlite as database. The frontend of the application is quite simple using only HTML and CSS.

My main motive behind this application is that when I have some stock bought and I wish to see their consolidated prices at one place and watch them in real time, there is no place to go to. This web app allowed me to do that using only some lines of code and a little logic.

Have a look over the code and improvements are heartly Welcomed.

<b>Details of the Files in Project:</b><br>
  1-static/style.css: This file contains the frontend styling for the Web application apart from the bootstrap utilised in designing.<br>
  2-templates/index.html: This file contains the HTML for the homepage of the web application.<br>
  3-app.py: This file contains all the code for backend consisting of the main logic and flask which makes the web application dynamic.<br><br>
  4-myTable.db: This file is the database for this project containing the table to store the stocks which the user wish to moniter.<br>

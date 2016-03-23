"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, jsonify

PASSWORD = "1234"
TOKEN = "ZkNjA4MzBiIiwiZW1haWwiOiJhQGEuY29tIiwibmFtZSI6ImEiLCJjYXJ0IjpbeyJpZCI6IjU1NjgzY2Q4ZmJiMmUxOTI0ZjE4YTRlYSIsInF0eSI6MX1dLCJwdXJjaGFzZXMiOlt7IlB1cmNoYXNlIG1hZGUgb24gMjktTWF5LTIwMTUgYXQgMTc6NTAiOlt7ImlkIjoiNTU2ODNjZDhmYmIyZTE5MjRmMThhNGU4IiwicXR5IjoxfV19LHsiUHVyY2hhc2UgbWFkZSBvbiAyOS1NYXktMjAxNSBhdCAxNzo1OSI6W3siaWQiOiI1NTY4M2NkOGZiYjJlMTkyNGYxOGE0ZWIiLCJxdHkiOjF9LHsiaWQiOiI1NTY4M2NkOGZiYjJlMTkyNGYxOGE0ZjYiLCJxdHkiOjF9LHsiaWQiOiI1NTY4M2NkOGZiYjJlMTkyNGYxOGE0ZjgiLCJxdHkiOjF9XX0seyJ"

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/api/user/login')
def user_login():
    """Processes an user login"""
    
    
    response = {}
    email = request.args.get('email')
    password = request.args.get('password')
    if password == PASSWORD:
       response['data'] = {}    
       response['data']['token'] = TOKEN
       response['data']['error'] = "null"
       response['data']['user'] = {
            "_id": "5568596827fccbc16d60830b",
            "email": email,
            "name": "Me Brown"}
    # processing
    else:
        response = {
             "error": "1",
             "data": {
              },
           "message": "Bad user name or password"
        } 
    return jsonify(response)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")

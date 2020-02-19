#!/usr/local/bin/python3
import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")
lastname = form.getvalue("lastname")


""" name = input("What's your name?")
last_name = input("What's your last name?")
print("Hi, " + name + last_name) """

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
  <h1>Hello {firstname} {lastname}, welcome to foundations</h1>
</body>

</html>
""".format(firstname=name, lastname=lastname)

print(html)

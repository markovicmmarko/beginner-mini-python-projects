from flask import Flask, render_template, request

app = Flask("my app")

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/report")
def report():
    uname = request.args.get('uname')
    lowers = any(char.islower() for char in uname)
    uppers = any(char.isupper() for char in uname)
    end_num = uname[-1].isdigit()
    poruka = ""

    if not lowers and uppers and end_num:
        poruka = "You have to use a lower case letter ...."
    elif lowers and not uppers and end_num:
        poruka = "You have to use an upper case letter...."
    elif not lowers and not uppers and end_num:
        poruka = "You didn't passed the upper and lower case letter requirement...."
    elif not lowers and uppers and not end_num:
        poruka = "You didn't passed the lower case letter requirement and last symbol digit requirement...."
    elif lowers and not uppers and not end_num:
        poruka = "You didn't passed the upper case letter requirement and last symbol digit requirement...."
    elif lowers and uppers and not end_num:
        poruka = "You didn't passed the last symbol digit requirement...."


    if not poruka:
        return render_template("report.html", uname=uname)
    else:
        return render_template("reportfalse.html", poruka=poruka)







app.run()
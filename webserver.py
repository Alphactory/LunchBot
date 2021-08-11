import flask

todays_orders = dict()
app = flask.Flask(__name__)


@app.route('/')
def index():
    return """
    <b>Lunch Form</b>
    <br>
    <form  action="/api" method="POST">
    Name:<br>
    <input type="text" id="name" name="name" value="John Doe"><br>
    Order:<br>
    <input type="text" id="lunchorder" name="lunchorder" value="Cheese Sandwich"><br>
    <input type="submit" value="Submit">
    </form>
    """


@app.route('/api', methods=['POST'])
def api():
    todays_orders[flask.escape(flask.request.form.get("name"))] = flask.escape(flask.request.form.get("lunchorder"))
    return flask.redirect("/orders", 302)

@app.route('/clear')
def clear_dict():
    todays_orders.clear()
    return flask.redirect("/orders", 302)


@app.route('/orders')
def show_orders():
    result = ""
    if len(todays_orders.keys()) < 1:
        return "No orders ~~(' u ')~~"
    for key in todays_orders.keys():
        result += f"{key} wants {todays_orders[key]}<br>"
    return result

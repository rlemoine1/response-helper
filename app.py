from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form.get('actively trading') == 'actively trading':
            return redirect(url_for("actively_trading")) 
        elif request.form.get('actively trading fiat') == 'actively trading fiat':
            return redirect(url_for("actively_trading_fiat"))
        elif request.form.get('stale fiat, active USD price') == 'stale fiat, active USD price':
            return redirect(url_for('stale_fiat_active_usd'))
        elif request.form.get('stable usd') == 'stable usd':
            return redirect(url_for('stable_usd'))
        elif request.form.get('further investigation') == 'further investigation':
            return render_template('further_inv.html')
        elif request.form.get('client provides alternative price') == 'client provides alternative price':
            return redirect(url_for('alt_price'))
        elif request.form.get('large movement') == 'large movement':
            return redirect(url_for('large_mov'))
        elif request.method == 'GET':
            return render_template('index.html', form=form)

    return render_template("index.html")

@app.route('/actively_trading', methods=['GET', 'POST'])
def actively_trading():
    if request.method == 'GET':
        return render_template("actively_trading.html")
    elif request.method == 'POST':  
        pe = request.form['pe']
    return render_template("actively_trading_email.html", pe = pe)


@app.route('/actively_trading_fiat', methods=['GET', 'POST'])
def actively_trading_fiat():
    if request.method == 'GET':
        return render_template("actively_trading_fiat.html")
    elif request.method == 'POST':  
        pe = request.form['pe']
        base = request.form['base']
    return render_template("actively_trading_fiat_email.html", pe=pe, base=base)

@app.route('/stale_fiat_active_usd', methods=['GET', 'POST'])
def stale_fiat_active_usd():
    if request.method == 'GET':
        return render_template("stale_fiat_active_usd.html")
    elif request.method == 'POST':
        pair_code = request.form['pair_code']
        pe = request.form['pe']
        base_pair = request.form['base_pair']
        time_stamp = request.form['time_stamp']
        price = request.form['price']
        base_counter_asset = request.form['base_counter_asset']
    return render_template("stale_fiat_active_usd_email.html", pair_code=pair_code, pe=pe,
    base_pair=base_pair, time_stamp=time_stamp, price=price, base_counter_asset=base_counter_asset)

@app.route('/stable_usd', methods=['GET', 'POST'])
def stable_usd():
    if request.method == 'GET':
        return render_template("stable_usd.html")
    elif request.method == 'POST':
        pair_code = request.form['pair_code']
        pe = request.form['pe']
        base_pair = request.form['base_pair']
        time_stamp = request.form['time_stamp']
        price = request.form['price']
    return render_template("stable_usd_email.html", pair_code=pair_code, pe=pe, base_pair=base_pair,
    time_stamp=time_stamp, price=price)

@app.route('/alt_price', methods=['GET','POST'])
def alt_price():
    if request.method == 'GET':
        return render_template("alt_price.html")
    elif request.method == 'POST':
        derived_asset = request.form['derived_asset']
        pe = request.form['pe']
    return render_template("alt_price_email.html", derived_asset=derived_asset, pe=pe)

@app.route('/large_mov', methods=['GET', 'POST'])
def large_mov():
    if request.method == 'GET':
        return render_template("large_mov.html")
    elif request.method == 'POST':
        pe = request.form['pe']
    return render_template("large_mov_email.html", pe=pe)


if __name__=='__main__':
	app.run(debug=True)


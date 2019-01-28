from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from cryptomaze.forms import SignUpForm, ClaimForm, WithdrawForm
from cryptomaze.models import User, Withdraw
from cryptomaze import app, db, bcrypt
from cryptomaze.referrals import ref_count, apply_discount
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import desc
from random import randint, uniform
from datetime import datetime
import cryptomaze.settings as settings
from cryptomaze.calculate_time import calc_time
from cryptomaze.send_bitcoin import send_bitcoin

#imports required for jQuery
from cryptomaze.validate_btc_address import check_bc


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home():
    js_scripts = ['toastr.min.js', 'signup-pg.js']
    users = db.session.query(User).count()
    records = Withdraw.query.all()
    paid = 0
    for record in records:
        paid =+ record.amount
    paid = round(paid, 8)

    if current_user.is_authenticated:
        return redirect(url_for('claim'))
    signupform = SignUpForm()
    if signupform.validate_on_submit():
        #users = db.session.query(User).count()
        user = User.query.filter_by(
            bitcoin_address=signupform.bitcoin_address.data).first()
        if user:
            login_user(user, remember=True)
            return redirect(url_for('claim'))
        else:
            referred_by = request.args.get('ref')
            if not referred_by:
                referred_by = 0
            user = User(bitcoin_address=signupform.bitcoin_address.data,
                        referred_by=referred_by)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('claim'))
    return render_template('index.html', faucet_name=settings.faucet_name, max_commission=settings.max_commission, time=int(settings.time/60), claim=settings.claim, signupform=signupform, users=users, paid=paid, index_page=True, js_scripts=js_scripts)


@app.route('/claim', methods=['GET', 'POST'])
@login_required
def claim():
    js_scripts = ['sweetalert2.min.js', 'claim-pg.js']
    claimform = ClaimForm()
    if claimform.validate_on_submit():
        if current_user.last_claim_date:
            time_count = calc_time(current_user.last_claim_date)
            if time_count >= settings.time:
                claim_amount = round(uniform(
                    settings.claim['starting amount'], settings.claim['last amount']), 8)
                current_user.btc_balance = round((current_user.btc_balance + claim_amount), 8)
                current_user.last_claim_date = datetime.utcnow()
                db.session.commit()

                # Calculating the referral amount and updating the database
                referred_user = User.query.get(current_user.referred_by)
                if referred_user:
                    ref_amount = round((apply_discount(ref_count(referred_user.id)) / 100.0 * claim_amount), 8)
                    referred_user.ref_balance = round((referred_user.ref_balance + ref_amount), 8)
                    referred_user.btc_balance = round((referred_user.btc_balance + ref_amount), 8)
                    db.session.commit()
                #

                flash('Boom! You claimed {} Satoshi!'.format(str(int(claim_amount * 100000000))), category='notify-claim-msg')
                return redirect(url_for('claim'))
            else:
                flash('Please wait {} minutes for next claim.'.format(
                    str(5 - int(time_count / 60))), category='notify-claim-warning')
                return redirect(url_for('claim'))
        else:
            claim_amount = round(uniform(
                settings.claim['starting amount'], settings.claim['last amount']), 8)
            current_user.btc_balance = round((current_user.btc_balance + claim_amount), 8)
            current_user.last_claim_date = datetime.utcnow()
            db.session.commit()
            flash('You have claimed {} sat!'.format(
                str(claim_amount)), category='info')
            return redirect(url_for('claim'))
    return render_template('claim.html', title='Claim', faucet_name=settings.faucet_name, claimform=claimform, max_commission=settings.max_commission, time=int(settings.time/60), claim=settings.claim, js_scripts=js_scripts)
    
    
@app.route('/referral')
@login_required
def referral():
    return render_template('referral.html', title='Referrals', faucet_name=settings.faucet_name, faucet_url=settings.faucet_url, ref_count=ref_count(current_user.id), ref_commission=apply_discount(ref_count(current_user.id)), discount_list=settings.sorted_discount_list, max_commission=settings.max_commission)


@app.route('/withdrawals', methods=['GET', 'POST'])
@login_required
def withdrawals():
    js_scripts = ['sweetalert2.min.js', 'withdrawal-pg.js']
    withdrawform = WithdrawForm()
    btc_balance = current_user.btc_balance
    if withdrawform.validate_on_submit():
        if current_user.btc_balance >= settings.threshold:
            if send_bitcoin(current_user.bitcoin_address, current_user.btc_balance):
                withdraw = Withdraw(amount=current_user.btc_balance, bitcoin_address=current_user.bitcoin_address,
                                withdraw_date=datetime.utcnow(), user_id=current_user.id)
                current_user.btc_balance = 0
                db.session.add(withdraw)
                db.session.commit()
                flash("Withdrawal placed", category="with-success")
                return redirect(url_for('withdrawals'))
            else:
                flash("We had some trouble sending Bitcoin", category="with-denied")
                return redirect(url_for('withdrawals'))
        else:
            flash('Please maintain at least {} Satoshi in your account to place a withdraw'.format(str(int(settings.threshold * 100000000))), category='enough-balance')
            return redirect(url_for('withdrawals'))

    user_withdrawals = Withdraw.query.filter_by(user_id=current_user.id).order_by(desc(Withdraw.withdraw_date))

    if user_withdrawals:
        page = request.args.get('item', 1, type=int)
        user_withdrawals = user_withdrawals.paginate(page, per_page=10).items
        iter_pages = Withdraw.query.paginate(page, per_page=10).iter_pages(
            left_edge=1, right_edge=1, left_current=1, right_current=2)

        for row in user_withdrawals:
            if not row.status == 1:
                if calc_time(row.withdraw_date) >= settings.sending_time:
                    row.status = 1
                    db.session.commit()
    else:
        iter_pages = None
        page = None

    return render_template('withdrawals.html', title='Withdrawals',  faucet_name=settings.faucet_name, withdrawform=withdrawform, btc_balance=btc_balance, user_withdrawals=user_withdrawals, iter_pages=iter_pages, page=page, js_scripts=js_scripts)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/ct65756587', methods=['POST'])
def checkbtcaddress():
    bitcoin_address = request.form['bitcoin_address']

    return jsonify({
        'status': check_bc(bitcoin_address)
    })

@app.route('/t8746544', methods=['GET', 'POST'])
def timecount():
    last_claim = current_user.last_claim_date.strftime('%c')
    return jsonify({
        'last': last_claim,
        'time': int(settings.time / 60)
    })


@app.route('/nojs')
def no_js():
   return '<h1>We need you to enable JavaScript in your browser before accessing this site! <br><a href="http://landofcoins.xyz">Go back home</a></h1>'

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('home'))

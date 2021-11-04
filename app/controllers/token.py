from flask import Blueprint, render_template
from flask import request
import requests
from json2html import *

bp_token = Blueprint('token', __name__, url_prefix='/')


@bp_token.route('/token/')
def token():
    try:
        url = 'https://ar-elections-2021-api.auth.us-east-2.amazoncognito.com/oauth2/token'
        authorization_code = request.args.get('code')
        client_id = '26mcuibmjcn677ikq9b1endmj1'
        grant_type = 'authorization_code'
        authorization = 'Basic MjZtY3VpYm1qY242Nzdpa3E5YjFlbmRtajEgMXMxN2hncDFkcXBhcHF1c2Q4NGo2N2xldTU1ajMybTkxdXBlYm1iMTRkc2ttZDlxOWdzOQ=='

        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': authorization,
        }

        body = 'grant_type=' + grant_type + '&client_id=' + client_id + '&code=' + authorization_code + '&redirect_uri=https://ar.apielectoral.org/token/'

        response = requests.request('POST', url, headers=headers, data=body)
        # print(response.request.url)
        # print(response.request.body)
        # print(response.request.headers)

        return render_template('token.html', authorization_code=authorization_code, response=json2html.convert(json=response.json()))
    excempt:
        return render_template('error.html')

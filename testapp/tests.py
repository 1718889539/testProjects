# coding: utf-8
import requests

url = 'http://sfapaas.sfair.com//login/accounts/is_login/'

bk_token = 'HsKjqI5ADYFoc5xx1YDb5PK0YTtTRHSMolHMwCZ21tI'

url_get_user = ' http://sfapaas.sfair.com/api/c/compapi/v2/bk_login/get_user/'


def check_bk_token(token):
    res = requests.get(url + '?bk_token=%s' % token)
    data = res.json()
    print data.get('message').encode('utf-8')


def check_user(token):
    res = requests.post(url_get_user, params=str({'bk_token': token}), data={''})
    data = res.json()
    print data


check_user(bk_token)

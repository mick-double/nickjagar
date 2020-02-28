''' 

いよいよ欲しかった情報に手を届かせる
AV女優リスト

'''
import urllib.request


# キーセット
APIID = 'wn2k2FSt6C1QFqcLLxgG'
AFFILIATEID = 'nickjagar-990'
KEYWORD = 'しのだ'
hitnum = '10'
outformat = 'json'

'''

memo:
https://api.dmm.com/affiliate/v3/ActressSearch?api_id=[APIID]&affiliate_id=[アフィリエイトID]&keyword=%e3%81%82%e3%81%95%e3%81%bf&gte_bust=90&lte_waist=60&sort=-bust&hits=10&offset=10&output=json

'''
url = 'https://api.dmm.com/affiliate/v3/ActressSearch?api_id='+APIID+'&affiliate_id='+AFFILIATEID+'&keyword='+KEYWORD+'&hits='+hitnum+'&output='+outformat

print(url)
#DMMのAPIからreqオブジェクト取得
req = urllib.request.Request(url)

try:
    with urllib.request.urlopen(req) as res:
        body = res.read()
        pritn(body)
except urllib.error.HTTPError as err:
    print(err.code)
except urllib.error.URLError as err:
    print(err.reason)


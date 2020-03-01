''' 

いよいよ欲しかった情報に手を届かせる
AV女優リスト

'''
import requests,bs4,csv,pprint,json


# キーセット
APIID = 'wn2k2FSt6C1QFqcLLxgG'
AFFILIATEID = 'nickjagar-990'
KEYWORD = 'ゆう'
hitnum = '100'
outformat = 'json'

# 出力ファイル名
output01_json = 'avlist.json'

'''

memo:
https://api.dmm.com/affiliate/v3/ActressSearch?api_id=[APIID]&affiliate_id=[アフィリエイトID]&keyword=%e3%81%82%e3%81%95%e3%81%bf&gte_bust=90&lte_waist=60&sort=-bust&hits=10&offset=10&output=json

'''
url = 'https://api.dmm.com/affiliate/v3/ActressSearch?api_id='+APIID+'&affiliate_id='+AFFILIATEID+'&keyword='+KEYWORD+'&hits='+hitnum+'&output='+outformat

print(url)
#DMMのAPIからreqオブジェクト取得
# req = urllib.request.Request(url)

res = requests.get(url)
# print(res.text)
pprint.pprint(res.json())
json_data = res.json()
print(type(json_data))

with open(output01_json,'w') as f:
    print('正常に読まれてavlist.jsonファイに書き込みます！')
    json.dump(json_data,f,indent=4,ensure_ascii=False)



actress = json_data['result']['actress']

print(type(actress))

for d in actress:
    actress_name = d.get('name')
    bustsize = d.get('bust')
    cupsize = d.get('cup')
    print(actress_name+':'+str(bustsize)+' '+str(cupsize))



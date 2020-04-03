''' 

いよいよ欲しかった情報に手を届かせる
AV女優リスト
ファイル名は指定したイニシャル＋avlist.txt

'''
import requests,bs4,csv,pprint,json

jp = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]


# キーセット
APIID = 'wn2k2FSt6C1QFqcLLxgG'
AFFILIATEID = 'nickjagar-990'
initial = jp[2]
KEYWORD = 'いい'
hitnum = '100'
outformat = 'json'

# 出力ファイル名
output01_json = 'avlist.json'
gazou_folder = '/home/mitsuya/Pictures/avact/'
avlist = 'avlist.txt'

'''

memo:
https://api.dmm.com/affiliate/v3/ActressSearch?api_id=[APIID]&affiliate_id=[アフィリエイトID]&keyword=%e3%81%82%e3%81%95%e3%81%bf&gte_bust=90&lte_waist=60&sort=-bust&hits=10&offset=10&output=json

'''
url = 'https://api.dmm.com/affiliate/v3/ActressSearch?api_id='+APIID+'&affiliate_id='+AFFILIATEID+'&initial='+initial+'&hits='+hitnum+'&output='+outformat

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


#辞書型は[]で場所特定して抽出

actress = json_data['result']['actress']
print(type(actress))

for d in actress:
    #リスト型は.getで抽出　一つずつ抽出する
    actress_name = d.get('name')
    bustsize = d.get('bust')
    cupsize = d.get('cup')
    waistsize = d.get('waist')
    hipsize = d.get('hip')
    # 画像取得（値がないときは100を返す）
    a_imageURL = d.get('imageURL',100)
    # 女優名と3サイズとcupサイズ
    nsize = actress_name+':'+str(bustsize)+' '+str(waistsize)+' '+str(hipsize)+' '+str(cupsize)+'cup'
    #print(actress_name+':'+str(bustsize)+' '+str(waistsize)+' '+str(hipsize)+' '+str(cupsize)+'cup')
    print(nsize)
    with open(initial+avlist,"a") as al:
        al.write(nsize+'\n')

    if not a_imageURL == 100:
        # print(type(a_imageURL))
        a_image = a_imageURL['large']
        print(a_image)
        # URLからjpgファイル名を抽出
        a_image_f = a_image[35:]
        print(a_image_f)
        print(gazou_folder+a_image_f)
        image_res = requests.get(a_image)
        a_image_con = image_res.content
        with open(gazou_folder+a_image_f,"wb") as aaa:
            aaa.write(a_image_con)




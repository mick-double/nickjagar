'''

AV女優リストを取り出すための前のテスト

'''
import requests,bs4,csv,pprint,json



d = {
    "request": {
        "parameters": {
            "api_id": "wn2k2FSt6C1QFqcLLxgG",
            "affiliate_id": "nickjagar-990",
            "keyword": "しのだ",
            "hits": "10",
            "output": "json"
        }
    },
    "result": {
        "status": "200",
        "result_count": 10,
        "total_count": "40",
        "first_position": 1,
        "actress": [
            {
                "id": "15301",
                "name": "篠田亜紀",
                "ruby": "しのだあき",
                "listURL": {
                    "digital": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D15301%2F&af_id=nickjagar-990&ch=api",
                    "monthly": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D15301%2F&af_id=nickjagar-990&ch=api",
                    "ppm": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fppm%2Fvideo%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D15301%2F&af_id=nickjagar-990&ch=api",
                    "mono": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmono%2Fdvd%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D15301%2F&af_id=nickjagar-990&ch=api",
                    "rental": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Frental%2Fppr%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D15301%2F&af_id=nickjagar-990&ch=api"
                }
            },
            {
                "id": "1001520",
                "name": "篠田秋乃",
                "ruby": "しのだあきの",
                "cup": "C",
                "waist": "60",
                "hip": "83",
                "height": "162",
                "listURL": {
                    "digital": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fdigital%2Fvideoa%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D1001520%2F&af_id=nickjagar-990&ch=api",
                    "monthly": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmonthly%2Fpremium%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D1001520%2F&af_id=nickjagar-990&ch=api",
                    "ppm": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fppm%2Fvideo%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D1001520%2F&af_id=nickjagar-990&ch=api",
                    "mono": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmono%2Fdvd%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D1001520%2F&af_id=nickjagar-990&ch=api",
                    "rental": "https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Frental%2Fppr%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D1001520%2F&af_id=nickjagar-990&ch=api"
                }
            }
        ]    
    }
}

# print(d)

actress = d['result']['actress']

# print(actress)

print(type(actress))

actress_name = [d.get('name') for d in actress]
print(actress_name)

# print(d['result']['actress']['name'])
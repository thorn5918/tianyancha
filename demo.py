import  requests

def getAuthorized():
    jsonNode = requests.get("http://tycservice.vipgz2.idcfengye.com/tyc/vip/getAuthorization?deviceId=095f80d134fb2b0873a47fe445ed0ca5").json()
    return jsonNode
if __name__ == '__main__':
    searchUrl = "https://api2.tianyancha.com/services/v3/search/sNorV3/{}?allowModifyQuery=1&pageSize=10&pageNum=1&sortType=0"
    header={
        "Authorization": "",
        "X-Auth-Token": "",
        "User-Agent": "com.tianyancha.skyeye/Dalvik/2.1.0 (Linux; U; Android 9; oppo qbs Build/PKQ1.180819.001;)",
        "version": "Android 8.5.1",
        "deviceID": "",
        "channelID": "PPZhuShou",
        "Content-Type": "application/json",
        "Host": "api2.tianyancha.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }

    # 获取天眼查app的Authorization
    authorized = getAuthorized()
    header['Authorization'] = authorized['Authorization']
    header['deviceID'] = authorized['deviceID']
    # 调用搜索接口获取公司列表
    resp = requests.get(searchUrl.format("北京公象未来科技"), headers= header, verify=False)
    print(resp.text)

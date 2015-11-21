#coding=utf-8
import urllib.request
import json

city = {'city':'beijing'}
url_city = urllib.parse.urlencode(city)
url = 'http://apis.baidu.com/heweather/weather/free'+'?'+url_city
header = {'apikey':'edca0f473f30494db08da4b090ba506a'}
req = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(req)
content = response.read()

s = json.loads(content.decode())
for key in s.keys():
    weatherAllInfoMap = s[key][0]
    
    #-------------基本信息---------------
    basicInfoMap = weatherAllInfoMap['basic']
    lat = basicInfoMap['lat'] #城市纬度
    lon = basicInfoMap['lon'] #城市经度
    updateInfoMap = basicInfoMap['update']
    loc = updateInfoMap['loc'] #当地时间

    #------------实况天气----------------
    todayWeatherInfpMap = weatherAllInfoMap['now']
    fl = todayWeatherInfpMap['fl'] #体感温度
    hum = todayWeatherInfpMap['hum'] #相对湿度
    tmp = todayWeatherInfpMap['tmp'] #温度
    pcpn = todayWeatherInfpMap['pcpn'] #降水量
    pres = todayWeatherInfpMap['pres'] #气压
    vis = todayWeatherInfpMap['vis']  #能见度(km)
    todayWindInfoMap = todayWeatherInfpMap['wind']
    deg = todayWindInfoMap['dir'] #风向
    sc = todayWindInfoMap['sc']   #风力
    spd = todayWindInfoMap['spd'] #风速
    todayStatusMap = todayWeatherInfpMap['cond']
    status = todayStatusMap['txt'] #天气状况描述(晴)

    #------------空气质量----------------
    airInfoMap = weatherAllInfoMap['aqi']['city']
    aqi = airInfoMap['aqi'] #空气质量指数
    pm25 = airInfoMap['pm25'] #PM2.5
    qlty = airInfoMap['qlty'] #空气质量类别

print('城市纬度:'+lat+'\r\n城市经度:'+lon+'\r\n温度:'+tmp+'\r\n天气状况:'+status+'\r\n空气质量指数:'+aqi+'\r\nPM2.5:'+pm25+'\r\n空气质量类别:'+qlty)

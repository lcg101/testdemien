#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Rack view


import urllib2, json, os, commands, sys

cnt=[]
loc= ""
loc_list=[]
loc_result=[]
location=[]


# 서버 정보
host_info_list=[]
barcode_list=[]
serial_list=[]
model_list=[]
osname_list=[]
mac_address_list=[]
vendor_list=[]

# 위치 정보
loc_b=[]
loc_f=[]
loc_x=[]
loc_y=[]
loc_z=[]

# color variable
C_POINT="\033[1m"  # 강조하기
C_YELLOW="\033[33m" # 노란색
C_GREEN="\033[32m" # 초록색
C_END="\033[0m" # 모든 효과 제거
C_RED="\033[31m" # 빨간색
C_CYAN="\033[36m" # 청록색
C_PURPLE="\033[35m" # 보라색
C_BLUE="\033[34m" # 파란색



try:
    loc = sys.argv[1].split("-")

    server_api_json = urllib2.urlopen("http://api.ims.daumkakao.io/v1/serverViews?loc_b=%s&loc_f=%s&loc_x=%s&loc_y=%s" %(loc[0].upper(),loc[1],loc[2],loc[3]))
    json_dic = json.loads(server_api_json.read())
    server_list = json_dic['results']

    for i in range(len(server_list)):
        if server_list[i] ['server_type'] == "VM":
            pass
        else:
            loc_result.append(server_list[i])

    loc_result.sort(key=lambda x: int(x['loc_z']), reverse=True)

    cnt = len(server_list)
    os.system('clear')



    print("="*20+C_YELLOW +loc[0]+'-'+loc[1]+'-'+loc[2]+'-'+loc[3]+C_END + " Rack View " + "="*20 )
    print(C_YELLOW + "     Hostname    Barcode  Serial    Vendor    Model     Ip         Management_ip       Location"+C_END  )
    for i in range(len(loc_result)):
         print("%s %s %s %s %s %s %s  %s-%s-%s-%s-%s" % ( loc_result[i]['hostname']  ,loc_result[i]['barcode'],loc_result[i]['serial'], C_GREEN + C_POINT + loc_result[i]['vendor'] + C_END , C_GREEN + loc_result[i]['model_name'] + C_END, C_BLUE + C_POINT + loc_result[i]['ip']+ C_END ,C_CYAN + C_POINT + loc_result[i]['management_ip'] + C_END , C_PURPLE + C_POINT + loc_result[i]['loc_b'],loc_result[i]['loc_f'],loc_result[i]['loc_x'],loc_result[i]['loc_y'],loc_result[i]['loc_z'] +C_END ))
    print(C_CYAN + "Server Total :  %s"  %(C_RED+C_POINT+ str(cnt) + C_END )+C_CYAN + "ea"+ C_END )
    print("=" * 55)



except IndexError:
    print(C_RED +"[Fail]" +C_END +" Input Rack. ex) ./Rack_View.py GS2-054-14-05")

except urllib2.HTTPError:
    print("찾을수 없는  정보를 입력하셨습니다.")
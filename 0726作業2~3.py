import os
import os.path
import shutil
import xlrd
import matplotlib.pyplot as plt    # 匯入 matplotlib 程式庫
import sys
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

"""
========題目-第二題=============
南投縣      全區     新增確診人數
南投縣      全部加起來     新增確診人數

台中市      全區     新增確診人數
台中市      全部加起來     新增確診人數

台北市      全區     新增確診人數
台北市      全部加起來     新增確診人數

==========題目-第三題========================
南投縣       台中市     台北市        新增確診人數
 圖形化
"""

read=xlrd.open_workbook('covidtable_taiwan_cdc4_1.xls')
sheet=read.sheets()[0]

####################南投縣##################################
def 南投縣():
    # 南投縣  全區新增確診人數
    for i in range(1,sheet.nrows):
        縣市=sheet.cell(i,3).value
        區域=sheet.cell(i,4).value
        確診人數=sheet.cell(i,5).value
        if 縣市=="南投縣" and 區域=="全區":
            print("南投縣全區新增確診人數：",確診人數)
            break

    # 南投縣全部加起來新增確診人數
    list_區域_確診人數=[]
    list_區域=[]
    total=0
    for i in range(1,sheet.nrows):
        縣市=sheet.cell(i,3).value
        區域=sheet.cell(i,4).value
        確診人數=sheet.cell(i,5).value
        if 縣市=="南投縣" and 區域!="全區":
            total=total+int(確診人數)
            list_區域_確診人數.append(int(確診人數))
            list_區域.append(區域)

    print("南投縣全部加起來新增確診人數：",total)
    print(list_區域_確診人數)
    print(list_區域)

    plt.plot(list_區域,list_區域_確診人數)      # 建立圖表 x軸(0,1,2,3) y軸[1,2,3,4]
    plt.xlabel('區')
    plt.ylabel('人數')



####################台中市##################################
def 台中市():
    # 台中市  全區新增確診人數
    for i in range(1, sheet.nrows):
        縣市 = sheet.cell(i, 3).value
        區域 = sheet.cell(i, 4).value
        確診人數 = sheet.cell(i, 5).value
        if 縣市 == "台中市" and 區域 == "全區":
                print("台中市全區新增確診人數：", 確診人數)
                break

    # 台中市全部加起來新增確診人數
    list_區域_確診人數 = []
    list_區域 = []
    total = 0
    for i in range(1, sheet.nrows):
        縣市 = sheet.cell(i, 3).value
        區域 = sheet.cell(i, 4).value
        確診人數 = sheet.cell(i, 5).value
        if 縣市 == "台中市" and 區域 != "全區":
            total = total + int(確診人數)
            list_區域_確診人數.append(int(確診人數))
            list_區域.append(區域)

    print("台中市全部加起來新增確診人數：", total)
    print(list_區域_確診人數)
    print(list_區域)

    plt.plot(list_區域,list_區域_確診人數)  # 建立圖表 x軸(0,1,2,3) y軸[1,2,3,4]
    plt.xlabel('區')
    plt.ylabel('人數')


####################台北市##################################
def 台北市():
    # 台北市  全區新增確診人數
    for i in range(1, sheet.nrows):
        縣市 = sheet.cell(i, 3).value
        區域 = sheet.cell(i, 4).value
        確診人數 = sheet.cell(i, 5).value
        if 縣市 == "台北市" and 區域 == "全區":
                print("台北市全區新增確診人數：", 確診人數)
                break

    # 台北市全部加起來新增確診人數
    list_區域_確診人數 = []
    list_區域 = []
    total = 0
    for i in range(1, sheet.nrows):
        縣市 = sheet.cell(i, 3).value
        區域 = sheet.cell(i, 4).value
        確診人數 = sheet.cell(i, 5).value
        if 縣市 == "台北市" and 區域 != "全區":
            total = total + int(確診人數)
            list_區域_確診人數.append(int(確診人數))
            list_區域.append(區域)

    print("台北市全部加起來新增確診人數：", total)
    print(list_區域_確診人數)
    print(list_區域)

    plt.plot(list_區域,list_區域_確診人數)  # 建立圖表 x軸(0,1,2,3) y軸[1,2,3,4]
    plt.xlabel('區')
    plt.ylabel('人數')





fig, axs = plt.subplots(3,3)
plt.subplot(3,1,1)
南投縣()
plt.subplot(3,1,2)
台中市()
plt.subplot(3,1,3)
台北市()
fig.tight_layout()
fig.suptitle( "南投縣,台中市,台北市  新增確診人數 :" )
plt.show()

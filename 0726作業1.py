import os
import os.path
import shutil
import MyFun01

#1 確認路徑下有沒有"New Floder"資料夾
print(MyFun01.是否有資料夾("New Floder"))

#2 創建一個"New Floder"資料夾
x=MyFun01.新增資料夾("New Floder")
print(x)
# 移動路徑到"New Floder"資料夾
x=MyFun01.移動路徑("New Floder")
print(x)
# 再新的路徑中創建一個"New Floder-1"資料夾
x=MyFun01.新增資料夾("New Floder-1")
print(x)
#在目前路徑下移除資料夾"New Floder-1"
x=MyFun01.移除資料夾("New Floder-1")
print(x)
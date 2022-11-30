import os
import os.path
import shutil


X=("..")

def 新增資料夾(X):
        if os.path.exists(X)==False: # 目前路徑下是否有 folder 資料夾
                os.mkdir(X) # 目前路徑下建立資料夾
        return True
print(os.getcwd())
新增資料夾(X)

def 是否有資料夾(檔名):
        os.path.exists(X)
        return True
y=是否有資料夾(X)
print(os.getcwd())

def 移除資料夾(X):
        os.rmdir(X) # 目前路徑下移除資料夾
        return True
print(os.getcwd())
def 移動路徑(X):
        os.chdir(X) # 移動路徑
        return True
移動路徑(X)
移動路徑("..")
print(os.getcwd())


 
 




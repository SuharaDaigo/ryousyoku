
#エクセルから今日の献立取得
import tweepy
from openpyxl import load_workbook
#日時取得
import datetime
#日本時間に変換
import pytz
#日にち取得
now=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
day=now.day

# エクセルファイルのロード
excel_path='ryousyoku.xlsx'
workbook = load_workbook(filename=excel_path, read_only=True)

# シートのロード
sheet = workbook['Sheet2']
date=0

i=1
while (i<100):
   cell_b_value = str(sheet['B{}'.format(i)].value) #str型にしないとNoneの時エラー

   # 取得した値の表
   
   if "{}".format(day) in cell_b_value:
        cell_c_value = sheet['C{}'.format(i)].value
        cell_d_value = sheet['D{}'.format(i)].value
        cell_g_value = sheet['G{}'.format(i)].value
        cell_h_value = sheet['H{}'.format(i)].value
        cell_k_value = sheet['K{}'.format(i)].value
        cell_m_value = sheet['M{}'.format(i)].value
        with open("ryousyoku.txt","w") as f:
         print(cell_b_value,file=f)
         print(file=f)
         print("------------- 朝食 -------------",file=f)      
         print(cell_c_value,file=f)
         print(cell_d_value,file=f)   

        with open("ryousyoku3.txt","w") as f3:   
         print(cell_b_value,file=f3)
         print(file=f3)
         print("------------- 昼食 --------------",file=f3)
         print(cell_g_value,file=f3)
         print(cell_h_value,file=f3)
      

        with open("ryousyoku2.txt","w") as f2:
         print(cell_b_value,file=f2)
         print(file=f2)
         print("------------- 夕食 -------------",file=f2)
         print(cell_k_value.replace("0","no B set"),file=f2)
         print(cell_m_value.replace("0"," "),file=f2)
      
         i = 100
 
   else:
     i = i+1 

# ロードしたExcelファイルを閉じる
workbook.close()
#夕食###############################################################
CK = "ZhiQDXi3WTgVg1cmBXgTimDkt"
CS = "DkfEjACdtF9K7cFQbzIrnNRvQ1oLubWO5isspDFjpfTqIkr9HE"
AT = "1517107959049846784-Q3bpbGOXcpDSh7EJ3EcAdPPL7T2LT9"
AS = "fZea1RAUSLDiiuTkPCpK3PFMlma87UsjU3RT5iM7R08Ao"

f = open('ryousyoku2.txt', 'r', encoding='UTF-8')
data2 = f.read()
print(data2)

STATUS2 = data2

def main():
    makeAPI().update_status(STATUS2)

def makeAPI():
    auth = tweepy.OAuthHandler(CK,CS)
    auth.set_access_token(AT,AS)
    return tweepy.API(auth)

if __name__ == "__main__":
  main()

#昼食#################################################################

f = open('ryousyoku3.txt', 'r', encoding='UTF-8')

data = f.read()
print(data)

STATUS = data

def main():
    makeAPI().update_status(STATUS)

def makeAPI():
    auth = tweepy.OAuthHandler(CK,CS)
    auth.set_access_token(AT,AS)
    return tweepy.API(auth)

if __name__ == "__main__":
  main()

#朝食######################################################


f = open('ryousyoku.txt', 'r', encoding='UTF-8')

data = f.read()
print(data)

STATUS = data

def main():
    makeAPI().update_status(STATUS)

def makeAPI():
    auth = tweepy.OAuthHandler(CK,CS)
    auth.set_access_token(AT,AS)
    return tweepy.API(auth)

if __name__ == "__main__":
  main()



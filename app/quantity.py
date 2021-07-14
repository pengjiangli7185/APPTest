# coding = utf-8
# @Time : 2021/6/28 17:28
# @Author : pengjiangli
# @File : quantity.py
# @Software: PyCharm
# @contact: 292617625@qq.com
'''
查询APP电量信息
'''
import csv
import os
import time


class QuantityTest(object):
    def __init__(self,counter):
        self.counter=counter
        self.alldata=[]

    #单次测试过程
    def testprocess(self):
        result=os.popen("adb shell dumpsys battery")
        for line in result:
            if "level" in line:
                power=line.split(":")[1]
                print("当前电量:%s",power)


        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,power))




    def run(self):
        os.popen("adb shell dumpsys battery set status 1")
        while self.counter>0:
            self.testprocess()
            self.counter=self.counter-1
            #每5秒采集一次数据
            time.sleep(5)

    def getCurrentTime(self):
        import time
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime


    def saveDateToCSV(self):
        # csvFile=open("power.csv",'wb')
        # csv_writer =csv.writer(csvFile)
        # csv_writer.writerows(self.alldata.)
        # csvFile.close()

        # 1. 创建文件对象
        f = open('pw.csv', 'w', encoding='utf-8')

        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)

        # 3. 构建列表头
       #csv_writer.writerow(["c", '20', '男'])
        csv_writer.writerows(self.alldata)

        # 5. 关闭文件
        f.close()



if __name__=='__main__':
    quantityTest= QuantityTest (5);
    quantityTest.run()
    quantityTest.saveDateToCSV()

from appium import webdriver
import datetime
import time

desired_caps = {
  'platformName': 'Android', #操作系统
        'deviceName': 'JUBNU18802101067', #设备名
        'platformVersion': '9', #版本号
        'appPackage': 'com.huawei.health', #包名
        'appActivity': '.MainActivity', #界面名
        'noReset': 'True'               #启动app时不要清除app里的原有的数据
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

#读取首页数据
steps=driver.find_element_by_id('com.huawei.health:id/stepsText').text #捕获步数信息
calori=driver.find_element_by_id('com.huawei.health:id/calories').text #捕获热量的元素
distence=driver.find_element_by_xpath(".//*[@text='公里']/preceding-sibling::*[1]").text#捕获移动距离信息
heartbeat=driver.find_element_by_xpath(".//*[@text='次/分钟']/preceding-sibling::*[1]").text#捕获心率信息
time=time.strftime("%m-%d", time.localtime())#获取当前系统时间
sleeping_hours=driver.find_element_by_xpath(".//*[@text='小时']/preceding-sibling::*[1]").text#捕获睡眠hour的元素
sleeping_min=driver.find_element_by_xpath(".//*[@text='分']/preceding-sibling::*[1]").text #捕获睡眠miniute的元素
#输出获取的数据信息
print('    ','当前时间    ',time,)
print('步数',steps,'步',end='          ')
print('距离',distence,'公里')
print('消耗卡路里',calori,'千卡',end='   ')
print(' 心率',heartbeat,'次/分钟')
print('今日睡眠时长',sleeping_hours,'时',sleeping_min,'分')

# 点击左上角步数,进入步数页面
driver.find_element_by_id("stepsText").click()
eles = []
dates = []
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
date = today
#循环六次
for i in range(6):
#近6天的步数，并加入列表eles
    driver.implicitly_wait(3)
    ele = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]")
    eles.append(ele.text)
    driver.find_element_by_id("older_switch_btn_outer_rect").click()
#近6天的日期，加入列表dates
    dates.append(str(date))
    date = today - oneday
    today = date
    i=+1

sport = dict(zip(eles,dates))
sport.items()

for key,value in sport.items():
    print(value,"运动步数：",key)
input('**** Press to quit**** ')
driver.quit()

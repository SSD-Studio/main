from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys, os, time

root = Tk()

def func(event):
    print("엔터키")
root.bind('<Return>', func)

root.title("EBS 자동화 프로그램 V1.2")
root.geometry("440x720")

Dev = Label(root, text="Made by 김태이(2-2) - 버젼 1.2")
Dev.pack()

school = Label(root, text="울산중앙중학교 전용")
school.pack()

texs2 = Label(root, text="온라인클래스 아이디를 입력해 주세요")
texs2.pack()

idvar = StringVar() #아이디 담을 변수
ns3 = ttk.Entry(root, width=20, textvariable=idvar)
ns3.pack()

texs3 = Label(root, text="온라인클래스 비번을 입력해 주세요")
texs3.pack()

passvar = StringVar()
ns4 = ttk.Entry(root, width=20, textvariable=passvar)
ns4.pack()

Datevar = StringVar()
date = Label(root, text="오늘 날짜를 입력해 주세요 12월 10일이면 12/10 이렇게")
date.pack()

Dateinput = ttk.Entry(root, width=10, textvariable=Datevar)
Dateinput.pack()

Lab = Label(root, text="과목명 입력")
Lab.pack()

Lab2 = Label(root, text="과학은 과학 김이면 과학(김), 최 면 과학(최)이렇게 입력")
Lab2.pack()

Lab3 = Label(root, text="다른 과목은 과목명만 입력하면 됨 수학이면 걍 수학 이렇게만")
Lab3.pack()


subjectvar1 = StringVar() #과목을 담을 변수
subjectvar2 = StringVar()
subjectvar3 = StringVar()
subjectvar4 = StringVar()
subjectvar5 = StringVar()
subjectvar6 = StringVar()
subjectvar7 = StringVar()

chat1 = StringVar() #차시 변수
chat2 = StringVar()
chat3 = StringVar()
chat4 = StringVar()
chat5 = StringVar()
chat6 = StringVar()

subjecttext1 = ttk.Entry(root, width=20, textvariable=subjectvar1) #과목 입력창, textvariable이 입력받는 내용을 변수에 저장해준다.
subjecttext1.pack()


chattext1 = ttk.Entry(root, width=5, textvariable=chat1) #차시 입력창 변수
chattext1.place(x=40,y=430)

chattext2 = ttk.Entry(root, width=5, textvariable=chat2)
chattext2.place(x=100,y=430)

chattext3 = ttk.Entry(root, width=5, textvariable=chat3)
chattext3.place(x=160,y=430)

chattext4 = ttk.Entry(root, width=5, textvariable=chat4)
chattext4.place(x=220,y=430)

chattext5 = ttk.Entry(root, width=5, textvariable=chat5)
chattext5.place(x=280,y=430)

chattext6 = ttk.Entry(root, width=5, textvariable=chat6)
chattext6.place(x=340,y=430)

def btncmd():
    print("버튼")
    driver = webdriver.Chrome("/Users/kimtaeyi/python_workspace/selenium_workspace/chromedriver")
    driver.get('https://oc38.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=03859&schCssTyp=online_mid');
    driver.maximize_window()
    
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div/a/img').click()
    time.sleep(0.8)
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div/div/ul/li[1]/a').click()
    id1 = str(idvar.get())
    password = str(passvar.get())
    print(password)
    time.sleep(1)
    driver.find_element_by_id("j_username").send_keys(id1)
    driver.find_element_by_id("j_password").send_keys(password)
    
    #driver.find_element_by_xpath('//*[@id="loginViewForm"]/div/div[1]/div[1]/label/i').click()
    time.sleep(0.3)

    driver.find_element_by_xpath('//*[@id="loginViewForm"]/div/div[1]/fieldset/div/button').click()

    #search_box = driver.find_element_by_name('q')
    #search_box.send_keys('네이버')
    #search_box.submit()

    #for i in range(10):
    #    search_box.send_keys(Keys.ENTER)
    body = driver.find_element_by_css_selector('body')
    #body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    #def secondsub(passvalue):

    if (subjecttext1.get() == "수학"):
        driver.find_element_by_partial_link_text("2학년 수학").click()
    elif(subjecttext1.get() == "과학(김)"):
        driver.find_element_by_partial_link_text("2학년 과학(목요일)").click()
    elif(subjecttext1.get() == "과학(최)"):
        driver.find_element_by_partial_link_text("2학년 과학(최)").click()
    elif(subjecttext1.get() == "역사"):
        driver.find_element_by_partial_link_text("2학년 역사").click()
    elif(subjecttext1.get() == "미술"):
        driver.find_element_by_partial_link_text("2학년 미술").click()
    elif(subjecttext1.get() == "음악"):
        driver.find_element_by_partial_link_text("2학년 음악").click()
    elif(subjecttext1.get() == "영어"):
        driver.find_element_by_partial_link_text("2학년 영어").click()
    elif(subjecttext1.get() == "가정"):
        driver.find_element_by_partial_link_text("2학년 가정").click()
    elif(subjecttext1.get() == "한문"):
        driver.find_element_by_partial_link_text("2학년 한문").click()
    elif(subjecttext1.get() == "기술"):
        driver.find_element_by_partial_link_text("2학년 기술").click()
    elif(subjecttext1.get() == "국어"):
        driver.find_element_by_partial_link_text("2학년 국어").click()
    elif(subjecttext1.get() == "도덕"):
        driver.find_element_by_partial_link_text("2학년 도덕").click()
    
def exit():
    driver.quit()

action = ttk.Button(root, text="동작", command=btncmd) #가로 세로 크기 지정 함수로 커맨드 연결
action.pack()

Guid2 = Label(root, text="참고로 과목 하나 끝났으면 프로그램 껏따 킬 필요 없이")
Guid2.pack()
Guid3 = Label(root, text="과목 입력 칸만 바꿔서 동작 누르면 된다.")
Guid3.pack()

Guid = Label(root, text="개발자 연락처 010-2710-7860 문자만")
Guid.pack()

chatinfo = Label(root, text="차시 입력칸, 시간표순으로")
chatinfo.pack()


root.mainloop()



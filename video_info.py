import requests
from bs4 import BeautifulSoup as bs
import time
from requests_html import HTMLSession
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import re
from datetime import date
Titleofvideo =[]
videoname=['5g']
visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
def open_youtube(gmail,password,chooseStrategy):#past in string with''
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 3)
    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(gmail)
    driver.find_element_by_id('identifierNext').click()
    driver.implicitly_wait(1)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(5)
    driver.find_element_by_id('passwordNext').click()
    time.sleep(5)
    driver.implicitly_wait(1)
    driver.get('https://www.youtube.com')
    time.sleep(3)
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located
    driver.get('https://www.youtube.com/results?search_query='+videoname[0])
    videos = driver.find_elements_by_id('video-title')
    videos[0].click()
    #driver.get(youtube_url)
    for i in range(2):
        try:
            time.sleep(10)
            CurrentURL=driver.current_url
            #print(CurrentURL,type(CurrentURL))
            title=Video_title(CurrentURL)
            view=Video_view(CurrentURL)
            likes=Video_like(CurrentURL)
            description=Video_description(CurrentURL)
            date=Video_date(CurrentURL)#$$All information until now are working
            recommendation1=Rrcom(CurrentURL)
            recommendation='\n'.join(recommendation1)
            ID=RrcomID(CurrentURL)
            uploader=Video_uploader(CurrentURL)
            date=VisitedTime()
            VIDEOINF=[]
            VIDEOINF.append(title)
            VIDEOINF.append(uploader)
            VIDEOINF.append(description)
            VIDEOINF.append(view)
            VIDEOINF.append(likes)
            VIDEOINF.append(date)
            VIDEOINF.append(recommendation)
            VIDEOINF.append(ID)
            VIDEOINF.append(date)
            #print(VIDEOINF)
            #print(i)
            #Write exist video information in to a CSV file
            CSV_Write(VIDEOINF)
            time.sleep(10)
            nextvideo = driver.find_elements_by_class_name("style-scope ytd-compact-video-renderer")
            try:
                nextvideo[chooseStrategy].click()
            except:
                nextvideo[1].click()
        except:
            pass

        
        
        
    print('yessss Sir')
    
def get_video_info(url):#cureent not working 
    # download HTML code
    content = requests.get(url)
    time.sleep(3) 
    # create beautiful soup object to parse HTML
    soup = bs(content.content, "html.parser")
    #for i in soup.findAll('span',{'class':'style-scope ytd-compact-video-renderer'}):
        #print (i)
        #print("1")
    subscribers = -1
        
    for like_count in soup.findAll('span', {'class': 'deemphasize style-scope yt-formatted-string'}):
        try:
            subscribers = 1
        except IndexError:
            pass 
    print (subscribers)
def Video_title(url):#worked! get video name
    # Initialize an HTML Session
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(3)
    soup = bs(response.html.html, "lxml")
    #
    #print("title:", soup.select_one('#container > h1').text)
    title=soup.select_one('#container > h1').text
    return title
def Video_description(url):#FIXED!
    # Initialize an HTML Session
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(3)
    soup = bs(response.html.html, "lxml")
    #
    description=soup.find('yt-formatted-string', class_="content style-scope ytd-video-secondary-info-renderer").text.strip()
    return description
def Video_view(url):#worked
    # Initialize an HTML Session
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(3)
    soup = bs(response.html.html, "lxml")
    #
    #print("title:", soup.select_one('#container > h1').text)
    view=soup.find('span', class_="view-count style-scope yt-view-count-renderer").text.strip()
    #print(view)
    return view
def Video_like(url):#worked

    # Initialize an HTML Session
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(5)
    soup = bs(response.html.html, "lxml")
    #
    #print("title:", soup.select_one('#container > h1').text)
    like=soup.find('yt-formatted-string', class_="style-scope ytd-toggle-button-renderer style-text").text.strip()
    
    return like       
def Video_dislike(url):#worked
    # Initialize an HTML Session
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(5)
    soup = bs(response.html.html, "lxml")
    dislike1=soup.find_all('yt-formatted-string', class_="style-scope ytd-toggle-button-renderer style-text")
    return dislike1
def Video_date(url):#Worked
    # Initialize an HTML Session
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(3)
    soup = bs(response.html.html, "lxml")
    date1=soup.find(id="date").text.strip()
    date=date1.strip('•')
    return date
def CSV_Write(data):
    #Write data in CSV
    with open('Videoinfo.csv','a',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        #writer.writerow(['Video Tittle','Video description','Views of Video','Like of Video','Date of upload'])
        writer.writerow(data)
    return 0
def Rrcom(url):#can finally get recomadation list!!!!!
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(3)
    a=''
    recom=[]
    soup = bs(response.html.html, "lxml")
    for i in soup.findAll('span', id="video-title"):
        V=i.text.strip()
        recom.append(V)
    return recom
def RrcomID(url):#worked
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(3)
    ID=[]
    soup = bs(response.html.html, "lxml")
    for item_section in soup.findAll('a', {'class': 'yt-simple-endpoint style-scope ytd-compact-video-renderer'}):
        x=item_section['href']
        ID.append(x)
    
    return ID
def bfSearch(visited, graph, node):#need more work
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
def Video_uploader(url):# worked
    # Initialize an HTML Session
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(5)
    soup = bs(response.html.html, "lxml")
    uploader=soup.find('yt-formatted-string', class_="style-scope ytd-channel-name").text.strip()
    #print(uploader)
    return uploader
def VisitedTime():# worked
    today = date.today()
    return today
def Video_tag(url):# worked
    # Initialize an HTML Session
    session = HTMLSession()
    # Get the html content
    response = session.get(url)
    # Execute JavaScript
    response.html.render(sleep=3)
    content = requests.get(url)
    time.sleep(5)
    soup = bs(response.html.html, "lxml")
    tag1=[]
    for i in soup.findAll('a', class_="yt-simple-endpoint style-scope yt-formatted-string"):
        x=i.text.strip()
        tag1.append(x)
    tag = list(set([s for s in tag1 if"#" in s]))
    #print(uploader)
    return tag
#get_video_info('https://www.youtube.com/watch?v=YHH2101OFfI')
# print in nice format
#print(Titleofvideo)
#open_youtube('francescacourtney3993@gmail.com','Qohlmyjgcoe',0) #test of open function
#Video_info('https://www.youtube.com/watch?v=D9dhzPc-zUE')
#Video_view('https://www.youtube.com/watch?v=D9dhzPc-zUE')
#Video_like('https://www.youtube.com/watch?v=D9dhzPc-zUE')
#Video_dislike('https://www.youtube.com/watch?v=D9dhzPc-zUE')
#Video_description('https://www.youtube.com/watch?v=D9dhzPc-zUE')
#Video_date('https://www.youtube.com/watch?v=D9dhzPc-zUE')
#test()
#CSV_Write('12')
#RrcomID('https://www.youtube.com/watch?v=D9dhzPc-zUE')
#Video_uploader('https://www.youtube.com/watch?v=6wqJte8lQc0')
#VisitedTime()
print(Video_tag('https://www.youtube.com/watch?v=PfnQlKdqLYQ'))
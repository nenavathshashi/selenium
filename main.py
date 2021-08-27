#importing webdriver
from selenium import webdriver


#importing actions
from selenium.webdriver.common.action_chains import ActionChains


#importing Keys
from selenium.webdriver.common.keys import Keys


#importing time module
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

#mouse actions
import mouse


#importing speech recognistion
import speech_recognition as sr
r = sr.Recognizer()

#importing pillow
from PIL import Image

#importing text_to_speech
import pyttsx3


def text_to_speech(asking):
    engine = pyttsx3.init()
    engine.say(asking)
    engine.runAndWait()

#speech_to_text function
def speech_to_text():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        text_to_speech("Start speaking")

        audio = r.listen(source,Timeout=None,duration=10)
    query = r.recognize_google(audio)
    return query


#path of the webdriver in pc
path = "C:\OOPs\chromedriver.exe"


def screen_shot():
    driver.save_screenshot("image.png")
    text_to_speech("Do you want to open the image")
    yes_or_no=speech_to_text()
    if yes_or_no == "yes":
        # Loading the image
        image = Image.open("image.png")
        # Showing the image
        image.show()
    else:
        pass


driver = webdriver.Chrome(path)


driver.get('https://learning.cbit.org.in/login/index.php')
text_to_speech("welcome to c b i t learning website.")
user_name = driver.find_element_by_id("username")
user_name.send_keys(input("Enter username"))
password= driver.find_element_by_id("password")
password.send_keys(input("Enter password"))
password.send_keys(Keys.RETURN)


#timer
def timer():
    text_to_speech("how much time you want to stay on this page?")
    time_wait=speech_to_text()
    time = int((time_wait[0] + time_wait[1]))
    if "seconds" in time_wait:
        WebDriverWait(driver, time)
        for i in range(time):
            print(str(time-i)+"seconds remaining")
            sleep(1)
            if (time-i)== 5:
                text_to_speech("only 5 second left.")
                return_back()
    elif "minutes" in time_wait:
        WebDriverWait(driver, time * 60)
        for i in range(time):
            print(str(time-i)+"seconds remaining")
            if (time-i)== 5:
                text_to_speech("only 5 second left.")
                return_back()
    else:
        text_to_speech("please spell in terms of seconds or minutes")
        timer()
#returning again
def return_back():
    text_to_speech("Do you want to exit from this page?")
    back_or_not=speech_to_text()
    if back_or_not =="yes":
        driver.back()
    elif back_or_not == "no":
        timer()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        return_back()


#files download
def files_download():
    text_to_speech("Do you want to download the file?")
    yes_or_no=speech_to_text()
    if yes_or_no == "yes":
        mouse.move(1251, 98, absolute=True)
        mouse.click(button="left")
        WebDriverWait(driver,10)
    elif yes_or_no== "no":
        text_to_speech("Okay")
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        files_download()


#files in oops
def oops_files_open():
    text_to_speech("which file you wish to open")
    file_name = speech_to_text()
    print(file_name)
    WebDriverWait(driver,10)
    if file_name == "unit 1":
        driver.find_element_by_xpath("//li[@id='module-55784']/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name == "unit 2":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name == "unit 3":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name in ["unit 4 point 1","unit 4.1"]:
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("// span / a / span[2]").click()
        driver.find_element_by_xpath("//div[2]/table/tbody/tr/td[3]/span/a/span[2]").click()
        driver.find_element_by_xpath("//div[3]/table/tbody/tr/td[3]/span/a/span[2]").click()
        text_to_speech("files are downloaded")
        return_back()
    elif file_name == "unit 5":
        driver.find_element_by_xpath("//td[@id='ygtvt1']/a").click()
        driver.find_element_by_xpath("//span/a/span[2]").click()
        driver.find_element_by_xpath("//div[2]/table/tbody/tr/td[3]/span/a/span[2]").click()
        driver.find_element_by_xpath("//div[3]/table/tbody/tr/td[3]/span/a/span[2]").click()
        text_to_speech("files are downloaded")
        return_back()
    elif file_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        oops_files_open()



#oops videos
def oops_videos_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    print(video_name)
    WebDriverWait(driver, 10)
    if video_name in  ["introduction to oops"]:
        driver.find_element_by_xpath("//li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["features of oops"]:
        driver.find_element_by_xpath("//li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["features of Python and applications"]:
        driver.find_element_by_xpath("//li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["variables", "identifiers", "keywords"]:
        driver.find_element_by_xpath("//li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["basic Data types","int float sting complex boolean )"]:
        driver.find_element_by_xpath("//li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["immutable", "input and output functions"]:
        driver.find_element_by_xpath("//li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in [" formatting strings", "type casting", "Bytes and Bytesarray data types"]:
        driver.find_element_by_xpath("//li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["range()","list data type","tuple"]:
        driver.find_element_by_xpath("//li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["tuple data type","Set data type","dict data type"]:
        driver.find_element_by_xpath("//li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["Arithmetic operators and Logical operators","Arithmetic operators","Logical operators"]:
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["operators in python"]:
        driver.find_element_by_xpath("//li[11]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["decision control statements"]:
        driver.find_element_by_xpath("//li[12]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["else clause","pass statement","functions"]:
        driver.find_element_by_xpath("//li[13]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["types of arguments"]:
        driver.find_element_by_xpath("//li[14]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["scope and lifetime of variables","local and global variables"]:
        driver.find_element_by_xpath("//li[15]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["recursion function","lambda functions"]:
        driver.find_element_by_xpath("//li[16]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["filter","map","reduce"]:
        driver.find_element_by_xpath("//li[17]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["nested functions","modules"]:
        driver.find_element_by_xpath("//li[18]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["random module","math module"]:
        driver.find_element_by_xpath("//li[19]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["list comprehension","name space","private variables"]:
        driver.find_element_by_xpath("//li[20]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["packages","command line arguments"]:
        driver.find_element_by_xpath("//li[21]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["classes","object","self variable","constructor"]:
        driver.find_element_by_xpath("//li[22]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["instance variables"]:
        driver.find_element_by_xpath("//li[23]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["static variables","public and private numbers"]:
        driver.find_element_by_xpath("//li[24]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["generation of programming languages"]:
        driver.find_element_by_xpath("//li[25]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["programming paradigms"]:
        driver.find_element_by_xpath("//li[26]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["revision of unit 2"]:
        driver.find_element_by_xpath("//li[27]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["function decorator","types of methods"]:
        driver.find_element_by_xpath("//li[28]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["built in class attributes","garbage collection"]:
        driver.find_element_by_xpath("//li[29]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["introduction to inheritance","types of inheritance"]:
        driver.find_element_by_xpath("//li[30]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["mro method"]:
        driver.find_element_by_xpath("//li[31]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["c3 algorithm","polymorphism"]:
        driver.find_element_by_xpath("//li[32]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["overloading","method overloading","overriding"]:
        driver.find_element_by_xpath("//li[33]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["compostition","abstract classes"]:
        driver.find_element_by_xpath("//li[34]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["abstract classes","file handling"]:
        driver.find_element_by_xpath("//li[35]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["file handling 2"]:
        driver.find_element_by_xpath("//li[36]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["exception handling 1"]:
        driver.find_element_by_xpath("//li[37]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["exception handling 2"]:
        driver.find_element_by_xpath("//li[38]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["finally keyword","customized exceptions"]:
        driver.find_element_by_xpath("//li[39]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["assertions","trace back"]:
        driver.find_element_by_xpath("//li[40]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["regular expressions 1"]:
        driver.find_element_by_xpath("//li[41]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["regular expressions 2"]:
        driver.find_element_by_xpath("//li[42]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["tkinter"]:
        driver.find_element_by_xpath("//li[43]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["tkinter 2"]:
        driver.find_element_by_xpath("//li[44]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["tkinter 3"]:
        driver.find_element_by_xpath("//li[45]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["tkinter 4"]:
        driver.find_element_by_xpath("//li[46]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["turtle 1"]:
        driver.find_element_by_xpath("//li[47]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        oops_videos_open()



#video recordings in I4.0
def industry_videos_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    print(video_name)
    WebDriverWait(driver, 10)
    if video_name =="Introduction":
        driver.find_element_by_xpath("//li[@id='module-55784']/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "Objectives of the course":
        driver.find_element_by_xpath("// li[3] / div[3] / ul / li[2] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "Industrial revolutions":
        driver.find_element_by_xpath("// li[3] / div[3] / ul / li[3] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "digitalization":
        driver.find_element_by_xpath("// li[3] / div[3] / ul / li[4] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "drivers of I4.0 and challenges":
        driver.find_element_by_xpath("// li[3] / div[3] / ul / li[5] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "drivers of I4.0":
        driver.find_element_by_xpath("// li[3] / div[3] / ul / li[6] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "I4.0 drivers":
        driver.find_element_by_xpath("// li[3] / div[3] / ul / li[7] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "predictive analysis":
        driver.find_element_by_xpath("// li[3] / div[3] / ul / li[8] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "iot":
        driver.find_element_by_xpath("// li[9] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "iiot overview":
        driver.find_element_by_xpath("// li[10] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "iiot":
        driver.find_element_by_xpath("// li[11] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "27th april predictive analysis":
        driver.find_element_by_xpath("// li[12] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "predictive":
        driver.find_element_by_xpath("// li[13] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 1 and 2 review":
        driver.find_element_by_xpath("// li[14] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 3 introduction":
        driver.find_element_by_xpath("// li[15] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "data enablers":
        driver.find_element_by_xpath("// li[16] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "cps unit 3":
        driver.find_element_by_xpath("// li[17] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "ai in I4.0":
        driver.find_element_by_xpath("// li[18] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "iiot ai":
        driver.find_element_by_xpath("// li[19] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 3 cps":
        driver.find_element_by_xpath("// li[20] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "augmented reality":
        driver.find_element_by_xpath("// li[21] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "ai and i4.0":
        driver.find_element_by_xpath("// li[22] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "i4.0 mc":
        driver.find_element_by_xpath("// li[23] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "support system i4.0":
        driver.find_element_by_xpath("// li[24] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 4":
        driver.find_element_by_xpath("// li[25] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "role of data":
        driver.find_element_by_xpath("// li[26] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "role of data and bigdata":
        driver.find_element_by_xpath("// li[27] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "cloud computing":
        driver.find_element_by_xpath("// li[28] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "cloud usage":
        driver.find_element_by_xpath("// li[29] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "i4.0 cloud":
        driver.find_element_by_xpath("// li[30] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5":
        driver.find_element_by_xpath("// li[31] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 1":
        driver.find_element_by_xpath("// li[32] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 2":
        driver.find_element_by_xpath("// li[33] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 3":
        driver.find_element_by_xpath("// li[34] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 4":
        driver.find_element_by_xpath("// li[35] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 5":
        driver.find_element_by_xpath("// li[36] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 6":
        driver.find_element_by_xpath("// li[37] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 7":
        driver.find_element_by_xpath("// li[38] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 8":
        driver.find_element_by_xpath("// li[39] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 9":
        driver.find_element_by_xpath("// li[40] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 10":
        driver.find_element_by_xpath("// li[41] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 11":
        driver.find_element_by_xpath("// li[42] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 12":
        driver.find_element_by_xpath("// li[43] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 13":
        driver.find_element_by_xpath("// li[44] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 14":
        driver.find_element_by_xpath("// li[45] / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name == "unit 5 case study 15":
        driver.find_element_by_xpath("// li[3] / div[3] / ul / li / div / div / div[2] / div / a / span").click()
        return_back()
    elif video_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        industry_videos_open()



#files in oops lab
def oops_lab_files_open():
    text_to_speech("which file you wish to download")
    file_name = speech_to_text()
    print(file_name)
    WebDriverWait(driver, 10)
    if file_name == "week 1":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 2":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 3":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 4":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 5":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 6":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 7":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 8":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[8]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 9":
        driver.find_element_by_xpath("//li[9]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name == "week 10":
        driver.find_element_by_xpath("//li[10]/div/div/div[2]/div/a/span").click()
        driver.find_element_by_xpath("//td[2]/div/div/a").click()
        text_to_speech("file downloaded")
        return_back()
    elif file_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        oops_lab_files_open()


#oops lab videos
def oops_lab_video_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    print(video_name)
    WebDriverWait(driver, 10)
    if video_name == "python installation":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
    elif video_name == "data types":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
    elif video_name == "control statements":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
    elif video_name == "modules and packages":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
    elif video_name == "viva":
        driver.find_element_by_xpath("//li[5]/div/div/div[2]/div/a/span").click()
    elif video_name == "lab internal 1":
        driver.find_element_by_xpath("//li[6]/div/div/div[2]/div/a/span").click()
    elif video_name == "week 7 programs":
        driver.find_element_by_xpath("//li[7]/div/div/div[2]/div/a/span").click()
    elif video_name == "week 8 programs":
        driver.find_element_by_xpath("//li[8]/div/div/div[2]/div/a/span").click()
    elif video_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        oops_lab_video_open()


#ee files
def ee_files_open():
    text_to_speech("which file you wish to open")
    file_name = speech_to_text()
    print(file_name)
    WebDriverWait(driver, 10)
    if file_name in ["unit 1","lesson 1","chapter 1"]:
        driver.find_element_by_xpath("// li[ @ id = 'module-73198'] / div / div / div[2] / div / a / span").click()
        files_download()
        return_back()
    elif file_name in ["unit 1 part 2","unit 1.2"]:
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name in ["unit 2","chapter 2","lesson 2"]:
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name in ["unit 2 part 1","unit 2.1"]:
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="unit 2 part 2":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="unit 3":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="unit 3 part 2":
        driver.find_element_by_xpath("//li[7]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="unit 3 part 3":
        driver.find_element_by_xpath("//li[8]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="unit 4":
        driver.find_element_by_xpath("//li[9]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="unit 5":
        driver.find_element_by_xpath("//li[10]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="unit 5 part 2":
        driver.find_element_by_xpath("//li[11]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        ee_files_open()


#wmp files
def wmp_files_open():
    text_to_speech("which file you wish to open")
    file_name = speech_to_text()
    print(file_name)
    WebDriverWait(driver, 10)
    if file_name == "carpentry":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="casting":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="fitting":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="house wiring":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="tinsmithy":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="machine shop":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="welding":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="carpentry exercises":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="casting exercises":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="welding exercises":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name=="tin smithy exercises":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        files_download()
        return_back()
    elif file_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        wmp_files_open()


#ee video lectures
def ee_video_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    print(video_name)
    WebDriverWait(driver, 10)
    if video_name =="ee overview intro ":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 1 role of engineers ":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 1 engineering problems and design class 3":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 1 engineering problems and design class 4":
        driver.find_element_by_xpath("//li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="intro to mechanics,kinematics,dynamics ":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="degrees of freedom,calculation,mech,inversion":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="single slider,double slider mechanism,inversion":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 2 aurdino":
        driver.find_element_by_xpath("//li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 2 simple robotic arm building":
        driver.find_element_by_xpath("//li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 3 data acquisition, primary data":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 3 secondary data collection,statistical methods":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 4 process management":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 4 project management,agile practices":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 5 statistical methods,ethics,engineering ethics":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="unit 5 sustainable engineering development":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="ideas part 1":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="ideas part 2":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="ideas part 3":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        ee_video_open()

#video recordings of maths
def maths_video_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    if video_name == "unit 1":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "Differential Equations":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "Exact differential equations":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "Exact differential equations part 2":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li[4]/div/div/div[2]/div/a").click()
        return_back()
    elif video_name == "differential equations part 1":
        driver.find_element_by_xpath("//li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "differential equations part 2":
        driver.find_element_by_xpath("//li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "differential equations part 3":
        driver.find_element_by_xpath("//li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "differential equations part 4":
        driver.find_element_by_xpath("//li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "differential equations part 5":
        driver.find_element_by_xpath("//li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "differential equations part 6":
        driver.find_element_by_xpath("//li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "clairaut's equation":
        driver.find_element_by_xpath("//li[11]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "reccati's equation":
        driver.find_element_by_xpath("//li[12]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "orthogonal trajectories":
        driver.find_element_by_xpath("//li[13]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "higher order differential equations":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "copentary funcion":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "problems on CF":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "p i exponential function":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "polynomials":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "sinax or cosax part 1":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "sinax or cosax part 2":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "p i when x":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "variation of parameters":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "LR and CR circuits":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "unit 2 revision":
        driver.find_element_by_xpath("//li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/spa").click()
        return_back()
    elif video_name == "power series solution":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li/div/div/div[2]/div/a").click()
        return_back()
    elif video_name == "power series solution problems":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li/div/div/div[2]/div/a").click()
        return_back()
    elif video_name == "unit 3 revision":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "legendre's polynomials part 1":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "legendre's polynomials part 2":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "legendre's polynomials part 3":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "legendre's polynomials part 4":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "legendre's polynomials part 5":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "bessel's function part 1":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "bessel's function part 2":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "recurrence relations ":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[11]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "fourier transforms":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "fourier transforms properties part 1":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "fourier transforms properties part 2":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "fourier transforms problems part 1":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "fourier transforms problems part 2":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "fourier transforms part 2":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "fourier transforms part 3":
        driver.find_element_by_xpath("//li[5]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "z transforms":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "z properties":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "z problems":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "initial and final values theorems part 1":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "initial and final values theorems part 2":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "problems on izt":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "problems on initial and final values theorems":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "inverse z transform by residue theorem":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "residue method":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "application of z tranform":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found please try saying again")
        maths_video_open()

#video recordings in maths lab
def maths_lab_video_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    print(video_name)
    WebDriverWait(driver, 10)
    if video_name =="experiment 1":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 2":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 1 and 2 executed by students":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 3":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 3 problems":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 3 execution":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 4":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 4 revision":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 6 and 7 19th june":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 6 and 7 23rd june":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 5 and 8":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[11]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "experiment 5 and 8 execution":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[12]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "execution of experiments":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[13]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "execution of 5,6,7,8 experiments":
        driver.find_element_by_xpath("//li[14]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found Please try again")
        maths_lab_video_open()



#chemistry
def chemistry_video_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    print(video_name)
    WebDriverWait(driver, 10)
    #unit-1
    if video_name =="Introduction to mot":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "mot and lcao method":
        driver.find_element_by_xpath("//li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "homo and hetronuclear diatomic molecules":
        driver.find_element_by_xpath("//li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "aromaticity of benzene":
        driver.find_element_by_xpath("//li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "first order kinetics":
        driver.find_element_by_xpath("//li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "second order kinetics":
        driver.find_element_by_xpath("//li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "unit-1 questions":
        driver.find_element_by_xpath("//li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    #unit-2
    elif video_name == "reversible and irreversible process":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "law of thermodynamics":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "free energy and internal energy":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "electrochemistry introduction":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "electrochemical series":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "saturated calomel electrodes":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "nernst equation":
        driver.find_element_by_xpath("//li[4]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "determination of ph using calomel electrode":
        driver.find_element_by_xpath("//li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "potentiometric titrations":
        driver.find_element_by_xpath("//li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "battery technology":
        driver.find_element_by_xpath("//li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "fuel cells":
        driver.find_element_by_xpath("//li[11]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "unit-2 question bank":
        driver.find_element_by_xpath("//li[12]/div/div/div[2]/div/a/span").click()
        return_back()
    #unit-3
    elif video_name == "unit 3 stereochemistry":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "optical isomerism":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "enantiomers ":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "conformational isomerism":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "absolute configuration":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "configurations":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "nitration of benzene":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "nucleophilic substitution reactions":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "radical substitution reactions":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "elimination reations ":
        driver.find_element_by_xpath("//li[6]/div[3]/ul/li[12]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "addition reactions":
        driver.find_element_by_xpath("//li[13]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "cyclo addition reactions":
        driver.find_element_by_xpath("//li[14]/div/div/div[2]/div/a/span").click()
        return_back()
    #unit-4
    elif video_name == "unit 4 water chemistry":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "hardness of water":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "industrial water":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "ion exchange process":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "lime soda process":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "desalination and disinfection":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "alkalinity of water":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "bod and cod":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "numericals on lime soda":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "unit-3 and unit-4 question bank":
        driver.find_element_by_xpath("//li[7]/div[3]/ul/li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    #unit-5
    elif video_name == "unit-5 polymers-introduction":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "uses of pvc and bakelite":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "elastomer natural rubber":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "conducting polymers":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "lithography":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "nanomaterials":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "carbon nano tubes":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "preparation of nanomaterials":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "sem and tem":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "drugs":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name == "uses of atenolol":
        driver.find_element_by_xpath("//li[8]/div[3]/ul/li[11]/div/div/div[2]/div/a/span").click()
        return_back()
    else:
        text_to_speech("Sorry File not found Please try again")
        chemistry_video_open()





#chemistry lab
def chemistry_lab_video_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    print(video_name)
    WebDriverWait(driver, 10)
    if video_name =="experiment1":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="experiment2":
        driver.find_element_by_xpath("//li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="experiment3":
        driver.find_element_by_xpath("//li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="experiment4":
        driver.find_element_by_xpath("//li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="experiment5 ":
        driver.find_element_by_xpath("//li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="experiment6":
        driver.find_element_by_xpath("//li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="experiment7":
        driver.find_element_by_xpath("//li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="experiment8":
        driver.find_element_by_xpath("//li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name=="experiment9":
        driver.find_element_by_xpath("//li[11]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found Please try again")
        chemistry_lab_video_open()


#wmp video lectures
def wmp_video_open():
    text_to_speech("which video you wish to open")
    video_name = speech_to_text()
    print(video_name)
    WebDriverWait(driver, 10)
    if video_name =="introduction to workshop ":
        driver.find_element_by_xpath("//li[2]/div[3]/ul/li/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" basics of carpentry exercise 1":
        driver.find_element_by_xpath("//li[2]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" carpentry exercise 2":
        driver.find_element_by_xpath("//li[3]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" part a fitting intro and exercise 1 ":
        driver.find_element_by_xpath("//li[4]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" part b fitting intro and exercise 1 ":
        driver.find_element_by_xpath("//li[5]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" casting introduction":
        driver.find_element_by_xpath("//li[6]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" casting exercise 1":
        driver.find_element_by_xpath("//li[7]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" casting exercise 2,3":
        driver.find_element_by_xpath("//li[8]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" fitting exercise 2,3":
        driver.find_element_by_xpath("//li[9]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" intro to welding":
        driver.find_element_by_xpath("//li[10]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" welding exercise 2":
        driver.find_element_by_xpath("//li[11]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" welding exercise 1 part a":
        driver.find_element_by_xpath("//li[12]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" welding exercise 1 part b":
        driver.find_element_by_xpath("//li[13]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" introduction to machine shop":
        driver.find_element_by_xpath("//li[14]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" step turning lathe":
        driver.find_element_by_xpath("//li[15]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" tinsmithy exercise 1":
        driver.find_element_by_xpath("//li[17]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" taper turning and knurling":
        driver.find_element_by_xpath("//li[18]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" tinsmithy exercise 2":
        driver.find_element_by_xpath("//li[19]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" tinsmithy exercise 3":
        driver.find_element_by_xpath("//li[20]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" house wiring introduction":
        driver.find_element_by_xpath("//li[21]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name==" house wiring exercise 1":
        driver.find_element_by_xpath("//li[22]/div/div/div[2]/div/a/span").click()
        return_back()
    elif video_name in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry File not found Please try again")
        wmp_video_open()


#ee files videos and grades
def ee_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    print(ask)
    WebDriverWait(driver, 10)
    if "files" in ask:
        ee_files_open()
        text_to_speech("you are back here again")
        ee_subject()
    elif "videos" in ask:
        ee_video_open()
        text_to_speech("you are back here again")
        ee_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        ee_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        ee_subject()

def wmp_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    print(ask)
    WebDriverWait(driver, 10)
    if "files" in ask:
        wmp_files_open()
        text_to_speech("you are back here again")
        wmp_subject()
    elif "videos" in ask:
        wmp_video_open()
        text_to_speech("you are back here again")
        wmp_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        wmp_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        wmp_subject()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        wmp_subject()


#oops files,videos and grades
def oops_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    print(ask)
    WebDriverWait(driver, 10)
    if "files" in ask:
        oops_lab_files_open()
        text_to_speech("you are back here again")
        oops_subject()
    elif "videos" in ask:
        oops_lab_video_open()
        text_to_speech("you are back here again")
        oops_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        ee_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        oops_subject()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        oops_subject()


#
def chemistry_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    print(ask)
    WebDriverWait(driver, 10)
    if "files" in ask:
        text_to_speech("Sorry no files are available in chemistry lab")
        chemistry_subject()
    elif "videos" in ask:
        chemistry_video_open()
        text_to_speech("you are back here again")
        chemistry_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        chemistry_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        chemistry_subject()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        chemistry_subject()



#maths lab files videos and grades
def maths_lab_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    print(ask)
    WebDriverWait(driver, 10)
    if "files" in ask:
        text_to_speech("Sorry no files are available in maths lab")
        maths_lab_subject()
    elif "videos" in ask:
        maths_lab_video_open()
        text_to_speech("you are back here again")
        maths_lab_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        maths_lab_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        maths_lab_subject()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        maths_lab_subject()



#oops files ,videos and grades
def oops_lab_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    if "files" in ask:
        oops_files_open()
        text_to_speech("you are back here again")
        oops_lab_subject()
    elif "videos" in ask:
        oops_videos_open()
        text_to_speech("you are back here again")
        oops_lab_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        oops_lab_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        oops_lab_subject()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        oops_lab_subject()


#industry files,videos and grades
def industry_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    print(ask)
    WebDriverWait(driver, 10)
    if "files" in ask:
        text_to_speech("Sorry no files are found in industry 4 point o")
        industry_subject()
    elif "videos" in ask:
        oops_videos_open()
        text_to_speech("you are back here again")
        industry_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        industry_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        industry_subject()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        industry_subject()



#chemistry files,videos and grades
def chemistry_lab_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    print(ask)
    WebDriverWait(driver, 10)
    if "files" in ask:
        text_to_speech("Sorry no files are available in chemistry")
        chemistry_lab_subject()
    elif "videos" in ask:
        chemistry_video_open()
        text_to_speech("you are back here again")
        chemistry_lab_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        chemistry_lab_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        chemistry_lab_subject()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        chemistry_lab_subject()


#maths files,videos and grades
def maths_subject():
    text_to_speech("Which page you want to navigate next?")
    ask = speech_to_text()
    print(ask)
    WebDriverWait(driver, 10)
    if "files" in ask:
        text_to_speech("Sorry no files are available in maths")
        maths_subject()
    elif "videos" in ask:
        maths_video_open()
        text_to_speech("you are back here again")
        maths_subject()
    elif ask in ["grades", "report", "slip test marks", "assignment marks"]:
        grades = driver.find_element_by_xpath("//div[@id='nav-drawer-container']/nav/a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=grades)
        action.perform()
        return_back()
        text_to_speech("you are back here again")
        maths_subject()
    elif ask in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        maths_subject()
    elif ask in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        maths_subject()



#accessing courses
def courses():
    text_to_speech("Which course do you wish to open?")
    course = speech_to_text()
    print(course)
    WebDriverWait(driver, 10)
    if course in ["engineering exploration","ee","double e"]:
        ee_course=driver.find_element_by_link_text("C3-Engineering Exploration-II-2020-21")
        ee_course.send_keys(Keys.RETURN)
        WebDriverWait(driver, 3)
        ee_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in ["wmp","workshop","workshop and manufacturing practices"]:
        element7=driver.find_element_by_link_text("C3-Workshop / Manufacturing Practice-II-2020-21")
        element7.send_keys(Keys.RETURN)
        wmp_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in ["oops lab", "object oriented programming lab","python lab"]:
        element8=driver.find_element_by_link_text("C3-Object Oriented Programming Lab-II-2020-21")
        element8.send_keys(Keys.RETURN)
        oops_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in ["chemistry lab","chem lab"]:
        element9=driver.find_element_by_link_text("C3-Chemistry Lab-II-2020-21")
        element9.send_keys(Keys.RETURN)
        chemistry_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in  ["maths lab","de and tt lab"]:
        element10=driver.find_element_by_link_text("C3-Differential Equations &Transform Theory Lab-II-2020-21")
        element10.send_keys(Keys.RETURN)
        maths_lab_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in ["oops","object oriented programming","pyhton"]:
        element11=driver.find_element_by_link_text("C3-Object Oriented Programming-II-2020-21")
        element11.send_keys(Keys.RETURN)
        oops_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in ["industry 4.0","i 4.0"]:
        element12=driver.find_element_by_link_text("C3-Industry 4.0-II-2020-21")
        element12.send_keys(Keys.RETURN)
        industry_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in  ["chemistry","chem"]:
        element13=driver.find_element_by_link_text("C3-Chemistry-II-2020-21")
        element13.send_keys(Keys.RETURN)
        chemistry_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in ["maths","de and tt"]:
        element14=driver.find_element_by_link_text("C3-Differential Equations and Transform Theory-II-2020-21")
        element14.send_keys(Keys.RETURN)
        maths_subject()
        text_to_speech("you are back here again")
        courses()
    elif course in ["screenshot", "ss"]:#screenshot any window
        screen_shot()
        courses()
    elif course in ["quit","close"]:
        driver.back()
    else:
        text_to_speech("Course not found Try another way")
        courses()



#calender or remainder
def reminder():
    text_to_speech("please spell out the date you wish to check")
    date=speech_to_text()
    print(date)
    #opening a calander
    driver.find_element_by_xpath("//a[3]/div/div/span/i").click()
    read1 =driver.find_element_by_xpath("//div[2]/table/tbody/tr/td").text
    read2 =driver.find_element_by_xpath("//div[2]/table/tbody/tr/td[2]").text
    read3 = driver.find_element_by_xpath("//div[2]/table/tbody/tr/td[3]").text
    read4 = driver.find_element_by_xpath("//div[2]/table/tbody/tr/td[4]").text
    read5 = driver.find_element_by_xpath("//div[2]/table/tbody/tr/td[5]").text
    read6 = driver.find_element_by_xpath("//div[2]/table/tbody/tr/td[6]").text
    read7 = driver.find_element_by_xpath("//div[2]/table/tbody/tr/td[7]").text
    read8 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td").text
    read9 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[2]").text
    read10 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[3]").text
    read11 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[4]").text
    read12 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[5]").text
    read13 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[6]").text
    read14 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[7]").text
    read15 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td").text
    read16 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[2]").text
    read17 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[3]").text
    read18 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[4]").text
    read19 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[5]").text
    read20 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[6]").text
    read21 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[3]/td[7]").text
    read22 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[4]/td").text
    read23 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[4]/td[2]").text
    read24 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[4]/td[3]").text
    read25 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[4]/td[4]").text
    read26 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[4]/td[5]").text
    read27 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[4]/td[6]").text
    read28 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[4]/td[7]").text
    read29 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[5]/td").text
    read30 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[5]/td[2]").text
    read31 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[5]/td[3]").text
    read32 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[5]/td[4]").text
    read33 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[5]/td[5]").text
    read34 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[5]/td[6]").text
    read35 = driver.find_element_by_xpath("//div[2]/table/tbody/tr[5]/td[7]").text
    l=[read1,read2,read3,read4,read5,read6,read7,read8,read9,read10,read11,read12,read13,read14,read15,read16,read17,read18,read19,read20,read21,read22,read23,read24,read25,read26,read27,read28,read29,read30,read31,read32,read33,read34,read35]
    for i in l:
        if date in i:
            answer = text_to_speech(i)
            break;
    if answer == []:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        reminder()

#main window
def main_mindow():
    text_to_speech("Which page you want to navigate to?")
    Input = speech_to_text()
    print(Input)
    WebDriverWait(driver, 10)
    if 'courses' in Input:
        Mycourses = driver.find_element_by_xpath("//a[5]/div/div/span/i")
        action = ActionChains(driver)
        action.click(on_element=Mycourses)
        action.perform()
        page_end = driver.find_element_by_tag_name("html")
        page_end.send_keys(Keys.END)
        WebDriverWait(driver, 3)
        sleep(10)
        page_2 = driver.find_element_by_xpath("(//a[contains(text(),'2')])[12]")
        page_2.send_keys(Keys.RETURN)
        WebDriverWait(driver, 3)
        sleep(10)
        courses()
        text_to_speech("you are back here again")
        main_mindow()
    elif Input in ["screenshot", "ss"]:
        screen_shot()
        main_mindow()
    elif Input in ["reminders", "reminder","calendar"]:
        reminder()
        text_to_speech("you are back here again")
        main_mindow()
    elif "quit" in Input:
        driver.quit()
    else:
        text_to_speech("Sorry We cannot recognise your voice Please try again")
        main_mindow()
#Asking through speech_to_text function to access the course
text_to_speech("please follow the sequential path to open a course, file or any video")
main_mindow()


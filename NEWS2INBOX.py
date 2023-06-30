import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime, time, os
import smtplib
from email.message import EmailMessage

def get_news():
    # create a webdriver object for chrome-option and configure
    wait_imp = 10
    CO = webdriver.ChromeOptions()
    CO.add_experimental_option('useAutomationExtension', False)
    CO.add_argument('--ignore-certificate-errors')
    CO.add_argument('--start-maximized')
    wd = webdriver.Chrome(r'C:\Windows\chromedriver.exe',options=CO)

    # Get today's date
    td = datetime.date.today()

    # Get news from Google News
    print ("Connecting to Authentic News source, Please wait .....\n")
    news_site = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
    wd.get(news_site)
    wd.implicitly_wait(wait_imp)
    elems = wd.find_elements(By.TAG_NAME, "h4")
    
    # Write news to file
    file_loc = r'C:\Users\91982\Desktop\project\data.txt'
    file_to_write = open(file_loc, 'w+',encoding="utf-8")
    ind = 0
    for elem in elems:
        file_to_write.write(str(ind)+ '>> ')
        file_to_write.write(elem.text+'\n')
        print (str(ind) + ") " + elem.text)
        ind += 1
    file_to_write.close()
    print('\n')

    # Get credentials from your system
    USER_EMAIL = "s1610.2003@gmail.com"
    MY_PASS = "zyzmqscirtmppixr"
    MY_EMAIL = "accdum666@gmail.com"
    
    # Compose message
    msg = EmailMessage()
    msg['From'] = MY_EMAIL
    msg['To']   = USER_EMAIL
    msg['Subject'] = " Hello ! Today's TOP news HEADLINES >>"

    with open(file_loc,'rb') as f:
        N_file = f.read()
    
    # Configure server
    server = smtplib.SMTP('smtp.gmail.com', 587) #tls , ssl
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(MY_EMAIL,MY_PASS)
    server.sendmail(MY_EMAIL,USER_EMAIL,N_file)

    # printing final info
    print ("A copy of this NEWS HEADLINES has been sent to your E-mail Successfuly !!")
    print ("Have a Nice Day !!")
    server.quit()

def show_news():
    # Open news file and display in a messagebox
    file_loc = r'C:\Users\91982\Desktop\project\data.txt'
    with open(file_loc, 'r', encoding='utf-8') as file:
        news = file.read()
    messagebox.showinfo('Top News Headlines', news)

# for buisness section
def get_news_buisness():
    # create a webdriver object for chrome-option and configure
    wait_imp = 10
    CO = webdriver.ChromeOptions()
    CO.add_experimental_option('useAutomationExtension', False)
    CO.add_argument('--ignore-certificate-errors')
    CO.add_argument('--start-maximized')
    wd = webdriver.Chrome(r'C:\Windows\chromedriver.exe',options=CO)

    # Get today's date
    td = datetime.date.today()

    #buisness news
    print ("Connecting to Authentic News source, Please wait .....\n")
    buisness_site = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    wd.get(buisness_site)
    wd.implicitly_wait(wait_imp)
    elems_buisness = wd.find_elements(By.CLASS_NAME, "gPFEn")
   
     # Write buisness news to file
    file_loc_buisness = r'C:\Users\91982\Desktop\project\data2.txt'
    file_to_write_buisness = open(file_loc_buisness, 'w+',encoding="utf-8")
    ind = 1
    for elem in elems_buisness:
        file_to_write_buisness.write(str(ind)+ '>> ')
        file_to_write_buisness.write(elem.text+'\n')
        print (str(ind) + ") " + elem.text)
        ind += 1
    file_to_write_buisness.close()
    print('\n')

    # Get credentials from your system
    USER_EMAIL = "studyjee004@gmail.com"
    MY_EMAIL = "shahnaman004@gmail.com"
    MY_PASS = "larcjyexujkrrryr"
    
    # Compose message
    msg = EmailMessage()
    msg['From'] = MY_EMAIL
    msg['To']   = USER_EMAIL
    msg['Subject'] = " Hello ! Today's TOP news HEADLINES >>"

    with open(file_loc_buisness,'rb') as f:
        N_file_buisness = f.read()   

    # Body of email of google buisness news
    msg.set_content("Find the attached document for detailed NEWS .. ")
    msg.add_attachment(N_file_buisness, maintype = 'document',subtype = 'txt', filename = f.name )

    # Configure server
    server = smtplib.SMTP('smtp.gmail.com', 587) #tls , ssl
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(MY_EMAIL,MY_PASS)
    server.send_message(msg)

    # printing final info
    print ("A copy of this NEWS HEADLINES has been sent to your E-mail Successfuly !!")
    print ("Have a Nice Day !!")
    server.quit()

def show_news_buisness():
    # Open news file and display in a messagebox
    file_loc_buisness = r'C:\Users\91982\Desktop\project\data2.txt'
    with open(file_loc_buisness, 'r', encoding='utf-8') as file:
        news = file.read()
    messagebox.showinfo('Top News Headlines', news)

# Create GUI
root = tk.Tk()
root.geometry("400x400")
root.config(bg='#069869')
main_frame=tk.Frame(root,width=400, height=400, highlightbackground="black", highlightthickness=3)
main_frame.pack()
main_frame.place(relx=0.5, rely=0.5, anchor='center')
root.title('Top News Headlines')

label = tk.Label(main_frame, text="get news",font=("sans-serif",25,'bold'),fg="#1a0c47")
label.pack()
get_news_button = tk.Button(main_frame, text='Get News', command=get_news,bg="blue",fg="white")
get_news_button.pack(pady=10)

show_news_button = tk.Button(main_frame, text='Show News', command=show_news,bg="blue",fg="white")
show_news_button.pack(pady=10)

get__buisness_news_ = tk.Button(main_frame, text='Get buisness News', command=get_news_buisness,bg="blue",fg="white")
get__buisness_news_.pack(pady=10)

show__buisness_news = tk.Button(main_frame, text='Show buisness News', command=show_news_buisness,bg="blue",fg="white")
show__buisness_news.pack(pady=10)


root.mainloop()


import requests
from bs4 import BeautifulSoup
import smtplib


Price_You_Want=400 #Specify the price you want to check

URL='https://www.walmart.com/ip/Vega-HDMI-720p-Front-RAM-Rose-FHD-8GB-display-AMD-Tuned-Radeon-14-Ryzen-Gold-THX-Graphics-IR-SSD-Laptop-MOTILE-5-Spatial-256GB-8-Performance-Audio-HD/909076408'

headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
def Check_Price():
	page = requests.get(URL, headers=headers)
	soup =BeautifulSoup(page.content,'html.parser')

	title =soup.find(content='MOTILE 14" Performance Laptop, FHD, AMD Ryzen 5 with Radeon Vega 8 Graphics, THX Spatial Audio, Tuned by THX display, 8GB RAM, 256GB SSD, HDMI, Front 720p HD IR Camera- Rose Gold').get_text()

	price =soup.find(itemprop='price').get_text()
	print(title)
	print(price)
	if (int(price)<Price_You_Want):
		send_mail()
	

def send_mail():
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('someone@email.com', 'pass****')
	
	subject='Price For Your Product Went Down'
	body='Check Link ',URL,'.'
	msg= f"Subject: {subject}\n\n{body}"
 
	server.sendmail(
		'someone@email.com',         #Add the sender mail ID
		'someoneelse@email.com', #Add the recieving mail ID
		msg
	)
	print('email send')
	server.quit()


Check_Price()

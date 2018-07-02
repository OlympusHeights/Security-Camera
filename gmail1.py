import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import os

def sendingImage(img, email, imgname):
		msg = MIMEMultipart()
		msg['Subject'] = 'footage'
		msg['From'] = 'surveillance1camera@gmail.com'
		msg['To'] = email
		text = MIMEText("I See You...")
		msg.attach(text)
		image = MIMEImage(img, name=os.path.basename(imgname))
		msg.attach(image)
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()
		s.login('surveillance1camera@gmail.com', 'Campuse1!')
		s.sendmail('surveillance1camera@gmail.com', email, msg.as_string())
		s.quit()
		os.remove(imgname)
		
	

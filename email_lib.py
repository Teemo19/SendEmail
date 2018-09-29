import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
class email_lib:
	def __init__(self,From,Pass,To,Subject,Text):
		self.From=From
		self.To=To
		self.Subject=Subject
		self.Pass=Pass
		self.Text=Text

	def send_text(self):
		try:
			msg = MIMEMultipart()
			msg['From'] = self.From
			msg['To'] = self.To
			msg['Subject'] = 'your_subject'
			msg.attach(MIMEText(self.Text, 'plain'))
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.ehlo()
			server.starttls()
			server.login(self.From,self.Pass)
			server.sendmail(self.From, self.To,msg.as_string())
			server.close()
		except:
			print("Wrong parameters !")
			pass
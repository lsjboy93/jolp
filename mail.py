import time, datetime
import subprocess
from subprocess import call #
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
import os

#sending email
def sendMail():
   sender = "*******@gmail.com" 
   receivers = ["*******@*******"] 
   subject = "raspberry3 - motion!!!"

   msg = MIMEMultipart()

   msg['From'] = sender
   msg['To'] = ", ".join(receivers)
   msg['Subject'] = Header(subject, 'utf8')
   
   #
   body = """\
   <h3>detected moving.</h3>
   <p>[notice] this mail is automaticaly.<br>
   <strong>please take care of attatcked file.</strong></p>
   """
   sub = subprocess
   dt = datetime.datetime.now()
   #print date
   dire = '/home/pi/Pictures/'
   time = dt.strftime('%d%d%d%d%d%d' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
   #attach = dire + time + '.png'
   cmd = 'raspistill -o ' + dire + time
   sub.call(cmd+'.png', shell = True)
   #attach = "/home/pi/Videos/"+180529-003945280737.jpg+".png"
   filename = time+'.png'
   attach = "/home/pi/Pictures/"+filename
   #print("attachFile:" + attach)

   if (os.path.exists(attach)): #
      msg.attach(MIMEText(body, 'html', _charset="utf8")) 
      
      attachFilename = filename
      #attachFilename = filename+".h264" //
      attachment = open(attach, "rb")
      part = MIMEBase('application', 'octet-stream', _charset="utf8")
      part.set_payload((attachment).read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', "attachment; filename= %s" % attachFilename)
      msg.attach(part)

      try:
         # Gmail SMTP 
         smtpserver = smtplib.SMTP("smtp.gmail.com", 587) 
         smtpserver.starttls() #tls connection
         smtpserver.login(sender, "**********")
         smtpserver.sendmail(sender, receivers, msg.as_string())
         print("Successfully sent email.")
         smtpserver.close()
         smtpserver.quit()
      except smtplib.SMTPException:
         print ("Error: Unable to send email.")
         
   else:
      print ("No attached.")
      
try:
    sendMail()
               
except KeyboardInterrupt:
   print ("Quit")

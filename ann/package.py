from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Model
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def enhance(model,accuracy): 
     while(accuracy<0.96):
         i=model.layers[-1].output.shape[1]
         j=model.layers[-2].output.shape[1]
         if j/2 > i:
             u= int(j/2)
         elif j/2 < i:
             u= int((i+j)/2)
             temp = Model(model.input, model.layers[-2].output)
             model=Sequential()
             model.add(temp)
             model.add(Dense(u, activation='relu'))
             model.add(Dense(i, activation='softmax'))
             model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
             mod=model.fit(x, y, epochs=5)
             accuracy=mod.history['accuracy'][-1]
     else:
         print("model is accurate enough",accuracy)
         gmailUser = 'arjunrekhi265@gmail.com'
         gmailPassword = ' arjun12b'
         recipient = 'arjunsja2000@gmail.com'
         message = f'Model trained successfully'
         msg = MIMEMultipart()
         msg['From'] = f'"Ajay" <{gmailUser}>'
         msg['To'] = 'Me'
         msg['Subject'] = "Sending mail from python"
         msg.attach(MIMEText(message))
         try:
             mailServer = smtplib.SMTP('smtp.gmail.com', 587)
             mailServer.ehlo()
             mailServer.starttls()
             mailServer.ehlo()
             mailServer.login(gmailUser, gmailPassword)
             mailServer.sendmail(gmailUser, recipient, msg.as_string())
             mailServer.close()
             print ('Email sent!')
         except:
             print ('Something went wrong...')
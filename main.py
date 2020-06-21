import subprocess
from datetime import datetime
from datetime import timedelta
import bluetooth
import BlynkLib
import time
import os

BLYNK_AUTH = 'c2eef4381dde4826ba98120c42774dc2'
data_path = '/home/pi/jolp/code/'
blynk = BlynkLib.Blynk(BLYNK_AUTH)
data_set = 0
mac = 0
life = 10
life_fire = 10
rec_fire = datetime.now()
rec_move = datetime.now()
current_time = datetime.now()

while ((os.path.exists('/dev/rfcomm0'))!= True) :
    print('find blue...')
    find_blue = subprocess.check_output('hcitool scan', shell = True).split('\t')
    for i in find_blue :
        print(i)
        if(i[0:5] == 'HC-06') :
            call_str = 'sudo rfcomm bind rfcomm0 ' + mac
            break
        else:
            mac = i

        time.sleep(1)

data_set = subprocess.check_output('head -n 1 /dev/rfcomm0', shell = True).split(' ')
print(data_set)


@blynk.VIRTUAL_READ(1)
def v1_read_handler():
    # This widget will show some time in seconds.
    data_set = subprocess.check_output('head -n 1 /dev/rfcomm0', shell = True).split(' ')
    print(data_set)
    print ('temp = '+data_set[0])
    blynk.virtual_write(1, data_set[0])
    #print('value : {}'.fromat(value))
@blynk.VIRTUAL_READ(2)
def v2_read_handler():
    #data_set = subprocess.check_output('head -n 1 /dev/rfcomm0', shell = True).split(' ')
    print('humi = '+data_set[1])
    blynk.virtual_write(2, data_set[1])

@blynk.VIRTUAL_READ(3)
def v3_read_handler() :
    data_set = subprocess.check_output('head -n 1 /dev/rfcomm0', shell = True).split(' ')
    print('fire = '+data_set[2][0])
    if (data_set[2][0] == '1') :
        global life_fire
        print('Fire')
        blynk.virtual_write(3, 'Fire')
        life_fire = life_fire -1
        #subprocess.call('python /home/pi/jolp/code/fire_mail.py')
        #current_time = datetime.now()
        #if(current_time - rec_fire > timedelta(minutes = 10)):
        if (life_fire < 0) :
            os.system('python /home/pi/jolp/code/fire_mail.py')
            life_fire = 60
 

    else :
        print('No Fire')
        print(life_fire)
        blynk.virtual_write(3, 'Nothing')


@blynk.VIRTUAL_READ(4)
def v4_read_handler() :
    blynk.virtual_write(4, "Nothing")
    print('micro = '+data_set[3][0])
    if (data_set[3][0]== '1') :
        global life
       
        blynk.virtual_write(4, 'Detected')
        life = life-1
        #subprocess.call('python /home/pi/jolp/code/mail.py', shell = False)
        if (life<0)  :
            print('Detected')
            os.system('python /home/pi/jolp/code/mail.py')
            life = 60
            blynk.virtual_write(4, 'Detected')
        else:
            print('Nothing')
            blynk.virtual_write(4, "Nothing")
        #rec_move = datetime.now()
        
    else :
        print('No Move ')
        print(life)
        blynk.virtual_write(4, 'Nothing')
    
    #blynk.virtual_write(4, 'efgh')
while 1:

    blynk.run()
    
    #sleep(1)
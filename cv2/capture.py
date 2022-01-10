import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    num=random.randint(0,100)
    vid=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vid.read()
        img_name="img"+str(num)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
        return img_name
        print("pic taken")
    vid.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.A_vAB4p58N7p13ahRzT20lF_3gdgqt3qni47JAhqu_K7cQnt0plxwRkxmWeRR9RBaprdlNo_E7CH3XfJ1pANBduUKqxISbvYipkZaIbg_mij4yKm4-ptsBb4psTnyVpvFQnGBSwMAPaH"
    file=img_name
    file_from=file
    file_to="/newFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to, node=dropbox.files.Writemode.overWrite)
        print("uploaded")

def main():
    while (True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)



    



take_snapshot()




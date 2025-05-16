import tkinter as tk
from PIL import Image , ImageTk
import csv
from datetime import date
import time
import numpy as np
import cv2
from tkinter.filedialog import askopenfilename
import os
import shutil

import Train_FDD_cnn as TrainM
from gtts import gTTS
import playsound
import sqlite3
import speech_recognition as sr
import smtplib
from email.message import EmailMessage


#==============================================================================
root = tk.Tk()
root.state('zoomed')

root.title("Garbage and Spit Detection ")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"g2.webp")
bg.resize((1300,600),Image.LANCZOS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
current_path = str(os.path.dirname(os.path.realpath('__file__')))

basepath=current_path  + "\\" 

# print(w,h)
# bg_img = ImageTk.PhotoImage(bg)
# bg_lbl = tk.Label(root,image=bg_img)
# bg_lbl.place(x=0,y=93)


label_l1 = tk.Label(root, text="Automated Garbage And Spit Detection",font=("Times New Roman", 30, 'bold'),
                    background="#B0E0E6", fg="black", width=67, height=2)
label_l1.place(x=0, y=0)


#============================================================================================================
def create_folder(FolderN):
    
    dst=os.getcwd() + "\\" + FolderN         # destination to save the images
    
    if not os.path.exists(dst):
        os.makedirs(dst)
    else:
        shutil.rmtree(dst, ignore_errors=True)
        os.makedirs(dst)


def CLOSE():
    root.destroy()
#####==========================================================================================================
    
def update_label(str_T):
    # clear_img()
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25),bg='cyan',fg='black' )
    result_label.place(x=400, y=400)

def train_model():
    Train = ""
    update_label("Model Training Start...............")
    
    start = time.time()

    X=TrainM.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    update_label(msg)

###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    


def run_video(VPathName,XV,YV,S1,S2):

    cap = cv2.VideoCapture(VPathName)
   

#    cap.set(cv2.CAP_PROP_FPS, 30)

#    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'mp4v'))
    def show_frame():
                    
        ret, frame = cap.read()
        cap.set(cv2.CAP_PROP_FPS, 30)
               
        out=cv2.transpose(frame)
    
        out=cv2.flip(out,flipCode=0)
    
        cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        img   = Image.fromarray(cv2image).resize((S1, S2))
    
        imgtk = ImageTk.PhotoImage(image = img)
        
        lmain = tk.Label(root)
#        lmain.place(x=560, y=190)
        lmain.place(x=XV, y=YV)

        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)
                
                
    show_frame()
        
def VIDEO():
    
    global fn
    
    fn=""
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                               filetypes=[("all files", "*.*")])

    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)
            
    if Sel_F!= 'mp4':
        print("Select Video .mp4 File!!!!!!")
    else:
        run_video(fn,560, 190,753, 485)

  
     
def F2V(VideoN):
    

    Video_Fname=F2V.Create_Video(basepath + 'result',VideoN)
    run_video(Video_Fname,1000, 250,753, 485)
    print(Video_Fname)

###################################################################################################################
###################################################################################################################
def show_FDD_video(video_path):
    ''' Display FDD video with annotated bounding box and labels '''
    from tensorflow.keras.models import load_model
    
    # video_path=r"D:\Alka_python_2019_20\FDD_Main\Video_File\fall-01.mp4"
    img_cols, img_rows = 224,224
    
    FALLModel=load_model(r'garbage.h5',compile=False)  
    #FALLModel=load_model('train_model.h5')#video = cv.VideoCapture(video_path);
    
    video = cv2.VideoCapture(video_path)
    
    # Get the original video's width and height
    width = int(video.get(3))
    height = int(video.get(4))

    # Calculate the new dimensions
    new_width = int(width * 100 / 100)
    new_height = int(height * 100 / 100)
    # Create VideoWriter object to save the resized video
    # fourcc = cv2.VideoWriter_fourcc(*'mp4')
    # out = cv2.VideoWriter(video, fourcc, 20.0, (new_width, new_height))
        
    # video = cv2.VideoCapture(0)

    if (not video.isOpened()):
        print("{} cannot be opened".format(video_path))
        # return False

    font = cv2.FONT_HERSHEY_SIMPLEX
    green = (0, 255, 0) 
    red = (0, 0, 255)
    # orange = (0, 127, 255)
    line_type = cv2.LINE_AA
    i=1
    
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        img=cv2.resize(frame,(img_cols, img_rows),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.array(img)
        
        X_img = img.reshape(-1, img_cols, img_rows, 1)
        X_img = X_img.astype('float32')
        
        X_img /= 255
        
        predicted =FALLModel.predict(X_img)

        if predicted[0][0] < 0.5:
            predicted[0][0] = 0
            predicted[0][1] = 1
            label = 1
        else:
            predicted[0][0] = 1
            predicted[0][1] = 0
            label = 0
          
        frame_num = int(i)  #.iloc[:1,0])
        # label = int(annotations['label'][i])
        label_text = ""
        
        color = (255, 255, 255)
        font = 5
        if  label == 1 :
            label_text = "Abnormal Activity Detected "
            color = red
            TTS = gTTS(label_text)
            TTS.save('audio.mp3')
            os.system('audio.mp3')
            
            
            time.sleep(5)
            from subprocess import call
            call(["python","mail.py"])
            
          

               
        
        else:
            label_text = "Normal Activity "
            color = green
            
        
        
        frame = cv2.putText(
            frame, "Frame: {}".format(frame_num), (5, 30),
            fontFace = font, fontScale = 1, color = color, lineType = line_type
        )
        frame = cv2.putText(
            frame, "Label: {}".format(label_text), (5, 60),
            fontFace = font, fontScale =1, color = color, lineType = line_type
        )

        i=i+1
        frame = cv2.resize(frame, (new_width, new_height))
        cv2.imshow('FDD', frame)
        # 
                
        if cv2.waitKey(30) == 27:
            break
    
    video.release()
    cv2.destroyAllWindows()
       
###################################################################################################################  
def Video_Verify():
    
    global fn
    
#    fn=r"D:\Alka_python_2019_20\Alka_python_2019_20\Video Piracy\Piracy_Preserving\result.mp4"
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                               filetypes=[("all files", "*.*")])

    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)
            
    if Sel_F!= 'mp4':
        print("Select Video File!!!!!!")
    else:
        
        show_FDD_video(fn)
        # run_video(fn,520, 190,400,500)    
########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
        
   
###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            

button5 = tk.Button(root,command = Video_Verify, text="Garbage and Spit Detection", width=20,font=("Times new roman", 25, "bold"),bg="#B0E0E6",fg="black")
button5.place(x=600,y=500)

button6 = tk.Button(root,command = train_model, text="Train Model", width=20,font=("Times new roman", 25, "bold"),bg="#B0E0E6",fg="black")
button6.place(x=600,y=350)

close = tk.Button(root,command = CLOSE, text="Exit", width=20,font=("Times new roman", 25, "bold"),bg="#B0E0E6",fg="Black")
close.place(x=600,y=650)


root.mainloop()







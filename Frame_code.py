from email.mime import image
import time
import tkinter
import tkinter as tk
from logging import root
from tkinter import *
from tkinter import filedialog, ttk
from tkinter.filedialog import askopenfilename
import os
from tkinter.font import BOLD
import cv2
import PIL.Image
import PIL.ImageTk
from cv2 import *
from numpy import pad
from PIL import Image, ImageTk
import numpy as np


flag=int(1)
global last_frame                                      
last_frame = np.zeros((480, 640, 3), dtype=np.uint8)





class App:
        def __init__(self,window,video_source=0):
            self.window = window
            window.title("multi-Frames")
            window.geometry('1080x1400')
            self.video_source = video_source
            self.vid=MyVideoCapture(self.video_source)
    

            ############ Frames################
            self.frame_one=Frame(window,highlightbackground="black",highlightthickness=2,padx=145,pady=125)
            self.frame_one.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

            self.f_label=Label(self.frame_one,text="FRAME 1",font=("courier 20 underline "),pady=8)
            self.f_label.grid(columnspan=2)
            self.f_label.place(relx =0.6, rely = -0.37, anchor = CENTER)



            ################frame 2#################
            self.frame_two=Frame(window,highlightbackground="black",highlightthickness=2,padx=1,pady=10)
            self.frame_two.grid(row=0,column=1,pady=10,sticky="nsew")
            
            self.lab_tit=Label(self.frame_two,text="FRAME 2",pady=10)
            self.lab_tit.grid(row=0,column=0,sticky="nsew")            


            self.frame_twoA=LabelFrame(self.frame_two,text="A fra",highlightbackground="blue",highlightthickness=2,padx=1,pady=1)
            self.frame_twoA.grid(sticky="nsew")
            
            self.lbhi=Label(self.frame_twoA,text=" photos and vdo's \n will be \n displayed here ",highlightbackground="black",highlightthickness=2,padx=205,pady=160)
            self.lbhi.grid()        
            

            self.frame_twoB=LabelFrame(self.frame_two,text="B fra",highlightbackground="yellow",highlightthickness=2,pady=1,padx=1)
            self.frame_twoB.grid(sticky="nsew")
            
            #########################frame 2##################################


            ###########################frame 3 #######################60s

            self.frame_th=LabelFrame(window,highlightbackground="black",highlightthickness=2,padx=10,pady=10)
            self.frame_th.grid(padx=10,pady=10,row=1,column=0,sticky="nsew")

            self.lb_title=Label(self.frame_th,text="FRAME 3",font=BOLD,pady=10)
            self.lb_title.grid(row=0,column=0)
            self.lb_title.place()

            self.frame_thA=LabelFrame(self.frame_th,text="frame thA",highlightbackground="black",highlightthickness=2,padx=1,pady=1)
            self.frame_thA.grid(sticky="nsew")
            
            self.lb=Label(self.frame_thA,text="images will \n appear here",highlightbackground="red",highlightthickness=2,padx=230,pady=160)
            self.lb.grid() 
                 

             #########################frame 4 ############################3            

            self.frame_fo=LabelFrame(window,highlightbackground="black",highlightthickness=2,padx=150,pady=185)
            self.frame_fo.grid(padx=10,pady=10,row=1,column=1,sticky="nsew")


            self.lb_title=Label(self.frame_fo,text="FRAME 4",font=("courier 20 underline "),padx=10,pady=10)
            self.lb_title.grid(padx=1,pady=1)
            self.lb_title.place(relx =0.6, rely = -2, anchor = CENTER)
            ###############Frames#############
       
            ############Frame one buttons#########
            self.imgbt=Button(self.frame_one,text="Capture Image",bg="blue",fg="white",width=20,pady=10,command=self.open_img)
            self.imgbt.grid(row=3,column=0,pady=10)
            

            self.imgbt=Button(self.frame_one,text="Capture an Video",bg="blue",fg="white",width=20,pady=10,command=self.open_vdo)
            self.imgbt.grid(row=4,column=0,pady=10)


            self.imgbt=Button(self.frame_one,text="Explore from the files",bg="blue",fg="white",width=20,pady=10,command=self.open_file)
            self.imgbt.grid(row=5,padx="10", pady="10")

            self.clrbt=Button(self.frame_one, text="Clear",fg="black",width=20,pady=10, command=self.clear_frame)
            self.clrbt.grid(row=6,padx=10,pady=10)

            self.bt=Button(self.frame_twoB,text="Process",bg="blue",fg="white",highlightbackground="black",highlightthickness=2,width=63,command=self.process)
            self.bt.grid()

            ############Frame one buttons#########       



            ############ Canvas button########
            #self.canvas = tkinter.Canvas(width = self.vid.width, height = self.vid.height)
            #self.canvas.grid()
            #self.canvas.place(relx=1,rely=1,anchor=CENTER)
            #sself.vid_frame = self.canvas.create_image(0, 0, anchor = NW)

            #self.delay = 15
            #self.update()
            #root.mainloop()
            ########### Canvas button############

            #################################function#####################################


            ##############Rescale function#############
        def rescaleframe(self,frame,scale=0):
            self.width=int(frame.shape[1]*scale)
            self.height=int(frame.shape[0]*scale)
            dimensions=(self.width,self.height)

            return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
            ############rescale function###########



            ################clear widgets##################
        def clear_frame(self):
            pass

            ################clear widgets##################3


            #######################temp  stor#######################
        def temp_stor(self):
            ret, frame=self.vid.get_frame()
            if ret:
                cv2.imwrite("frame-"+time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
            #######################temp  stor#######################
            
            
            
            #######################update#######################

        def update(self):
            ret, frame = self.vid.get_frame()

            if ret:
                img = Image.fromarray(frame)
                img=img.resize((515,360),Image.ANTIALIAS)  #resizing should always indicated after 
                #the pil conversion of number format and before to the photoimage conversion 
                self.photo = ImageTk.PhotoImage(image=img)
                #self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.lbhi.image = self.photo
                self.lbhi.configure(image=self.photo)
                self.window.after(self.delay, self.update)

        def update1(self):
            # Get a frame from the video source
            ret, frame = self.vid.get_frame()

            if ret:
                self.window.after(self.delay, self.update)

            #######################update#######################
            
            ####################### forget ######################


        def forget(self):
            function.forget()
            ####################### forget ######################
                  


        ############ open file ############
        def open_file(self):
            global panelA,panelB
            path=askopenfilename()
            if len(path) > 0:
                # load the image from disk, convert it to grayscale, and detect edges in it
                #self.clear_frame()
                
                image = cv2.imread(path)
                #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                #edged = cv2.Canny(gray, 50, 100)
                # OpenCV represents images in BGR order; however PIL represents images in RGB order, so we need to swap the channels
                #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                # convert the images to PIL format...
                image = Image.fromarray(image)
                #edged = Image.fromarray(edged)
                #resize
                image=image.resize((515,360),Image.ANTIALIAS)
                
		        # ...and then to ImageTk format
                imagetk = ImageTk.PhotoImage(image=image)
                #edged = ImageTk.PhotoImage(edged)		# if the panels are None, initialize them
                #if panelA is None :#or panelB is None:
                    # the first panel will store our original image
                self.lbhi.image=imagetk
                self.lbhi.configure (image= imagetk)
                flag=2
                print(flag)

               ############ open file ############
                

              ############ open video ############


        def open_vdo(self):
            global flag 
            flag=4
            print(flag)     
                                          ###1st type##
            ret, frame = self.vid.get_frame()
            if ret is None:
                print( "Major error!")
            elif ret:
                global last_frame
                last_frame = frame.copy()
                
            frame = self.rescaleframe(frame,scale=1.5)
            pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)     #we can change the display color of the frame gray,black&white here
            img = Image.fromarray(pic)
            img=img.resize((515,360),Image.ANTIALIAS)  #resizing should always indicated after 
            #the pil conversion of number format and before to the photoimage conversion 
            imagetk = ImageTk.PhotoImage(image=img)
            self.lbhi.image = imagetk
            self.lbhi.configure(image=imagetk)
            self.delay = 10
            self.update()
        

                                 ### 2nd type ####
            '''''''''
            ret, frame = self.vid.get_frame()
            if ret is None:
                print( "Major error!")
            #elif ret:
                #global last_frame
                #last_frame = frame.copy()
            #frame = self.rescaleframe(frame,scale=1.5)
            pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)     #we can change the display color of the frame gray,black&white here
            img = Image.fromarray(pic)
            img=img.resize((515,360),Image.ANTIALIAS)  #resizing should always indicated after 
            #the pil conversion of number format and before to the photoimage conversion 
                      
            imgtk = ImageTk.PhotoImage(image=img)
            self.lbhi.imgtk = imgtk
            self.lbhi.configure(image=imgtk)
            self.lbhi.after(10, self.open_vdo) 
              '''''

               ############ open video ############
        

              ############ open image ############
        
        def open_img(self):           
            global flag      
            
            ret,frame=self.vid.get_frame()            
            path=("/home/user/image processing/kamal pro/cap img/")            
            if ret:
                cv2.imwrite(path+"frame-"+time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
            image=cv2.imread(path) 
            image = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)            
            image = Image.fromarray(image)
            image=image.resize((515,360),Image.ANTIALIAS)            
            imagetk = ImageTk.PhotoImage(image=image)

            self.lbhi.image=imagetk
            self.lbhi.configure(image=imagetk)
            flag=3 
            print(flag)
            return frame 
           
      
        ############ open image ############

        def ret_img(self,):
            pass

        def process(self):
            global flag   
            if (flag==3):
                ret,frame=self.vid.get_frame() 
                path=("/home/user/image processing/kamal pro/cap img/")            
                if ret:
                                                
                    cv2.imwrite(path+"frame-"+time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
                    image=cv2.imread(path) 
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)            
                    image = Image.fromarray(image)
                    image=image.resize((515,360),Image.ANTIALIAS)            
                    imagetk = ImageTk.PhotoImage(image=image)

                    self.lb.image=imagetk
                    self.lb.configure(image=imagetk) 
            elif (flag==4):
                ret, frame = self.vid.get_frame()
                if ret is None:
                    print( "Major error!")
                elif ret:
                    global last_frame
                    last_frame = frame.copy()
                frame = self.rescaleframe(frame,scale=1.5)
                pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)     #we can change the display color of the frame gray,black&white here
                img = Image.fromarray(pic)
                img=img.resize((515,360),Image.ANTIALIAS)  #resizing should always indicated after 
                #the pil conversion of number format and before to the photoimage conversion 
                imagetk = ImageTk.PhotoImage(image=img)
                self.lb.image = imagetk
                self.lb.configure(image=imagetk)
                self.lb.after(10, self.open_vdo)
                
            else:
                pass
                              

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()





root = Tk()
app = App(root)
root.mainloop()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import the necessary packages
from __future__ import print_function
from PIL import Image
from PIL import ImageTk
import Tkinter as tki
import threading
import datetime
import imutils
import cv2
import os, time
import thread
import numpy as np

class tkinter:
	def __init__(self):
		# store the video stream object and output path, then initialize
		# the most recently read frame, thread for reading frames, and
		# the thread stop event
		self.thread = None
		self.state = False
		self.stopEvent = None

		# initialize the root window and image panel
		self.root = tki.Tk()
		#self.toggle_fullscreen();
		#self.root.call('wm', 'attributes', '.', '-topmost', '1')
		self.panel = None
		import sys
		reload(sys)
		sys.setdefaultencoding('utf-8')
		# create a button, that when pressed, will take the current
		# frame and save it to file
		
		self.btn = tki.Button(self.root, text="SQL", height=1,
			command=self.convert)
		self.btn.pack(side="bottom", fill="both", expand="yes", padx=5,
			pady=10)
			
		self.textsql = tki.Text(self.root, height=10)
		self.textsql.pack(side="bottom", fill="both", padx=10, pady=10)
		
		self.textip = tki.Text(self.root, height=10)
		self.textip.pack(side="bottom", fill="both", padx=10, pady=10)
			
		#self.stopEvent = threading.Event()
		#self.thread = threading.Thread(target=self.videoLoop, args=())
		#self.thread.start()


		# set a callback to handle when the window is closed
		self.root.wm_title("IPTV Convert to SQL")
		self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)
	def toggle_fullscreen(self, event=None):
		self.state = not self.state
		self.root.attributes("-fullscreen", self.state);
		return "break";
	def end_fullscreen(self, event=None):
		self.state = False
		self.root.attributes("-fulscreen", False);
		return "break"

	def convert(self):
		iptvtext = self.textip.get(1.0, tki.END);
		iptvtext = iptvtext.replace("#EXTINF:0,", "").replace("#EXTM3U", "").replace(".ts", ".ts | ");
		array = iptvtext.split("|");
		self.sql = "";
		for item in array:
			try:
				channel = item.split("http")
				name = channel[0].rstrip().lstrip();
				url = "http"+channel[1];
				self.sql = self.sql+"INSERT INTO channels (title, rtmp, image, cat_id, sira)VALUES('"+name+"', '"+url+"', '','0', '0');";
			except IndexError:
				print("index hatası");
		self.writeSQL();
		
	def writeSQL(self):
		#self.textsql.delete(1.0, "END")
		self.textsql.insert(1.0, self.sql)
		text_file = open("insert.sql", "w");
		text_file.write(self.sql);
		text_file.close();
	def onClose(self):
		# set the stop event, cleanup the camera, and allow the rest of
		# the quit process to continue
		print("[INFO] closing...")
		#self.stopEvent.set()
		#self.vs.stop()
		#self.capture.stop();
		self.root.quit()

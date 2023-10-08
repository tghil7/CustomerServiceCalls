import matplotlib.pyplot as plt
import datetime
import pandas as pd
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import csv
import numpy as np
import copy


m = tk.Tk()

class CustomerServiceCalls():
	


	def openFile(self):
		filename = filedialog.askopenfilename(initialdir = "C:/Users/Anicet/Documents/ESU/IS 826 OA",
										  title = "Select a File",
										  filetypes = (('text files', '*.txt'),
													   ("all files",
														"*.*")))
		return filename
	
	def readFromFile(self, filename): 
		grades = []
		with open(filename, newline="") as file: 
			reader = csv.reader(file) 
			for row in reader: grades.append(row)
		return grades
	
	def callAnalysisByRep(self):
		#Get the data from the file
		list_rep  = [] # Initial list of the company representatives, contains duplicates
		#Get the file name 
		file = self.openFile()
		call_data = pd.read_csv(file) # Get the data frame
		call_data_file = self.readFromFile(file) # Get the data in a list for computing purposes
		call_data_file.pop(0) # Pop the first item in the list since it is only the header. 
		for item in call_data_file:
			list_rep.append(item[len(item)-1])

		unique_rep = set (list_rep)
  
		list_of_outgoing_calls_per_rep = [] # List of outgoing call counts per representative
		list_of_incoming_calls_per_rep  = [] # List of incoming call counts per representative
		count_in = 0 # Count of incoming calls.
		count_out = 0 # count of outgoing calls. 
		
		#Convert the unique_rep from a tuple back to a list
		unique_rep_list = list(unique_rep)
		#Compute the count of calls.
		for name in unique_rep_list:
			for item in call_data_file:
				if (item[3] == 'Outgoing' and item[len(item)- 1] == name):
					count_out += 1
				elif (item[3] == 'Incoming' and item[len(item)- 1] == name):
					count_in += 1
			'''print ('Name: ' + name)	
			print ('Count In: ' + str(count_in)) 
			print ('Count Out: ' + str(count_out)) '''   
			list_of_incoming_calls_per_rep.append (count_in)
			list_of_outgoing_calls_per_rep.append(count_out)
			# Resetting the counts for the next representative.
			count_in = 0
			count_out = 0
		# Setting the axis for my two plots
		x = call_data['Rep ID'].unique()
		y1 = list_of_incoming_calls_per_rep
		y2 = list_of_outgoing_calls_per_rep

		#Arrange the display on the bar chart 
		X_axis = np.arange(len(x))
		bar_width = 0.5
		plt.bar(X_axis - 0.2, y1, color ='blue', width = bar_width, label= 'Incoming Calls')
		plt.bar(X_axis + 0.2, y2, color ='orange',width = bar_width, label= 'Outgoing Calls')
		plt.xlabel('Representative')
		plt.ylabel('Number of Calls')
		plt.title('Total Number of Calls By Representative')
		plt.xticks(X_axis, x, rotation=45)
		#Save the chart
		plt.savefig('plot1.jpg')
		plt.show()

	def callAnalysisByTime(self):
		#Get the data from the file
		list_times  = [] # Initial list of the company representatives, contains duplicates
		#Get the file name 
		file = self.openFile()
		call_data = pd.read_csv(file) # Get the data frame
		call_data_file = self.readFromFile(file) # Get the data in a list for computing purposes
		call_data_file.pop(0) # Pop the header item. 
		#Make a copy of the data file so that calculations do not affect it. 
		for item in call_data_file:
			list_times.append(item[2])
		
		# Get each unique time used 
		unique_times = set (list_times)
  
		list_of_incoming_call_counts_per_unique_time = [] # List of incoming count calls per unique time. 
		list_of_outgoing_call_counts_per_unique_time = [] # List of outgoing count calls per unique time. 
		count_in = 0
		count_out = 0
		

		#Convert the unique_rep from a tuple back to a list
		unique_time_list = list(unique_times)
		#Compute the count of calls.
		for time in unique_time_list:
			for item in call_data_file:
				if (item[3] == 'Outgoing' and time == item[2]):
					count_out += 1
				elif (item[3] == 'Incoming' and  time == item[2] ):
					count_in += 1
			 
			list_of_incoming_call_counts_per_unique_time.append (count_in)
			list_of_outgoing_call_counts_per_unique_time.append(count_out)
			# Relist_of_outgoing_call_counts_per_unique_timesetting the counts for the next representative.
			count_in = 0
			count_out = 0
		
		# Setting the axis for my two plots
		x = call_data['Time Block'].unique()
		y1 = list_of_incoming_call_counts_per_unique_time
		y2 = list_of_outgoing_call_counts_per_unique_time
		#Arrange the display on the bar chart 
		X_axis = np.arange(len(x))
		plt.plot(x, y1, color ='blue',  label= 'Incoming Calls')
		plt.plot(x, y2, color ='orange', label= 'Outgoing Calls')
		plt.xlabel('Time Block')
		plt.ylabel('Number of Calls')
		plt.title('Total Number of Calls By Time Block')
		plt.xticks(rotation=45)
		#Save the chart
		plt.savefig('plot2.jpg')
		plt.show()


	def timeHistogram(self):
		#Get the data from the file
		list_times  = [] # Initial list of the company representatives, contains duplicates
		#Get the file name 
		file = self.openFile()
		call_data = pd.read_csv(file) # Get the data frame
		call_data_file = self.readFromFile(file) # Get the data in a list for computing purposes
		call_data_file.pop(0) # Pop the header item. 
		#Make a copy of the data file so that calculations do not affect it. 
		for item in call_data_file:
			list_times.append(item[2])
		
		# Get each unique time used 
		unique_times = set (list_times)
  
		list_of_call_counts_per_unique_time = [] # List of count calls per unique time. 
		count = 0
		

		#Convert the unique_rep from a tuple back to a list
		unique_time_list = list(unique_times)
		#Compute the count of calls.
		for time in unique_time_list:
			for item in call_data_file:
				if (time == item[2]):
					count += 1
			list_of_call_counts_per_unique_time.append (count)
			count = 0 # Resetting the count for each time frame
		
		# Setting the axis for my two plots
		x = call_data['Time Block']
		y = list_of_call_counts_per_unique_time
		
		#Arrange the display on the bar chart 
		plt.hist(x, bins=len(y), color='blue', edgecolor='black')
		plt.xlabel('Time Block')
		plt.ylabel('Number of Calls')
		plt.title('Histogram Time Block')
		plt.xticks(rotation=45)
		#Save the chart
		plt.savefig('plot3.jpg')
		plt.show()

	def callAnalysisByPurpose(self):
		#Get the data from the file
		list_purposes  = [] # Initial list of the call purposes, contains duplicates
		#Get the file name 
		file = self.openFile()
		call_data = pd.read_csv(file) # Get the data frame
		call_data_file = self.readFromFile(file) # Get the data in a list for computing purposes
		call_data_file.pop(0) # Pop the header item. 
		#Make a copy of the data file so that calculations do not affect it. 
		for item in call_data_file:
			list_purposes.append(item[1])
		
		# Get each unique time used 
		unique_purposes = set (list_purposes)
  
		list_of_call_counts_per_unique_purpose = [] # List of count calls per unique time. 
		count = 0
		

		#Convert the unique_rep from a tuple back to a list
		unique_purpose_list = list(unique_purposes)
		#Compute the count of calls.
		for purpose in unique_purpose_list:
			for item in call_data_file:
				if (purpose == item[1]):
					count += 1
			list_of_call_counts_per_unique_purpose.append (count)
			count = 0 # Resetting the count for each time frame
		list_of_call_counts_per_unique_purpose.sort() # Sorting to make sure the order of items displayed is preserved.
		# Setting the axis for my two plots
		x = list_of_call_counts_per_unique_purpose
		y = call_data['Call Purpose'].unique()
		
		#Arrange the display on the bar chart 
		plt.pie(x, labels= y, autopct='%1.2f%%')
		plt.title('Volume of Calls by Call Purpose')
		#Save the chart
		plt.savefig('plot4.jpg')
		plt.show()

	def createDashboard(self):
		#Create the interface
		m.title ('Dashboard for Customer Service Performance Analysis.')
		m.geometry ('1200x900')
		# Create a label frame for the "Welcome" text
		welcome_frame = LabelFrame(m)
		welcome_frame.pack(fill="both", padx=10, pady=10)

		# Create a label with the "Welcome" text inside the label frame
		welcome_label = Label(welcome_frame, text="Dashboard for Customer Service Performance Analysis")
		welcome_label.pack(padx=10, pady=10)

		# Create a frame for the images
		image_frame = LabelFrame(m, text="Image Gallery")
		image_frame.pack(fill="both", expand="yes", padx=10, pady=10)

		# Load and display the .jpg images
		image_filenames = ["plot1.jpg", "plot2.jpg", "plot3.jpg", "plot4.jpg"]
		img1 = Image.open("plot1.jpg")
		img1=img1.resize((400, 400))
		img1 = ImageTk.PhotoImage(img1)
		img1_label = Label(image_frame, image=img1)
		img1_label.image = img1
		img1_label.pack(side="left", padx=5, pady=5)

		img2 = Image.open("plot2.jpg")
		img2=img2.resize((400, 400))
		img2 = ImageTk.PhotoImage(img2)
		img2_label = Label(image_frame, image=img2)
		img2_label.image = img2
		img2_label.pack(side="right", padx=5, pady=5)

		img3 = Image.open("plot3.jpg")
		img3 = img3.resize((400, 400))
		img3 = ImageTk.PhotoImage(img3)
		img3_label = Label(image_frame, image=img3)
		img3_label.image = img3
		img3_label.pack(side="left", padx=5, pady=5)

		img4 = Image.open("plot4.jpg")
		img4 = img4.resize((400, 400))
		img4 = ImageTk.PhotoImage(img4)
		img4_label = Label(image_frame, image=img4)
		img4_label.image = img4
		img4_label.pack(side="right", padx=5, pady=5)



	




def main ():
	my_customer_calls = CustomerServiceCalls() # Create an instance of the class, and call each of its functions. 
	'''my_customer_calls.callAnalysisByRep()
	my_customer_calls.callAnalysisByTime()
	my_customer_calls.timeHistogram()
	my_customer_calls.callAnalysisByPurpose()'''
	my_customer_calls.createDashboard()

if __name__=='__main__':
	main()
	m.mainloop()



	



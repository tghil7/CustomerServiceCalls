import matplotlib.pyplot as plt
import datetime
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import csv
import numpy as np


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
		plt.savefig('../plot1.jpg')
		plt.show()


def main ():
	my_customer_calls = CustomerServiceCalls()
	my_customer_calls.callAnalysisByRep()

if __name__=='__main__':
	main()



	



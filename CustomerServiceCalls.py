import matplotlib.pyplot as plt
import datetime;
import csv;
import copy;
import tkinter as tk
from tkinter import filedialog


class CustomerServiceCalls():


    def readFromFile(self,filename): 
        call_data = []
        with open(filename, newline="") as file: 
            reader = csv.reader(file) 
            for row in reader: call_data.append(row)
        return call_data
    
    
    def openFile(self):
        filename = filedialog.askopenfilename(initialdir = "C:/Users/Anicet/Documents/ESU/IS 826 OA",
                                          title = "Select a File",
                                          filetypes = (('text files', '*.txt'),
                                                       ("all files",
                                                        "*.*")))
        file_read = self.readFromFile(filename)
        return file_read
    
    def callAnalysisByRep(self):
        #Get the data from the file
        call_data = self.openFile()
        print ('The list :' )
        print (call_data)


def main ():
    my_customer_calls = CustomerServiceCalls()
    my_customer_calls.callAnalysisByRep()

if __name__=='__main__':
    main()



    



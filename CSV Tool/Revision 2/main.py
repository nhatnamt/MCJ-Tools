#!/usr/bin/env python

"""
MCJ Parcel Importer Tool
Big thanks to ZetCode wxPython tutorial for the drag drop UI

v2.0 Changelog:
 - Added Drag and Drop UI
 - Bug fix for item's price > $1000
 - Warning and Exclude Local pickup items

"""

import csv
import math
import time
from os import path

class FileDrop(wx.FileDropTarget):

    def __init__(self, window):

        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):

        for name in filenames:

            try:
                file = open(name, 'r')
                text = file.read()
                csv_f = csv.reader(file)
                self.window.WriteText(text)
                eBay_to_parcelSend(csv_f)

            except IOError as error:

                msg = "Error opening file\n {}".format(str(error))
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()

                return False

            except UnicodeDecodeError as error:

                msg = "Cannot open non ascii files\n {}".format(str(error))
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()

                return False

            finally:

                file.close()

        return True

class mainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(mainFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.text = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.TE_READONLY)
        dt = FileDrop(self.text)

        self.text.SetDropTarget(dt)

        self.SetTitle('MCJ Shipping and Stock Control Tool')
        self.Centre()

def eBay_to_parcelSend():
    print("Parcel send csv creating tool v1.2")
    print("Only works for domestic delivery")
    name = input("Path to file (Press enter for default (eBay.csv)): ")
    if name == '':
        name = 'eBay.csv'
    time.sleep(0.2)

    print('Run... \n')

    try:
        with open(name, 'r') as input_csv:
            try :
                eBay_csv = csv.DictReader(input_csv, delimiter=',',
                    skipinitialspace=True,
                    quoting=csv.QUOTE_ALL)
                print(eBay_csv)
                csv_f = csv.reader(input_csv)
                row = list(csv_f)
                for entry in eBay_csv:
                    print(entry['Sales Record Number'])
            except:
                print('Invalid character in csv file, please check again!')
    except IOError:
        f_n = input("File not found, please enter a new path (Enter for default): ")
        if f_n == '':
            f_n = 'eBay.csv'
        time.sleep(0.2)

        #print(row['Sales Record Number'])
    # list_len = len(row)-3
    # writing_list = [['Row type', 'Recipient contact name', 'Recipient business name', 'Recipient address line 1', 'Recipient address line 2', 'Recipient address line 3', 'Recipient suburb', 'Recipient state', 'Recipient postcode', 'Send tracking email to recipient', 'Recipient email address', 'Recipient phone number', 'Delivery/special instruction 1', 'Special instruction 2', 'Special instruction 3', 'Sender reference 1 ', 'Sender reference 2', 'Product id', 'Authority to leave', 'Safe drop ', 'Quantity', 'Packaging type', 'Weight', 'Length', 'Width', 'Height', 'Parcel contents', 'Transit cover value']]
    # sp = ['']

    # start = 2 #start reading position
    # try:
    #     if row[2][1] == '':
    #         start = 3
    # except IndexError:
    #         start = 3
    # print(row)
    # for i in range(start,list_len):
    #     if row[i][19].lower() != 'australia': #skip for international
    #         continue
    #     lst = [''] * 28
    #     lst[0] = 'S'
    #     lst[1] = row[i][12] #name
    #     lst[3] = row[i][15] #adr1
    #     if lst[3][:4].lower() == 'ebay':
    #         lst[3] = row[i][14]
    #     lst[6] = row[i][16] #suburb
    #     lst[7] = row[i][17] #state
    #     lst[8] = row[i][18] #postcode
    #     lst[9] = 'YES' #traking
    #     lst[10] = row[i][4] #email
    #     lst[11] = '0' + row[i][13][4:] #phone
    #     lst[15] = row[i][20] #Ad ID
    #     price = float(row[i][25][4:].translate({ord(','): None}))
    #     if  price < 2000: #transit cover
    #         lst[27] = math.ceil(price)
    #     else: 
    #         lst[27] = 2000
    #     writing_list.append(lst)

    # time.sleep(0.5) 
    # with open("out.csv", "w", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(writing_list)
    # time.sleep(0.5)
    
    p = input('Done, press Enter to exit')
    # time.sleep(0.5) 

def main():

    app = wx.App()
    ex = mainFrame(None)
    ex.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()


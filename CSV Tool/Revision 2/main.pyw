import csv
import math
import os
import wx
import time

writing_list = [['Row type', 
                 'Recipient contact name', 
                 'Recipient business name', 
                 'Recipient address line 1', 
                 'Recipient address line 2', 
                 'Recipient address line 3', 
                 'Recipient suburb', 
                 'Recipient state', 
                 'Recipient postcode', 
                 'Send tracking email to recipient', 
                 'Recipient email address', 
                 'Recipient phone number', 
                 'Delivery/special instruction 1', 
                 'Special instruction 2', 
                 'Special instruction 3', 
                 'Sender reference 1 ', 
                 'Sender reference 2', 
                 'Product id', 
                 'Authority to leave', 
                 'Safe drop ', 
                 'Quantity',
                 'Packaging type', 
                 'Weight', 
                 'Length', 
                 'Width', 
                 'Height', 
                 'Parcel contents', 
                 'Transit cover value']]
# Handle File Dropped on the window
class FileDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
    
    def OnDropFiles(self, x, y, filenames):
        for name in filenames:
            try:
                file = open(name, 'r')
                self.window.WriteText("Opening file " + name +"\n")
                time.sleep(0.1)
                eBay2PSend(self.window,file)
            
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

# Main UI Panel
class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.my_text = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        btn = wx.Button(self, label='Browse..')
        btn.Bind(wx.EVT_BUTTON, self.onOpen)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.my_text, 1, wx.ALL|wx.EXPAND)
        sizer.Add(btn, 0, wx.ALL|wx.ALIGN_RIGHT, 5)

        self.SetSizer(sizer)

        dropt = FileDrop(self.my_text)
        self.my_text.SetDropTarget(dropt)

    def onOpen(self, event):
        wildcard = "TXT files (*.csv)|*.csv"
        dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        path = dialog.GetPath()

        if os.path.exists(path):
            with open(path) as fobj:
                self.my_text.WriteText("Opening file " + path +"\n")
                time.sleep(0.1)
                eBay2PSend(self.my_text,fobj)

# Extract information from eBay csv and export it to toParcelSend.csv
def eBay2PSend(window,file):
    csv_f = csv.reader(file)
    try :
        row = list(csv_f)
        window.WriteText("Imported \r\n")
    except:
        window.WriteText("Nein \r\n")

    list_len = len(row)-3
    sp = ['']

    start = 2 #start reading position
    try:
        if row[2][1] == '':
            start = 3
    except IndexError:
            start = 3
    for i in range(start,list_len):
        if row[i][19].lower() != 'australia': #skip for international
            continue
        if row[i][50].lower() == 'local pickup':
            continue
        lst = [''] * 28
        lst[0] = 'S'
        lst[1] = row[i][12] #name
        lst[3] = row[i][14] + ' ' + row[i][15] #adr1
        lst[6] = row[i][16] #suburb
        lst[7] = row[i][17] #state
        lst[8] = row[i][18] #postcode
        lst[9] = 'YES' #traking
        lst[10] = row[i][4] #email
        lst[11] = '0' + row[i][13][4:] #phone
        lst[15] = row[i][20] #Ad ID
        price = float(row[i][25][4:].translate({ord(','): None}))
        if  price < 2000: #transit cover
            lst[27] = math.ceil(price)
        else: 
            lst[27] = 2000
        writing_list.append(lst)
    with open("toParcelSend.csv", "w", newline="") as f:
        window.WriteText("Exporting... \r\n")
        writer = csv.writer(f)
        writer.writerows(writing_list)
    
    time.sleep(0.1)
    window.WriteText("Done")

class mainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Text File Reader')
        self.InitUI()

    def InitUI(self):
        panel = MyPanel(self)
        self.SetTitle('MCJ Parcel Send Importer')
        self.SetIcon(wx.Icon("app.ico", wx.BITMAP_TYPE_ICO))
        self.Center()
        self.Show()

def main():
    app = wx.App(False)
    frame = mainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
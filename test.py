import glob2
import shutil
import os
from os.path import expanduser

dict={'img':['.jpg','.jpeg','.gif','.png','.bmp','tif'],'docs':['.doc','.docx','.txt','.msg','.log','.rtf','.crt'],'excel':['.csv','.xls','.xlsx'],'pdf':['.pdf','.psd'],'software':['.exe','.app','.bat','.wsf'],'audio':['.mp3','.wav'],'video':['.avi','.flv','.mp4','.mov'],'software':['.zip'],'powerpoint':['.ppt','.pptx','.potx'],'xml&sql':['.sql','.xml']}
file=['xml&sql', 'music', 'video', 'powerpoint', 'files', 'docs', 'excel', 'pictures', 'pdf', 'zip', 'software']
home = expanduser("~")
newpath = home+'\Downloads'

if not os.path.exists(newpath+'\pictures'):
    os.makedirs(newpath+'\pictures')
if not os.path.exists(newpath+'\docs'):
    os.makedirs(newpath+'\docs')
if not os.path.exists(newpath+'\excel'):
    os.makedirs(newpath+'\excel')
if not os.path.exists(newpath+'\pdf'):
    os.makedirs(newpath+'\pdf')
if not os.path.exists(newpath+'\software'):
    os.makedirs(newpath+'\software')
if not os.path.exists(newpath+'\\music'):
    os.makedirs(newpath+'\\music')
if not os.path.exists(newpath+'\powerpoint'):
    os.makedirs(newpath+'\powerpoint')
if not os.path.exists(newpath+'\\xml&sql'):
    os.makedirs(newpath+'\\xml&sql')
if not os.path.exists(newpath+'\zip'):
    os.makedirs(newpath+'\zip')



source='C:\\Users\JD050692\Downloads\*'

dest='C:\\Users\JD050692\Downloads'
for f in glob2.glob(source):
    for item in dict:
        for i in dict[item]:
            if f.endswith(i):
                if os.path.exists(f):
                    os.remove(f)
                else:
                    shutil.move(f, dest+'\\'+item)













############################################################
##========================IMPORTS=========================##

import ch
import random
import sys
import os
import re
import time
import json
import urllib
import traceback
import __future__
import shelve
from time import localtime, strftime
from urllib.parse import quote
from urllib.request import urlopen
import urllib.request as urlreq
from urllib.request import urlopen
from xml.etree import cElementTree as ET
from urllib.request import unquote
from random import choice
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq
import datetime
import sys
import urllib.request 
import urllib.parse
import socket
from threading import Timer
from threading import Thread
import random
import re
import time
import json
import datetime
import os
import subprocess

lockdown = False
activated = True

startTime = time.time()
def getUptime():
  return time.time() - startTime  
##========================IMPORTS=========================##
############################################################
##========================FILES===========================##

rooms = []
file = open("files/rooms2.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    rooms.append(name.strip())
print("Loading Room: [Rooms] ")
file.close()

seven = []
file = open("files/seven.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    seven.append(name.strip())
print("Loading Room: [Rooms] ")
file.close()

ranks=dict()
f = open("files/rank.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,lvl,by,tmp,cor = json.loads(line.strip())
      ranks[user] = json.dumps([lvl,by,tmp,cor])
  except:
    print("[ERROR]Cant load CASH: %s" % line)
f.close()

locks=dict()
f = open("files/lock.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,lvl,by,tmp = json.loads(line.strip())
      locks[user] = json.dumps([lvl,by,tmp])
  except:
    print("[ERROR]Cant load CASH: %s" % line)
f.close()

cmds=dict()
f = open("files/cmd.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,lvl,by,tmp = json.loads(line.strip())
      cmds[user] = json.dumps([lvl,by,tmp])
  except:
    print("[ERROR]Cant load CASH: %s" % line)
f.close()

inboxs=dict()
f = open("files/inbox.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,lvl,by,tmp = json.loads(line.strip())
      inboxs[user] = json.dumps([lvl,by,tmp])
  except:
    print("[ERROR]Cant load CASH: %s" % line)
f.close()

dfs= dict()
f = open("files/df.txt", "r") # read-only
print("Loading Dict: [Status Dictionary] ")
for line in f.readlines():
  try:
    if len(line.strip())>0:
      word, definition, name, tmp = json.loads(line.strip())
      dfs[word] = json.dumps([definition, name, tmp])
  except:
    print("[ERROR]Cant load definition: %s" % line)
f.close()

notifics=dict()
f = open("files/notific.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,yt,join,leave = json.loads(line.strip())
      notifics[user] = json.dumps([yt,join,leave])
  except:
    print("[ERROR]Cant load CASH: %s" % line)
f.close()

hist = dict()
try:
  print("Loading Dict: [Status Wordtoday] ")
  f = open("files/hist.txt", "r")
  hist = eval(f.read())
  f.close()
except:pass

notif = []
f = open("files/notif.txt", "r")
print("Loading Notif: [Status Notifi] ")
for name in f.readlines():
  if len(name.strip())>0: notif.append(name.strip())
f.close

aviso = []
f = open("files/aviso.txt", "r")
print("Loading Notif: [Status Notifi] ")
for name in f.readlines():
  if len(name.strip())>0: aviso.append(name.strip())
f.close

welcome = []
f = open("files/welcome.txt", "r")
print("Loading Notif: [Status Notifi] ")
for name in f.readlines():
  if len(name.strip())>0: welcome.append(name.strip())
f.close

user_ip = dict()
try:
  print("Loading Dict: [Status Wordtoday] ")
  f = open("files/ip.txt", "r")
  user_ip = eval(f.read())
  f.close()
except:pass

##========================FILES===========================##
############################################################

def hexfont():
    hexs = ""
    clist = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    ignorehex = ['151C1F', '151C1F', '202020', '37212B', '151B20', '06241D', '800000', '4B0082']
    for i in range(6):
        hexs = hexs+random.choice(clist)
    if hexs in ignorehex:
        font(text)
    else:
        return hexs

def color(username):
    user = username.lower()
    if user in ranks:
        lvl,by,tmp,cor = json.loads(ranks[user])
        return cor
    else:
        return "FFFFFF"


#############################################################
##========================Variables========================##

botname = "lsabelita" 
botpassword = "92725430" 
cek_mods = dict()

##===========================End===========================##
#############################################################

#setting colors

class TestBot(ch.RoomManager):
  def onInit(self):
    self.setNameColor("999")
    self.setFontColor("FFF")
    self.setFontFace("1")
    self.setFontSize(10)
    self.enableBg()
    self.enableRecording()



  def getAccess(self, room, user):
    try:
      lvl,by,tmp,cor = json.loads(ranks[user.name])
      sts,by,tmp = json.loads(locks[room.name])
      if lvl == "god (7)" : return 7
      if lvl == "serafin (6)": return 6
      if lvl == "querubin (5)": return 5
      if lvl == "archangel (4)": return 4
      if lvl == "angel (3)" and sts == "unlock" : return 3
      if lvl == "angel (3)" and sts == "join" : return 3
      if lvl == "angel (3)" and sts == "sleep": return -3
      if lvl == "human (2)" and sts == "unlock" : return 2
      if lvl == "human (2)" and sts == "join" : return 2
      if lvl == "human (2)" and sts == "lock" : return -2
      if lvl == "human (2)" and sts == "sleep" : return -2
      if lvl == "human (2)" and sts == "blacklist" : return -2
      if lvl == "fallen angel (-1)": return -1
    except:
        sts,by,tmp = json.loads(locks[room.name])
        if sts == "unlock" : return 1
        if sts == "join": return 1
        if sts == "lock": return -2
        if sts == "sleep": return -2  
        if sts == "blacklist": return -2  

#############################################
##connecting and disconnecting crap##

  def onMessage(self, room, user, message):
   try:
    if user == self.user:
        return
    global activated
    global lockdown
    global prefix
    global owner
    global mod
    global registered
    def roomusers():
        usrs = []
        gay = []
        prop = 0
        prop = prop + len(room._userlist) - 1
        for i in room._userlist:
          i = str(i)
          usrs.append(i)
        while prop >= 0:
          j = usrs[prop].replace("<user : ", "")
          i = j.replace(">", "")
          gay.append(i)
          prop = prop - 1
        return gay
    def pars(args):
        args=args.lower()
        userlist = roomusers()
        for name in userlist:
          if args in name:return name
    def roompars(args):
      args = args.lower()
      for name in self.roomnames:
        if args in name:return name
    def getParticipant(arg):
          rname = self.getRoom(arg)
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(rname._userlist) - 1
          for i in rname._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<user : ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for j in gay:
            if j not in finale:
              finale.append(j)
    try:
      if room.getLevel(self.user) > 0:
         user_ip.update({user.name:message.ip})
         f = open('files/ip.txt', "w")
         f.write(str(user_ip))
         f.close
         print("[%s]\033[94m[MSG]\033[0m\033[31m[Rank %s]\033[0m\033[41m[%s][%s] %s: %s" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, message.ip, user.name.title(), message.body))
      else:
        print("[%s]\033[94m[MSG]\033[0m\033[31m[Rank %s]\033[0m\033[41m[%s][user_IP: Null] %s: %s" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, user.name.title(), message.body))
    except:pass


##################################################################################################################################################################################

    if user.name.startswith("#") or user.name.startswith("!"):return
    if self.getAccess(room, user) > 0:
      if not activated and self.getAccess(room, user) < 4: return #return, if not activated and user rank is less than 4.
    ##Commands: You design great commands for your bot in this part
      if message.body[0] == "+/-*-*-*": #prefixy usage in this line (for this case I use "*" as prefixy)
        data = message.body[1:].split(" ", 1) #This part splits message body into [0]prefixy and [1:]data ([1:] <- this means the message body's second character and after) and data will be split into 2 (cmd(data[0]), args(data[1])) which is very usefull. (Many thanks to TryHardHusky)
        if len(data) == 2: #If there are more than 1 data (This is where we will get args)
          cmd, args = data[0], data[1] #the first data (data[0]) will be the cmd (specified command) and the next data will be args (it doesn't matter how many word next to the cmd, It'd eventually be args)
        else: #If there is only 1 data (No args)
          cmd, args = data[0], "" #the arg will simply be "" (Empty)
        cmd == cmd.lower()



   except Exception as e:
         try:
          et, ev, tb = sys.exc_info()
          lineno = tb.tb_lineno
          fn = tb.tb_frame.f_code.co_filename
          self.getRoom("project-koqu").message("<br/><f x10FFFFFF='1'>.<br/><br/><f x10606060='1'>[<f x10E78696='1'><b>Error</b><f x10606060='1'>] <b/><br/>File : <f x10E78696='1'>/home/desktop/yuka/bot.rb   <br/><f x10606060='1'>Line :  <f x10E78696='1'>%i  <br/> <f x10606060='1'>Error : <f x10E78696='1'>%s "% (lineno, str(e)), True)
          return
         except:
          print("Undescribeable error detected !!")
          return

  def onPMMessage(self, pm, user, body):
       pm.message(user, "Hello I'm a bot created by http://lsabelita.chatango.com | Please visit my chat http://project-koqu.chatango.com for more information | I do not run in pm, visit a chat that I'm online to use.")
       self.pm.message(ch.User("lsabelita"), "[PM] - "+body+" ~"+user.name)

  


def hexc(e):
  et, ev, tb = sys.exc_info()
  if not tb: print(str(e))
  while tb:
    lineno = tb.tb_lineno
    fn = tb.tb_frame.f_code.co_filename
    tb = tb.tb_next
  print("(%s:%i) %s" % (fn, lineno, str(e)))
  
if __name__ == "__main__":
   try:
     os.system("clear")
     TestBot.easy_start(rooms, botname, botpassword)
   except KeyboardInterrupt:
     print("Console initiated a kill.")
   except Exception as e:
     hexc(e)

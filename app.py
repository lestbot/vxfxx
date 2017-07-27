
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
file = open("files/rooms.txt", 'r')
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

botname = "Koqu" 
botpassword = "daniel157" 
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

  def onJoin(self, room, user, target):
    case = 1
    namu = user.name
    hist.update({namu:[case,time.time(), room.name, "hey"]})
    if user.name not in welcome:
     if room.name == "harsilent-gahara-san":
       room.message("Hola <f x10"+color(namu)+"='1'> @"+(namu)+" <f x10FFFFFF='1'> sea bienvenido al mejor chat del chatango, si quería usarme solo teclear <f x10"+color(namu)+"='1'>#wl", True)
       welcome.append(user.name)
       f = open("files/welcome.txt", "w")
       f.write("\n".join(welcome))
       f.close() 

  def onLeave(self, room, user, target):
    case = 2
    namu = user.name
    hist.update({namu:[case,time.time(), room.name, "hey"]})
    print("< x10FFFFFF='1'>The user <f x10E78696='1'>"+(namu)+"<f x10606060='1'> leave in chat", True)

  def onModAdd(self, room, user):
      room.message("<f x10E78696='1'>"+(user.name)+ "<f x10606060='1'> was promoted to mod/staff of chat <f x10606060='1'>"+room.name, True)

  def onModRemove(self, room, user):
      room.message("<f x10E78696='1'>"+(user.name)+ "<f x10606060='1'> was removed from the chat four/staff position <f x10606060='1'>"+room.name, True)
     
  def onBan(self, room, user, target):
      room.message("<f x10E78696='1'>"+target.name+"<f x10606060='1'> was ban from chat <f x10E78696='1'>"+room.name+"<f x10606060='1'> by <f x10E78696='1'>"+user.name , True)

  def onUnban(self, room, user, target):
      room.message("<f x10E78696='1'>"+target.name+"<f x10606060='1'> was unban from chat <f x10E78696='1'>"+room.name+"<f x10606060='1'> by <f x10E78696='1'>"+user.name , True)

  def onReconnect(self, room):
      self.getRoom("project-koqu").message("<f x10606060='1'>[<f x10606060='1'>Bot info<f x10606060='1'>] reconectado em: <f x10606060='1'>" +room.name, True)

  def onDisconnect(self, room):
    self.getRoom("project-koqu").message("<f x10606060='1'>[<f x10606060='1'>Bot info<f x10606060='1'>] offline em: <f x10606060='1'>" +room.name, True)
    if len(self.roomnames) == 0:
       roomies = ["project-koqu"]
       for i in roomies:
        time.sleep(4600)
        self.joinRoom(i)

  def onFloodBan(self, room):
      self.getRoom("project-koqu").message("<f x10606060='1'>[<f x10606060='1'>Bot info<f x10606060='1'>] flood em: <f x10606060='1'>" +room.name, True)

  def onFloodWarning(self, room):
      self.getRoom("project-koqu").message("<f x10606060='1'>[<f x10606060='1'>Bot info<f x10606060='1'>] flood em: <f x10606060='1'>" +room.name, True)

  def onConnect(self, room):
    print("[+] Mad Hatter Connected to "+room.name)
    for i in cek_mods: #Di onJoin
      if len(cek_mods[i]) > 1:
        rmm, rmd = json.loads(cek_mods[i])
        self.getRoom(rmm).message("<br/><f x10FFFFFF='1'>.<br/><br/><f x10606060='1'> [<f x10E78696='1'><b>Moderation</b><f x10606060='1'>] <br/>Chat : <f x10E78696='1'>"+rmd+"<br/><f x10606060='1'>Owner : <f x10E78696='1'>"+ (self.getRoom(rmd).ownername) +"<br/><f x10606060='1'>Mods : <f x10E78696='1'>"+", ".join(self.getRoom(rmd).modnames), True)
        cek_mods.pop(i)
        return


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
        print("[%s]\033[94m[MSG]\033[0m\033[31m[Rank %s]\033[0m\033[41m[%s][%s] %s: %s" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, message.ip, user.name.title(), message.body))
      else:
        print("[%s]\033[94m[MSG]\033[0m\033[31m[Rank %s]\033[0m\033[41m[%s][user_IP: Null] %s: %s" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, user.name.title(), message.body))
    except:pass


##################################################################################################################################################################################

    if user.name.startswith("#") or user.name.startswith("!"):return
    if self.getAccess(room, user) > 0:
      if not activated and self.getAccess(room, user) < 4: return #return, if not activated and user rank is less than 4.

      if "banana" == message.body.lower() or "koqu" == message.body.lower():
           c=(random.choice(["hugs","kiss","my sweet","hi ","ya ","hola"]))
           room.message("<f x10FFFFFF='1'>* "+c+"<f x10"+color(user.name)+"='1'> "+(user.name)+"<f x10FFFFFF='1'> * ^^",True)

    ##Commands: You design great commands for your bot in this part
      if message.body[0] == "#": #prefixy usage in this line (for this case I use "*" as prefixy)
        data = message.body[1:].split(" ", 1) #This part splits message body into [0]prefixy and [1:]data ([1:] <- this means the message body's second character and after) and data will be split into 2 (cmd(data[0]), args(data[1])) which is very usefull. (Many thanks to TryHardHusky)
        if len(data) == 2: #If there are more than 1 data (This is where we will get args)
          cmd, args = data[0], data[1] #the first data (data[0]) will be the cmd (specified command) and the next data will be args (it doesn't matter how many word next to the cmd, It'd eventually be args)
        else: #If there is only 1 data (No args)
          cmd, args = data[0], "" #the arg will simply be "" (Empty)
        cmd == cmd.lower()


#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################## ROOM ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

############################################################################## CLEAR ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

############################################################################## JOIN ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "join" and self.getAccess(room, user) >= 3:
         a = user.name
         if args:
          if not args in rooms:
             user=args.lower()
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
             lvl ="join"
             by = a
             locks[user] = json.dumps([lvl,by,tmp])
             self.joinRoom(user)
             rooms.append(user)
             room.message("<f x10FFFFFF='1'>I'm joining in <f x10"+color(a)+"='1'>"+args+"",True)
             f = open("files/lock.txt", "w")
             for user in locks:
               lvl,by,tmp = json.loads(locks[user])
               f.write(json.dumps([user,lvl,by,tmp])+"\n")
             f.close() 
             f = open("files/rooms.txt", "w")
             f.write("\n".join(rooms))
             f.close() 
          else:
            room.message("<f x10FFFFFF='1'>I'm online in <f x10"+color(a)+"='1'>"+args,True)

############################################################################## LEAVE ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "leave" and self.getAccess(room, user) >= 3:
         a = user.name
         if args:
          if args in rooms:
             a = user.name
             user=args.lower()
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
             lvl ="leave"
             by = a
             locks[user] = json.dumps([lvl,by,tmp])
             self.leaveRoom(user)
             rooms.remove(user)
             room.message("<f x10FFFFFF='1'>I'm leaving in <f x10"+color(a)+"='1'>"+args+"",True)
             f = open("files/lock.txt", "w")
             for user in locks:
               lvl,by,tmp = json.loads(locks[user])
               f.write(json.dumps([user,lvl,by,tmp])+"\n")
             f.close() 
             f = open("files/rooms.txt", "w")
             f.write("\n".join(rooms))
             f.close() 
          else:
            room.message("<f x10FFFFFF='1'>I'm not online in <f x10"+color(a)+"='1'>"+args,True)

############################################################################## ROOM ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "lockstatus" and self.getAccess(room, user) >= 2:
          if not args:args=room.name
          if args in locks:
            lvl,by,tmp = json.loads(locks[args])
            room.message("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Lockstatus</b><f x10FFFFFF='1'>] <br/>Room : <f x10"+color(user.name)+"='1'>"+args+"<br/><f x10FFFFFF='1'>Status : <f x10"+color(user.name)+"='1'>"+lvl+"<br/><f x10FFFFFF='1'>Status by : <f x10"+color(user.name)+"='1'>"+by+"<br/><f x10FFFFFF='1'>Temp : <f x10"+color(user.name)+"='1'>"+tmp+" (GMT - 3)", True)
          else:
            room.message("<f x10FFFFFF='1'>The chat <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is not registered in my database", True)

############################################################################## BANLIST ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "banlist":
         if room.getLevel(self.user) >= 1 :
          if self.getAccess(room, user) >= 4:
              a = len([x.name for x in room.banlist])
              room.message("<f x10FFFFFF='1'>Banlist (<f x10"+color(user.name)+"='1'>"+str(a)+"<f x10FFFFFF='1'>) : <f x10"+color(user.name)+"='1'>"+", ".join([x.name for x in room.banlist]), True)
          else:
              room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, you do not have rank for user this command", True)
         else:
            room.message("<f x10FFFFFF='1'>I'm no have rank in the chat to show banlist", True)

############################################################################## ROOM ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "ban":
          if self.getAccess(room, ch.User(args)) >= 4:
             room.message("<f x10FFFFFF='1'>It is not possible to ban the user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> because its rank is high", True)
          else:
             if room.getLevel(self.user) >= 1 :
              if self.getAccess(room, user) >= 4:
               if ch.User(args) not in room._getBanlist():
                  room.banUser(ch.User(args))
                  room.message("<f x10FFFFFF='1'>The user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> was banned from chat", True)
               if ch.User(args) in room._getBanlist():
                  room.message("<f x10FFFFFF='1'>The user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is already banned", True)
              else:
               room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, you do not have rank for user this command", True)
             else:
                room.message("<f x10FFFFFF='1'>I'm no have rank in the chat to unban.", True)

############################################################################## ROOM ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "unban":
          if self.getAccess(room, user) >= 4:
           if room.getLevel(self.user) >= 1 :
             if args == "": return
             if ch.User(args) not in room._getBanlist():
                 room.message("<f x10FFFFFF='1'>The user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is not banned.", True)
             if ch.User(args) in room._getBanlist():
                 room.unban(ch.User(args))
                 room.message("<f x10FFFFFF='1'>Has removed banned from <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'>, do not abuse the rule again, it prevents ban", True)
           else:
             room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, you do not have rank for user this command", True)
          else:
             room.message("<f x10FFFFFF='1'>You do not have rank for unban", True)

############################################################################## MODS ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "mods" and self.getAccess(room, user) >= 4:
          args = args.lower()
          if args == "":
              room.message("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Moderation</b><f x10FFFFFF='1'>]<br/>Chat : <f x10"+color(user.name)+"='1'>"+room.name+"<br/><f x10FFFFFF='1'>Owner : <f x10"+color(user.name)+"='1'>"+ (room.ownername) +"<br/><f x10FFFFFF='1'>Mods : <f x10"+color(user.name)+"='1'>"+", ".join(room.modnames), True)
              return 
          if args in self.roomnames:
             modask = self.getRoom(args).modnames
             owner = self.getRoom(args).ownername
             room.message("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Moderation</b><f x10FFFFFF='1'>] <br/>Chat : <f x10"+color(user.name)+"='1'>"+args+"<br/><f x10FFFFFF='1'>Owner : <f x10"+color(user.name)+"='1'>"+ (owner) +"<br/><f x10FFFFFF='1'>Mods : <f x10"+color(user.name)+"='1'>"+", ".join(modask), True)
          else:
             self.joinRoom(args)
             cek_mods[user.name] = json.dumps([room.name,args])
             self.setTimeout(4, self.leaveRoom, args)

############################################################################## SLEEP ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "broadcast":
          a = "bc"
          lvl,by,tmp = json.loads(cmds[a])
          if lvl == "disable":
             room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(user.name)+"='1'>broadcast<f x10FFFFFF='1'> is locked",True)
          else:
            if self.getAccess(room, user) >= 5:
               self.getRoom("project-koqu").message("<f x10FFFFFF='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10FFFFFF='1'><b>Log</b><f x10FFFFFF='1'>] <br/>User : <f x10FFFFFF='1'>%s <br/><f x10FFFFFF='1'>Room : <f x10FFFFFF='1'>%s <br/><f x10FFFFFF='1'>Cmd : <f x10FFFFFF='1'>%s %s <br/><f x10FFFFFF='1'>Ip : <f x10FFFFFF='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)
               for room in self.rooms:
                    room.message("<f x10FFFFFF='1'>[<f x10"+color(user.name)+"='1'><b>Broadcast</b><f x10FFFFFF='1'>]  <f x10FFFFFF='1'>"+args+" <f x10FFFFFF='1'>~<f x10"+color(user.name)+"='1'>"+user.name, True)              
            else:
              room.message("<f x10FFFFFF='1'>You do not have rank to use this command.",True)

############################################################################## SLEEP ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "fax" and self.getAccess(room, user) >= 5:
          a = "fax"
          lvl,by,tmp = json.loads(cmds[a])
          if lvl == "disable":
             room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(user.name)+"='1'>fax<f x10FFFFFF='1'> is locked",True)
          else:
            if self.getAccess(room, user) >= 5:
               name, body = args.split(" ", 1)
               self.getRoom(name).message("<f x10FFFFFF='1'>[<f x10"+color(user.name)+"='1'><b>Message</b><f x10FFFFFF='1'>] <f x10FFFFFF='1'>"+body+" <f x10FFFFFF='1'>~<f x10"+color(user.name)+"='1'>"+user.name, True)              
               room.message("<f x10FFFFFF='1'>OK! I sent the message",True)
            else:
              room.message("<f x10FFFFFF='1'>You do not have rank to execute this command")

############################################################################## SLEEP ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "sleep" and self.getAccess(room, user) >= 5:
         if not args:args=room.name
         if args:
          if args in locks:
            a = user.name
            user=args.lower()
            lvl,by,tmp = json.loads(locks[user])
            if lvl == "sleep":
             room.message("<f x10FFFFFF='1'>The room <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'> is locked",True)
            else:
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
             lvl ="sleep"
             by = a
             locks[args] = json.dumps([lvl,by,tmp])
             room.message("<f x10FFFFFF='1'>I'm locking the chat <f x10"+color(a)+"='1'>"+args+"",True)
             f = open("files/lock.txt", "w")
             for user in locks:
               lvl,by,tmp = json.loads(locks[user])
               f.write(json.dumps([user,lvl,by,tmp])+"\n")
             f.close() 
          else:
            room.message("<f x10FFFFFF='1'>The room <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is not logged in on my system",True)

############################################################################## LOCK ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "lock" and self.getAccess(room, user) >= 3:
         if not args:args=room.name
         if args:
          if args in locks:
            a = user.name
            user=args.lower()
            lvl,by,tmp = json.loads(locks[user])
            if lvl == "lock":
             room.message("<f x10FFFFFF='1'>The room <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'> is locked",True)
            else:
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
             lvl ="lock"
             by = a
             locks[args] = json.dumps([lvl,by,tmp])
             room.message("<f x10FFFFFF='1'>I'm locking the chat <f x10"+color(a)+"='1'>"+args+"",True)
             f = open("files/lock.txt", "w")
             for user in locks:
               lvl,by,tmp = json.loads(locks[user])
               f.write(json.dumps([user,lvl,by,tmp])+"\n")
             f.close() 
          else:
            room.message("<f x10FFFFFF='1'>The room <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is not logged in on my system",True)

############################################################################## ROOMS ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "rooms" and self.getAccess(room, user)>= 2:
             f = [] 
             for i in rooms: 
               f.append(" "+i+" (%s)" % str(self.getRoom(i).usercount)) 
               f.sort() 
             room.message("<f x10FFFFFF='1'>Rooms <f x10FFFFFF='1'>(<f x10"+color(user.name)+"='1'>%s<f x10FFFFFF='1'>) :  "%(len(self.roomnames))+"<f x10"+color(user.name)+"='1'>"+" ".join(f), True)

############################################################################## ROOMS ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "find" and len(args) > 0 and self.getAccess(room, user) >= 2:
          name = args.split()[0].lower()
          if not ch.User(name).roomnames:
            room.message("<f x10FFFFFF='1'>I can not find the <f x10"+color(user.name)+"='1'>"+args, True)
          else:
            room.message("<f x10FFFFFF='1'>The user <f x10"+color(user.name)+"='1'>%s <f x10FFFFFF='1'> online in : <f x10"+color(user.name)+"='1'>%s  " % (args, ", ".join(ch.User(name).roomnames)), True)

############################################################################## UNLOCK ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "unlock" and self.getAccess(room, user) >= 1:
         if not args:args=room.name
         if args:
          if args in locks:
            a = user.name
            user=args.lower()
            lvl,by,tmp = json.loads(locks[user])
            if lvl == "unlock":
             room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> has already been disabled",True)
            else:
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
             lvl ="unlock"
             by = a
             locks[args] = json.dumps([lvl,by,tmp])
             room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> has been disabled",True)
             f = open("files/lock.txt", "w")
             for user in locks:
               lvl,by,tmp = json.loads(locks[user])
               f.write(json.dumps([user,lvl,by,tmp])+"\n")
             f.close() 
          else:
            room.message("<f x10FFFFFF='1'>The room <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is not logged in on my system",True)

############################################################################## STATUS ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "stats" and self.getAccess(room, user) >= 2:
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y (GMT - 3)"))
             timey = message.time-time.time()+0.5
             minute = 60
             hour = minute * 60
             day = hour * 24
             days =  int(timey / day)
             hours = int((timey % day) / hour)
             minutes = int((timey % hour) / minute)
             seconds = int(timey % minute)
             string = ""
             if days > 0:
               string += str(days) + " " + (days == 1 and "day" or "days" ) + " "
             if len(string) > 0 or hours > 0:
               string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + " "
             if len(string) > 0 or minutes > 0:
               string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + " "
             string += str(seconds) + " " + (seconds == 1 and "sec" or "sec" )
             lvl1,by1,tmp1 = json.loads(cmds["ping"])
             lvl2,by2,tmp2 = json.loads(cmds["bc"])
             lvl3,by3,tmp3 = json.loads(cmds["fax"])
             lvl4,by4,tmp4 = json.loads(cmds["pm"])
             room.message("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Stats</b><f x10FFFFFF='1'>]<br/>Cmd ping : <f x10"+color(user.name)+"='1'>"+lvl1+"<br/><f x10FFFFFF='1'>Cmd broadcast (bc) : <f x10"+color(user.name)+"='1'>"+lvl2+"<br/><f x10FFFFFF='1'>Cmd fax : <f x10"+color(user.name)+"='1'>"+lvl3+"<br/><f x10FFFFFF='1'>Cmd pm : <f x10"+color(user.name)+"='1'>"+lvl4+"<br/><f x10FFFFFF='1'>Timelocal : <f x10"+color(user.name)+"='1'>"+tmp+"<br/><f x10FFFFFF='1'>Lag info : <f x10"+color(user.name)+"='1'>"+string, True)

############################################################################## TIME ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "lag" and self.getAccess(room, user) >= 2:
             timey = message.time-time.time()
             minute = 60
             hour = minute * 60
             day = hour * 24
             days =  int(timey / day)
             hours = int((timey % day) / hour)
             minutes = int((timey % hour) / minute)
             seconds = int(timey % minute)
             string = ""
             if days > 0:
               string += str(days) + " " + (days == 1 and "day" or "days" ) + " "
             if len(string) > 0 or hours > 0:
               string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + " "
             if len(string) > 0 or minutes > 0:
               string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + " "
             string += str(seconds) + " " + (seconds == 1 and "sec" or "sec" )
             room.message("<f x10FFFFFF='1'>Lag info : <f x10"+color(user.name)+"='1'>"+string, True)

############################################################################## TIME ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "server" and self.getAccess(room, user) >= 1:
             a = random.randint(100,250)
             timey = message.time-time.time()+0.5
             minute = 60
             hour = minute * 60
             day = hour * 24
             days =  int(timey / day)
             hours = int((timey % day) / hour)
             minutes = int((timey % hour) / minute)
             seconds = int(timey % minute)
             string = ""
             if days > 0:
               string += str(days) + " " + (days == 1 and "day" or "days" ) + " "
             if len(string) > 0 or hours > 0:
               string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + " "
             if len(string) > 0 or minutes > 0:
               string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + " "
             string += str(seconds) + " " + (seconds == 1 and "sec" or "sec" )
             b = "<f x10FFFFFF='1'>Lag info : <f x10"+color(user.name)+"='1'>"+string
             timey = getUptime()
             minute = 60
             hour = minute * 60
             day = hour * 24
             days =  int(timey / day)
             hours = int((timey % day) / hour)
             minutes = int((timey % hour) / minute)
             seconds = int(timey % minute)
             string = ""
             if days > 0:
               string += str(days) + " " + (days == 1 and "day" or "days" ) + " "
             if len(string) > 0 or hours > 0:
               string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + " "
             if len(string) > 0 or minutes > 0:
               string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + " "
             string += str(seconds) + " " + (seconds == 1 and "sec" or "sec" )
             room.message("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Server</b><f x10FFFFFF='1'>]<br/><f x10FFFFFF='1'>Model : <f x10"+color(user.name)+"='1'>Intel(R) Xeon(R) CPU E5-2686 v4 @ 3.30GHz, 3, cores : 2<br/><f x10FFFFFF='1'>Os : <f x10"+color(user.name)+"='1'>Ubuntu (Custom SxP) <br/><f x10FFFFFF='1'>Lang : <f x10"+color(user.name)+"='1'>Python 3.6.1 64Bits <br/><f x10FFFFFF='1'>Memory : <f x10"+color(user.name)+"='1'>2"+str(a)+"/3512MB <br/><f x10FFFFFF='1'>Running : <f x10"+color(user.name)+"='1'>"+string+"<br/>"+str(b), True)

############################################################################## LOG ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "log" and self.getAccess(room, user) >= 7:
           if args.lower() == "koqu":
              room.logout()
              room.login("Koqu", "daniel157")
              self.enableBg()
              self.setTimeout(int(1), room.message, "<f x10FFFFFF='1'>I changed to <f x10"+color(user.name)+"='1'>"+args, True)
           if args.lower() == "Ahenn":
              room.logout()
              room.login("Ahenn", "92725430")
              self.enableBg()
              self.setTimeout(int(1), room.message, "<f x10FFFFFF='1'>I changed to <f x10"+color(user.name)+"='1'>"+args, True)
           if args.lower() == "xpy":
              room.logout()
              room.login("xpy", "daniel157")
              self.enableBg()
              self.setTimeout(int(1), room.message, "<f x10FFFFFF='1'>I changed to <f x10"+color(user.name)+"='1'>"+args, True)
           if args.lower() == "off":
              room.logout()

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################## RANK ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

############################################################################## WL ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "wl" and self.getAccess(room, user) >= 1:
         if not args:args=user.name
         a = user.name
         if args:
          if not args in ranks:
            user=args.lower()
            tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
            lvl ="human (2)"
            by = "system"
            cor = hexfont()
            ranks[user] = json.dumps([lvl,by,tmp,cor])
            room.message("<f x10FFFFFF='1'>Dear user <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> successfully registered in the rank <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> at <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)"+"<f x10FFFFFF='1'> to show the available list of commands type <f x10"+color(a)+"='1'>#cmds<f x10FFFFFF='1'>",True)
            f = open("files/rank.txt", "w")
            for user in ranks:
              lvl,by,tmp,cor = json.loads(ranks[user])
              f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
            f.close() 
          else:
            room.message("<f x10FFFFFF='1'>User <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> registered", True)


############################################################################# BL ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower().lower() == "bl" and self.getAccess(room, user) >= 4:
         if not args:args=user.name
         a = user.name
         if args:
          if args in ranks:
           lvl,by,tmp,cor = json.loads(ranks[args])
           if lvl == "fallen angel (-1)":
              room.message("<f x10FFFFFF='1'>The user <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> is already registered in the blacklist",True)
           else:
             a = user.name
             user=args.lower()
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
             lvl ="fallen angel (-1)"
             by = a
             cor = "ff0000"
             ranks[user] = json.dumps([lvl,by,tmp,cor])
             room.message("<f x10FFFFFF='1'>The user <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> was added to rank <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)", True)
             f = open("files/rank.txt", "w")
             for user in ranks:
               lvl,by,tmp,cor = json.loads(ranks[user])
               f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
             f.close() 
          else:
            room.message("<f x10FFFFFF='1'>The user <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> is not registered", True)

        if cmd.lower() == "unbl" and self.getAccess(room, user) >= 5:
         if not args:args=user.name
         a = user.name
         if args:
          if args in ranks:
           lvl,by,tmp,cor = json.loads(ranks[args])
           if lvl == "fallen angel (-1)":
              a = user.name
              user=args.lower()
              tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
              lvl ="human (2)"
              by = a
              cor = hexfont()
              ranks[user] = json.dumps([lvl,by,tmp,cor])
              room.message("<f x10FFFFFF='1'>The user <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> was added to rank <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)", True)
              f = open("files/rank.txt", "w")
              for user in ranks:
                lvl,by,tmp,cor = json.loads(ranks[user])
                f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
              f.close() 
           else:
            room.message("<f x10FFFFFF='1'>The user <f x10"+color(a)+"='1'>"+args+"<f x10FFFFFF='1'> is not on blacklist", True)


############################################################################## STAFF ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "staff":
             arr = []
             i = "god (7)"           
             g = "god (7)"
             for i in ranks:
               if g in ranks[i]:
                 arr.append(i)
             if len(arr) > 0:
               a = "<br/><f x10FFFFFF='1'>Rank God (<f x10"+color(user.name)+"='1'>"+str(len(arr))+"<f x10FFFFFF='1'>) :  <f x10"+color(user.name)+"='1'>%s"% (', '.join(sorted(arr)))
             else:
               a = "<br/><f x10FFFFFF='1'>Rank God (<f x10"+color(user.name)+"='1'>0<f x10FFFFFF='1'>) :  <f x10"+color(user.name)+"='1'>empty"
             arr = []
             i = "serafin (6)"           
             g = "serafin (6)"
             for i in ranks:
               if g in ranks[i]:
                 arr.append(i)
             if len(arr) > 0:
               b = "<br/><f x10FFFFFF='1'>Rank Serafin (<f x10"+color(user.name)+"='1'>"+str(len(arr))+"<f x10FFFFFF='1'>) :  <f x10"+color(user.name)+"='1'>%s"% (', '.join(sorted(arr)))
             else:
               b = "<br/><f x10FFFFFF='1'>Rank Serafin (<f x10"+color(user.name)+"='1'>0<f x10FFFFFF='1'>) :  <f x10"+color(user.name)+"='1'>empty"
             arr = []
             i = "querubin (5)"           
             g = "querubin (5)"
             for i in ranks:
               if g in ranks[i]:
                 arr.append(i)
             if len(arr) > 0:
               c = "<br/><f x10FFFFFF='1'>Rank Querubin (<f x10"+color(user.name)+"='1'>"+str(len(arr))+"<f x10FFFFFF='1'>) :  <f x10"+color(user.name)+"='1'>%s"% (', '.join(sorted(arr)))
             else:
               c = "<br/><f x10FFFFFF='1'>Rank Querubin (<f x10"+color(user.name)+"='1'>0<f x10FFFFFF='1'>) :  <f x10"+color(user.name)+"='1'>empty"
             arr = []
             i = "archangel (4)"
             g = "archangel (4)"
             for i in ranks:
               if g in ranks[i]:
                 arr.append(i)
             if len(arr) > 0:
               d = "<br/><f x10FFFFFF='1'>Rank Archangel (<f x10"+color(user.name)+"='1'>"+str(len(arr))+"<f x10FFFFFF='1'>) : <f x10"+color(user.name)+"='1'>%s"% (', '.join(sorted(arr)))
             else:
               d = "<br/><f x10FFFFFF='1'>Rank Archangel (<f x10"+color(user.name)+"='1'>0<f x10FFFFFF='1'>) :  <f x10"+color(user.name)+"='1'>empty"
             arr = []
             i = "angel (3)"
             g = "angel (3)"
             for i in ranks:
               if g in ranks[i]:
                 arr.append(i)
             if len(arr) > 0:
               e = "<br/><f x10FFFFFF='1'>Rank Angel (<f x10"+color(user.name)+"='1'>"+str(len(arr))+"<f x10FFFFFF='1'>) : <f x10"+color(user.name)+"='1'>%s"% (', '.join(sorted(arr)))
             else:
               e = "<br/><f x10FFFFFF='1'>Rank Angel (<f x10"+color(user.name)+"='1'>0<f x10FFFFFF='1'>) :  <f x10"+color(user.name)+"='1'>empty"
             room.message("<br/><f x10000000='1'>.<br/><br/><f x10FFFFFF='1'>[<f x10"+color(user.name)+"='1'><b>Staff of Koqu</b><f x10FFFFFF='1'>]  "+a+" "+b+" "+c+" "+d+" "+e,True)

############################################################################## RANK ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "rank":
         if not args:
          if user.name in ranks:
             lvl,by,tmp,cor = json.loads(ranks[user.name])
             room.message("<f x10"+color(user.name)+"='1'>"+user.name.title()+"<f x10FFFFFF='1'> your rank is <f x10"+color(user.name)+"='1'>"+str(lvl)+"<f x10FFFFFF='1'> you were placed in that rank by <f x10"+color(user.name)+"='1'>"+str(by)+"<f x10FFFFFF='1'> at <f x10"+color(user.name)+"='1'>"+str(tmp)+" (GMT - 3)", True)
          else:
            room.message("<f x10"+color(user.name)+"='1'>"+user.name.title()+"<f x10FFFFFF='1'> you do not have a registered rank in my system, let's say that your rank is <f x10"+color(user.name)+"='1'>null<f x10FFFFFF='1'>,type <<f x10"+color(user.name)+"='1'>#wl<f x10FFFFFF='1'> to register is to have a valid rank", True)
         else:
           args=args.lower()
           if args in ranks:
              lvl,by,tmp,cor = json.loads(ranks[args])
              room.message("<f x10"+color(user.name)+"='1'>"+args.title()+"<f x10FFFFFF='1'> your rank is <f x10"+color(user.name)+"='1'>"+str(lvl)+"<f x10FFFFFF='1'> you were placed in that rank by <f x10"+color(user.name)+"='1'>"+str(by)+"<f x10FFFFFF='1'> at <f x10"+color(user.name)+"='1'>"+str(tmp)+" (GMT - 3)", True)
           else:
             room.message("<f x10FFFFFF='1'>The user <f x10"+color(user.name)+"='1'>"+args.title()+"<f x10FFFFFF='1'> does not have a registered rank in my system" , True)

############################################################################## SETRANK ###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "setrank" and self.getAccess(room, user) >= 6:
          a = user.name
          help_output = "1,2,3,4,5,6 "
          if args == "":
            room.message(help_output, True)
          if args != "":
#           try:
            args = args.lower()
            user, rank = args.split(" ", 1)
            user = str(user)
            rank = int(rank)
            available_rank = [-1,1,2,3,4,5,6,7]
            if not rank in available_rank:
              room.message("Type on rank")
              return
            if rank == 2:
               tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
               lvl ="human (2)"
               by = a
               cor = hexfont()
               ranks[user] = json.dumps([lvl,by,tmp,cor])
               room.message("<f x10FFFFFF='1'>Dear <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'>, you have been promoted to <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)",True)
               f = open("files/rank.txt", "w")
               for user in ranks:
                 lvl,by,tmp,cor = json.loads(ranks[user])
                 f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
               f.close() 
            if rank == 3:
               tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
               lvl ="angel (3)"
               by = a
               cor = hexfont()
               ranks[user] = json.dumps([lvl,by,tmp,cor])
               room.message("<f x10FFFFFF='1'>Dear <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'>, you have been promoted to <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)",True)
               f = open("files/rank.txt", "w")
               for user in ranks:
                 lvl,by,tmp,cor = json.loads(ranks[user])
                 f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
               f.close() 
            if rank == 4:
               tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
               lvl ="archangel (4)"
               by = a
               cor = hexfont()
               ranks[user] = json.dumps([lvl,by,tmp,cor])
               room.message("<f x10FFFFFF='1'>Dear <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'>, you have been promoted to <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)",True)
               f = open("files/rank.txt", "w")
               for user in ranks:
                 lvl,by,tmp,cor = json.loads(ranks[user])
                 f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
               f.close() 
            if rank == 5:
               tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
               lvl ="querubin (5)"
               by = a
               cor = hexfont()
               ranks[user] = json.dumps([lvl,by,tmp,cor])
               room.message("<f x10FFFFFF='1'>Dear <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'>, you have been promoted to <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)",True)
               f = open("files/rank.txt", "w")
               for user in ranks:
                 lvl,by,tmp,cor = json.loads(ranks[user])
                 f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
               f.close() 
            if rank == 6:
               tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
               lvl ="serafin (6)"
               by = a
               cor = hexfont()
               ranks[user] = json.dumps([lvl,by,tmp,cor])
               room.message("<f x10FFFFFF='1'>Dear <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'>, you have been promoted to <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)",True)
               f = open("files/rank.txt", "w")
               for user in ranks:
                 lvl,by,tmp,cor = json.loads(ranks[user])
                 f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
               f.close() 
            if rank == 7:
               tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
               lvl ="god (7)"
               by = a
               cor = hexfont()
               ranks[user] = json.dumps([lvl,by,tmp,cor])
               room.message("<f x10FFFFFF='1'>Dear <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'>, you have been promoted to <f x10"+color(a)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(a)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(a)+"='1'>"+tmp+" (GMT - 3)",True)
               f = open("files/rank.txt", "w")
               for user in ranks:
                 lvl,by,tmp,cor = json.loads(ranks[user])
                 f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
########################################################################### CMDS ############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

########################################################################### DISABLE ############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "disable" and self.getAccess(room, user) >= 7:
          if args in ["pm","ping","bc","fax"]:
             a = user.name
             user = args.lower()
             lvl,by,tmp = json.loads(cmds[user])
             if lvl == "disable":
                room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'> has already been disable",True)
             else:
               tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
               lvl ="disable"
               by = a
               cmds[user] = json.dumps([lvl,by,tmp])
               room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'> has been disable",True)
               f = open("files/cmd.txt", "w")
               for user in cmds:
                 lvl,by,tmp = json.loads(cmds[user])
                 f.write(json.dumps([user,lvl,by,tmp])+"\n")
               f.close() 
          else:
             room.message("<f x10FFFFFF='1'>The cmd <f x10FFFFFF='1'>"+args+"<f x10FFFFFF='1'> is not available for lock, the command list available is <f x10FFFFFF='1'>pm,ping,bc,fax", True)

########################################################################### ENABLE ############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "enable" and self.getAccess(room, user) >= 7:
          if args in ["pm","ping","bc","fax"]:
             a = user.name
             user = args.lower()
             lvl,by,tmp = json.loads(cmds[user])
             if lvl == "enable":
                room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'> has already been enable",True)
             else:
               tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
               lvl ="disable"
               by = a
               cmds[user] = json.dumps([lvl,by,tmp])
               room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(a)+"='1'>"+user+"<f x10FFFFFF='1'> has been enable",True)
               f = open("files/cmd.txt", "w")
               for user in cmds:
                 lvl,by,tmp = json.loads(cmds[user])
                 f.write(json.dumps([user,lvl,by,tmp])+"\n")
               f.close() 
          else:
             room.message("<f x10FFFFFF='1'>The cmd <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is not available for unlock, the command list available is <f x10"+color(user.name)+"='1'>pm, ping, bc, fax", True)

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################ ADMIM ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "ev" or cmd.lower() == "eval":
         if self.getAccess(room, user) >= 7:
          ret = eval(args)
          if ret == None:
           room.message("<f x10FFFFFF='1'>Update", True)
           return
          room.message(str(ret) ,True)
         else:
           if user.name not in aviso:
              aviso.append(user.name)
              room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, if you try to use the command <f x10"+color(user.name)+"='1'>"+cmd+"<f x10FFFFFF='1'> again you will be placed on blacklist", True)
           else:
             a = "system"
             b = user.name
             user = user.name
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
             lvl ="fallen angel (-1)"
             by = a
             cor = "ff0000"
             ranks[user] = json.dumps([lvl,by,tmp,cor])
             room.message("<f x10FFFFFF='1'>The user <f x10"+color(b)+"='1'>"+args+"<f x10FFFFFF='1'> was added to rank <f x10"+color(b)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(b)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(b)+"='1'>"+tmp+" (GMT - 3)", True)
             f = open("files/rank.txt", "w")
             for user in ranks:
               lvl,by,tmp,cor = json.loads(ranks[user])
               f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
             f.close() 

############################################################################ EXECUTE ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "exec" or cmd.lower() == "ex":
         if self.getAccess(room, user) >= 7:
          ret = exec(args)
          if ret == None:
           room.message("<f x10FFFFFF='1'>Update", True)
           return
          room.message(str(ret) ,True)
         else:
           if user.name not in aviso:
              aviso.append(user.name)
              room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, if you try to use the command <f x10"+color(user.name)+"='1'>"+cmd+"<f x10FFFFFF='1'> again you will be placed on blacklist", True)
           else:
             a = "system"
             b = user.name
             user = user.name
             tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
             lvl ="fallen angel (-1)"
             by = a
             cor = "ff0000"
             ranks[user] = json.dumps([lvl,by,tmp,cor])
             room.message("<f x10FFFFFF='1'>The user <f x10"+color(b)+"='1'>"+args+"<f x10FFFFFF='1'> was added to rank <f x10"+color(b)+"='1'>"+lvl+"<f x10FFFFFF='1'> by <f x10"+color(b)+"='1'>"+by+"<f x10FFFFFF='1'> in <f x10"+color(b)+"='1'>"+tmp+" (GMT - 3)", True)
             f = open("files/rank.txt", "w")
             for user in ranks:
               lvl,by,tmp,cor = json.loads(ranks[user])
               f.write(json.dumps([user,lvl,by,tmp,cor])+"\n")
             f.close() 

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################ MESSAGE ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "say" and self.getAccess(room, user) >= 2:
            if args:
              room.message(args, True)
            else:
              room.message("<f x10FFFFFF='1'>What do you want me to say? <f x10"+color(user.name)+"='1'>#say + word", True)

############################################################################ RSAY ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "rsay" and self.getAccess(room, user) >= 2:
          if args:
            room.message(args[::-1])
          else:
            room.message("<f x10FFFFFF='1'>What do you want me to say? <f x10"+color(user.name)+"='1'>#rsay + word", True)

############################################################################ RSAY ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "rb" and self.getAccess(room, user) >= 2:
          if args:
           word = args
           length = len(word)
           r = 255 
           g = 0
           b = 0
           sub = int(765/length)
           counter = 0
           string = ""
           for x in range(0, length):
               letter = word[counter]
               s = '<f x11%02X%02X%02X="1">%s' % (r, g, b, letter)
               string = string+s
               counter+=1
               if (r == 255) and (g >= 0) and (b == 0): #if all red
                   g = g+sub
                   if g > 255: g = 255
               if (r > 0) and (g == 255) and (b == 0): #if some red and all green
                   r = r-sub #reduce red to fade from yellow to green
                   if r<0: r = 0 #if red gets lower than 0, set it back to 0
               if (r == 0) and (g == 255) and (b >= 0):
                   b = b+sub
                   if b>255:
                      b = 255
                      trans = True
               if (r == 0) and (g > 0) and (b == 255):
                   g = g-sub
                   if g<0: g = 0
               if (r >= 0) and (g == 0) and (b == 255):
                   r = r+sub
                   if r>255: r = 255
           a = string
           room.message("<f x10FFFFFF='1'>Rainbow : "+a, True)
          else:
            room.message("<f x10FFFFFF='1'>What do you want me to say? <f x10"+color(user.name)+"='1'>#rb + word", True)

############################################################################ RSAY ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "rbc" and self.getAccess(room, user) >= 2:
          if args:
           word = args
           length = len(word)
           r = 255 
           g = 0
           b = 0
           sub = int(765/length)
           counter = 0
           string = ""
           for x in range(0, length):
               letter = word[counter]
               s = '<f x11%02X%02X%02X="1">%s' % (r, g, b, letter)
               string = string+s
               counter+=1
               if (r == 255) and (g >= 0) and (b == 0): #if all red
                   g = g+sub
                   if g > 255: g = 255
               if (r > 0) and (g == 255) and (b == 0): #if some red and all green
                   r = r-sub #reduce red to fade from yellow to green
                   if r<0: r = 0 #if red gets lower than 0, set it back to 0
               if (r == 0) and (g == 255) and (b >= 0):
                   b = b+sub
                   if b>255:
                      b = 255
                      trans = True
               if (r == 0) and (g > 0) and (b == 255):
                   g = g-sub
                   if g<0: g = 0
               if (r >= 0) and (g == 0) and (b == 255):
                   r = r+sub
                   if r>255: r = 255
           a = string
           room.message("Rainbow : "+a, False)
          else:
            room.message("<f x10FFFFFF='1'>What do you want me to say? <f x10"+color(user.name)+"='1'>#rb + word", True)

############################################################################ NG ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "ng" and len(args)>0:
         try:   
            text = args
            hexs = ""
            text = ""
            for letter in list(args):
                text = text + "<f x"+str(random.randint(9,14))+hexfont()+"=\""+str(random.randint(1,8))+"\">"+letter
            a = text
            room.message("<f x10FFFFFF='1'>Nick generator : "+a, True)
         except Exception as e:
             print(str(e))

############################################################################ NGC ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "ngc" and len(args)>0:
         try:   
            text = args
            hexs = ""
            text = ""
            for letter in list(args):
                text = text + "<f x"+str(random.randint(9,14))+hexfont()+"=\""+str(random.randint(1,8))+"\">"+letter
            a = text
            room.message("Code : "+a, False)
         except Exception as e:
             print(str(e))

############################################################################ NGC ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "ip" and self.getAccess(room, user) >= 2:
         if not args:
           room.message("<f x10FFFFFF='1'>Hey type #ip + number.ip ",True)
         else:
           try:
             free = json.loads(urllib.request.urlopen("http://www.freegeoip.net/json/{0}".format(args)).read().decode("utf-8").replace("\n",""))
             ip = json.loads(urllib.request.urlopen("http://ip-api.com/json/{0}".format(args)).read().decode("utf-8").replace("\n",""))
             ex = json.loads(urllib.request.urlopen("http://extreme-ip-lookup.com/json/{0}".format(args)).read().decode("utf-8").replace("\n",""))
             a = ("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Ip info</b><f x10FFFFFF='1'>]<br/><f x10FFFFFF='1'>Ip : <f x10"+color(user.name)+"='1'>"+free["ip"]+"<br/><f x10FFFFFF='1'>Country : <f x10"+color(user.name)+"='1'>"+free["country_name"]+" - "+free["region_code"]+"<br/><f x10FFFFFF='1'>City : <f x10"+color(user.name)+"='1'>"+free["city"]+"<br/><f x10FFFFFF='1'>Host : <f x10"+color(user.name)+"='1'>"+ip["as"]+"<br/><f x10FFFFFF='1'>Isp : <f x10"+color(user.name)+"='1'>"+ip["org"]+"<br/><f x10FFFFFF='1'>Timezone : <f x10"+color(user.name)+"='1'>"+ip["timezone"]+"<br/><f x10FFFFFF='1'>Coordinate (lat & long) : <f x10"+color(user.name)+"='1'>"+ex["lat"]+" & "+ex["lon"])
             room.message(a,True)
           except:
               room.message("<f x10FFFFFF='1'>Type <f x10"+color(user.name)+"='1'>#ip + 5.0.0.1 ",True)

############################################################################ NGC ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "ip1" and self.getAccess(room, user) >= 2:
           if not args:
            try:
              free = json.loads(urllib.request.urlopen("http://www.freegeoip.net/json/{0}".format(user_ip[user.name])).read().decode("utf-8").replace("\n",""))
              ip = json.loads(urllib.request.urlopen("http://ip-api.com/json/{0}".format(user_ip[user.name])).read().decode("utf-8").replace("\n",""))
              ex = json.loads(urllib.request.urlopen("http://extreme-ip-lookup.com/json/{0}".format(user_ip[user.name])).read().decode("utf-8").replace("\n",""))
              a = ("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Ip info</b><f x10FFFFFF='1'>]<br/>User : <f x10"+color(user.name)+"='1'>"+user.name+"<br/><f x10FFFFFF='1'>Ip : <f x10"+color(user.name)+"='1'>hide <br/><f x10FFFFFF='1'>Country : <f x10"+color(user.name)+"='1'>"+free["country_name"]+" - "+free["region_code"]+"<br/><f x10FFFFFF='1'>City : <f x10"+color(user.name)+"='1'>"+free["city"]+"<br/><f x10FFFFFF='1'>Host : <f x10"+color(user.name)+"='1'>"+ip["as"]+"<br/><f x10FFFFFF='1'>Isp : <f x10"+color(user.name)+"='1'>"+ip["org"]+"<br/><f x10FFFFFF='1'>Timezone : <f x10"+color(user.name)+"='1'>"+ip["timezone"]+"<br/><f x10FFFFFF='1'>Coordinate (lat & long) : <f x10"+color(user.name)+"='1'>"+ex["lat"]+" & "+ex["lon"])
              room.message(a,True)
            except:
                room.message("<f x10FFFFFF='1'>Hey <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'> there is no ip registered in my database, to register come to my chat <f x10"+color(user.name)+"='1'>http://project-koqu.chatango.com ",True)
           else:
            try:
             free = json.loads(urllib.request.urlopen("http://www.freegeoip.net/json/{0}".format(user_ip[args])).read().decode("utf-8").replace("\n",""))
             ip = json.loads(urllib.request.urlopen("http://ip-api.com/json/{0}".format(user_ip[args])).read().decode("utf-8").replace("\n",""))
             ex = json.loads(urllib.request.urlopen("http://extreme-ip-lookup.com/json/{0}".format(user_ip[args])).read().decode("utf-8").replace("\n",""))
             a = ("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Ip info</b><f x10FFFFFF='1'>]<br/>User : <f x10"+color(user.name)+"='1'>"+args+"<br/><f x10FFFFFF='1'>Ip : <f x10"+color(user.name)+"='1'>hide <br/><f x10FFFFFF='1'>Country : <f x10"+color(user.name)+"='1'>"+free["country_name"]+" - "+free["region_code"]+"<br/><f x10FFFFFF='1'>City : <f x10"+color(user.name)+"='1'>"+free["city"]+"<br/><f x10FFFFFF='1'>Host : <f x10"+color(user.name)+"='1'>"+ip["as"]+"<br/><f x10FFFFFF='1'>Isp : <f x10"+color(user.name)+"='1'>"+ip["org"]+"<br/><f x10FFFFFF='1'>Timezone : <f x10"+color(user.name)+"='1'>"+ip["timezone"]+"<br/><f x10FFFFFF='1'>Coordinate (lat & long) : <f x10"+color(user.name)+"='1'>"+ex["lat"]+" & "+ex["lon"])
             room.message(a,True)
            except:
                room.message("<f x10FFFFFF='1'>The user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> has no registered ip",True)

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################ ADMIM ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

############################################################################# GS ######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "gs" and self.getAccess(room, user) >= 2:
          if not args:
             room.message("<f x10FFFFFF='1'>To do a google search <f x10FFFFFF='1'>(ex : <f x10"+color(user.name)+"='1'>#gs python<f x10FFFFFF='1'>)", True)
          else:
            room.message(gs(args), True)

############################################################################# GS ######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "gis" and self.getAccess(room, user) >= 2:
          if not args:
             room.message("<f x10FFFFFF='1'>To do a google search image <f x10FFFFFF='1'>(ex : <f x10"+color(user.name)+"='1'>#gis lolis<f x10FFFFFF='1'>)", True)

          else:
            room.message("<f x10FFFFFF='1'>Disable, erro in ch.py, google no act conexion to cmd, and bing restrict my ip.. sorry :| try fix but this hard to me... ~att <f x10"+color(user.name)+"='1'>lsabelita", True)

############################################################################# YOUTUBE ######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "yt" and self.getAccess(room, user) >= 2:
          if not args:
             room.message("<f x10FFFFFF='1'>To do a search on youtube <f x10FFFFFF='1'>(ex : <f x10"+color(user.name)+"='1'>#yt a7x stage<f x10FFFFFF='1'>)", True)
          else:
           len(args) > 0
           s_result = "";
           sarr = args;
           for i in range(0, len(sarr)):
             if(ord(sarr[i]) < 128):
                   s_result += sarr[i]
           site= "https://www.googleapis.com/youtube/v3/search?q=" + s_result.replace(" ", "%20")  + "&part=snippet&key=AIzaSyAig0iRsiSYnZ-Dc1VAKYF4lkVQkofjO8I"
           response = urlopen(site).read()
           json_response = json.loads(response.decode())
           if(len(json_response["items"]) > 0):
                video = json_response["items"][0]["id"]["videoId"]
                title = json_response["items"][0]["snippet"]["title"]
                uploader = json_response["items"][0]["snippet"]["channelTitle"]
                count = json_response["items"][0]["snippet"]["publishedAt"].replace("T", " | ").replace(".000Z", "").replace("-", "/")
                description = json_response["items"][0]["snippet"]["description"]
                room.message("<f x10000000='1'><br/>.<br/><br/><f x10"+color(user.name)+"='1'>https://www.youtube.com/watch?v="+video+"<f x10FFFFFF='1'><br/>Title : <f x10"+color(user.name)+"='1'>"+title+"<br/><f x10FFFFFF='1'>Channel : <f x10"+color(user.name)+"='1'>"+uploader+"<f x10FFFFFF='1'><br/>Time uploaded : <f x10"+color(user.name)+"='1'>"+count, True)

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################ CHATANGO ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "prof" or cmd == "profile" or cmd == "Prof" or cmd == "Profile":
          if not args:args=user.name
          try:
            args=args.lower()
            stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
            wl = args.lower() in ranks
            white = ""
            resp = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
            fap = bool('chat with' in resp.lower())
            fapper = ""
            crap, age = stuff.split('<span class="profile_text"><strong>Age:</strong></span></td><td><span class="profile_text">', 1)
            age, crap = age.split('<br /></span>', 1)
            crap, gender = stuff.split('<span class="profile_text"><strong>Gender:</strong></span></td><td><span class="profile_text">', 1)
            gender, crap = gender.split(' <br /></span>', 1)
            if fap == True:
              fapper += "<f x1033FF33='1'>Online"
            if fap == False:
              fapper += "<f x10FF0000='1'>Offline"
            if wl == True:
              lvl,by,tmp,cor = json.loads(ranks[args])
              white += "<f x10"+color(user.name)+"='1'>"+lvl
            if wl == False:
              white += "<f x10"+color(user.name)+"='1'>no registered"
            if gender == 'M':
                gender = 'Male'
            if gender == 'F':
                gender = 'Female'
            else:
                gender = '?'
            crap, location = stuff.split('<span class="profile_text"><strong>Location:</strong></span></td><td><span class="profile_text">', 1)
            location, crap = location.split(' <br /></span>', 1)
            crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
            mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
            mini=mini.replace("<img","<!")
            picture = '<a href="http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg</a>'
            prodata = '<f x10000000="1"><br/>.<f x10FFFFFF="1"><br/><br/>[<f x10'+color(user.name)+'="1"><b>Profile of '+args.lower()+'</b><f x10FFFFFF="1">]<br/><a href="http://chatango.com/fullpix?' + args + '" target="_blank">' + picture + '<br/>''<f x10FFFFFF="1">Name : <f x10'+color(user.name)+'="1">'+ args.capitalize() +'<br/><f x10FFFFFF="1">Age : <f x10'+color(user.name)+'="1">'+ age + ' <br/><f x10FFFFFF="1">Gender : <f x10'+color(user.name)+'="1">' + gender +  ' <br/><f x10FFFFFF="1">Location : <f x10'+color(user.name)+'="1">' +  location + '<br/><f x10FFFFFF="1">Rank : <f x10'+color(user.name)+'="1">' + white + ' <br/><f x10FFFFFF="1">Status : <f x10'+color(user.name)+'="1">'+ fapper +'<br/><f x10FFFFFF="1">Html : <f x10'+color(user.name)+'="1">http://ruby-hoax.rhcloud.com/profile/?user='+args
            room.message(prodata,True)
          except:
            room.message("<f x10"+color(user.name)+"='1'>"+args+" not found ")

############################################################################ BG ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "bgtime" and self.getAccess(room, user) >= 2: 
             if not args:args=user.name
             args=args.lower()
             try:
                 a = user.name
                 b = user.name
                 x = "http://fp.chatango.com/profileimg/%s/%s/%s/msgbg.xml" % (args[0], args[1], args)
                 img = "http://fp.chatango.com/profileimg/%s/%s/%s/msgbg.jpg" % (args[0], args[1], args)
                 data = urllib.request.urlopen(x).read().decode()
                 data = dict([x.replace('"', '').split("=") for x in re.findall('(\w+=".*?")', data)[1:]])
                 a = ("<br/><f x10FFFFFF='1'>Img transparency : <f x10"+color(a)+"='1'>"+data["ialp"]+"%"+"<br/><f x10FFFFFF='1'>Bg transparency : <f x10"+color(a)+"='1'>"+data["bgalp"]+"%"+"<br/><f x10FFFFFF='1'>Bg color : <f x10"+color(a)+"='1'>"+data["bgc"]+ " <f x10FFFFFF='1'>[<f x10"+data["bgc"]+"='1'>▇▇▇▇<f x10FFFFFF='1'>]<br/><f x10FFFFFF='1'>Img position : <f x10"+color(a)+"='1'>"+data["align"].replace("br", "bottom right").replace("bl", "bottom left").replace("tl", "top left").replace("tr", "top right")+"<br/><f x10FFFFFF='1'>Use image : <f x10"+color(a)+"='1'>"+data["useimg"].replace("0", "no").replace("1", "yes"))
                 if len(args.split(" ", -1)) != 1:
                    return
                 if len(args) == 1:
                    f_args, s_args = args, args
                 if len(args) > 1:
                    f_args, s_args = args[0], args[1]
                 def getBgtime(user):
                     expired = True
                     url = ("http://st.chatango.com/profileimg/" + f_args + "/" + s_args + "/" + args + "/mod1.xml")
                     f = urllib.request.urlopen(url)
                     data = f.read().decode("utf-8")
                     e = ET.XML(data)
                     bg = e.findtext("d")
                     bg = int(urllib.request.unquote(bg))
                     if bg - int(time.time()) < 0:
                       total_seconds = int(time.time())-bg
                     else:
                       total_seconds = bg-int(time.time())
                       expired = False
                     MINUTE  = 60
                     HOUR    = MINUTE * 60
                     DAY     = HOUR * 24
                     days    = int( total_seconds / DAY )
                     hours   = int( ( total_seconds % DAY ) / HOUR )
                     minutes = int( ( total_seconds % HOUR ) / MINUTE )
                     seconds = int( total_seconds % MINUTE )
                     string = ""
                     if days > 0 or days < 0:
                         string += str(days) + "" + (days == 1 and "d" or "d" ) + ", "
                     if len(string) > 0 or hours > 0:
                         string += str(hours) + "" + (hours == 1 and "h" or "h" ) + ", "
                     if len(string) > 0 or minutes > 0:
                         string += str(minutes) + "" + (minutes == 1 and "m" or " m" ) + ", "
                     string += str(seconds) + "" + (seconds == 1 and "s" or "s" )
                     timeLeft =str(datetime.datetime.fromtimestamp(int(bg)).strftime("%I:%M:%S %p %d/%m/%Y (GMT - 3)"))

                     if expired == True:
                       return "<br/>"+img+"<br/><f x10FFFFFF='1'>User : <f x10"+color(b)+"='1'>"+args+"<f x10FFFFFF='1'><br/>Status : <f x10FF0000='1'>expired <br/><f x10FFFFFF='1'>Time expired : <f x10"+color(b)+"='1'>"+string+"<f x10FFFFFF='1'> (expired on <f x10"+color(b)+"='1'>"+timeLeft+"<f x10FFFFFF='1'>)"+a
                     if expired == False:
                       return "<br/>"+img+"<br/><f x10FFFFFF='1'>User : <f x10"+color(b)+"='1'>"+args+"<f x10FFFFFF='1'><br/>Status : <f x1033FF33='1'>not expired <br/><f x10FFFFFF='1'>Time remaining : <f x10"+color(b)+"='1'>"+string+"<f x10FFFFFF='1'> (will end up in <f x10"+color(b)+"='1'>"+timeLeft+"<f x10FFFFFF='1'>)"+a
                 return   room.message("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(b)+"='1'><b>Background</b><f x10FFFFFF='1'>] "+getBgtime(args), True)
             except:
                  room.message("<f x10FFFFFF='1'>This user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> never had premium.",True)

############################################################################ CSO ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "cso" and self.getAccess(room, user) >= 2: 
         if not args:
           room.message("Type <f x10"+color(user.name)+"='1'>#cso + username", True)
         else:
           offline = None
           url = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
           if not "buyer" in url:
             room.message("<f x10FFFFFF='1'>Hi, are you sure this user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> really exists?", True)
           else:
             url2 = urlreq.urlopen("http://"+args+".chatango.com").readlines()
             for line in url2:
               line = line.decode('utf-8')
               if "leave a message for" in line.lower():
                 offline = True
             if offline:
               room.message("<f x10FFFFFF='1'>The user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is <f x10FF0000='1'>offline", True)
             if not offline:
               room.message("<f x10FFFFFF='1'>The user <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is <f x1033FF33='1'>online", True)

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################ FUN ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

############################################################################ UD ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "ud" and self.getAccess(room, user) >= 2:
                nword=args.replace(" ","+")
                ndata= urlreq.urlopen("http://www.urbandictionary.com/define.php?term="+nword)
                nread= str(ndata.read())
                if "no-results" in nread:
                    room.message("<f x10FFFFFF='1'>The word <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> is not defined, such as setting it at <f x10"+color(user.name)+"='1'>http://www.urbandictionary.com", True)
                else:
                    trash , nclean=nread.split('<div class="meaning">', 1)
                    nclean , trash=nclean.split("</div>",1)
                    trash , aclean=nread.split('<div class="example">', 1)
                    aclean , trash=aclean.split("</div>",1)
                    trash , bclean=nread.split('<div class="contributor">', 1)
                    bclean , trash=bclean.split("</div>",1)
                    room.message("<f x10FFFFFF='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(user.name)+"='1'><b>Urban Dictionary</b><f x10FFFFFF='1'>]<br/> Word : <f x10"+color(user.name)+"='1'>"+args.capitalize()+"<br/><f x10FFFFFF='1'>Meaning : <f x10"+color(user.name)+"='1'>"+nclean.replace("\\'>\\n"," ").replace("\\n", " ").replace("\\r"," ").replace("<br/>"," ").replace("<br>"," ")+"<br/><f x10FFFFFF='1'>Example : <f x10"+color(user.name)+"='1'>"+aclean.replace("\\'>\\n"," ").replace("\\n", " ").replace("\\r"," ").replace("<br/>"," ").replace("<br>"," ").replace("c\xc3\xba","ú")+"<br/><f x10FFFFFF='1'>Defined by : <f x10"+color(user.name)+"='1'>"+bclean.replace("\\'>\\n"," ").replace("\\n", " ").replace("\\r"," ").replace("<br/>",",").replace("<br>"," ").replace("by"," "), True)

############################################################################ FUN ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "userlist" and self.getAccess(room, user) >= 2:
          a = len([ser.name for ser in room._getUserlist(1)])
          room.message("<f x10000000='1'>Current <f x10CC9E8F='1'>"+str(a)+"<f x10000000='1'> users of this room : <f x10CC9E8F='1'>"+", ".join([ser.name for ser in room._getUserlist(1)]), True)

############################################################################ FUN ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

  
        if cmd == "ping" and self.getAccess(room, user) >= 2:
         if room.name not in noping:
            room.message("@"+" @".join([ser.name for ser in room._getUserlist(1)]), True)
         else:
            room.message("<f x10000000='1'>Comand is not available in this chat, possibly blocked", True)

############################################################################ FUN ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "pm" and self.getAccess(room, user) >= 2:
         if room.name not in nopm:
            name, msg = args.split(" ", 1)
            if name == "chatango" or name == "koqu":
               room.message("<f x10000000='1'>You can not send message to <f x10CC9E8F='1'>"+name, True) 
            else:
              self.pm.message(ch.User(name), "[PM] Message : "+msg+" sent by "+user.name)
              room.message("<f x10000000='1'>The message has been sent to <f x10CC9E8F='1'>"+name+"<f x10000000='1'> inbox" , True)
         else:
            room.message("<f x10000000='1'>Command is not available in this chat, possibly blocked", True)


############################################################################ FUN ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "hc" and self.getAccess(room, user) >= 2:
              try:
                if args == "aries":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/aries")
                   x = "http://delas.ig.com.br/horoscopo/aries"
                if args == "taurus":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/touro")
                   x = "http://delas.ig.com.br/horoscopo/touro"
                if args == "gemini":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/gemeos")
                   x = "http://delas.ig.com.br/horoscopo/gemeos"
                if args == "cancer":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/cancer")
                   x = "http://delas.ig.com.br/horoscopo/cancer"
                if args == "leo":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/leao")
                   x = "http://delas.ig.com.br/horoscopo/leao"
                if args == "virgo":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/virgem")
                   x = "http://delas.ig.com.br/horoscopo/virgem"
                if args == "libra":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/libra")
                   x = "http://delas.ig.com.br/horoscopo/libra"
                if args == "scorpio":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/escorpiao")
                   x = "http://delas.ig.com.br/horoscopo/escorpiao"
                if args == "sagittarius":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/sagitario")
                   x = "http://delas.ig.com.br/horoscopo/sagitario"
                if args == "capricorn":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/capricornio")
                   x = "http://delas.ig.com.br/horoscopo/capricornio"
                if args == "aquarius":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/aquario")
                   x = "http://delas.ig.com.br/horoscopo/aquario"
                if args == "pisces":
                   ndata= urlreq.urlopen("http://delas.ig.com.br/horoscopo/peixes")
                   x = "http://delas.ig.com.br/horoscopo/peixe"

                nread= str(ndata.read().decode('utf-8'))
                if "no-results" in nread:
                    room.message("<f x10FFFFFF='1'>The word <f x10FFFFFF='1'>"+args+"<f x10FFFFFF='1'> is not defined, such as setting it at <f x10FFFFFF='1'>http://www.urbandictionary.com", True)
                else:
                    trash , nclean=nread.split('<p class="CHE17712-texto">', 1)
                    nclean , trash=nclean.split("</p>",1)
                    a = nclean[:170].replace("ê","e").replace("ã","a").replace("é","e").replace("ú","u").replace("\\'>\\n"," ").replace("\\n", " ").replace("\\r"," ").replace("<br/>"," ").replace("<br>"," ")
                    b = (__import__("gt").teng(a))
                    c = user.name
                    room.message("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(c)+"='1'><b>Horoscope</b><f x10FFFFFF='1'>]<br/>Sign : <f x10"+color(c)+"='1'>"+args+"<f x10FFFFFF='1'><br/><f x10FFFFFF='1'>Phrase : <f x10"+color(c)+"='1'>"+b+"...<br/><f x10FFFFFF='1'>Full phrase : <f x10"+color(c)+"='1'>"+x, True)
              except:
                  room.message("<f x10FFFFFF='1'>The sign <f x10"+color(user.name)+"='1'>"+args+"<f x10FFFFFF='1'> does not exist try to use one from the list next :<f x10"+color(user.name)+"='1'> aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces", True) 

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################ TRADUTOR ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

############################################################################ TC ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "tc" and self.getAccess(room, user) >= 2:
          if args:
            args = quote(args)
            headers = {}
            headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|ZH", headers = headers)
            resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
            data = json.loads(resp)
            translation = data['responseData']['translatedText']
            if not isinstance(translation, bool):
              room.message("<f x10FFFFFF='1'>Chinese : <f x10"+color(user.name)+"='1'>"+translation.replace("PLEASE SELECT TWO DISTINCT LANGUAGES", "<f x10FFFFFF='1'>Dear <f x10FFFFFF='1'>"+user.name+"<f x10FFFFFF='1'>, please select two distinct languages"), True)
            else:
              matches = data['matches']
              for match in matches:
               if not isinstance(match['translation'], bool):
                next_best_match = match['translation']
                break
          else:
            room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, to translate a text or phrase to the chinese type <f x10"+color(user.name)+"='1'>#"+cmd+" + text<f x10FFFFFF='1'>, remember the translator has a limitation of 200 characters", True) 

############################################################################ TP ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "tp" and self.getAccess(room, user) >= 2:
          if args:
            args = quote(args)
            headers = {}
            headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|PT", headers = headers)
            resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
            data = json.loads(resp)
            translation = data['responseData']['translatedText']
            if not isinstance(translation, bool):
              room.message("<f x10FFFFFF='1'>Portuguese : <f x10"+color(user.name)+"='1'>"+translation.replace("PLEASE SELECT TWO DISTINCT LANGUAGES", "<f x10FFFFFF='1'>Dear <f x10FFFFFF='1'>"+user.name+"<f x10FFFFFF='1'>, please select two distinct languages"), True)
            else:
              matches = data['matches']
              for match in matches:
               if not isinstance(match['translation'], bool):
                next_best_match = match['translation']
                break
          else:
            room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, to translate a text or phrase to the portuguese type <f x10"+color(user.name)+"='1'>#"+cmd+" + text<f x10FFFFFF='1'>, remember the translator has a limitation of 200 characters", True) 

############################################################################ TJ ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "tj" and self.getAccess(room, user) >= 2:
          if args:
            args = quote(args)
            headers = {}
            headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|JA", headers = headers)
            resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
            data = json.loads(resp)
            translation = data['responseData']['translatedText']
            if not isinstance(translation, bool):
              room.message("<f x10FFFFFF='1'>Japonese : <f x10"+color(user.name)+"='1'>"+translation.replace("PLEASE SELECT TWO DISTINCT LANGUAGES", "<f x10FFFFFF='1'>Dear <f x10FFFFFF='1'>"+user.name+"<f x10FFFFFF='1'>, please select two distinct languages"), True)
            else:
              matches = data['matches']
              for match in matches:
               if not isinstance(match['translation'], bool):
                next_best_match = match['translation']
                break
          else:
            room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, to translate a text or phrase to the japonese type <f x10"+color(user.name)+"='1'>#"+cmd+" + text<f x10FFFFFF='1'>, remember the translator has a limitation of 200 characters", True) 

############################################################################ TJ ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "ts" and self.getAccess(room, user) >= 2:
          if args:
            args = quote(args)
            headers = {}
            headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|ES", headers = headers)
            resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
            data = json.loads(resp)
            translation = data['responseData']['translatedText']
            if not isinstance(translation, bool):
              room.message("<f x10FFFFFF='1'>Spanish : <f x10"+color(user.name)+"='1'>"+translation.replace("PLEASE SELECT TWO DISTINCT LANGUAGES", "<f x10FFFFFF='1'>Dear <f x10FFFFFF='1'>"+user.name+"<f x10FFFFFF='1'>, please select two distinct languages"), True)
            else:
              matches = data['matches']
              for match in matches:
               if not isinstance(match['translation'], bool):
                next_best_match = match['translation']
                break
          else:
            room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, to translate a text or phrase to the spanish type <f x10"+color(user.name)+"='1'>#"+cmd+" + text<f x10FFFFFF='1'>, remember the translator has a limitation of 200 characters", True) 

############################################################################ TJ ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "te" and self.getAccess(room, user) >= 2:
          if args:
            args = quote(args)
            headers = {}
            headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|EN", headers = headers)
            resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
            data = json.loads(resp)
            translation = data['responseData']['translatedText']
            if not isinstance(translation, bool):
              room.message("<f x10FFFFFF='1'>English : <f x10"+color(user.name)+"='1'>"+translation.replace("PLEASE SELECT TWO DISTINCT LANGUAGES", "<f x10FFFFFF='1'>Dear <f x10FFFFFF='1'>"+user.name+"<f x10FFFFFF='1'>, please select two distinct languages"), True)
            else:
              matches = data['matches']
              for match in matches:
               if not isinstance(match['translation'], bool):
                next_best_match = match['translation']
                break
          else:
            room.message("<f x10FFFFFF='1'>Dear <f x10"+color(user.name)+"='1'>"+user.name+"<f x10FFFFFF='1'>, to translate a text or phrase to the english type <f x10"+color(user.name)+"='1'>#"+cmd+" + text<f x10FFFFFF='1'>, remember the translator has a limitation of 200 characters", True) 

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################ SN ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

############################################################################ SN ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "sn" and self.getAccess(room, user) >= 2:
          b = user.name
          tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
          if not args:
            room.message("<f x10FFFFFF='1'>To send a message to the user type <f x10FFFFFF='1'>#sn + username + text",True)
          else:
            args.lower()
            untuk, pesan = args.split(" ", 1)
            if untuk not in ranks:
               room.message("<f x10FFFFFF='1'>The user <f x10"+color(b)+"='1'>"+(untuk)+"<f x10FFFFFF='1'> is registered?" , True)
            else:
              untuk, pesan = args.split(" ", 1)
              if untuk in inboxs:
                inboxs[untuk].append([user.name, pesan, tmp])
                f = open('files/inbox.txt', "w")
                f.write(str(inboxs))
                f.close
                if untuk not in notif:
                  notif.append(untuk)
                  f = open("files/notif.txt","w")
                  f.write("\n".join(notif))
                  f.close
                else:pass
              else:
                inboxs.update({untuk:[]})
                inboxs[untuk].append([user.name, pesan, tmp])
                f = open('files/inbox.txt', "w")
                f.write(str(inboxs))
                f.close
                if untuk not in notif:
                  notif.append(untuk)
                  f = open("files/notif.txt","w")
                  f.write("\n".join(notif))
                  f.close
                else:pass
              room.message("<f x10FFFFFF='1'>The message has been sent to <f x10"+color(b)+"='1'>"+(untuk)+"<f x10FFFFFF='1'> inbox" , True)

############################################################################ RN ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd =="rn" and self.getAccess(room, user) >= 2:
            b = user.name
            if user.name not in inboxs:
              inboxs.update({user.name:[]})
            user=user.name.lower()
            if len(inboxs[user]) > 0:
              messg = inboxs[user][0]
              dari, pesen, timey = messg
              room.message("<f x10FFFFFF='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(b)+"='1'><b>Inbox</b><f x10FFFFFF='1'>] <br/>From : <f x10"+color(b)+"='1'>"+dari+"<br/><f x10FFFFFF='1'>Time : <f x10"+color(b)+"='1'>"+timey+" (GMT - 3) <br/><f x10FFFFFF='1'>Message : <f x10"+color(b)+"='1'>"+pesen, True)
              try:
                del inboxs[user][0]
                f = open('files/inbox.txt', "w")
                f.write(str(inboxs))
                f.close
              except:pass
            else:room.message("<f x10"+color(b)+"='1'>"+user+"<f x10FFFFFF='1'> you dont have any messages in your inbox" , True)

############################################################################ DF ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "define" or cmd == "df" and len(args) and self.getAccess(room, user) >= 2:
           b = user.name
           tmp = str(datetime.datetime.fromtimestamp(int(time.time()-0)).strftime("%I:%M:%S %p %d/%m/%Y"))
           try:
             try:
               word, definition = args.split(" + ",1)
               word = word.lower()
             except:
               word = args
               definition = ""
             if len(word.split()) > 4:
               room.message("<f x10FFFFFF='1'>Fail", True)
               return
             if len(definition) > 0:
               if word in dfs:
                 room.message("<f x10FFFFFF='1'>My master <f x10"+color(b)+"='1'>"+(user.name)+"<f x10FFFFFF='1'>this is already set", True)
               else:
                 dfs[word] = json.dumps([definition, user.name, tmp])
                 f =open("files/df.txt", "w")
                 for word in dfs:
                   definition, name, tmp = json.loads(dfs[word])
                   f.write(json.dumps([word, definition, name, tmp])+"\n")
                 f.close
                 room.message("<f x10FFFFFF='1'>The word has been defined", True)

             else:
              if word in dfs:
                 definition, name, tmp = json.loads(dfs[word])
                 room.message("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>[<f x10"+color(b)+"='1'><b>Dictionary</b><f x10FFFFFF='1'>] <br/>Word :  <f x10"+color(b)+"='1'>"+word+" <br/><f x10FFFFFF='1'>Definition :  <f x10"+color(b)+"='1'>"+definition+"<br/><f x10FFFFFF='1'>Defined by  <f x10"+color(b)+"='1'>"+name+"<br/><f x10FFFFFF='1'>Time : <f x10"+color(b)+"='1'>"+tmp,True)
              else:
                 room.message("<f x10"+color(b)+"='1'>"+args+"<f x10FFFFFF='1'> is not defined", True)
           except:
             room.message("<f x10FFFFFF='1'>There's something wrong", True)

############################################################################ UDF ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "undf" and len(args) > 0 and self.getAccess(room, user) >= 2:
           b = user.name
           try:
             word = args
             if word in dfs:
               definition, name, tmp = json.loads(dfs[word])
               if name == user.name or self.getAccess(room, user) >= 4:
                 del dfs[word]
                 f =open("files/df.txt", "w")
                 for word in dfs:
                   definition, name, tmp = json.loads(dfs[word])
                   f.write(json.dumps([word, definition, name, tmp])+"\n")
                 f.close
                 room.message("<f x10FFFFFF='1'>Definition <f x10"+color(b)+"='1'>"+args+"<f x10FFFFFF='1'> has been removed from the database",True)
                 return
               else:
                 room.message("<f x10FFFFFF='1'>Only the user who has set or rank greater than 4 can remove settings",True)

                 return
             else:
                room.message("<f x10"+color(b)+"='1'>"+args+"<f x10FFFFFF='1'> is not defined", True)
           except:
             room.message("<f x10FFFFFF='1'>null", True)
             return

############################################################################ UDF ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "mydf" and self.getAccess(room, user) >= 2:
           b = user.name
           if not args:args=user.name
           arr = []
           for i in dfs:
             if args in dfs[i]:
               arr.append(i)
           if len(arr) > 0:
             room.message("<f x10FFFFFF='1'>Word (<f x10"+color(b)+"='1'>"+str(len(arr))+"<f x10FFFFFF='1'>) :  <f x10"+color(b)+"='1'>%s"% (', '.join(sorted(arr))), True)
           else:
             room.message("<f x10"+color(b)+"='1'>"+args.title()+" has no definite words", True)

        if cmd == "seen" and self.getAccess(room, user) >= 2:
         b = "<f x10"+color(user.name)+"='1'>"
         c = user.name
         if not args:
           room.message("<f x10FFFFFF='1'>Type <f x10"+color(c)+"='1'>#seen + user.name", True)
         else:
            nama = args
            if nama in hist:
                case, timey, ruang, bodi = hist[nama]
                string = ""
                timey = time.time() - int(timey)
                minute = 60
                hour = minute * 60
                day = hour * 24
                days =  int(timey / day)
                hours = int((timey % day) / hour)
                minutes = int((timey % hour) / minute)
                seconds = int(timey % minute)
                if days > 0:
                  string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                if len(string) > 0 or hours > 0:
                  string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                if len(string) > 0 or minutes > 0:
                  string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + " and "
                string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                if case == 1:
                  hasil = ("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>["+b+"<b>Seen</b><f x10FFFFFF='1'>]<br/>User : "+b+""+nama+" <br/><f x10FFFFFF='1'>Status : "+b+"join <br/><f x10FFFFFF='1'>Room : "+b+""+ruang+" <br/><f x10FFFFFF='1'>Time : "+b+""+string+" ago")
                if case == 2:
                  hasil = ("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>["+b+"<b>Seen</b><f x10FFFFFF='1'>]<br/>User : "+b+""+nama+" <br/><f x10FFFFFF='1'>Status : "+b+"leave <br/><f x10FFFFFF='1'>Room : "+b+""+ruang+" <br/><f x10FFFFFF='1'>Time : "+b+""+string+" ago")
                if case == 3:
                  hasil = ("<f x10000000='1'><br/>.<f x10FFFFFF='1'><br/><br/>["+b+"<b>Seen</b><f x10FFFFFF='1'>]<br/>User : "+b+""+nama+" <br/><f x10FFFFFF='1'>Status : "+b+"posting <br/><f x10FFFFFF='1'>Text : "+b+""+bodi+" <br/><f x10FFFFFF='1'>Room : "+ruang+" <br/><f x10FFFFFF='1'>Time : "+b+""+string+" ago")

                room.message(hasil, True)
            else:
              room.message("I haven't seen such user.")

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd == "cmds":
         if self.getAccess(room, user) == 2:
           room.message("<f x10FFFFFF='1'>Cmds <f x10"+color(user.name)+"='1'>human (2) <f x10FFFFFF='1'>: <f x10"+color(user.name)+"='1'>lockstatus, rooms, stats, lag, server, wl, staff, rank, pm, ping, say, rb, rbc, ng, ngc, gs, gis, yt , profile, bgtime, cso, ud, hc, (tc,tj,tp,ts.te), sn, rn, df, undf, mydf", True)
         if self.getAccess(room, user) == 3:
           room.message("<f x10FFFFFF='1'>Cmds <f x10"+color(user.name)+"='1'>angel (3) <f x10FFFFFF='1'>: <f x10"+color(user.name)+"='1'>lockstatus, rooms, stats, lag, server, wl, staff, rank, pm, ping, say, rb, rbc, ng, ngc, gs, gis, yt , profile, bgtime, cso, ud, hc, (tc,tj,tp,ts.te), sn, rn, df, undf, mydf, lock, unlock", True)
         if self.getAccess(room, user) == 4:
           room.message("<f x10FFFFFF='1'>Cmds <f x10"+color(user.name)+"='1'>archangel (4) <f x10FFFFFF='1'>: <f x10"+color(user.name)+"='1'>lockstatus, rooms, stats, lag, server, wl, staff, rank, pm, ping, say, rb, rbc, ng, ngc, gs, gis, yt , profile, bgtime, cso, ud, hc, (tc,tj,tp,ts.te), sn, rn, df, undf, mydf, lock, unlock, join, leave, ban, unban, mods, sleep, bl, unbl", True)
         if self.getAccess(room, user) == 5:
           room.message("<f x10FFFFFF='1'>Cmds <f x10"+color(user.name)+"='1'>querubin (5) <f x10FFFFFF='1'>: <f x10"+color(user.name)+"='1'>lockstatus, rooms, stats, lag, server, wl, staff, rank, pm, ping, say, rb, rbc, ng, ngc, gs, gis, yt , profile, bgtime, cso, ud, hc, (tc,tj,tp,ts.te), sn, rn, df, undf, mydf, lock, unlock, join, leave, ban, unban, mods, sleep, bl, unbl", True)
         if self.getAccess(room, user) == 6:
           room.message("<f x10FFFFFF='1'>Cmds <f x10"+color(user.name)+"='1'>serafin (6) <f x10FFFFFF='1'>: <f x10"+color(user.name)+"='1'>lockstatus, rooms, stats, lag, server, wl, staff, rank, pm, ping, say, rb, rbc, ng, ngc, gs, gis, yt , profile, bgtime, cso, ud, hc, (tc,tj,tp,ts.te), sn, rn, df, undf, mydf, lock, unlock, join, leave, ban, unban, mods, sleep, bl, unbl, setrank", True)
         if self.getAccess(room, user) == 7:
           room.message("<f x10FFFFFF='1'>Cmds <f x10"+color(user.name)+"='1'>god (7) <f x10FFFFFF='1'>: <f x10"+color(user.name)+"='1'>lockstatus, rooms, stats, lag, server, wl, staff, rank, pm, ping, say, rb, rbc, ng, ngc, gs, gis, yt , profile, bgtime, cso, ud, hc, (tc,tj,tp,ts.te), sn, rn, df, undf, mydf, lock, unlock, join, leave, ban, unban, mods, sleep, bl, unbl, log, eval, exec, setrank, disable, enable", True)

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

        if cmd.lower() == "not" and self.getAccess(room, user) >= 1:
          b = user.name
          if args == "yt":
             user=user.name
             yt1,join1,leave1 = json.loads(notifics[user])
             if yt1 == "enable":
               yt = "disable"
               join = join1
               leave = leave1
               notifics[user] = json.dumps([yt,join,leave])
               room.message("<f x10FFFFFF='1'>Notification youtube has been <f x10"+color(b)+"='1'>"+yt,True)
               f = open("files/notific.txt", "w")
               for user in notifics:
                 yt,join,leave = json.loads(notifics[user])
                 f.write(json.dumps([user,yt,join,leave])+"\n")
               f.close() 
             else:
               yt = "enable"
               join = join1
               leave = leave1
               notifics[user] = json.dumps([yt,join,leave])
               room.message("<f x10FFFFFF='1'>Notification youtube has been <f x10"+color(b)+"='1'>"+yt,True)
               f = open("files/notific.txt", "w")
               for user in notifics:
                 yt,join,leave = json.loads(notifics[user])
                 f.write(json.dumps([user,yt,join,leave])+"\n")
               f.close() 

#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
############################################################################ ADMIM ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################
#################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################33333333333333##############################################################################################

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

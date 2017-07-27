############### IMPORTS #######################
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
############### IMPORTS#######################

def ti(args):
  args = quote(args)
  headers = {}
  headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|ID", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def tp(args):
  args = quote(args)
  headers = {}
  headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|PT", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def tj(args):
  args = quote(args)
  headers = {}
  headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|JA", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def te(args):
  args = quote(args)
  headers = {}
  headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|ES", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def teng(args):
  args = quote(args)
  headers = {}
  headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|EN", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def tc(args):
  args = quote(args)
  headers = {}
  headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=|ZH", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def tl(args):
  url = "http://ws.detectlanguage.com/0.2/detect?q="+"+".join(quote(args).split())+"&key=demo"
  headers = {}
  headers['user-Agent'] = "Mozilla/5.0 (x11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request(url, headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('  ','').replace(' Subtitle Indonesia','').replace('-subtitle-indonesia','')
  res = re.findall('"language":"(.*?)"', resp)
  newset = list()
  num = 1
  return "".join(res).upper().replace("PT", "Portuguese")

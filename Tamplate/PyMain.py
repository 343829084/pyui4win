# coding=gbk
#__author__ = huqinghua
import string
import os
import time

from PyUI import *
from PyFrameBase import *
from CommonUtil import *

def PyAppInit():
    CommonUtils.SaveExePath()
    pyFrameObj = PyFrameCreator()
    obj = pyFrameObj.CreateForm(0, 'MainFrame', 'MainFrame', 'pyui4win����ʾ��')
    pyFrameObj.Show()
    CPaintManagerUI.MessageLoop()
    #ģ̬�Ի���
    #obj = pyFrameObj.CreateDialog(0, 'MainFrame', 'MainFrame', 'pyui4win����ʾ��')
    #pyFrameObj.ShowModal()
    
def PyAppInit4Debug():
    CommonUtils.SaveExePath()
    pyFrameObj = PyFrameCreator()
    obj = pyFrameObj.CreateForm(0, 'MainFrame', 'MainFrame', 'pyui4win����ʾ��')
    pyFrameObj.Show()
    CPaintManagerUI.MessageLoop()
    #ģ̬�Ի���
    #obj = pyFrameObj.CreateDialog(0, 'MainFrame', 'MainFrame', 'pyui4win����ʾ��')
    #pyFrameObj.ShowModal()
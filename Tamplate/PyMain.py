# coding=gbk
#__author__ = huqinghua
import string
import os
import time

from PyUI import *
from MsgBox import *
from PyFrameBase import *
import UICommon
from CommonUtil import CommonUtils

def PyAppInit():
    CommonUtils.SaveExePath()
    pyFrameObj = PyFrameCreator()
    obj = pyFrameObj.CreateForm(0, 'MainFrame', 'MainFrame', 'pyui4win����ʾ��')
    pyFrameObj.Show()
    CPaintManagerUI.MessageLoop()
    #ģ̬�Ի���
    #obj = pyFrameObj.CreateDialog(0, 'MainFrame', 'MainFrame', 'pyui4win����ʾ��')
    #pyFrameObj.ShowModal()
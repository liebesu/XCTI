#coding:utf-8
import os
from lib.common.logo import logo
from lib.common.constants import PD_UPDATE_ROOT
from lib.PD_update.md5_update import md5_update
from lib.common.prepare import make_new_floder
def create_diectory():
    '''创建所需文件夹'''
    if os.path.exists(os.path.join(PD_UPDATE_ROOT,"data")):
        pass
    else:
        os.makedirs(os.path.join(PD_UPDATE_ROOT,"data"))
        
if __name__=="__main__":
    logo()
    make_new_floder()
    md5_update()
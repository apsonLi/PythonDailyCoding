# -*- coding: utf-8 -*-
__author__ = '''
       ________  ________   __
      / /  _/  |/  /  _/ | / /
 __  / // // /|_/ // //  |/ / 
/ /_/ // // /  / // // /|  /  
\____/___/_/  /_/___/_/ |_/ '''


class JmError(BaseException):
    pass


class DBError(JmError):
    pass


class DatabaseNameError(DBError):
    pass


class ConnectDatabaseError(DBError):
    pass


class UnknownError(DBError):
    pass


class NetError(JmError):
    pass

#!/usr/bin/python
# -*- coding: utf-8 -*-

# persistant Objects
# ==================
# this module provides a class that serialises
# its attributes as they are set and gets them
# from the backend when requested. this should
# create fully persistant objects... I hope.



import sqlite3
import json
import pickle


class Persistent(object):
    """
    Base persistence object
    =======================
    this is the general object
    """
    
    class backends():
        SQLite3 = 'sqlite3'
        Pickle = 'pickle'
    
    def __init__(self, Backend=backends.SQLite3, storeFile='./'+__name__+'.prs'):
        if Backend in self.backends:
            self._backend = Backend
        else:
            return None
        self._storeFile = storeFile
    
    def __getattribute__(self, name):
        '''grabs the data from the storage backend'''
        if self._backend == self.backends.Pickle:
            self._getPickle(name, value)
        elif self._backend == self.backends.SQLite3:
            self._getSQLite3(name, value)
        else:
            return None
    
    def _getSQLite3(self, name, value):
        '''unserialise data from the SQLite3 backend'''
        pass

    def _getPickle(self, name, value):
        '''unserialise data from a pickle file'''
        pass
    
    def __setattr__(self, name, value):
        '''serializes the data in the selected format to the selected backend'''
        if self._backend = self.backends.Pickle:
            self._setPickle(name, value)
        elif self._backend = self.backends.sqlite3:
            self._setSQLite3(name, value)
        else:
            return None
    
    def _setSQLite3(self, name, value):
        '''serialise data to the SQLite3 backend'''
        pass
    
    def _setPickle(self, name, value):
        '''serialise the data to a pickle file'''
        pass
    
    def __delattr__(self, name):
        '''deletes an attribute from the backend'''
        pass




if __name__ == '__main__':
    pass

#
# Copyright (c) 2013 - 2016 MasterCard International Incorporated
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

"""
Config File for MasterCard APIs Core SDK
"""

from constants import Constants

class Config(object):
    """
    Configurable options for MasterCard APIs Core SDK
    """

    sandbox         = True
    debug           = False
    authentication  = None
    localhost       = False

    def __init__(self):
        pass

    @classmethod
    def setDebug(cls,debug):
        cls.debug = debug

    @classmethod
    def isDebug(cls):
        return cls.debug

    @classmethod
    def setSandbox(cls,sandbox):
        cls.sandbox = sandbox

    @classmethod
    def isSandbox(cls):
        return cls.sandbox

    @classmethod
    def setLocal(cls,local):
        cls.localhost = local

    @classmethod
    def isLocal(cls):
        return cls.localhost

    @classmethod
    def setAuthentication(cls,authentication):
        cls.authentication = authentication

    @classmethod
    def getAuthentication(cls):
        return cls.authentication

    @classmethod
    def getAPIBaseURL(cls):
        if cls.localhost:
            return Constants.API_BASE_LOCALHOST_URL
        elif cls.sandbox:
            return Constants.API_BASE_SANDBOX_URL
        else:
            return Constants.API_BASE_LIVE_URL
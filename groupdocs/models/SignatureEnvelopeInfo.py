#!/usr/bin/env python
"""
Copyright 2012 GroupDocs.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class SignatureEnvelopeInfo:
    """
    
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'creationDateTime': 'str',
            'ownerShouldSign': 'bool',
            'recipients': 'list[SignatureEnvelopeRecipientInfo]',
            'status': 'int',
            'envelopeExpireTime': 'float',
            'reminderTime': 'float',
            'emailSubject': 'str',
            'statusDateTime': 'str',
            'id': 'str',
            'stepExpireTime': 'float',
            'emailBody': 'str',
            'documentsCount': 'float',
            'orderedSignature': 'bool',
            'documentsPages': 'float',
            'ownerGuid': 'str',
            'name': 'str'

        }


        self.creationDateTime = None # str
        self.ownerShouldSign = None # bool
        self.recipients = None # list[SignatureEnvelopeRecipientInfo]
        self.status = None # int
        self.envelopeExpireTime = None # float
        self.reminderTime = None # float
        self.emailSubject = None # str
        self.statusDateTime = None # str
        self.id = None # str
        self.stepExpireTime = None # float
        self.emailBody = None # str
        self.documentsCount = None # float
        self.orderedSignature = None # bool
        self.documentsPages = None # float
        self.ownerGuid = None # str
        self.name = None # str
        

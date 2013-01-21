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
class FileSystemFolder:
    """
    
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'folder_count': 'int',
            'file_count': 'int',
            'id': 'float',
            'guid': 'str',
            'name': 'str',
            'access': 'str',
            'owner': 'UserInfo',
            'sharers': 'list[UserInfo]',
            'dir': 'bool',
            'modified_on': 'long',
            'created_on': 'long'

        }


        self.folder_count = None # int
        self.file_count = None # int
        self.id = None # float
        self.guid = None # str
        self.name = None # str
        self.access = None # str
        self.owner = None # UserInfo
        self.sharers = None # list[UserInfo]
        self.dir = None # bool
        self.modified_on = None # long
        self.created_on = None # long
        
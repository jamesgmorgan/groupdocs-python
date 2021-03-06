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
class GetCollaboratorsResult:
    """
    
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'documentGuid': 'str',
            'sessionGuid': 'str',
            'owner': 'ReviewerInfo',
            'collaborators': 'list[ReviewerInfo]',
            'shared_link_access_rights': 'int'

        }


        self.documentGuid = None # str
        self.sessionGuid = None # str
        self.owner = None # ReviewerInfo
        self.collaborators = None # list[ReviewerInfo]
        self.shared_link_access_rights = None # int
        

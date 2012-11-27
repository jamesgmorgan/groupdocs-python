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

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *
from groupdocs.FileStream import FileStream
from groupdocs.ApiClient import ApiException

class AntApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient
        self.__basePath = "https://api.groupdocs.com/v2.0"

    @property
    def basePath(self):
        return self.__basePath
    
    @basePath.setter
    def basePath(self, value):
        self.__basePath = value

    
    def CreateAnnotation(self, userId, fileId, body, **kwargs):
        """Create annotation

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            body, AnnotationInfo: annotation (required)
            
        Returns: CreateAnnotationResponse
        """
        if( userId == None or fileId == None or body == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'fileId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method CreateAnnotation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/files/{fileId}/annotations'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CreateAnnotationResponse')
        return responseObject
        
        
    def ListAnnotations(self, userId, fileId, **kwargs):
        """Get list of annotations

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            
        Returns: ListAnnotationsResponse
        """
        if( userId == None or fileId == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'fileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ListAnnotations" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/files/{fileId}/annotations'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ListAnnotationsResponse')
        return responseObject
        
        
    def DeleteAnnotation(self, userId, annotationId, **kwargs):
        """Delete annotation

        Args:
            userId, str: User GUID (required)
            annotationId, str: Annotation ID (required)
            
        Returns: DeleteAnnotationResponse
        """
        if( userId == None or annotationId == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'annotationId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteAnnotation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/annotations/{annotationId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('annotationId' in params):
            replacement = str(self.apiClient.toPathValue(params['annotationId']))
            resourcePath = resourcePath.replace('{' + 'annotationId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeleteAnnotationResponse')
        return responseObject
        
        
    def CreateAnnotationReply(self, userId, annotationId, body, **kwargs):
        """Create annotation reply

        Args:
            userId, str: User GUID (required)
            annotationId, str: Annotation ID (required)
            body, AnnotationReplyInfo: Reply (required)
            
        Returns: AddReplyResponse
        """
        if( userId == None or annotationId == None or body == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'annotationId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method CreateAnnotationReply" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/annotations/{annotationId}/replies'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('annotationId' in params):
            replacement = str(self.apiClient.toPathValue(params['annotationId']))
            resourcePath = resourcePath.replace('{' + 'annotationId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AddReplyResponse')
        return responseObject
        
        
    def EditAnnotationReply(self, userId, replyGuid, body, **kwargs):
        """Edit annotation reply

        Args:
            userId, str: User GUID (required)
            replyGuid, str: Reply GUID (required)
            body, str: Message (required)
            
        Returns: EditReplyResponse
        """
        if( userId == None or replyGuid == None or body == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'replyGuid', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method EditAnnotationReply" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/replies/{replyGuid}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('replyGuid' in params):
            replacement = str(self.apiClient.toPathValue(params['replyGuid']))
            resourcePath = resourcePath.replace('{' + 'replyGuid' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'EditReplyResponse')
        return responseObject
        
        
    def DeleteAnnotationReply(self, userId, replyGuid, **kwargs):
        """Delete annotation reply

        Args:
            userId, str: User GUID (required)
            replyGuid, str: Reply GUID (required)
            
        Returns: DeleteReplyResponse
        """
        if( userId == None or replyGuid == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'replyGuid']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteAnnotationReply" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/replies/{replyGuid}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('replyGuid' in params):
            replacement = str(self.apiClient.toPathValue(params['replyGuid']))
            resourcePath = resourcePath.replace('{' + 'replyGuid' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeleteReplyResponse')
        return responseObject
        
        
    def ListAnnotationReplies(self, userId, annotationId, after, **kwargs):
        """Get list of annotation replies

        Args:
            userId, str: User GUID (required)
            annotationId, str: Annotation ID (required)
            after, long: After (required)
            
        Returns: ListRepliesResponse
        """
        if( userId == None or annotationId == None or after == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'annotationId', 'after']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ListAnnotationReplies" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/annotations/{annotationId}/replies?after={after}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('after' in params):
            queryParams['after'] = self.apiClient.toPathValue(params['after'])
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('annotationId' in params):
            replacement = str(self.apiClient.toPathValue(params['annotationId']))
            resourcePath = resourcePath.replace('{' + 'annotationId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ListRepliesResponse')
        return responseObject
        
        
    def SetAnnotationCollaborators(self, userId, fileId, version, **kwargs):
        """Set annotation collaborators

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            version, str: Annotation version (required)
            body, List[str]: Collaborators (optional)
            
        Returns: SetCollaboratorsResponse
        """
        if( userId == None or fileId == None or version == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'fileId', 'version', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method SetAnnotationCollaborators" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/files/{fileId}/version/{version}/collaborators'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        if ('version' in params):
            replacement = str(self.apiClient.toPathValue(params['version']))
            resourcePath = resourcePath.replace('{' + 'version' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SetCollaboratorsResponse')
        return responseObject
        
        
    def GetAnnotationCollaborators(self, userId, fileId, **kwargs):
        """Get list of annotation collaborators

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            
        Returns: GetCollaboratorsResponse
        """
        if( userId == None or fileId == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'fileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetAnnotationCollaborators" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/files/{fileId}/collaborators'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetCollaboratorsResponse')
        return responseObject
        
        
    def AddAnnotationCollaborator(self, userId, fileId, **kwargs):
        """Add an annotation collaborator

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            body, ReviewerInfo: Reviewer Info (optional)
            
        Returns: AddCollaboratorResponse
        """
        if( userId == None or fileId == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'fileId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method AddAnnotationCollaborator" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/files/{fileId}/collaborators'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'AddCollaboratorResponse')
        return responseObject
        
        
    def GetReviewerContacts(self, userId, **kwargs):
        """Get list of reviewer contacts

        Args:
            userId, str: User GUID (required)
            
        Returns: GetReviewerContactsResponse
        """
        if( userId == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetReviewerContacts" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/contacts'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetReviewerContactsResponse')
        return responseObject
        
        
    def SetReviewerContacts(self, userId, **kwargs):
        """Get list of reviewer contacts

        Args:
            userId, str: User GUID (required)
            body, List[ReviewerContactInfo]: Reviewer Contacts Array (optional)
            
        Returns: GetReviewerContactsResponse
        """
        if( userId == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method SetReviewerContacts" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/reviewerContacts'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetReviewerContactsResponse')
        return responseObject
        
        
    def MoveAnnotation(self, userId, annotationId, body, **kwargs):
        """Move annotation

        Args:
            userId, str: User GUID (required)
            annotationId, str: Annotation ID (required)
            body, Point: position (required)
            
        Returns: MoveAnnotationResponse
        """
        if( userId == None or annotationId == None or body == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'annotationId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method MoveAnnotation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/annotations/{annotationId}/position'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('annotationId' in params):
            replacement = str(self.apiClient.toPathValue(params['annotationId']))
            resourcePath = resourcePath.replace('{' + 'annotationId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'MoveAnnotationResponse')
        return responseObject
        
        
    def SetAnnotationAccess(self, userId, annotationId, body, **kwargs):
        """Set Annotation Access

        Args:
            userId, str: User GUID (required)
            annotationId, str: Annotation ID (required)
            body, int: Annotation Access (required)
            
        Returns: SetAnnotationAccessResponse
        """
        if( userId == None or annotationId == None or body == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'annotationId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method SetAnnotationAccess" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/annotations/{annotationId}/annotationAccess'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('annotationId' in params):
            replacement = str(self.apiClient.toPathValue(params['annotationId']))
            resourcePath = resourcePath.replace('{' + 'annotationId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SetAnnotationAccessResponse')
        return responseObject
        
        
    def MoveAnnotationMarker(self, userId, annotationId, body, **kwargs):
        """Move Annotation Marker

        Args:
            userId, str: User GUID (required)
            annotationId, str: Annotation ID (required)
            body, Point: position (required)
            
        Returns: MoveAnnotationResponse
        """
        if( userId == None or annotationId == None or body == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'annotationId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method MoveAnnotationMarker" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/annotations/{annotationId}/markerPosition'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('annotationId' in params):
            replacement = str(self.apiClient.toPathValue(params['annotationId']))
            resourcePath = resourcePath.replace('{' + 'annotationId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'MoveAnnotationResponse')
        return responseObject
        
        
    def SetReviewerRights(self, userId, fileId, body, **kwargs):
        """Set Reviewer Rights

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            body, List[ReviewerInfo]: Collaborators (required)
            
        Returns: SetReviewerRightsResponse
        """
        if( userId == None or fileId == None or body == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'fileId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method SetReviewerRights" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/files/{fileId}/reviewerRights'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SetReviewerRightsResponse')
        return responseObject
        
        
    def GetSharedLinkAccessRights(self, userId, fileId, **kwargs):
        """Get Shared Link Access Rights

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            
        Returns: GetSharedLinkAccessRightsResponse
        """
        if( userId == None or fileId == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'fileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetSharedLinkAccessRights" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/files/{fileId}/sharedLinkAccessRights'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetSharedLinkAccessRightsResponse')
        return responseObject
        
        
    def SetSharedLinkAccessRights(self, userId, fileId, body, **kwargs):
        """Set Shared Link Access Rights

        Args:
            userId, str: User GUID (required)
            fileId, str: File ID (required)
            body, int: Access Rights for the collaborate link (required)
            
        Returns: SetSharedLinkAccessRightsResponse
        """
        if( userId == None or fileId == None or body == None ):
            raise ApiException("missing required parameters")
        allParams = ['userId', 'fileId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method SetSharedLinkAccessRights" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ant/{userId}/files/{fileId}/sharedLinkAccessRights'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('fileId' in params):
            replacement = str(self.apiClient.toPathValue(params['fileId']))
            resourcePath = resourcePath.replace('{' + 'fileId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SetSharedLinkAccessRightsResponse')
        return responseObject
        
        
    



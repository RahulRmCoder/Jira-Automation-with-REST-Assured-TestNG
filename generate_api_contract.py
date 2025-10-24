# Save this as: generate_api_contract.py
# Run: python generate_api_contract.py
# Output: jira_api_contract.txt

def generate_jira_api_contract():
    contract = """
================================================================================
                    JIRA REST API CONTRACT DOCUMENTATION
================================================================================
Project: Jira Automation Testing Framework
API Version: Jira Cloud REST API v3 & Agile API v1.0
Base URL: https://your-domain.atlassian.net
Authentication: Basic Auth (Preemptive)
Date: October 24, 2025
================================================================================

TABLE OF CONTENTS
================================================================================
1. Authentication Configuration
2. Issue Operations (Create, Read, Update, Delete)
3. Agile Operations (Board, Sprint Management)
4. Additional Operations (Comments, Transitions)
5. Common Response Codes
6. Error Handling
================================================================================


================================================================================
1. AUTHENTICATION CONFIGURATION
================================================================================

Headers Required for All Requests:
-----------------------------------
Authorization: Basic <base64_encoded_credentials>
Content-Type: application/json
Accept: application/json

Credentials Format:
-------------------
Username: your-email@example.com
API Token: Generate from https://id.atlassian.com/manage-profile/security/api-tokens

Base64 Encoding:
----------------
Encode "email:api_token" in Base64 format
Example: echo -n "user@example.com:token123" | base64


================================================================================
2. ISSUE OPERATIONS
================================================================================


################################################################################
# 2.1 CREATE EPIC
################################################################################

Endpoint:
---------
POST /rest/api/3/issue

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "project": {
      "key": "SCRUM"
    },
    "summary": "E-commerce Platform Development",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Complete e-commerce platform with payment gateway integration, user management, and product catalog"
            }
          ]
        }
      ]
    },
    "issuetype": {
      "name": "Epic"
    }
  }
}

Expected Response:
------------------
Status Code: 201 Created

Response Body:
{
  "id": "10001",
  "key": "SCRUM-1",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10001"
}

Fields to Extract:
------------------
- key: "SCRUM-1" (Epic key - needed to link stories)
- id: "10001" (Epic ID)
- self: Full URL to the created issue


################################################################################
# 2.2 CREATE STORY (Linked to Epic)
################################################################################

Endpoint:
---------
POST /rest/api/3/issue

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "project": {
      "key": "SCRUM"
    },
    "summary": "User Registration and Authentication",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "As a user, I want to register and login to the platform so that I can access personalized features"
            }
          ]
        }
      ]
    },
    "issuetype": {
      "name": "Story"
    },
    "parent": {
      "key": "SCRUM-1"
    }
  }
}

Expected Response:
------------------
Status Code: 201 Created

Response Body:
{
  "id": "10002",
  "key": "SCRUM-2",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002"
}

Fields to Extract:
------------------
- key: "SCRUM-2" (Story key - needed to create subtasks)
- id: "10002" (Story ID)


################################################################################
# 2.3 CREATE STORY (Without Epic Link)
################################################################################

Endpoint:
---------
POST /rest/api/3/issue

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "project": {
      "key": "SCRUM"
    },
    "summary": "Shopping Cart Management",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "As a user, I want to add items to cart, update quantities, and remove items"
            }
          ]
        }
      ]
    },
    "issuetype": {
      "name": "Story"
    }
  }
}

Expected Response:
------------------
Status Code: 201 Created

Response Body:
{
  "id": "10003",
  "key": "SCRUM-3",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10003"
}


################################################################################
# 2.4 CREATE SUBTASK
################################################################################

Endpoint:
---------
POST /rest/api/3/issue

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "project": {
      "key": "SCRUM"
    },
    "summary": "Create Registration Form UI",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Design and implement registration form with fields: email, password, confirm password, name with validation"
            }
          ]
        }
      ]
    },
    "issuetype": {
      "name": "Subtask"
    },
    "parent": {
      "key": "SCRUM-2"
    }
  }
}

Expected Response:
------------------
Status Code: 201 Created

Response Body:
{
  "id": "10004",
  "key": "SCRUM-4",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10004"
}

Fields to Extract:
------------------
- key: "SCRUM-4" (Subtask key)
- id: "10004" (Subtask ID)


################################################################################
# 2.5 CREATE BUG
################################################################################

Endpoint:
---------
POST /rest/api/3/issue

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "project": {
      "key": "SCRUM"
    },
    "summary": "Login button not responding on mobile",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "When clicking the login button on mobile devices (iOS Safari and Chrome), nothing happens. Works fine on desktop browsers."
            }
          ]
        }
      ]
    },
    "issuetype": {
      "name": "Bug"
    }
  }
}

Expected Response:
------------------
Status Code: 201 Created

Response Body:
{
  "id": "10006",
  "key": "SCRUM-6",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10006"
}


################################################################################
# 2.6 CREATE TASK
################################################################################

Endpoint:
---------
POST /rest/api/3/issue

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "project": {
      "key": "SCRUM"
    },
    "summary": "Setup CI/CD Pipeline",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Configure Jenkins pipeline for automated builds and deployments to staging and production environments"
            }
          ]
        }
      ]
    },
    "issuetype": {
      "name": "Task"
    }
  }
}

Expected Response:
------------------
Status Code: 201 Created

Response Body:
{
  "id": "10007",
  "key": "SCRUM-7",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10007"
}


################################################################################
# 2.7 GET ISSUE DETAILS
################################################################################

Endpoint:
---------
GET /rest/api/3/issue/{issueIdOrKey}

Example:
--------
GET /rest/api/3/issue/SCRUM-2

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Query Parameters:
-----------------
None required (but can add fields, expand, properties parameters)

Expected Response:
------------------
Status Code: 200 OK

Response Body:
{
  "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations",
  "id": "10002",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002",
  "key": "SCRUM-2",
  "fields": {
    "statuscategorychangedate": "2025-10-24T10:00:00.000+0000",
    "issuetype": {
      "self": "https://your-domain.atlassian.net/rest/api/3/issuetype/10001",
      "id": "10001",
      "description": "Stories track functionality or features expressed as user goals.",
      "iconUrl": "https://your-domain.atlassian.net/images/icons/issuetypes/story.svg",
      "name": "Story",
      "subtask": false,
      "hierarchyLevel": 0
    },
    "parent": {
      "id": "10001",
      "key": "SCRUM-1",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10001",
      "fields": {
        "summary": "E-commerce Platform Development",
        "status": {
          "self": "https://your-domain.atlassian.net/rest/api/3/status/10000",
          "description": "",
          "iconUrl": "https://your-domain.atlassian.net/",
          "name": "To Do",
          "id": "10000",
          "statusCategory": {
            "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/2",
            "id": 2,
            "key": "new",
            "colorName": "blue-gray",
            "name": "To Do"
          }
        },
        "priority": {
          "self": "https://your-domain.atlassian.net/rest/api/3/priority/3",
          "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/medium.svg",
          "name": "Medium",
          "id": "3"
        },
        "issuetype": {
          "self": "https://your-domain.atlassian.net/rest/api/3/issuetype/10000",
          "id": "10000",
          "description": "A big user story that needs to be broken down.",
          "iconUrl": "https://your-domain.atlassian.net/images/icons/issuetypes/epic.svg",
          "name": "Epic",
          "subtask": false,
          "hierarchyLevel": 1
        }
      }
    },
    "project": {
      "self": "https://your-domain.atlassian.net/rest/api/3/project/10000",
      "id": "10000",
      "key": "SCRUM",
      "name": "SCRUM Project",
      "projectTypeKey": "software",
      "simplified": false,
      "avatarUrls": {
        "48x48": "https://your-domain.atlassian.net/secure/projectavatar?pid=10000&avatarId=10324",
        "24x24": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000&avatarId=10324",
        "16x16": "https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000&avatarId=10324",
        "32x32": "https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000&avatarId=10324"
      }
    },
    "created": "2025-10-24T10:00:00.000+0000",
    "priority": {
      "self": "https://your-domain.atlassian.net/rest/api/3/priority/3",
      "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/medium.svg",
      "name": "Medium",
      "id": "3"
    },
    "labels": [],
    "assignee": {
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=123456",
      "accountId": "123456:abcd1234-5678-90ab-cdef-1234567890ab",
      "emailAddress": "user@example.com",
      "avatarUrls": {
        "48x48": "https://secure.gravatar.com/avatar/abc123?d=https%3A%2F%2Favatar-management.services.atlassian.com%2Finitials%2FJD-0.png",
        "24x24": "https://secure.gravatar.com/avatar/abc123?d=https%3A%2F%2Favatar-management.services.atlassian.com%2Finitials%2FJD-0.png",
        "16x16": "https://secure.gravatar.com/avatar/abc123?d=https%3A%2F%2Favatar-management.services.atlassian.com%2Finitials%2FJD-0.png",
        "32x32": "https://secure.gravatar.com/avatar/abc123?d=https%3A%2F%2Favatar-management.services.atlassian.com%2Finitials%2FJD-0.png"
      },
      "displayName": "John Doe",
      "active": true,
      "timeZone": "America/New_York",
      "accountType": "atlassian"
    },
    "updated": "2025-10-24T10:30:00.000+0000",
    "status": {
      "self": "https://your-domain.atlassian.net/rest/api/3/status/10000",
      "description": "",
      "iconUrl": "https://your-domain.atlassian.net/images/icons/statuses/generic.png",
      "name": "To Do",
      "id": "10000",
      "statusCategory": {
        "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/2",
        "id": 2,
        "key": "new",
        "colorName": "blue-gray",
        "name": "To Do"
      }
    },
    "summary": "User Registration and Authentication",
    "creator": {
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=123456",
      "accountId": "123456:abcd1234-5678-90ab-cdef-1234567890ab",
      "emailAddress": "user@example.com",
      "displayName": "John Doe",
      "active": true,
      "timeZone": "America/New_York",
      "accountType": "atlassian"
    },
    "subtasks": [
      {
        "id": "10004",
        "key": "SCRUM-4",
        "self": "https://your-domain.atlassian.net/rest/api/3/issue/10004",
        "fields": {
          "summary": "Create Registration Form UI",
          "status": {
            "self": "https://your-domain.atlassian.net/rest/api/3/status/10000",
            "description": "",
            "iconUrl": "https://your-domain.atlassian.net/",
            "name": "To Do",
            "id": "10000",
            "statusCategory": {
              "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/2",
              "id": 2,
              "key": "new",
              "colorName": "blue-gray",
              "name": "To Do"
            }
          },
          "priority": {
            "self": "https://your-domain.atlassian.net/rest/api/3/priority/3",
            "iconUrl": "https://your-domain.atlassian.net/images/icons/priorities/medium.svg",
            "name": "Medium",
            "id": "3"
          },
          "issuetype": {
            "self": "https://your-domain.atlassian.net/rest/api/3/issuetype/10003",
            "id": "10003",
            "description": "The sub-task of the issue",
            "iconUrl": "https://your-domain.atlassian.net/images/icons/issuetypes/subtask.svg",
            "name": "Subtask",
            "subtask": true,
            "hierarchyLevel": -1
          }
        }
      },
      {
        "id": "10005",
        "key": "SCRUM-5",
        "self": "https://your-domain.atlassian.net/rest/api/3/issue/10005",
        "fields": {
          "summary": "Implement Backend API for Registration",
          "status": {
            "name": "To Do"
          }
        }
      }
    ],
    "reporter": {
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=123456",
      "accountId": "123456:abcd1234-5678-90ab-cdef-1234567890ab",
      "emailAddress": "user@example.com",
      "displayName": "John Doe",
      "active": true
    },
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "As a user, I want to register and login to the platform so that I can access personalized features"
            }
          ]
        }
      ]
    }
  }
}

Key Fields to Extract:
----------------------
- fields.summary: Issue title
- fields.status.name: Current status ("To Do", "In Progress", "Done")
- fields.assignee.displayName: Assigned user name
- fields.priority.name: Priority level
- fields.parent.key: Parent issue key (Epic)
- fields.subtasks: Array of subtasks
- fields.created: Creation timestamp
- fields.updated: Last update timestamp


################################################################################
# 2.8 UPDATE ISSUE (Both Summary and Description)
################################################################################

Endpoint:
---------
PUT /rest/api/3/issue/{issueIdOrKey}

Example:
--------
PUT /rest/api/3/issue/SCRUM-2

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "summary": "User Registration, Authentication and Profile Management",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "As a user, I want to register, login, and manage my profile so that I can access personalized features and update my information"
            }
          ]
        }
      ]
    }
  }
}

Expected Response:
------------------
Status Code: 204 No Content

Response Body:
(Empty - success indicated by 204 status code)


################################################################################
# 2.9 UPDATE ISSUE (Summary Only)
################################################################################

Endpoint:
---------
PUT /rest/api/3/issue/{issueIdOrKey}

Example:
--------
PUT /rest/api/3/issue/SCRUM-1

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "summary": "E-commerce Platform v2.0"
  }
}

Expected Response:
------------------
Status Code: 204 No Content

Response Body:
(Empty - success indicated by 204 status code)


################################################################################
# 2.10 UPDATE ISSUE (Description Only)
################################################################################

Endpoint:
---------
PUT /rest/api/3/issue/{issueIdOrKey}

Example:
--------
PUT /rest/api/3/issue/SCRUM-3

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Updated description with more detailed requirements and acceptance criteria"
            }
          ]
        }
      ]
    }
  }
}

Expected Response:
------------------
Status Code: 204 No Content


################################################################################
# 2.11 UPDATE ISSUE PRIORITY
################################################################################

Endpoint:
---------
PUT /rest/api/3/issue/{issueIdOrKey}

Example:
--------
PUT /rest/api/3/issue/SCRUM-6

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "priority": {
      "name": "High"
    }
  }
}

Priority Options:
-----------------
- Highest
- High
- Medium
- Low
- Lowest

Expected Response:
------------------
Status Code: 204 No Content


################################################################################
# 2.12 UPDATE ISSUE ASSIGNEE
################################################################################

Endpoint:
---------
PUT /rest/api/3/issue/{issueIdOrKey}

Example:
--------
PUT /rest/api/3/issue/SCRUM-2

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "fields": {
    "assignee": {
      "accountId": "123456:abcd1234-5678-90ab-cdef-1234567890ab"
    }
  }
}

Note:
-----
To get accountId, use: GET /rest/api/3/user/search?query=email@example.com

Expected Response:
------------------
Status Code: 204 No Content


################################################################################
# 2.13 DELETE ISSUE
################################################################################

Endpoint:
---------
DELETE /rest/api/3/issue/{issueIdOrKey}

Example:
--------
DELETE /rest/api/3/issue/SCRUM-10

Headers:
--------
Authorization: Basic <credentials>

Query Parameters (Optional):
-----------------------------
deleteSubtasks: true (if issue has subtasks)

Example with Subtasks:
----------------------
DELETE /rest/api/3/issue/SCRUM-10?deleteSubtasks=true

Expected Response:
------------------
Status Code: 204 No Content

Response Body:
(Empty - success indicated by 204 status code)

Verification (Should return 404):
----------------------------------
GET /rest/api/3/issue/SCRUM-10
Status Code: 404 Not Found


================================================================================
3. AGILE OPERATIONS
================================================================================


################################################################################
# 3.1 GET BOARD ID
################################################################################

Endpoint:
---------
GET /rest/agile/1.0/board

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Query Parameters:
-----------------
projectKeyOrId: SCRUM

Example:
--------
GET /rest/agile/1.0/board?projectKeyOrId=SCRUM

Expected Response:
------------------
Status Code: 200 OK

Response Body:
{
  "maxResults": 50,
  "startAt": 0,
  "total": 1,
  "isLast": true,
  "values": [
    {
      "id": 1,
      "self": "https://your-domain.atlassian.net/rest/agile/1.0/board/1",
      "name": "SCRUM board",
      "type": "scrum",
      "location": {
        "projectId": 10000,
        "displayName": "SCRUM",
        "projectName": "SCRUM",
        "projectKey": "SCRUM",
        "projectTypeKey": "software",
        "avatarURI": "https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000&avatarId=10324",
        "name": "SCRUM"
      }
    }
  ]
}

Fields to Extract:
------------------
- values[0].id: Board ID (e.g., 1) - needed to get sprints
- values[0].name: Board name
- values[0].type: Board type ("scrum", "kanban")
- values[0].location.projectKey: Project key


################################################################################
# 3.2 GET ALL SPRINTS
################################################################################

Endpoint:
---------
GET /rest/agile/1.0/board/{boardId}/sprint

Example:
--------
GET /rest/agile/1.0/board/1/sprint

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Query Parameters (Optional):
-----------------------------
state: future, active, closed (filter by sprint state)
startAt: 0 (pagination start)
maxResults: 50 (max results per page)

Example with Filters:
---------------------
GET /rest/agile/1.0/board/1/sprint?state=active

Expected Response:
------------------
Status Code: 200 OK

Response Body:
{
  "maxResults": 50,
  "startAt": 0,
  "isLast": true,
  "values": [
    {
      "id": 1,
      "self": "https://your-domain.atlassian.net/rest/agile/1.0/sprint/1",
      "state": "future",
      "name": "SCRUM Sprint 1",
      "startDate": "2025-10-24T10:00:00.000Z",
      "endDate": "2025-11-07T10:00:00.000Z",
      "originBoardId": 1,
      "goal": "Complete user registration and shopping cart features"
    },
    {
      "id": 2,
      "self": "https://your-domain.atlassian.net/rest/agile/1.0/sprint/2",
      "state": "active",
      "name": "SCRUM Sprint 2",
      "startDate": "2025-11-08T10:00:00.000Z",
      "endDate": "2025-11-22T10:00:00.000Z",
      "originBoardId": 1,
      "goal": "Payment integration"
    }
  ]
}

Sprint States:
--------------
- future: Sprint not yet started
- active: Sprint currently running
- closed: Sprint completed

Fields to Extract:
------------------
- values[0].id: Sprint ID (e.g., 1)
- values[0].state: Sprint state
- values[0].name: Sprint name
- values[0].startDate: Start date (ISO format)
- values[0].endDate: End date (ISO format)
- values[0].goal: Sprint goal


################################################################################
# 3.3 CREATE SPRINT
################################################################################

Endpoint:
---------
POST /rest/agile/1.0/sprint

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "name": "SCRUM Sprint 1",
  "originBoardId": 1
}

Expected Response:
------------------
Status Code: 201 Created

Response Body:
{
  "id": 1,
  "self": "https://your-domain.atlassian.net/rest/agile/1.0/sprint/1",
  "state": "future",
  "name": "SCRUM Sprint 1",
  "originBoardId": 1
}

Fields to Extract:
------------------
- id: Sprint ID (e.g., 1)
- state: "future" (newly created sprint)
- name: Sprint name


################################################################################
# 3.4 ADD ISSUES TO SPRINT
################################################################################

Endpoint:
---------
POST /rest/agile/1.0/sprint/{sprintId}/issue

Example:
--------
POST /rest/agile/1.0/sprint/1/issue

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "issues": [
    "SCRUM-2",
    "SCRUM-3"
  ]
}

Note:
-----
- Can add multiple issues at once
- Issues must exist and not be in another active sprint
- Only Stories and Tasks can be added (not Epics)

Expected Response:
------------------
Status Code: 204 No Content

Response Body:
(Empty - success indicated by 204 status code)


################################################################################
# 3.5 START SPRINT
################################################################################

Endpoint:
---------
POST /rest/agile/1.0/sprint/{sprintId}

Example:
--------
POST /rest/agile/1.0/sprint/1

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body (with goal):
-------------------------
{
  "name": "Sprint 1 - E-commerce Core Features",
  "startDate": "2025-10-24T10:00:00.000Z",
  "endDate": "2025-11-07T10:00:00.000Z",
  "goal": "Complete user registration and shopping cart features"
}

Request Body (without goal):
-----------------------------
{
  "name": "Sprint 1 - E-commerce Core Features",
  "startDate": "2025-10-24T10:00:00.000Z",
  "endDate": "2025-11-07T10:00:00.000Z"
}

Date Format:
------------
ISO 8601 format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'
Example: 2025-10-24T10:00:00.000Z

Expected Response:
------------------
Status Code: 200 OK

Response Body:
{
  "id": 1,
  "self": "https://your-domain.atlassian.net/rest/agile/1.0/sprint/1",
  "state": "active",
  "name": "Sprint 1 - E-commerce Core Features",
  "startDate": "2025-10-24T10:00:00.000Z",
  "endDate": "2025-11-07T10:00:00.000Z",
  "originBoardId": 1,
  "goal": "Complete user registration and shopping cart features"
}

Fields to Extract:
------------------
- id: Sprint ID
- state: "active" (sprint is now running)
- startDate: Actual start date
- endDate: Planned end date


################################################################################
# 3.6 CLOSE/COMPLETE SPRINT
################################################################################

Endpoint:
---------
POST /rest/agile/1.0/sprint/{sprintId}

Example:
--------
POST /rest/agile/1.0/sprint/1

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "state": "closed"
}

Expected Response:
------------------
Status Code: 200 OK

Response Body:
{
  "id": 1,
  "self": "https://your-domain.atlassian.net/rest/agile/1.0/sprint/1",
  "state": "closed",
  "name": "Sprint 1 - E-commerce Core Features",
  "startDate": "2025-10-24T10:00:00.000Z",
  "endDate": "2025-11-07T10:00:00.000Z",
  "completeDate": "2025-11-07T18:00:00.000Z",
  "originBoardId": 1,
  "goal": "Complete user registration and shopping cart features"
}

Fields to Extract:
------------------
- state: "closed"
- completeDate: Actual completion timestamp


################################################################################
# 3.7 GET ISSUES IN SPRINT
################################################################################

Endpoint:
---------
GET /rest/agile/1.0/sprint/{sprintId}/issue

Example:
--------
GET /rest/agile/1.0/sprint/1/issue

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Query Parameters (Optional):
-----------------------------
startAt: 0 (pagination)
maxResults: 50 (max results per page)
jql: Additional JQL filter
fields: Comma-separated list of fields to return

Example with Parameters:
------------------------
GET /rest/agile/1.0/sprint/1/issue?maxResults=10&fields=summary,status

Expected Response:
------------------
Status Code: 200 OK

Response Body:
{
  "expand": "schema,names",
  "startAt": 0,
  "maxResults": 50,
  "total": 2,
  "issues": [
    {
      "expand": "operations,versionedRepresentations,editmeta,changelog,renderedFields",
      "id": "10002",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002",
      "key": "SCRUM-2",
      "fields": {
        "summary": "User Registration and Authentication",
        "status": {
          "self": "https://your-domain.atlassian.net/rest/api/3/status/3",
          "description": "This issue is being actively worked on at the moment.",
          "iconUrl": "https://your-domain.atlassian.net/images/icons/statuses/inprogress.png",
          "name": "In Progress",
          "id": "3",
          "statusCategory": {
            "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/4",
            "id": 4,
            "key": "indeterminate",
            "colorName": "yellow",
            "name": "In Progress"
          }
        },
        "assignee": {
          "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=123456",
          "accountId": "123456:abcd1234-5678-90ab-cdef-1234567890ab",
          "displayName": "John Doe",
          "active": true
        },
        "sprint": {
          "id": 1,
          "self": "https://your-domain.atlassian.net/rest/agile/1.0/sprint/1",
          "state": "active",
          "name": "Sprint 1 - E-commerce Core Features"
        }
      }
    },
    {
      "id": "10003",
      "key": "SCRUM-3",
      "fields": {
        "summary": "Shopping Cart Management",
        "status": {
          "name": "To Do"
        },
        "assignee": null,
        "sprint": {
          "id": 1,
          "name": "Sprint 1 - E-commerce Core Features",
          "state": "active"
        }
      }
    }
  ]
}

Fields to Extract:
------------------
- total: Total number of issues in sprint
- issues[].key: Issue key
- issues[].fields.summary: Issue title
- issues[].fields.status.name: Current status
- issues[].fields.assignee: Assigned user


================================================================================
4. ADDITIONAL OPERATIONS
================================================================================


################################################################################
# 4.1 ADD COMMENT TO ISSUE
################################################################################

Endpoint:
---------
POST /rest/api/3/issue/{issueIdOrKey}/comment

Example:
--------
POST /rest/api/3/issue/SCRUM-2/comment

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body:
-------------
{
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "type": "text",
            "text": "This story needs database schema design before implementation. Please review the attached ERD."
          }
        ]
      }
    ]
  }
}

Expected Response:
------------------
Status Code: 201 Created

Response Body:
{
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002/comment/10000",
  "id": "10000",
  "author": {
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=123456",
    "accountId": "123456:abcd1234-5678-90ab-cdef-1234567890ab",
    "emailAddress": "user@example.com",
    "avatarUrls": {
      "48x48": "https://secure.gravatar.com/avatar/abc123",
      "24x24": "https://secure.gravatar.com/avatar/abc123",
      "16x16": "https://secure.gravatar.com/avatar/abc123",
      "32x32": "https://secure.gravatar.com/avatar/abc123"
    },
    "displayName": "John Doe",
    "active": true,
    "timeZone": "America/New_York",
    "accountType": "atlassian"
  },
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "type": "text",
            "text": "This story needs database schema design before implementation. Please review the attached ERD."
          }
        ]
      }
    ]
  },
  "updateAuthor": {
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=123456",
    "accountId": "123456:abcd1234-5678-90ab-cdef-1234567890ab",
    "displayName": "John Doe",
    "active": true
  },
  "created": "2025-10-24T10:30:00.000+0000",
  "updated": "2025-10-24T10:30:00.000+0000",
  "jsdPublic": true
}

Fields to Extract:
------------------
- id: Comment ID
- author.displayName: Comment author
- created: Comment timestamp
- body.content[0].content[0].text: Comment text


################################################################################
# 4.2 GET AVAILABLE TRANSITIONS
################################################################################

Endpoint:
---------
GET /rest/api/3/issue/{issueIdOrKey}/transitions

Example:
--------
GET /rest/api/3/issue/SCRUM-4/transitions

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Expected Response:
------------------
Status Code: 200 OK

Response Body:
{
  "expand": "transitions",
  "transitions": [
    {
      "id": "11",
      "name": "To Do",
      "to": {
        "self": "https://your-domain.atlassian.net/rest/api/3/status/10000",
        "description": "",
        "iconUrl": "https://your-domain.atlassian.net/",
        "name": "To Do",
        "id": "10000",
        "statusCategory": {
          "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/2",
          "id": 2,
          "key": "new",
          "colorName": "blue-gray",
          "name": "To Do"
        }
      },
      "hasScreen": false,
      "isGlobal": true,
      "isInitial": false,
      "isAvailable": true,
      "isConditional": false,
      "isLooping": false
    },
    {
      "id": "21",
      "name": "In Progress",
      "to": {
        "self": "https://your-domain.atlassian.net/rest/api/3/status/3",
        "description": "This issue is being actively worked on at the moment by the assignee.",
        "iconUrl": "https://your-domain.atlassian.net/images/icons/statuses/inprogress.png",
        "name": "In Progress",
        "id": "3",
        "statusCategory": {
          "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/4",
          "id": 4,
          "key": "indeterminate",
          "colorName": "yellow",
          "name": "In Progress"
        }
      },
      "hasScreen": false,
      "isGlobal": true,
      "isInitial": false,
      "isAvailable": true,
      "isConditional": false,
      "isLooping": false
    },
    {
      "id": "31",
      "name": "Done",
      "to": {
        "self": "https://your-domain.atlassian.net/rest/api/3/status/10001",
        "description": "",
        "iconUrl": "https://your-domain.atlassian.net/",
        "name": "Done",
        "id": "10001",
        "statusCategory": {
          "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/3",
          "id": 3,
          "key": "done",
          "colorName": "green",
          "name": "Done"
        }
      },
      "hasScreen": false,
      "isGlobal": true,
      "isInitial": false,
      "isAvailable": true,
      "isConditional": false,
      "isLooping": false
    }
  ]
}

Common Transition IDs (May vary by workflow):
----------------------------------------------
- "11": To Do
- "21": In Progress
- "31": Done
- "41": In Review (if exists)
- "51": Resolved (if exists)

Fields to Extract:
------------------
- transitions[].id: Transition ID (needed to move issue)
- transitions[].name: Transition name
- transitions[].to.name: Target status name
- transitions[].isAvailable: Whether transition is available


################################################################################
# 4.3 TRANSITION ISSUE (Change Status)
################################################################################

Endpoint:
---------
POST /rest/api/3/issue/{issueIdOrKey}/transitions

Example:
--------
POST /rest/api/3/issue/SCRUM-4/transitions

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Request Body (Move to In Progress):
------------------------------------
{
  "transition": {
    "id": "21"
  }
}

Request Body (Move to Done):
-----------------------------
{
  "transition": {
    "id": "31"
  }
}

Note:
-----
Always use GET transitions API first to get the correct transition IDs
for your specific project workflow.

Expected Response:
------------------
Status Code: 204 No Content

Response Body:
(Empty - success indicated by 204 status code)

Verification:
-------------
GET /rest/api/3/issue/SCRUM-4
Check fields.status.name in response


################################################################################
# 4.4 SEARCH ISSUES (JQL)
################################################################################

Endpoint:
---------
GET /rest/api/3/search

Headers:
--------
Content-Type: application/json
Authorization: Basic <credentials>

Query Parameters:
-----------------
jql: JQL query string (URL encoded)
startAt: 0 (pagination start)
maxResults: 50 (max results per page)
fields: Comma-separated list of fields to return

Example 1 - All Stories:
-------------------------
GET /rest/api/3/search?jql=project=SCRUM AND issuetype=Story&maxResults=50

Example 2 - All Bugs:
---------------------
GET /rest/api/3/search?jql=project=SCRUM AND issuetype=Bug

Example 3 - Issues in Epic:
----------------------------
GET /rest/api/3/search?jql=project=SCRUM AND parent=SCRUM-1

Example 4 - Issues in Current Sprint:
--------------------------------------
GET /rest/api/3/search?jql=project=SCRUM AND sprint in openSprints()

Example 5 - My Assigned Issues:
--------------------------------
GET /rest/api/3/search?jql=project=SCRUM AND assignee=currentUser()

Example 6 - High Priority Bugs:
--------------------------------
GET /rest/api/3/search?jql=project=SCRUM AND issuetype=Bug AND priority=High

Expected Response:
------------------
Status Code: 200 OK

Response Body:
{
  "expand": "schema,names",
  "startAt": 0,
  "maxResults": 50,
  "total": 2,
  "issues": [
    {
      "expand": "operations,versionedRepresentations,editmeta,changelog,renderedFields",
      "id": "10002",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002",
      "key": "SCRUM-2",
      "fields": {
        "summary": "User Registration and Authentication",
        "status": {
          "self": "https://your-domain.atlassian.net/rest/api/3/status/3",
          "name": "In Progress",
          "id": "3",
          "statusCategory": {
            "key": "indeterminate",
            "colorName": "yellow",
            "name": "In Progress"
          }
        },
        "issuetype": {
          "name": "Story"
        },
        "priority": {
          "name": "Medium"
        },
        "assignee": {
          "displayName": "John Doe"
        }
      }
    },
    {
      "id": "10003",
      "key": "SCRUM-3",
      "fields": {
        "summary": "Shopping Cart Management",
        "status": {
          "name": "To Do"
        },
        "issuetype": {
          "name": "Story"
        }
      }
    }
  ]
}

Common JQL Patterns:
--------------------
- Filter by project: project = SCRUM
- Filter by type: issuetype = Story
- Filter by status: status = "In Progress"
- Filter by assignee: assignee = currentUser()
- Filter by priority: priority = High
- Filter by parent: parent = SCRUM-1
- Filter by sprint: sprint in openSprints()
- Created date: created >= -7d
- Updated date: updated >= -1w
- Combine with AND/OR: project = SCRUM AND status = "To Do"


================================================================================
5. COMMON RESPONSE CODES
================================================================================

Success Codes:
--------------
200 OK                  - Successful GET request
201 Created             - Successful POST request (resource created)
204 No Content          - Successful PUT/DELETE request (no response body)

Client Error Codes:
-------------------
400 Bad Request         - Invalid request format or missing required fields
401 Unauthorized        - Authentication failed (invalid credentials)
403 Forbidden           - User lacks permission to perform action
404 Not Found           - Resource does not exist
405 Method Not Allowed  - HTTP method not supported for endpoint
409 Conflict            - Resource conflict (e.g., issue already in sprint)

Server Error Codes:
-------------------
500 Internal Server Error - Server encountered an unexpected condition
502 Bad Gateway          - Invalid response from upstream server
503 Service Unavailable  - Server temporarily unavailable


================================================================================
6. ERROR HANDLING
================================================================================


################################################################################
# 6.1 ERROR RESPONSE FORMAT
################################################################################

When an error occurs, Jira returns a JSON response with error details:

Example Error Response (400 Bad Request):
------------------------------------------
{
  "errorMessages": [],
  "errors": {
    "project": "project is required"
  }
}

Example Error Response (401 Unauthorized):
-------------------------------------------
{
  "errorMessages": [
    "Client must be authenticated to access this resource."
  ],
  "errors": {}
}

Example Error Response (404 Not Found):
----------------------------------------
{
  "errorMessages": [
    "Issue does not exist or you do not have permission to see it."
  ],
  "errors": {}
}

Example Error Response (400 - Invalid Field):
----------------------------------------------
{
  "errorMessages": [],
  "errors": {
    "issuetype": "issue type is required",
    "summary": "You must specify a summary of the issue."
  }
}


################################################################################
# 6.2 COMMON ERROR SCENARIOS
################################################################################

Scenario 1: Invalid API Token
------------------------------
Request: Any API call with wrong token
Response Code: 401 Unauthorized
Error Message: "Client must be authenticated to access this resource."
Solution: Regenerate API token and update credentials

Scenario 2: Project Does Not Exist
-----------------------------------
Request: Create issue with invalid project key
Response Code: 400 Bad Request
Error Message: "project" : "project is required" or "A value with ID 'XXX' does not exist"
Solution: Verify project key exists in Jira

Scenario 3: Issue Type Not Available
-------------------------------------
Request: Create Epic in project without Epic type enabled
Response Code: 400 Bad Request
Error Message: "issuetype" : "Valid values: Story, Task, Bug"
Solution: Enable Epic in project settings or use available issue type

Scenario 4: Issue Already in Sprint
------------------------------------
Request: Add issue to sprint when already in another active sprint
Response Code: 400 Bad Request
Error Message: "Issue SCRUM-2 is already in an active sprint"
Solution: Remove from current sprint first or use different issue

Scenario 5: Sprint Already Started
-----------------------------------
Request: Start sprint that is already active
Response Code: 400 Bad Request
Error Message: "The sprint is already started"
Solution: Check sprint state before starting

Scenario 6: Missing Required Fields
------------------------------------
Request: Create issue without summary
Response Code: 400 Bad Request
Error Message: "summary" : "You must specify a summary of the issue."
Solution: Include all required fields in request body

Scenario 7: Invalid Transition
-------------------------------
Request: Transition issue with invalid transition ID
Response Code: 400 Bad Request
Error Message: "transition" : "Transition could not be performed"
Solution: Get valid transitions first using GET transitions API

Scenario 8: Rate Limiting
--------------------------
Request: Too many requests in short time
Response Code: 429 Too Many Requests
Error Message: "Rate limit exceeded"
Solution: Implement exponential backoff and retry logic


################################################################################
# 6.3 BEST PRACTICES FOR ERROR HANDLING
################################################################################

1. Always check HTTP status code before parsing response
2. Implement retry logic with exponential backoff for 5xx errors
3. Log complete error responses for debugging
4. Validate input data before sending requests
5. Use GET requests to verify state before POST/PUT/DELETE
6. Handle 401/403 errors by re-authenticating or checking permissions
7. Parse errorMessages and errors arrays for detailed error information
8. Implement circuit breaker pattern for repeated failures
9. Set appropriate timeouts for API calls
10. Monitor API usage to stay within rate limits


================================================================================
7. COMPLETE API ENDPOINT SUMMARY
================================================================================

Issue Operations:
-----------------
POST   /rest/api/3/issue                          - Create Issue (201)
GET    /rest/api/3/issue/{issueKey}               - Get Issue (200)
PUT    /rest/api/3/issue/{issueKey}               - Update Issue (204)
DELETE /rest/api/3/issue/{issueKey}               - Delete Issue (204)

Comment Operations:
-------------------
POST   /rest/api/3/issue/{issueKey}/comment       - Add Comment (201)
GET    /rest/api/3/issue/{issueKey}/comment       - Get Comments (200)

Transition Operations:
----------------------
GET    /rest/api/3/issue/{issueKey}/transitions   - Get Transitions (200)
POST   /rest/api/3/issue/{issueKey}/transitions   - Transition Issue (204)

Search Operations:
------------------
GET    /rest/api/3/search                         - Search Issues (200)

Board Operations:
-----------------
GET    /rest/agile/1.0/board                      - Get Boards (200)
GET    /rest/agile/1.0/board/{boardId}/sprint     - Get Sprints (200)

Sprint Operations:
------------------
POST   /rest/agile/1.0/sprint                     - Create Sprint (201)
POST   /rest/agile/1.0/sprint/{sprintId}          - Update/Start Sprint (200)
POST   /rest/agile/1.0/sprint/{sprintId}/issue    - Add Issues to Sprint (204)
GET    /rest/agile/1.0/sprint/{sprintId}/issue    - Get Sprint Issues (200)


================================================================================
8. QUICK REFERENCE - PAYLOAD TEMPLATES
================================================================================

Create Epic:
------------
{"fields":{"project":{"key":"SCRUM"},"summary":"Epic Name","description":{"type":"doc","version":1,"content":[{"type":"paragraph","content":[{"type":"text","text":"Description"}]}]},"issuetype":{"name":"Epic"}}}

Create Story:
-------------
{"fields":{"project":{"key":"SCRUM"},"summary":"Story Name","description":{"type":"doc","version":1,"content":[{"type":"paragraph","content":[{"type":"text","text":"Description"}]}]},"issuetype":{"name":"Story"},"parent":{"key":"SCRUM-1"}}}

Create Subtask:
---------------
{"fields":{"project":{"key":"SCRUM"},"summary":"Subtask Name","description":{"type":"doc","version":1,"content":[{"type":"paragraph","content":[{"type":"text","text":"Description"}]}]},"issuetype":{"name":"Subtask"},"parent":{"key":"SCRUM-2"}}}

Create Bug:
-----------
{"fields":{"project":{"key":"SCRUM"},"summary":"Bug Title","description":{"type":"doc","version":1,"content":[{"type":"paragraph","content":[{"type":"text","text":"Description"}]}]},"issuetype":{"name":"Bug"}}}

Update Issue:
-------------
{"fields":{"summary":"New Summary","description":{"type":"doc","version":1,"content":[{"type":"paragraph","content":[{"type":"text","text":"New Description"}]}]}}}

Add Comment:
------------
{"body":{"type":"doc","version":1,"content":[{"type":"paragraph","content":[{"type":"text","text":"Comment text"}]}]}}

Transition Issue:
-----------------
{"transition":{"id":"21"}}

Add to Sprint:
--------------
{"issues":["SCRUM-2","SCRUM-3"]}

Start Sprint:
-------------
{"name":"Sprint 1","startDate":"2025-10-24T10:00:00.000Z","endDate":"2025-11-07T10:00:00.000Z","goal":"Sprint goal"}


================================================================================
                            END OF API CONTRACT
================================================================================

For more information:
- Official Jira REST API Documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/
- Jira Agile REST API: https://developer.atlassian.com/cloud/jira/software/rest/
- API Token Management: https://id.atlassian.com/manage-profile/security/api-tokens

Last Updated: October 24, 2025
Version: 1.0
"""
    
    # Write to file
    with open('jira_api_contract.txt', 'w', encoding='utf-8') as f:
        f.write(contract)
    
    print("✅ API Contract generated successfully!")
    print("📄 File saved as: jira_api_contract.txt")
    print(f"📊 Total characters: {len(contract)}")
    print(f"📏 Total lines: {contract.count(chr(10)) + 1}")

if __name__ == "__main__":
    generate_jira_api_contract()
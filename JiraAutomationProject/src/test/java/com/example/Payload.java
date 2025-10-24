package com.example;

public class Payload {

    //Payload for creating Epic

    public static String createEpic(String projectKey, String epicName, String epicDescription) {
        return "{\r\n" +
                "  \"fields\": {\r\n" +
                "    \"project\": {\r\n" +
                "      \"key\": \"" + projectKey + "\"\r\n" +
                "    },\r\n" +
                "    \"summary\": \"" + epicName + "\",\r\n" +
                "    \"description\": {\r\n" +
                "      \"type\": \"doc\",\r\n" +
                "      \"version\": 1,\r\n" +
                "      \"content\": [\r\n" +
                "        {\r\n" +
                "          \"type\": \"paragraph\",\r\n" +
                "          \"content\": [\r\n" +
                "            {\r\n" +
                "              \"type\": \"text\",\r\n" +
                "              \"text\": \"" + epicDescription + "\"\r\n" +
                "            }\r\n" +
                "          ]\r\n" +
                "        }\r\n" +
                "      ]\r\n" +
                "    },\r\n" +
                "    \"issuetype\": {\r\n" +
                "      \"name\": \"Epic\"\r\n" +
                "    }\r\n" +
                "  }\r\n" +
                "}";
    }

    //Payload for creating Story

    public static String createStory(String projectKey, String summary, String description, String epicKey) {
        return "{\r\n" +
                "  \"fields\": {\r\n" +
                "    \"project\": {\r\n" +
                "      \"key\": \"" + projectKey + "\"\r\n" +
                "    },\r\n" +
                "    \"summary\": \"" + summary + "\",\r\n" +
                "    \"description\": {\r\n" +
                "      \"type\": \"doc\",\r\n" +
                "      \"version\": 1,\r\n" +
                "      \"content\": [\r\n" +
                "        {\r\n" +
                "          \"type\": \"paragraph\",\r\n" +
                "          \"content\": [\r\n" +
                "            {\r\n" +
                "              \"type\": \"text\",\r\n" +
                "              \"text\": \"" + description + "\"\r\n" +
                "            }\r\n" +
                "          ]\r\n" +
                "        }\r\n" +
                "      ]\r\n" +
                "    },\r\n" +
                "    \"issuetype\": {\r\n" +
                "      \"name\": \"Story\"\r\n" +
                "    },\r\n" +
                "    \"parent\": {\r\n" +
                "      \"key\": \"" + epicKey + "\"\r\n" +
                "    }\r\n" +
                "  }\r\n" +
                "}";
    }

    //Payload for creating Sub task

    public static String createSubtask(String projectKey, String summary, String description, String parentKey) {
        return "{\r\n" +
                "  \"fields\": {\r\n" +
                "    \"project\": {\r\n" +
                "      \"key\": \"" + projectKey + "\"\r\n" +
                "    },\r\n" +
                "    \"summary\": \"" + summary + "\",\r\n" +
                "    \"description\": {\r\n" +
                "      \"type\": \"doc\",\r\n" +
                "      \"version\": 1,\r\n" +
                "      \"content\": [\r\n" +
                "        {\r\n" +
                "          \"type\": \"paragraph\",\r\n" +
                "          \"content\": [\r\n" +
                "            {\r\n" +
                "              \"type\": \"text\",\r\n" +
                "              \"text\": \"" + description + "\"\r\n" +
                "            }\r\n" +
                "          ]\r\n" +
                "        }\r\n" +
                "      ]\r\n" +
                "    },\r\n" +
                "    \"issuetype\": {\r\n" +
                "      \"name\": \"Subtask\"\r\n" +
                "    },\r\n" +
                "    \"parent\": {\r\n" +
                "      \"key\": \"" + parentKey + "\"\r\n" +
                "    }\r\n" +
                "  }\r\n" +
                "}";
    }

    // Create Bug
    public static String createBug(String projectKey, String summary, String description) {
        return "{\r\n" +
                "  \"fields\": {\r\n" +
                "    \"project\": {\r\n" +
                "      \"key\": \"" + projectKey + "\"\r\n" +
                "    },\r\n" +
                "    \"summary\": \"" + summary + "\",\r\n" +
                "    \"description\": {\r\n" +
                "      \"type\": \"doc\",\r\n" +
                "      \"version\": 1,\r\n" +
                "      \"content\": [\r\n" +
                "        {\r\n" +
                "          \"type\": \"paragraph\",\r\n" +
                "          \"content\": [\r\n" +
                "            {\r\n" +
                "              \"type\": \"text\",\r\n" +
                "              \"text\": \"" + description + "\"\r\n" +
                "            }\r\n" +
                "          ]\r\n" +
                "        }\r\n" +
                "      ]\r\n" +
                "    },\r\n" +
                "    \"issuetype\": {\r\n" +
                "      \"name\": \"Bug\"\r\n" +
                "    }\r\n" +
                "  }\r\n" +
                "}";
    }

    // Add Comment
    public static String addComment(String commentText) {
        return "{\r\n" +
                "  \"body\": {\r\n" +
                "    \"type\": \"doc\",\r\n" +
                "    \"version\": 1,\r\n" +
                "    \"content\": [\r\n" +
                "      {\r\n" +
                "        \"type\": \"paragraph\",\r\n" +
                "        \"content\": [\r\n" +
                "          {\r\n" +
                "            \"type\": \"text\",\r\n" +
                "            \"text\": \"" + commentText + "\"\r\n" +
                "          }\r\n" +
                "        ]\r\n" +
                "      }\r\n" +
                "    ]\r\n" +
                "  }\r\n" +
                "}";
    }

    // Update Issue Status (Transition)
    public static String transitionIssue(String transitionId) {
        return "{\r\n" +
                "  \"transition\": {\r\n" +
                "    \"id\": \"" + transitionId + "\"\r\n" +
                "  }\r\n" +
                "}";
    }

    // Move Issues to Sprint
    public static String moveIssuesToSprint(int sprintId, String[] issueKeys) {
        StringBuilder issues = new StringBuilder();
        for (int i = 0; i < issueKeys.length; i++) {
            issues.append("\"").append(issueKeys[i]).append("\"");
            if (i < issueKeys.length - 1) {
                issues.append(",");
            }
        }
        
        return "{\r\n" +
                "  \"issues\": [" + issues.toString() + "]\r\n" +
                "}";
    }

    // Start Sprint (Note: You need to get the sprint ID first)
    public static String startSprint(int sprintId, String sprintName, String startDate, String endDate) {
        return "{\r\n" +
                "  \"name\": \"" + sprintName + "\",\r\n" +
                "  \"startDate\": \"" + startDate + "\",\r\n" +
                "  \"endDate\": \"" + endDate + "\"\r\n" +
                "}";
    }

    // Close Sprint
    public static String closeSprint() {
        return "{\r\n" +
                "  \"state\": \"closed\"\r\n" +
                "}";
    }
    public static String updateIssue(String summary, String description) {
        return "{\r\n" +
                "  \"fields\": {\r\n" +
                "    \"summary\": \"" + summary + "\",\r\n" +
                "    \"description\": {\r\n" +
                "      \"type\": \"doc\",\r\n" +
                "      \"version\": 1,\r\n" +
                "      \"content\": [\r\n" +
                "        {\r\n" +
                "          \"type\": \"paragraph\",\r\n" +
                "          \"content\": [\r\n" +
                "            {\r\n" +
                "              \"type\": \"text\",\r\n" +
                "              \"text\": \"" + description + "\"\r\n" +
                "            }\r\n" +
                "          ]\r\n" +
                "        }\r\n" +
                "      ]\r\n" +
                "    }\r\n" +
                "  }\r\n" +
                "}";
    }
    public static String createTask(String projectKey, String summary, String description) {
        return "{\r\n" +
                "  \"fields\": {\r\n" +
                "    \"project\": {\r\n" +
                "      \"key\": \"" + projectKey + "\"\r\n" +
                "    },\r\n" +
                "    \"summary\": \"" + summary + "\",\r\n" +
                "    \"description\": {\r\n" +
                "      \"type\": \"doc\",\r\n" +
                "      \"version\": 1,\r\n" +
                "      \"content\": [\r\n" +
                "        {\r\n" +
                "          \"type\": \"paragraph\",\r\n" +
                "          \"content\": [\r\n" +
                "            {\r\n" +
                "              \"type\": \"text\",\r\n" +
                "              \"text\": \"" + description + "\"\r\n" +
                "            }\r\n" +
                "          ]\r\n" +
                "        }\r\n" +
                "      ]\r\n" +
                "    },\r\n" +
                "    \"issuetype\": {\r\n" +
                "      \"name\": \"Task\"\r\n" +
                "    }\r\n" +
                "  }\r\n" +
                "}";
    }


    
}

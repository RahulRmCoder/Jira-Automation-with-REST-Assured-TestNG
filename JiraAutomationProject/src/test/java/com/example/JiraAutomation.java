package com.example;

import io.restassured.RestAssured;
import io.restassured.path.json.JsonPath;
import io.restassured.response.Response;
import static io.restassured.RestAssured.*;

import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class JiraAutomation {

    private String baseURI = "https://rahulrajasekharanmenon64325.atlassian.net";
    private String username = "EMAIL";
    private String apiToken = "APITOKEN";
    private String projectKey = "PROJECTKEY";

    private String epicKey;
    private String story1Key;
    private String story2Key;
    private String subtask11Key;
    private String subtask12Key;
    private String subtask21Key;
    private String bugKey;
    private int sprintId;
    private int boardId;
    private String tempIssueKey;

    @BeforeClass
    public void setUp(){
        RestAssured.baseURI = baseURI;
    }

    @Test(priority = 1)
    public void test01_CreateEpic() {
        System.out.println("========== Creating Epic ==========");

        String response = given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .body(Payload.createEpic(projectKey, "E-commerce Platform", "Build complete e-commerce platform with user management and shopping features"))
                .when().post("/rest/api/3/issue")
                .then().log().all()
                .assertThat().statusCode(201)
                .extract().response().asString();

        JsonPath js = new JsonPath(response);
        epicKey = js.getString("key");
        System.out.println("Epic Created: " + epicKey);
        Assert.assertNotNull(epicKey, "Epic Key should not be null");
    }

    @Test(priority = 2, dependsOnMethods = "test01_CreateEpic")
    public void test02_CreateStory1() {
        System.out.println("========== Creating Story 1 ==========");

        String response = given().log().all().auth().preemptive().basic(username,apiToken).header("Content-type","application/json")
        .body(Payload.createStory(projectKey, "User Registration", "Implement user registration with email verification", epicKey))
        .when().post("rest/api/3/issue")
        .then().log().all().assertThat().statusCode(201).extract().response().asString();

        JsonPath js = new JsonPath(response);
        story1Key = js.getString("key");
        System.out.println("Story 1 Created " + story1Key);
        Assert.assertNotNull(story1Key, "Story Key should not be null");
    }

    @Test(priority = 3, dependsOnMethods = "test01_CreateEpic")
    public void test03_CreateStory2() {
        System.out.println("========== Creating Story 2 ==========");

        String response = given().log().all().auth().preemptive().basic(username,apiToken).header("Content-type","application/json")
        .body(Payload.createStory(projectKey, "Shopping Cart", "Implement shopping cart functionality with add/remove items", epicKey))
        .when().post("rest/api/3/issue")
        .then().log().all().assertThat().statusCode(201).extract().response().asString();

        JsonPath js = new JsonPath(response);
        story2Key = js.getString("key");
        System.out.println("Story 2 Created: " + story2Key);
        Assert.assertNotNull(story2Key, "Story Key should not be null");
    }

    @Test(priority = 4, dependsOnMethods = "test02_CreateStory1")
    public void test04_CreateSubtask11() {
        System.out.println("========== Creating Subtask 1 for Story 1 ==========");

        String response = given().log().all().auth().preemptive().basic(username,apiToken).header("Content-type","application/json")
        .body(Payload.createSubtask(projectKey, "Create registration form UI", "Design and implement registration form with validation", story1Key))
        .when().post("rest/api/3/issue")
        .then().log().all().assertThat().statusCode(201).extract().response().asString();

        JsonPath js = new JsonPath(response);
        subtask11Key = js.getString("key");
        System.out.println("Subtask 1 Created for Story 1: " + subtask11Key);
        Assert.assertNotNull(subtask11Key, "Subtask Key should not be null");
    }

    @Test(priority = 5, dependsOnMethods = "test02_CreateStory1")
    public void test05_CreateSubtask12() {
        System.out.println("========== Creating Subtask 2 for Story 1 ==========");

        String response = given().log().all().auth().preemptive().basic(username,apiToken).header("Content-type","application/json")
        .body(Payload.createSubtask(projectKey, "Create registration form UI", "Design and implement registration form with validation", story1Key))
        .when().post("rest/api/3/issue")
        .then().log().all().assertThat().statusCode(201).extract().response().asString();

        JsonPath js = new JsonPath(response);
        subtask12Key = js.getString("key");
        System.out.println("Subtask 2 Created for Story 1: " + subtask12Key);
        Assert.assertNotNull(subtask12Key, "Subtask Key should not be null");
    }

    @Test(priority = 6, dependsOnMethods = "test03_CreateStory2")
    public void test06_CreateSubtask21() {
        System.out.println("========== Creating Subtask 1 for Story 2 ==========");

        String response = given().log().all().auth().preemptive().basic(username,apiToken).header("Content-type","application/json")
        .body(Payload.createSubtask(projectKey, "Design Cart UI Components", "Create responsive cart UI with item list, quantity controls, price calculation, and checkout button", story2Key))
        .when().post("rest/api/3/issue")
        .then().log().all().assertThat().statusCode(201).extract().response().asString();

        JsonPath js = new JsonPath(response);
        subtask21Key = js.getString("key");
        System.out.println("Subtask 1 Created for Story 2: " + subtask21Key);
        Assert.assertNotNull(subtask21Key, "Subtask Key should not be null");
    }

    @Test(priority = 7)
    public void test07_CreateBug() {
        System.out.println("========== Creating Bug ==========");
        
        String response = given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .body(Payload.createBug(projectKey, "Login button not responsive", "The login button doesn't respond when clicked on mobile devices"))
                .when().post("/rest/api/3/issue")
                .then().log().all()
                .assertThat().statusCode(201)
                .extract().response().asString();

        JsonPath js = new JsonPath(response);
        bugKey = js.getString("key");
        System.out.println("Bug Created: " + bugKey);
        Assert.assertNotNull(bugKey, "Bug Key should not be null");
    }

    @Test(priority = 8)
    public void test08_GetBoardId() {
        System.out.println("========== Getting Board ID ==========");
        
        String response = given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .queryParam("projectKeyOrId", projectKey)
                .when().get("/rest/agile/1.0/board")
                .then().log().all()
                .assertThat().statusCode(200)
                .extract().response().asString();

        JsonPath js = new JsonPath(response);
        boardId = js.getInt("values[0].id");
        System.out.println("Board ID: " + boardId);
    }

    @Test(priority = 9, dependsOnMethods = "test08_GetBoardId")
    public void test09_GetSprintId() {
        System.out.println("========== Getting Sprint ID ==========");
        
        String response = given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .when().get("/rest/agile/1.0/board/" + boardId + "/sprint")
                .then().log().all()
                .assertThat().statusCode(200)
                .extract().response().asString();

        JsonPath js = new JsonPath(response);
        sprintId = js.getInt("values[0].id");
        System.out.println("Sprint ID: " + sprintId);
    }

    @Test(priority = 10, dependsOnMethods = {"test09_GetSprintId", "test02_CreateStory1", "test03_CreateStory2"})
    public void test10_AddStoriesToSprint() {
        System.out.println("========== Adding Stories to Sprint ==========");
        
        String[] issues = {story1Key, story2Key};
        
        given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .body(Payload.moveIssuesToSprint(sprintId, issues))
                .when().post("/rest/agile/1.0/sprint/" + sprintId + "/issue")
                .then().log().all()
                .assertThat().statusCode(204);

        System.out.println("Stories added to Sprint successfully");
    }

    @Test(priority = 11, dependsOnMethods = "test10_AddStoriesToSprint")
    public void test11_StartSprint() {
        System.out.println("========== Starting Sprint ==========");
        
        // Date format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'
        String startDate = "2025-10-24T10:00:00.000Z";
        String endDate = "2025-11-07T10:00:00.000Z"; // 2 weeks sprint
        
        given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .body(Payload.startSprint(sprintId, "Sprint 1 - E-commerce", startDate, endDate))
                .when().post("/rest/agile/1.0/sprint/" + sprintId)
                .then().log().all()
                .assertThat().statusCode(200);

        System.out.println("Sprint started successfully");
    }

    @Test(priority = 12, dependsOnMethods = "test02_CreateStory1")
    public void test12_AddCommentToStory() {
        System.out.println("========== Adding Comment to Story ==========");
        
        given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .body(Payload.addComment("This story needs database schema design before implementation"))
                .when().post("/rest/api/3/issue/" + story1Key + "/comment")
                .then().log().all()
                .assertThat().statusCode(201);

        System.out.println("Comment added successfully");
    }
    @Test(priority = 13, dependsOnMethods = "test02_CreateStory1")
    public void test13_GetIssueDetails() {
        System.out.println("========== Getting Issue Details ==========");
        
        Response response = given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .when().get("/rest/api/3/issue/" + story1Key)
                .then().log().all()
                .assertThat().statusCode(200)
                .extract().response();

        JsonPath js = new JsonPath(response.asString());
        String summary = js.getString("fields.summary");
        String status = js.getString("fields.status.name");
        
        System.out.println("Issue Summary: " + summary);
        System.out.println("Issue Status: " + status);
    }

    @Test(priority = 14, dependsOnMethods = "test04_CreateSubtask11")
    public void test14_GetTransitions() {
        System.out.println("========== Getting Available Transitions ==========");
        
        String response = given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .when().get("/rest/api/3/issue/" + subtask11Key + "/transitions")
                .then().log().all()
                .assertThat().statusCode(200)
                .extract().response().asString();

        JsonPath js = new JsonPath(response);
        System.out.println("Available transitions: " + js.getString("transitions.name"));
    }

    @Test(priority = 15, dependsOnMethods = "test07_CreateBug")
    public void test15_UpdateIssue() {
        System.out.println("========== Updating Bug Issue ==========");
        
        // Update the bug with new summary and description
        given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .body(Payload.updateIssue(
                    "Login button not responsive on mobile and tablet devices", 
                    "The login button doesn't respond when clicked on mobile devices (iOS and Android) and tablets. Works fine on desktop browsers. Priority: High"
                ))
                .when().put("/rest/api/3/issue/" + bugKey)
                .then().log().all()
                .assertThat().statusCode(204);

        System.out.println("Bug updated successfully: " + bugKey);
        
        // Verify the update by getting the issue details
        Response response = given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .when().get("/rest/api/3/issue/" + bugKey)
                .then().log().all()
                .assertThat().statusCode(200)
                .extract().response();

        JsonPath js = new JsonPath(response.asString());
        String updatedSummary = js.getString("fields.summary");
        System.out.println("Updated Issue Summary: " + updatedSummary);
        Assert.assertTrue(updatedSummary.contains("tablet"), "Updated summary should contain 'tablet'");
    }

    @Test(priority = 16, dependsOnMethods = "test03_CreateStory2")
    public void test16_UpdateStoryIssue() {
        System.out.println("========== Updating Story Issue ==========");
        
        given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .body(Payload.updateIssue(
                    "Shopping Cart with Wishlist Integration", 
                    "Implement shopping cart functionality with add/remove items, quantity management, and integration with wishlist feature"
                ))
                .when().put("/rest/api/3/issue/" + story2Key)
                .then().log().all()
                .assertThat().statusCode(204);

        System.out.println("Story updated successfully: " + story2Key);
    }

    
    @Test(priority = 17)
    public void test17_CreateTempIssueForDeletion() {
        System.out.println("========== Creating Temporary Issue for Deletion Test ==========");
        
        String response = given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .body(Payload.createTask(projectKey, "Temporary Task - To Be Deleted", "This is a temporary task created only for testing the delete functionality"))
                .when().post("/rest/api/3/issue")
                .then().log().all()
                .assertThat().statusCode(201)
                .extract().response().asString();

        JsonPath js = new JsonPath(response);
        tempIssueKey = js.getString("key");
        System.out.println("Temporary Issue Created for Deletion: " + tempIssueKey);
        Assert.assertNotNull(tempIssueKey, "Temp Issue Key should not be null");
    }

    @Test(priority = 18, dependsOnMethods = "test17_CreateTempIssueForDeletion")
    public void test18_DeleteIssue() {
        System.out.println("========== Deleting Temporary Issue ==========");
        
        given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .when().delete("/rest/api/3/issue/" + tempIssueKey)
                .then().log().all()
                .assertThat().statusCode(204);

        System.out.println("Issue deleted successfully: " + tempIssueKey);
        
        // Verify deletion by trying to get the issue (should return 404)
        given().log().all()
                .auth().preemptive().basic(username, apiToken)
                .header("Content-Type", "application/json")
                .when().get("/rest/api/3/issue/" + tempIssueKey)
                .then().log().all()
                .assertThat().statusCode(404);

        System.out.println("Verified: Issue no longer exists");
    }


}

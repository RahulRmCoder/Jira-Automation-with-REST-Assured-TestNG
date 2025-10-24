# 🧠 Jira Automation with REST Assured & TestNG

This project automates Jira issue management workflows using **Atlassian Jira Cloud REST APIs**, **Rest Assured**, and **TestNG**.
It programmatically creates and manages **Epics, Stories, Subtasks, Bugs, Sprints, Comments, and Issue Updates** within a Jira project.

---

## 🚀 Features Automated

The automation script performs the following operations:

| Step | Test Case                             | Description                                          |
| ---- | ------------------------------------- | ---------------------------------------------------- |
| 1    | `test01_CreateEpic()`                 | Creates an **Epic** in Jira                          |
| 2    | `test02_CreateStory1()`               | Creates first **Story** linked to Epic               |
| 3    | `test03_CreateStory2()`               | Creates second **Story** linked to Epic              |
| 4    | `test04_CreateSubtask11()`            | Creates Subtask 1 under Story 1                      |
| 5    | `test05_CreateSubtask12()`            | Creates Subtask 2 under Story 1                      |
| 6    | `test06_CreateSubtask21()`            | Creates Subtask 1 under Story 2                      |
| 7    | `test07_CreateBug()`                  | Creates a **Bug** issue                              |
| 8    | `test08_GetBoardId()`                 | Fetches the Jira **Board ID**                        |
| 9    | `test09_GetSprintId()`                | Retrieves **Sprint ID** for the board                |
| 10   | `test10_AddStoriesToSprint()`         | Adds created stories to the Sprint                   |
| 11   | `test11_StartSprint()`                | Starts the Sprint with start and end dates           |
| 12   | `test12_AddCommentToStory()`          | Adds a comment to a Story                            |
| 13   | `test13_GetIssueDetails()`            | Fetches Story details (summary, status)              |
| 14   | `test14_GetTransitions()`             | Retrieves available transitions for a subtask        |
| 15   | `test15_UpdateIssue()`                | Updates an existing Bug issue (summary, description) |
| 16   | `test16_UpdateStoryIssue()`           | Updates Story 2 with new details                     |
| 17   | `test17_CreateTempIssueForDeletion()` | Creates a temporary Task issue                       |
| 18   | `test18_DeleteIssue()`                | Deletes the temporary Task and verifies deletion     |

---

## 🧩 Project Structure

📁 src
└── 📁 test
　 └── 📁 java
　　 └── 📁 com.example
　　　　├── JiraAutomation.java — Main TestNG test class
　　　　└── Payload.java — JSON payload builder class

---

## ⚙️ Setup Instructions

### 1. Prerequisites

* **Java JDK 8+**
* **Maven**
* **TestNG plugin** (for running tests)
* **Atlassian Jira Cloud account**
* **API Token** from [Atlassian Account Settings](https://id.atlassian.com/manage-profile/security/api-tokens)

---

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/jira-automation.git
cd jira-automation
```

---

### 3. Configure Your Jira Credentials

Edit `JiraAutomation.java`:

```java
private String baseURI = "https://<your-domain>.atlassian.net";
private String username = "<your-email>@gmail.com";
private String apiToken = "<your-api-token>";
private String projectKey = "<your-project-key>";
```

> 🔐 **Note:** Don’t commit API tokens. Use environment variables or `config.properties` in real deployments.

---

### 4. Run the Tests

#### Option 1: From Command Line

```bash
mvn clean test
```

#### Option 2: From IntelliJ / Eclipse

Right-click on `JiraAutomation.java` → **Run with TestNG**.

---

## 📄 Payload Management

All JSON request bodies live in `Payload.java`, built dynamically per test.
Example:

```java
public static String createStory(String projectKey, String summary, String description, String epicKey) {
    return "{ \"fields\": { ... } }";
}
```

---

## 🧪 Sample Output

```
========== Creating Epic ==========
POST /rest/api/3/issue
Response: 201 Created
Epic Created: RRMAUT-1

========== Creating Story 1 ==========
POST /rest/api/3/issue
Response: 201 Created
Story 1 Created: RRMAUT-2
```

---

## 📘 Tech Stack

* **Java**
* **REST Assured**
* **TestNG**
* **Maven**
* **Jira Cloud REST API v3**

---

## 🛡️ Error Handling

* Validates status codes (200, 201, 204)
* Uses `Assert.assertNotNull()` for creation checks
* Manages dependencies with `dependsOnMethods` in TestNG

---

## 🧰 Troubleshooting

| Problem          | Possible Cause    | Solution                       |
| ---------------- | ----------------- | ------------------------------ |
| 401 Unauthorized | Wrong credentials | Recheck Jira email + API token |
| 400 Bad Request  | Invalid JSON      | Fix `Payload.java`             |
| 404 Not Found    | Wrong project key | Verify `projectKey` & endpoint |
| 409 Conflict     | Duplicate issue   | Use unique summaries           |

---

## 📜 License

Licensed under the **MIT License** — free for personal and educational use.

---

## 👨‍💻 Author

**Rahul Rajasekharanmenon**
📍 Based in India
💬 Passionate about API automation, REST Assured & full-stack development with Java and MongoDB.

---

✅ Copy everything from here directly into `README.md` — it’s one continuous markdown file (no split boxes or YAML formatting).

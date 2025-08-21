Specification Heading: Task Management API

Scenario: Create a new task
  Given I have a task with name "Test Task"
  When I send a POST request to /tasks/
  Then the task is created successfully with status "created"

Scenario: Get list of tasks
  When I send a GET request to /tasks/
  Then I should receive a list of tasks

Scenario: Update a task
  Given an existing task
  When I send a PUT request to /tasks/{uuid}
  Then the task is updated successfully

Scenario: Delete a task
  Given an existing task
  When I send a DELETE request to /tasks/{uuid}
  Then the task is deleted successfully

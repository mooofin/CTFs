

### Testing for Server-Side Parameter Pollution (SSPP) in Structured Data Formats

* **Concept:** Attackers can manipulate input parameters to inject additional fields into server-side structured data (e.g., JSON, XML), potentially causing privilege escalation or other vulnerabilities.

* **Example scenario:**

  * User edits their profile name via a POST request:

    ```
    POST /myaccount
    name=peter
    ```
  * Server processes this as a JSON PATCH request:

    ```json
    PATCH /users/7312/update
    {"name":"peter"}
    ```

* **Malicious input attempt:**

  ```
  POST /myaccount
  name=peter","access_level":"administrator
  ```

* **If the server concatenates user input into JSON without sanitization, the resulting request might be:**

  ```json
  PATCH /users/7312/update
  {"name":"peter","access_level":"administrator"}
  ```

* **Impact:** The user "peter" could be assigned administrator privileges unexpectedly.

* **Testing approach:** Inject unexpected structured data fields into user inputs and monitor how the server processes these inputs to detect vulnerabilities caused by parameter pollution.



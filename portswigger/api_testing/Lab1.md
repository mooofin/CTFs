

---

## Write-Up: Solving the API Documentation Lab (API Testing Academy)

### Lab Goal

The objective was to **find the exposed API documentation and delete the user carlos** by exploiting an interactive API interface. Credentials provided for the wiener user.

---

### Steps Taken

####  Logging In

* Logged in to the application using the following credentials:

  * **Username:** `wiener`
  * **Password:** `peter`
* Confirmed successful login and access to the user profile.

---

#### Updating Email Address

* Updated the email address via the profile page to ensure an entry appeared in Burp’s HTTP history for the user-specific API endpoint.

---

####  Analyzing the PATCH Request

* Located the **`PATCH /api/user/wiener`** request in Burp’s **Proxy > HTTP history**.
* Right-clicked this request and selected **Send to Repeater** for further testing.

---

####  Testing the Endpoint

* In the **Repeater** tab:

  * Sent the **PATCH /api/user/wiener** request.
  * Observed that it retrieved credentials for user wiener, confirming the endpoint’s responsiveness.

---

####  Exploring the API Structure

* Removed `/wiener` from the endpoint, modifying it to:

  ```
  PATCH /api/user
  ```

  * Sent the request.
  * Observed an error response because a user identifier was required.

* Further removed `/user` from the path:

  ```
  PATCH /api
  ```

  * Sent the request.
  * Observed that it returned a **JSON response** containing API documentation, confirming that the API documentation was exposed.

---

####  Accessing the API Documentation

* Right-clicked the response in the Repeater and selected **Show response in browser**.

* Copied the generated URL and pasted it into Burp’s browser.

* In the browser, the documentation was **interactive** and allowed direct API interactions.

---
### Deleting Carlos

* In the interactive API documentation:

  * Located the **DELETE** operation.
  * Entered **carlos** as the target user for deletion.
  * Clicked **Send request** to delete the user carlos.

* Verified that the user **carlos** was successfully deleted.
![image](https://github.com/user-attachments/assets/7591aa99-49e2-45db-ac8e-b69b738aa320)
![image](https://github.com/user-attachments/assets/08559f09-d8d2-4706-bfce-cc93ba51e4f8)




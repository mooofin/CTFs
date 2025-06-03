I started by triggering a password reset for the **administrator** user in Burp’s browser. In **Proxy > HTTP history**, I noticed the `POST /forgot-password` request and the related JavaScript file `/static/js/forgotPassword.js`.

I sent the `POST /forgot-password` request to **Repeater** to verify that the response stayed the same for valid requests. To test how it handled errors, I changed the `username` to `administratorx`, which returned an “Invalid username” message.

To see if I could add extra parameters, I injected a URL-encoded `&` character in the request:

```
username=administrator%26x=y
```

The server responded with “Parameter is not supported,” indicating that `&x=y` was treated as a separate parameter on the backend.

Next, I tried to truncate the query string by using a URL-encoded `#` character:

```
username=administrator%23
```

This time, I got a “Field not specified” error, hinting that there might be an additional parameter, likely named `field`, that was missing in the truncated request.

To confirm this, I added a fake `field` parameter:

```
username=administrator%26field=x%23
```

This resulted in an “Invalid field” message, showing that the server recognized `field` as a real parameter.

I wanted to see what valid field names the server supported. I used Burp’s **Intruder** to brute-force the `field` parameter with common server-side variable names:

```
username=administrator%26field=§x§%23
```

After running the attack, I found that both `username` and `email` were valid fields, as they gave back a 200 response.

To confirm, I tried:

```
username=administrator%26field=email%23
```

which returned the same successful response as before.

Looking in `/static/js/forgotPassword.js`, I saw a clue: a password reset endpoint using a `reset_token` parameter:

```
/forgot-password?reset_token=${resetToken}
```

I then tested if `reset_token` was a valid field. I changed the request to:

```
username=administrator%26field=reset_token%23
```

This gave me the **password reset token** for the administrator account.

Finally, in Burp’s browser, I visited the password reset endpoint, added the token as a query parameter:

```
/forgot-password?reset_token=zrg1mtkj7ubaz914jnh4mw56sow1b6nj
```

I reset the administrator’s password, logged in, and accessed the Admin panel to delete the `carlos` user and solve the lab.
![image](https://github.com/user-attachments/assets/eadc9694-1214-45e1-8167-b7c4c9627c4e)
![image](https://github.com/user-attachments/assets/2a5d2f16-6516-426a-b064-d0ed72c7ed53)



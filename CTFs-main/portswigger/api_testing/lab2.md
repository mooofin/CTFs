![image](https://github.com/user-attachments/assets/238947ac-e96d-4be0-aed1-fd8941998e56)


---

To solve the lab, I started by accessing the product page in Burp’s browser and looking at the API request for the product’s price. I noticed it was a GET request to `/api/products/1/price`, so I sent this request to Repeater to experiment with it.

In Repeater, I changed the HTTP method from GET to OPTIONS to see what methods were allowed. The response showed that GET and PATCH were allowed. Next, I tried changing the method to PATCH and sent the request, but I got an Unauthorized response. I figured this was because I wasn’t logged in yet.

So I logged in using the provided credentials (`wiener:peter`) and revisited the leather jacket product page. I found the same API request for the jacket’s price and sent it to Repeater again.

This time, when I tried PATCH, I got an error about the Content-Type header. The error said it should be `application/json`, so I added that header and tried sending an empty JSON object (`{}`) as the request body. That caused another error telling me the request body was missing the `price` parameter.

Finally, I added the `price` parameter to the JSON body like this:

```json
{
  "price": 0
}
```

When I sent that, I got a 200 OK response.

Back in the browser, I refreshed the page and saw that the jacket’s price had changed to \$0.00. I added it to my basket, went to checkout, and placed the order to complete the lab.

Here’s the final PATCH request I used:

```
PATCH /api/products/1/price HTTP/2
Host: 0ad900bb048afe7280ed3acc009b007c.web-security-academy.net
Cookie: session=sLtpnVJ0U9bJgt2OdJnHu0Lactf6jLXC
Content-Type: application/json

{
  "price": 0
}
```

Let me know if you’d like to adjust or reword it further!

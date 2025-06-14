![image](https://github.com/user-attachments/assets/a62f5ced-7da0-4b3b-88bf-3a39f34ade8d)


To solve this lab, I started by logging into the application with the credentials **wiener\:peter** in Burp’s browser. I navigated to the **Lightweight “l33t” Leather Jacket** product and added it to my basket. When I went to my basket and tried to place the order, I saw that I didn’t have enough credit to complete the purchase.

Next, I looked at Burp’s **Proxy > HTTP history** and noticed two API requests for **/api/checkout**: a GET and a POST. I saw that the response to the GET request contained a **chosen\_discount** parameter in the JSON, but the POST request didn’t include it.

I right-clicked the POST **/api/checkout** request and sent it to Repeater. In the Repeater tab, I edited the JSON body of the POST request to add the missing **chosen\_discount** parameter like this:

```json
{
  "chosen_discount": {
    "percentage": 0
  },
  "chosen_products": [
    {
      "product_id": "1",
      "quantity": 1
    }
  ]
}
```

I sent this modified request and saw that the API didn’t return any error, which suggested the server was accepting the **chosen\_discount** parameter.

Then, to test how the server processed this parameter, I changed the discount percentage to a string value of “x” and sent the request. The API returned an error, confirming that it expected a number here.

Finally, I changed the **percentage** value to **100**, effectively giving myself a full 100% discount:

```json
{
  "chosen_discount": {
    "percentage": 100
  },
  "chosen_products": [
    {
      "product_id": "1",
      "quantity": 1
    }
  ]
}
```

I sent this final request and it went through successfully, solving the lab by applying the maximum discount and bypassing the insufficient credit check.
![image](https://github.com/user-attachments/assets/d8d778a8-9317-49e4-af62-7bc67cf560d7)


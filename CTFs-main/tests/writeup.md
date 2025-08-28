# QSN 1


<img width="826" height="530" alt="screenshot-1756409094" src="https://github.com/user-attachments/assets/3d097414-3354-4d5c-a3de-0407a5d60218" />



#### 

## Giveaway Payload

```jinja
{{ (7*7).join(['f','o','o']) }}
````

### Server Response

```text
49.join(['f','o','o'])
```


### Thoughts 
Template engines dont usually execute code like that, the math worked because the engine could evaluate it , method call didn’t work because template engines usually limit or sandbox method access .


### Notes

* Template engines (Jinja2, Twig, Handlebars, etc.) use `{{ ... }}` for evaluation.
* Math worked (`7*7 → 49`) because the engine can evaluate expressions.
* `.join(...)` did not execute; it was rendered literally.
* This happens because template engines **sandbox or restrict method access**.
* Such **partial evaluation** is a strong indicator of **SSTI**.



## Further Reading

[https://arxiv.org/pdf/2405.01118](https://arxiv.org/pdf/2405.01118)


# QSN 2


<img width="800" height="556" alt="screenshot-1756409617" src="https://github.com/user-attachments/assets/ddc8cbf0-de37-4148-88a9-4bc5ad97a54f" />


The payloads actually confirm that it can be attacked with injection with the prompts being evaluatted , thus logically processing injected SQL code.

The initial payload ' UNION SELECT 1,2,3,4-- likely failed because of a data type mismatch (e.g., trying to union an integer with a string column)

The final payload, ' UNION SELECT id,name,price,description FROM products WHERE id=1-- :)

Also the explanation for union attacks covers this and among the options UNION seems to be the correct option among all this 

<img width="1086" height="643" alt="screenshot-1756410070" src="https://github.com/user-attachments/assets/bc47a9cf-d9be-4522-8f3e-712b2fb4d525" />

Other SQL injection types don’t apply here: Boolean-based blind SQLi only reveals true/false differences without showing actual data, Second-order SQLi requires stored payloads that execute later, Error-based SQLi depends on database error messages leaking data, and Inference-based SQLi relies on timing or side effects to infer results. In this case, none are relevant because the injected UNION queries directly returned and displayed database content in the response.



## Further Reading 
[https://portswigger.net/web-security/sql-injection/union-attacks#retrieving-multiple-values-within-a-single-column](https://portswigger.net/web-security/sql-injection/union-attacks#retrieving-multiple-values-within-a-single-column)


# Q 3
<img width="675" height="687" alt="screenshot-1756411977" src="https://github.com/user-attachments/assets/2672d18c-eaa3-4c54-8daf-03e337d0a7a1" />


About this one , it showed a POST req to a domain called -(https://partner-offers.com)


1)Cross-Site Request Forgery (CSRF)
2)Server-Side Request Forgery (SSRF)
3)Cross-Site Scripting (XSS)



It is not SSRF, since the requests originate in the browser, not the server; not session token exposure, because the token itself isn’t leaked but misused; and not XSS, since the malicious script doesn’t run on the banking site but on a trusted third-party origin.

 CSRF involves tricking a user into performing an action (like transferring money). The attacker typically cannot see the response from the server. This vulnerability is about reading data, which is a different class of attack enabled by the CORS policy

 To sum it up , the attacker accessed resources located outside of a given domain .

Hence this vulnerability is a CORS Policy Bypass caused by a misconfiguration where the banking API explicitly trusts https://partner-offers.com and also sets Access-Control-Allow-Credentials: true. This allows any JavaScript running on that domain to send authenticated requests with the victim’s cookies and directly read the sensitive API responses, such as balances and transactions

  
## Further reading 
[https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/07-Testing_Cross_Origin_Resource_Sharing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/07-Testing_Cross_Origin_Resource_Sharing)









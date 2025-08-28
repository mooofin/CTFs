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


# Q 4 

<img width="740" height="641" alt="image" src="https://github.com/user-attachments/assets/0eb241c0-d6e3-41ea-84af-6526e837a9a4" />

This question is about SSH authentication failures caused by incorrect file permissions !!



Linux file permissions can be expressed as a three-digit number. Each of the digits represent: Owner, Group, Others.

Digit |  Permissions
------------------------------
0     |  None
1     |  Execute
2     |  Write
3     |  Write and Execute
4     |  Read
5     |  Read and Execute
6     |  Read and Write
7     |  Read, Write and Execute

With 755, you'd give reading and execution permissions to everyone. With 644, you'd be giving reading permissions to everyone.

SSH clients and servers will remind you to use strong permissions to ensure that you don't accidentally share your private key with every user on a server.

Traditionallly Unix & Linux servers are designed to be multi-user systems. Due to the implications of using Public / Private Key Cryptography, it becomes important to keep the Private Key secret . 

A little overkill imo , Ssh is actually pretty strict on permissions, if it thinks you've set them too liberally it will ignore those files and it won't work as you expect it to, so you don't really have to think about hardening in this way, if it's working it's likely hard enough. 

Coming to the question 


```
chmod 700 ~/.ssh → makes the .ssh directory accessible only to the owner (rwx------). SSH will reject keys if this directory is world-readable.

chmod 600 ~/.ssh/authorized_keys → restricts the key file so that only the owner can read/write (rw-------). This prevents other users from snooping or modifying your authorized keys.
```
### Aliter:
Alternative: chattr

Some Linux filesystems supports file attributes, notably an immutable flag. Files/directories with the immutable flag set cannot be deleted, modified, or have their permissions changed. Only root can set/clear this flag.

This command would do the trick, even with the default ownership/permissions:

```bash
 chattr +i ~test/.ssh/{authorized_keys,}
```
Now .ssh and authorized_keys cannot be modified in any way, not even by root. If root needs to update these files, you'll need to chattr -i them first. Use lsattr to check for attributes.

This approach is simpler, but less flexible. It also needs filesystem support; I believe it's supported on at least ext2/3/4, XFS, and btrfs

### aliter: 2
 Run a cron job to fix permissions each night

 ## Futher reading 


 [https://www.redhat.com/en/blog/linux-access-control-lists](https://www.redhat.com/en/blog/linux-access-control-lists)


# Q 5 


<img width="740" height="600" alt="image" src="https://github.com/user-attachments/assets/f4761088-8c84-416b-b4d3-11a8f4853096" />

### TLDR

An attacker broke into the web server and ran a fake program called kworker that looked like a normal Linux process. They deleted the file after starting it so it wouldn’t be easy to find, but the process kept running in memory. This program used almost all the CPU power, which is a strong sign of cryptomining malware maybe or not :( . Finally, the malware connected out to a suspicious server on the internet, which is how it either received commands or sent the mining results. In short: the attacker hacked in, installed hidden malware, and used the server’s resources for their own purpose


Also uname -a is important because it quickly reveals the system’s operating system, kernel version, and architecture , which they can craft payloads using Metasploit :( . 

ps -aux also showed a process is running as the www-data user, indicating the web service account was the entry point of the compromise 








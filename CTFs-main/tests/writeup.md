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








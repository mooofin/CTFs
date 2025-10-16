The search blog feature contains a DOM-based cross-site scripting vulnerability. Client-side code reads data from location.search and assigns it directly to a div using innerHTML, allowing attacker-controlled input to be parsed as HTML and execute JavaScript in victims’ browsers


So i opened the given url in 
```
https://0a12009504c474f480df80a0008f007e.web-security-academy.net/?q=<img src=1 onerror=alert(1)>
```
to check if there was a xss error , and it gave a popup with alert window . 

When the page renders the injected HTML, the browser tries to load the image, triggers the onerror handler, and alert(1) runs 

I tried using curl , but then i realised u need java script for this 

After this i solved the lab : 3 



The vulnarability is that the browser parsed user input as HTML instead of plain text . tiny HTML element with an event handler, e.g. <img src=1 onerror=alert(1)>, becomes executable when it is reflected into the page via innerHTML 

The safest immediate fix is to stop inserting untrusted strings as HTML: use textContent for text or explicitly create DOM nodes

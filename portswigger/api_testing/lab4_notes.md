

 Certain characters in URLs have special roles and can lead to interesting behaviors when exploited. Two of the most common are `&` and `#`.

The `&` character acts as a separator between parameters in a URL query string. For example, consider this URL:

```
/profile?name=alice&age=25
```

The backend interprets this as two separate parameters: `name=alice` and `age=25`. But if we URL-encode the `&` as `%26` and include it in a parameter value like this:

```
/profile?name=alice%26age=25
```

the server might still treat it as a real `&` and split it, mistakenly parsing it as two separate parameters again. This behavior can let us inject new parameters into the backend’s query handling.

The `#` character, on the other hand, is used as a fragment identifier by browsers. For example, `/profile?name=alice#bio` means that the browser jumps to the `bio` section of the page. However, everything after the `#` isn’t sent to the server by default. If you URL-encode the `#` as `%23`, like this:

```
/profile?name=alice%23bio
```

the entire string `alice#bio` is sent to the server. Some backends interpret the `#` as a special stop marker, causing the backend to ignore or truncate everything after it. This can let you bypass or remove parts of server-side logic.

In this lab, we used these concepts to manipulate the username field in the password reset flow. By adding a URL-encoded `&` (`%26`) to sneak in an extra `field` parameter and a URL-encoded `#` (`%23`) to truncate parts of the request, we were able to trick the server into revealing a sensitive reset token. Understanding how `&` and `#` work under the hood is key to finding and exploiting these subtle bugs.

\*Footnote: This was hard  :((

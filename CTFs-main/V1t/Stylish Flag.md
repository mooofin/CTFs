When the website opens up 

<img width="1242" height="495" alt="image" src="https://github.com/user-attachments/assets/9fb6b531-31ae-4ea5-ba48-26595ef2f050" />

The page souce has this - 

```

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Stylish Flag</title>
  <link rel="stylesheet" href="csss.css">
</head>

<body>
  <h1>where is the flag ;-;</h1>
  <br>
  <div hidden class="flag"></div>
</body>

</html>
```


The flag is encoded as pixel art using CSS box-shadow 
The `.flag` class has an 8×8px base element with hundreds of `box-shadow` offsets that create 8×8 pixel blocks forming readable text

So i extracted them and parsed all the `box-shadow` pixel coordinates .

```python
from PIL import Image
coords = {(int(x), int(y)) for pair in css_content.split(',') for x, y in [pair.split()]}
img = Image.new('RGB', (max(x for x,y in coords)+16, max(y for x,y in coords)+16), '#111')
for x,y in coords:
    for dx in range(8):
        for dy in range(8):
            img.putpixel((x+dx, y+dy), (0,255,0))
img.save('flag.png')
```

and got the flag  image 
<img width="4896" height="288" alt="image" src="https://github.com/user-attachments/assets/fff80946-22cd-4761-8c46-7684ff98639b" />

ALSOO i could just edit the opacity and the hidden tag and get the flag too which was more easier ! 


<img width="1144" height="310" alt="image" src="https://github.com/user-attachments/assets/f0280f1f-6774-49ef-9e62-70af56b4317b" />

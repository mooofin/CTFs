# picoCTF Challenge Write-Up: Decoding the Coordinates

## Challenge Overview
In this picoCTF challenge, we were given a set of geographic coordinates embedded within the flag format:

```
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

The goal of the challenge was to determine what these coordinates represent and extract the correct flag.

## Step 1: Identifying the Locations
To solve this challenge, we looked up each coordinate pair to find the corresponding city:

| Coordinates               | City               | Country           |
|---------------------------|--------------------|-------------------|
| (35.028309, 135.753082)   | Kyoto              | Japan             |
| (46.469391, 30.740883)    | Odesa              | Ukraine           |
| (39.758949, -84.191605)   | Dayton             | USA               |
| (41.015137, 28.979530)    | Istanbul           | Turkey            |
| (24.466667, 54.366669)    | Abu Dhabi          | UAE               |
| (3.140853, 101.693207)    | Kuala Lumpur       | Malaysia          |
| (9.005401, 38.763611)     | Addis Ababa        | Ethiopia          |
| (-3.989038, -79.203560)   | Loja               | Ecuador           |
| (52.377956, 4.897070)     | Amsterdam          | Netherlands       |
| (41.085651, -73.858467)   | White Plains       | USA               |
| (57.790001, -152.407227)  | Kodiak             | USA (Alaska)      |
| (31.205753, 29.924526)    | Alexandria         | Egypt             |

## Step 2: Extracting the Flag
Observing the city names, we noticed that the first letter of each city formed a meaningful phrase:

- **Kyoto, Odesa, Dayton, Istanbul, Abu Dhabi, Kuala Lumpur** → **KODIAK**
- **Addis Ababa, Loja, Amsterdam, White Plains, Kodiak, Alexandria** → **ALASKA**

The underscore in the given flag format suggests a separation between two words, which aligns perfectly with "KODIAK" and "ALASKA."

Thus, the final flag was:

```
picoCTF{KODIAK_ALASKA}
```

## Conclusion
This challenge tested our ability to recognize geographic coordinates and extract meaningful information from them. By systematically identifying each city and analyzing their initials, we successfully decoded the flag.

**Flag:** `picoCTF{KODIAK_ALASKA}` ✅

---

### Key Takeaways:
1. **Use online tools** like Google Maps to quickly find locations from coordinates.
2. **Look for patterns** in names or letters that could form a meaningful phrase.
3. **Underscores or separators** in the given format can hint at the structure of the final answer.

This challenge reinforced the importance of **geolocation lookups** and **pattern recognition** in CTF challenges!


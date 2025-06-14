```bash
$input = ".\input.txt"

$out = Get-Content -Path $input
$enc = [System.IO.File]::ReadAllBytes("$input")
$encoding = [system.Text.Encoding]::UTF8
$total = 264
$t = ($total + 1) * 5
$numLength = ($total * 30 ) + $t
if ($out.Length -gt 5 -or $enc.count -ne $numLength)
{
  Write-Output "Wrong format 5"
  Exit
}

else
{
  for($i=0; $i -lt $enc.count ; $i++)
  {
    if (($enc[$i] -ne 49) -and ($enc[$i] -ne 48) -and ($enc[$i] -ne 10) -and ($enc[$i] -ne 13) -and ($enc[$i] -ne 32))
    {
      Write-Output "Wrong format 1/0/"
      Exit
    }
  }
}

$blocks = @{}
for ($i=0; $i -lt $out.Length ; $i++)
{
  $r = $out[$i].Split(" ")
  if ($i -gt 0)
  {
    for ($j=0; $j -lt $r.Length ; $j++)
    {
    if ($r[$j].Length -ne 6)
    {
      Write-Output "Wrong Format 6" $r[$j].Length
      Exit
    }
      $blocks[$j] += $r[$j]
    }
  }
  else
  {
    for ($j=0; $j -lt $r.Length ; $j++)
    {
    if ($r[$j].Length -ne 6)
    {
      Write-Output "Wrong Format 6" $r[$j].Length
      Exit
    }
      $blocks[$j] = @()
      $blocks[$j] += $r[$j]
    }
  }

}


function Exit  {
  exit
}


function Random-Gen {
  $list1 = @()
  for ($i=1; $i -lt ($blocks.count + 1); $i++)
  {
    $y = ((($i * 327) % 681 ) + 344) % 313
    $list1 += $y
  }
  return $list1
}


function Scramble {
    param (
        $block,
        $seed
    )
    $raw = [system.String]::Join("", $block)
    $bm = "10 " * $raw.Length
    $bm = $bm.Split(" ")
    for ($i=0; $i -lt $raw.Length ; $i++)
    {

      $y = ($i * $seed) % $raw.Length
      $n = $bm[$y]
      while ($n -ne "10")
      {
        $y = ($y + 1) % $raw.Length
        $n = $bm[$y]
      }
      if ($raw[$i] -eq "1" )
      {
        $n = "11"
      }
      else
      {
      $n = "00"
      }
      $bm[$y] = $n
    }
    $raw2 = [system.String]::Join("", $bm)
    $b = [convert]::ToInt64($raw2,2)
    return $b
}


$result = 0
$seeds = @()
for ($i=1; $i -lt ($blocks.count +1); $i++)
{
  $seeds += ($i * 127) % 500
}

$randoms = Random-Gen
$output_file = @()
for ($i=0; $i -lt $blocks.count ; $i++)
{

  $fun = Scramble -block $blocks[$i] -seed $seeds[$i]
  if($i -eq 263)
  {
  Write-Output $seeds[$i]
  Write-Output $randoms[$i]
  Write-Output $fun
  }
  $result = $fun -bxor $result -bxor $randoms[$i]
  $output_file += $result
}
  Add-Content -Path output.txt -Value $output_file
```


#### 1. Reading input file

```powershell
$input = ".\input.txt"
$out = Get-Content -Path $input
$enc = [System.IO.File]::ReadAllBytes("$input")
$encoding = [system.Text.Encoding]::UTF8
```

* `$input` is the path to the input file.
* `$out` reads the file **line by line** as strings.
* `$enc` reads the file as an array of bytes (raw byte data).
* `$encoding` is set to UTF8 (unused later in the script).

---

#### 2. Length & format checks

```powershell
$total = 264
$t = ($total + 1) * 5
$numLength = ($total * 30 ) + $t

if ($out.Length -gt 5 -or $enc.count -ne $numLength)
{
  Write-Output "Wrong format 5"
  Exit
}
```

* `$total` is fixed at 264.
* `$t` and `$numLength` calculate expected byte count in the file:

  * `$numLength = (264 * 30) + (265 * 5) = 7920 + 1325 = 9245 bytes`
* It checks that the file length (bytes) matches this expected length.
* Also checks if the number of lines (`$out.Length`) is greater than 5.
* If either check fails, it exits with error "Wrong format 5".

---

#### 3. Byte content validation

```powershell
for($i=0; $i -lt $enc.count ; $i++)
{
  if (($enc[$i] -ne 49) -and ($enc[$i] -ne 48) -and ($enc[$i] -ne 10) -and ($enc[$i] -ne 13) -and ($enc[$i] -ne 32))
  {
    Write-Output "Wrong format 1/0/"
    Exit
  }
}
```

* Loops over every byte in the file.
* Checks if every byte is one of the following ASCII codes:

  * 49 = '1'
  * 48 = '0'
  * 10 = newline (LF)
  * 13 = carriage return (CR)
  * 32 = space
* If any byte is not one of these, it exits with "Wrong format 1/0/".

So the file should only contain '1', '0', spaces, and newline characters — basically some kind of textual binary data arranged in lines.

---

#### 4. Parsing input into blocks

```powershell
$blocks = @{}
for ($i=0; $i -lt $out.Length ; $i++)
{
  $r = $out[$i].Split(" ")
  if ($i -gt 0)
  {
    for ($j=0; $j -lt $r.Length ; $j++)
    {
      if ($r[$j].Length -ne 6)
      {
        Write-Output "Wrong Format 6" $r[$j].Length
        Exit
      }
      $blocks[$j] += $r[$j]
    }
  }
  else
  {
    for ($j=0; $j -lt $r.Length ; $j++)
    {
      if ($r[$j].Length -ne 6)
      {
        Write-Output "Wrong Format 6" $r[$j].Length
        Exit
      }
      $blocks[$j] = @()
      $blocks[$j] += $r[$j]
    }
  }
}
```

* `$blocks` is a hashtable/dictionary mapping from column index `$j` to an array of strings.
* For each line `$i` in `$out`, split the line by spaces into `$r`.
* For each part `$r[$j]`:

  * Check if length is exactly 6 characters (all substrings must be length 6).
  * For the first line (`$i -eq 0`), initialize `$blocks[$j]` as an array and add the 6-char string.
  * For subsequent lines, append the 6-char strings to the corresponding block.

**Effect:**
This reorganizes the input data column-wise, concatenating the 6-character strings vertically for each column into a "block".

---

#### 5. Define function `Exit`

```powershell
function Exit  {
  exit
}
```

* A custom function to call `exit` (probably for code clarity).

---

#### 6. Define function `Random-Gen`

```powershell
function Random-Gen {
  $list1 = @()
  for ($i=1; $i -lt ($blocks.count + 1); $i++)
  {
    $y = ((($i * 327) % 681 ) + 344) % 313
    $list1 += $y
  }
  return $list1
}
```

* Generates a list of integers (length = number of blocks).
* For each index `i` from 1 to block count:

  * Calculates a number `$y` by a deterministic formula involving modulo operations.
* Returns the list.

---

#### 7. Define function `Scramble`

```powershell
function Scramble {
    param (
        $block,
        $seed
    )
    $raw = [system.String]::Join("", $block)
    $bm = "10 " * $raw.Length
    $bm = $bm.Split(" ")
    for ($i=0; $i -lt $raw.Length ; $i++)
    {
      $y = ($i * $seed) % $raw.Length
      $n = $bm[$y]
      while ($n -ne "10")
      {
        $y = ($y + 1) % $raw.Length
        $n = $bm[$y]
      }
      if ($raw[$i] -eq "1" )
      {
        $n = "11"
      }
      else
      {
        $n = "00"
      }
      $bm[$y] = $n
    }
    $raw2 = [system.String]::Join("", $bm)
    $b = [convert]::ToInt64($raw2,2)
    return $b
}
```

* Takes a `$block` (array of strings concatenated earlier) and a `$seed` number.
* Joins the `$block` into one long string `$raw` of '1' and '0'.
* Initializes an array `$bm` with `"10"` repeated `$raw.Length` times (each element is "10").
* Then for each position `i` in `$raw`:

  * Calculates position `$y = (i * seed) mod raw length`.
  * Finds the next index `$y` where `$bm[$y]` is "10" (skipping until found).
  * If `$raw[$i]` is '1', set `$bm[$y] = "11"`, else "00".
* Joins the modified `$bm` array to a string `$raw2`.
* Converts the binary string `$raw2` (composed of pairs like "11","00","10") to a 64-bit integer.
* Returns the integer.

**Note:** The binary string `$raw2` can be very long, but only the last 64 bits will be converted (because of Int64).

This scrambling injects '1' or '0' bits into a mask based on the input block and seed, rearranged by `$y`.

---

#### 8. Main processing loop

```powershell
$result = 0
$seeds = @()
for ($i=1; $i -lt ($blocks.count +1); $i++)
{
  $seeds += ($i * 127) % 500
}

$randoms = Random-Gen
$output_file = @()
for ($i=0; $i -lt $blocks.count ; $i++)
{

  $fun = Scramble -block $blocks[$i] -seed $seeds[$i]
  if($i -eq 263)
  {
    Write-Output $seeds[$i]
    Write-Output $randoms[$i]
    Write-Output $fun
  }
  $result = $fun -bxor $result -bxor $randoms[$i]
  $output_file += $result
}
Add-Content -Path output.txt -Value $output_file
```

* Initializes `$result` to 0.
* Builds `$seeds` array with a formula for each block index.
* Calls `Random-Gen` to get `$randoms` array.
* For each block `i`:

  * Calls `Scramble` with the block and the seed.
  * If `i == 263` (the last block), outputs the seed, random number, and scramble result (debug info).
  * Updates `$result` by XORing with the scramble result and the random number.
  * Adds the updated `$result` to `$output_file` array.
* At the end, appends all `$output_file` values to `output.txt`.

---
* The output file is 
```bash
879059547225600221
71793452475485205
1148698281253257227
217070812329394967
1085086090799284516
4238685779263969
1085311228075820020
4486897510174167
879257471590075933
233062363111948053
879310247956329413
220620237942043428
864704387274818528
219564707018453810
1080930139169943704
284575531841633519
1095289279840717921
219827558966836273
922164813414728577
71789326353092547
922970468266331303
284624197914774733
935887582569446640
233341656386976839
1095496211378261093
270431259404009621
922112088142040996
271114274360574141
936480455350027154
14580558453485969
1149315982842597017
273649820165456770
1134960775807159720
69285389258153
868979240123514018
230541216188255296
1148645726972267632
72057336087430075
1135966209599275106
220398260916600638
1152010064483073927
271272397879702293
1139343700758887558
271077784355540943
1139146754428701768
4222399461461231
922326496319573062
283942073776672713
1081923578845401015
274442431825195106
1097967845536444498
16944574752682771
935675805365747915
67832102939014098
1081920473329287448
1073068336005587
1081721748899955656
55155024869773009
918738451380057054
274652781735887568
918791227752582714
270430592862047689
922960640253902083
17112864268238567
878479842607955275
229951587760733494
881632416504951469
1112495565767363
882638470697435530
17112815333330190
1151848652045611600
54057266045841968
919582927853977200
274441624099950113
881860882925030709
58476429884768707
869190591810957703
220606270746394268
1138496186912600710
288226252967132741
1139407393294925175
68609593282673765
1095272117148061322
68468771777351541
935689876626275940
287170512185785987
1098877480162557621
220452029779136139
1138341911719821923
287966424658087442
933159088420617518
57487952572330426
1084466749241033436
13735927918412192
881805026941256233
216450958350103112
1135821692603413223
284838396737815122
1148422235162410505
271130552259837474
922972957682372071
220675298603830864
1139406530802367886
18010259016859042
879323443101908642
284839262375919183
1149490972761796781
58493138394427981
922182117624696644
71780503401582160
922129603001122379
13464974967361
918750881951576401
57636189074621104
882438342200737477
233910087384579782
882635416186125660
288018432198980036
882691507922931320
229740485016616693
1081778432842190433
274504086948213472
919012484050846377
273870767986373374
1098653128292552208
17789823524785699
936484823391600233
288006061884174664
1135755039810466391
220610149264392545
923026816572866165
220673079782928545
1084509890119794064
57698195299630181
1098597714352143950
273662949817528928
1084245170751013532
233289910418682556
1152868676445159022
273861906596622869
1152062995421196783
16892006533755522
878202962169560357
219551526581911207
1081712678517132855
54901075530993324
1138351810784785110
287368617589457513
918959449055625535
68663387948777742
864744991438602546
17789270218755452
879100224243548756
18010272116257113
879323430003683923
284839275073057464
935837243715555216
233127265157825173
1098822166335471510
284585233327522172
1081089049280840078
66190813938289
1085311369869266603
217017417431055728
1085086103734386376
4238672944955073
868969548061077922
230585125518176963
1134964279694586486
58532504927404773
935903202292740735
13788713532460788
1098610032472277687
273808907837424086
1098611059250691362
287170705462591839
935904280600953359
54953797377651428
1081972437337034002
3431352717032734
882490899915869684
217017478683823314
1080880677300142569
3395020505739494
864760452650840824
68399248252862156
1152854450759479489
72056508471328536
1135967031275879667
220398260878299005
923237031130165425
220461087109169122
1081778639814733919
54940658191577131
1094599850818548609
271327652553490220
1080916961136738199
229961702408703798
868279998848633946
54044282154139485
879258544116612891
284625063628717240
879258296069853009
284798865657302933
1152867835705298073
55168202888248452
1138513488130130342
287107984222384471
1085089592271237237
271274871827451557
923224455449361838
67817894327611560
878469330928386996
270483416669012830
879274208876507235
220675540129136812
868980306940527370
230594235130183793
1094599899900607733
217282137553960044
1094652833283493100
283796252737158241
878482303020224500
270496420967206807
1138513245732277422
220675350747672793
1085300646950993669
14570660180524263
1149279867130331935
283727823485587214
1135765772921798622
55164714502340078
919001518395568616
14422035514995649
919002553226628642
270494089596571160
1081075896199954192
233909007654326019
1081765291043638494
3645104131685402
881847842601189364
287158284404650157
933353496081530906
288213815831556244
868082087813444404
71833031890124679
882441640700022534
233962879194169438
1151852763148127243
274455678322262261
869181263355903934
274442229753314412
1135751534516958032
71776131962646638
932248434541314171
229697655603511460
1149491014637175127
271063908134941100
936537392976704440
14636695302442350
1098824639182863983
216398129639732071
1084469432518917257
216177127761104710
```




The script expects an input file with:
- **5 lines** (checked via `$out.Length -gt 5`).
- Each line contains **264 blocks** (6-character binary strings like `"100001"`).
- Blocks are separated by **spaces**.
- Lines end with a **Unix-style `\n`** (not Windows `\r\n`).

### **How do we know there are 264 blocks per line?**
- The script calculates:
  ```powershell
  $total = 264
  $t = ($total + 1) * 5
  $numLength = ($total * 30) + $t
  ```
- Each block is **6 chars** + **1 space** = **7 chars per block**.
- Each line has **264 blocks × 7 = 1848 chars** + **1 (`\n`)** = **1849 chars total**.
- The script enforces this with `$r[$j].Length -ne 6`.

---

## **2. How the Script Processes the Input**
### **Step 1: Splitting into Blocks**
- Each line is split into **264 blocks** of 6 binary digits (`"100001"`, `"110011"`, etc.).
- The script then **groups blocks vertically** (not line-by-line):
  - `blocks[0]` = `line1[0] + line2[0] + line3[0] + line4[0] + line5[0]`
  - `blocks[1]` = `line1[1] + line2[1] + line3[1] + line4[1] + line5[1]`
  - ... and so on for all 264 blocks.

### **Step 2: Generating Seeds and Randoms**
The script creates two arrays:
1. **`$seeds`** = `(i * 127) % 500` (for `i` from 1 to 264)
2. **`$randoms`** = `((i * 327) % 681 + 344) % 313` (for `i` from 1 to 264)

These are **deterministic** (same every time) and used later for scrambling.

### **Step 3: The Scramble Function**
This is the **core transformation**:
1. Takes a **block** (e.g., `"100001110011..."`).
2. Initializes a **markers array** filled with `"?"` (unknown values).
3. For each bit (`0` or `1`) in the input:
   - Computes an **index** = `(i * seed) % length`.
   - If the index is taken, finds the next available slot.
   - Writes `"11"` if the bit is `1`, `"00"` if `0`.
4. Joins the markers into a **binary string** and converts it to an **int64**.

### **Step 4: XOR Mixing**
The scrambled numbers are **XORed** together with a rolling `$result` and `$randoms[i]`:
```powershell
$result = $fun -bxor $result -bxor $randoms[$i]
```
This creates a **chain of dependencies** between numbers.

---


   From the forward:

   ```
   result_i = Scramble_i XOR result_{i-1} XOR random_i
   ```

   Rearranged:

   ```
   Scramble_i = result_i XOR result_{i-1} XOR random_i
   ```

   Since `result_{-1} = 0` for i=0.

4. Once you get `Scramble_i`, invert the `Scramble` function to get back the original block bits.

---



* **Invert Scramble:**
  Scramble builds a mask `$bm` from an initial array of "10" strings and replaces them with "11" or "00" based on bits in the original block at positions mapped by `$y = (i * seed) % length`.

  To invert, you must know the seed, length, and output number, then reconstruct the original bits by reversing the mask manipulation.

* **Convert the integer back to binary mask string.**

---



```powershell
# === Reverse Scramble function ===
function Reverse-Scramble {
    param (
        [Int64] $scrambledValue,
        [int] $blockLength,
        [int] $seed
    )

    # Convert Int64 back to binary string padded to 2 * blockLength bits (because each bit encoded as 2 bits in mask)
    $binStr = [Convert]::ToString($scrambledValue, 2).PadLeft($blockLength * 2, '0')

    # Split into 2-bit chunks (like ["11","00","10"...])
    $maskArray = @()
    for ($i = 0; $i -lt $binStr.Length; $i += 2) {
        $maskArray += $binStr.Substring($i, 2)
    }

    # Initialize output bits array
    $originalBits = New-Object char[] $blockLength

    # We have to invert scrambling logic:
    # For i in 0..blockLength-1:
    # y = (i * seed) % blockLength
    # At position y in maskArray, maskArray[y] = "11" if original bit 1 else "00"
    # But if maskArray[y] != "10", that position is used, else keep moving forward circularly until found.

    for ($i = 0; $i -lt $blockLength; $i++) {
        $y = ($i * $seed) % $blockLength

        # Find the position y where maskArray[y] is "00" or "11" (not "10")
        $pos = $y
        while ($maskArray[$pos] -eq "10") {
            $pos = ($pos + 1) % $blockLength
        }

        # Original bit is 1 if mask is "11", else 0
        if ($maskArray[$pos] -eq "11") {
            $originalBits[$i] = '1'
        }
        elseif ($maskArray[$pos] -eq "00") {
            $originalBits[$i] = '0'
        }
        else {
            throw "Unexpected mask value at pos $pos: $($maskArray[$pos])"
        }
    }

    return -join $originalBits
}

# === Reverse the XOR chain to get all scrambled values ===
function Reverse-XOR-Chain {
    param (
        [Int64[]] $outputResults,
        [int[]] $randoms
    )

    $scrambleValues = @()
    $previous = 0
    for ($i = 0; $i -lt $outputResults.Count; $i++) {
        $scramble_i = $outputResults[$i] -bxor $previous -bxor $randoms[$i]
        $scrambleValues += $scramble_i
        $previous = $outputResults[$i]
    }
    return $scrambleValues
}

# === Example usage ===

# Load output.txt integers (one per line)
$outputResults = Get-Content -Path "output.txt" | ForEach-Object { [Int64]$_ }

# Recreate randoms and seeds as original script
$totalBlocks = $outputResults.Count

# Recreate randoms (from Random-Gen function)
function Random-Gen {
  param([int] $count)
  $list1 = @()
  for ($i=1; $i -le $count; $i++) {
    $y = ((($i * 327) % 681 ) + 344) % 313
    $list1 += $y
  }
  return $list1
}

$randoms = Random-Gen -count $totalBlocks

# Seeds as in original
$seeds = @()
for ($i=1; $i -le $totalBlocks; $i++) {
    $seeds += ($i * 127) % 500
}

# Get scrambled values by reversing XOR chain
$scrambledValues = Reverse-XOR-Chain -outputResults $outputResults -randoms $randoms

# Block length in bits: based on your input, each block concatenates 6-char strings per line and number of lines
# Here we must know the length of each block in bits.
# From original script:
# each block is made from concatenating the 6-char strings from each line
# So block length = number_of_lines * 6
# We can read lines from input file to get this info:

$inputLines = Get-Content -Path ".\input.txt"
$lineCount = $inputLines.Length

$blockLength = $lineCount * 6

# Now reverse each scrambled value to original block bits
$recoveredBlocks = @()
for ($i = 0; $i -lt $totalBlocks; $i++) {
    $bits = Reverse-Scramble -scrambledValue $scrambledValues[$i] -blockLength $blockLength -seed $seeds[$i]
    $recoveredBlocks += $bits
}

# $recoveredBlocks now contains strings of '0'/'1' representing the original block bits

# You can output or save them to file
$recoveredBlocks | Out-File -FilePath "recovered_blocks.txt"
```





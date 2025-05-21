# **Rust XOR Decryption Challenge Writeup**


### **Key Observations**
1. **Encrypted Data**: The flag is stored as an array of hex strings (`hex_values`).
2. **Decryption Key**: The XOR key is `"CSUCKS"`.
3. **String Mutation**: The decrypted flag should be appended to an existing mutable string (`party_foul`).

---

## **Step-by-Step Solution**

### **1. Convert Hex Strings to Bytes**
The encrypted flag is given as an array of hex strings:
```rust
let hex_values = ["41", "30", "20", "63", ...];
```
We need to convert these into a `Vec<u8>` for decryption:
```rust
let encrypted_buffer: Vec<u8> = hex_values.iter()
    .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
    .collect();
```
- `iter()`: Iterates over the hex strings.
- `map()`: Converts each hex string to a byte.
- `collect()`: Gathers the bytes into a `Vec<u8>`.

---

### **2. XOR Decryption with `xor_cryptor`**
The `XORCryptor` crate is used for decryption:
```rust
let key = String::from("CSUCKS");
let xrc = XORCryptor::new(&key).unwrap(); // Handle error if key is invalid
let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
```
- `XORCryptor::new(&key)`: Initializes the decryptor.
- `decrypt_vec()`: Decrypts the byte vector.

---

### **3. Modify a Borrowed String**
The challenge requires modifying an existing string (`party_foul`) inside the `decrypt` function.  
**Problem in Original Code**:  
The function took `&String`, which is immutable. To modify it, we need `&mut String`.

#### **Fix: Use Mutable References**
```rust
fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");
    // ... (decrypt and append flag)
}
```
In `main()`, we pass it as:
```rust
let mut party_foul = String::from("Using memory unsafe languages is a: ");
decrypt(encrypted_buffer, &mut party_foul);
```
- `mut party_foul`: Makes the string mutable.
- `&mut party_foul`: Passes a mutable reference to `decrypt`.

---

### **4. Final Output**
After decryption, the flag is appended to `party_foul` and printed:
```rust
borrowed_string.push_str(&String::from_utf8_lossy(&decrypted_buffer));
println!("{}", borrowed_string);
```
- `from_utf8_lossy()`: Converts bytes to a string (handles invalid UTF-8 gracefully).
- `push_str()`: Appends the decrypted flag.

---

## **Final Code**
```rust
use xor_cryptor::XORCryptor;

fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
    let key = String::from("CSUCKS");
    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");

    let xrc = XORCryptor::new(&key).unwrap();
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    
    borrowed_string.push_str(&String::from_utf8_lossy(&decrypted_buffer));
    println!("{}", borrowed_string);
}

fn main() {
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "0d", "c4", "60", "f2", "12", "a0", "18", "03", "51", "03", "36", "05", "0e", "f9", "42", "5b"];
    
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    let mut party_foul = String::from("Using memory unsafe languages is a: ");
    decrypt(encrypted_buffer, &mut party_foul);
}
```

### **Key Takeaways**
1. **Mutable References (`&mut`)**: Needed to modify borrowed variables.
2. **Hex to Bytes Conversion**: Use `u8::from_str_radix(hex, 16)`.
3. **Early Returns**: `return` works like in other languages.
4. **String Manipulation**: `push_str` modifies strings in-place.

---
```bash
C:\Users\SIDDHARTH U\projects\game>cargo run
warning: use of deprecated method `xor_cryptor::XORCryptor::<xor_cryptor::V1>::decrypt_vec`
  --> src\main.rs:18:32
   |
18 |     let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
   |                                ^^^^^^^^^^^
   |
   = note: `#[warn(deprecated)]` on by default

warning: `game` (bin "game") generated 1 warning
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.03s
     Running `target\debug\game.exe`
Using memory unsafe languages is a: PARTY FOUL! Here is your flag: picoCTF{4r3_y0u_h4v1n5_fun_y31?}
```

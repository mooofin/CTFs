# Escape the Wall - Unity CTF Challenge Writeup

## Challenge Description
Upon launching the game (`/win/pico.exe`), we find ourselves trapped inside a walled area with text at the top stating, **"Escape to find the flag."** The game, built with the Unity engine, allows movement using **W, A, S, D**, running, jumping, crouching, climbing ladders, and changing weapons with the scroll wheel.

While attempting to escape, we notice that reaching the large white flag is impossible due to an invisible wall blocking the final platform.

## Reverse Engineering with dnSpy
Since the game is made with Unity, we inspect its core logic by reverse engineering `Assembly-CSharp.dll`, which is located in the `pico_Data/Managed/` folder. Using **dnSpy**, we analyze the game's movement mechanics, particularly the jumping logic.

### Jumping Code Analysis
We locate the following code snippet handling the jump mechanics:

```csharp
if (Input.GetButton("Jump") && this.canMove && this.characterController.isGrounded && !this.isClimbing)
{
    this.moveDirection.y = this.jumpSpeed;
}
else
{
    this.moveDirection.y = y;
}
```

This condition checks:
- If the **Jump** button is pressed.
- If the player **can move**.
- If the player is **on the ground**.
- If the player is **not climbing**.

Only when all conditions are met does the character execute a jump.

## Modifying the Game to Bypass the Wall
To gain an unfair advantage, we edit the code in **dnSpy**:
- We remove `&& this.characterController.isGrounded` from the condition.
- This allows the player to **jump in mid-air**.

### Modified Code:
```csharp
if (Input.GetButton("Jump") && this.canMove && !this.isClimbing)
{
    this.moveDirection.y = this.jumpSpeed;
}
else
{
    this.moveDirection.y = y;
}
```

### Steps to Apply the Patch:
1. Open `Assembly-CSharp.dll` in **dnSpy**.
2. Locate the jump function.
3. Enter **Edit Mode**.
4. Remove `&& this.characterController.isGrounded`.
5. Save the modified DLL.
6. Relaunch the game.

## Retrieving the Flag
With this modification, we can now **jump multiple times in the air**, bypass the invisible wall, and reach the flag. As soon as we touch it, the flag appears on the screen.

Don't forget to submit the flag in the correct format:
```
picoCTF{<flag>}
```



## Screenshot
Below is a screenshot of the jump logic in **dnSpy**:

![Jump Logic in dnSpy](attachment:image.png)




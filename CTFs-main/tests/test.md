Ds speedrun blog hack 👍


We need to talk about how teleport works in darksouls first .
Three is sm called default position 
default pos is what the devs intended as a failsafe
There are 3 ways to warp or teleport in darksouls , which are 








<img width="679" height="207" alt="image" src="https://github.com/user-attachments/assets/9ae5b544-1bf8-4b17-a09c-cdb0ac6dc047" />







Before going more  i need to explain what a force quit is in darksouls : )


The Force Quit category in Dark Souls speedrunning revolves around a powerful sequence-breaking glitch known as the Wrong Warp.

What is Force Quit/Wrong Warp?
Mechanism: Speedrunners trigger a warp (via a bonfire, item, or death) and then manually force the game to close using the console or PC interface during the loading screen .
The Effect: By interrupting the loading process, the game loses track of the player's intended destination. Upon reloading the save, the game defaults the player to a specific coordinate within a new area instead of the intended one .
Ds was first released onxbox360 and ps3 

So suppose if i quit from here .

<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/fae9e3f8-f90a-48d2-8d45-a9bbd68f05c4" />



After using the force quit i would respawn into 

<img width="670" height="453" alt="image" src="https://github.com/user-attachments/assets/bf7fe025-403f-49e3-9c5c-b86d589142df" />


But a single area can have 2 points too , 

In the game files valley of drakes and new londo are considered the same area .

<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/02092f24-21a0-410d-b63b-26b988e6798f" />


So player can go to either of these 2 locations using wrong warp 👍


<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/198e5db1-bdf4-49a2-ae3b-96b28880b05e" />


So earlier versions used this to speedrun between places 

Now Lets dive more further . In ds each character has 2 variable buffer for the positions .
One is  immediate position and stores position .
Stored position is a set of coordinates written to the game's save file used to respawn the player character after a reload . Under normal circumstances, this is determined by the ground the character is standing on, meaning the game does not store a position while in the air 
Normally, the character's immediate position (where they are physically located) and their stored position remain in sync with a four-frame buffer, meaning the stored position is always four frames behind the immediate position when the character is moving .

<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/935090a8-6018-4959-86da-45a70324798f" />


However, the game implements specific rules for boss arenas to prevent players from respawning in the middle of active combat 
When a player is inside a boss arena, the game deliberately prevents the stored position from updating to the player's current location within the room. Instead, upon reloading the game, the system is designed to move the player back to the entrance of the boss arena . This mechanism ensures that the player doesn't spawn directly back into the heat of the boss fight, effectively resetting them to the designated entry point.


When using ladders in Dark Souls, the game handles your stored position differently to ensure you don't spawn in dangerous or broken areas. Here is how that mechanic functions:
Locking the Position: When you begin climbing a ladder, the game locks your stored position (the coordinates used for your respawn point) to the exact spot where the climb started 
The Storage State: As long as you are considered to be "on the ladder," this stored position remains fixed. This prevents the game from updating your coordinates as you move up or down the rungs Interrupting the State: The ladder storage glitch exploits this by using a riposte or backstab to interrupt the climbing animation. Because the game believes you are still on the ladder, it keeps your stored position locked to the base of the ladder, even if you run off to a completely different part of the map 
The Reset Mechanism: This persistent lock is why the game doesn't update your position while you are exploring. If you were to save and quit while this state is active, the game would attempt to reload you back at the coordinates of the ladder, which is the foundational mechanic behind the ladder warp .

<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/02f4ee0e-ec91-4aaf-ae55-e629bf0a541f" />


So when you dont do any actions such a climbing a ladder or pivoting your location is registered there itself .

Now how do we break the game with this ?

<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/70200f3d-f6e8-4507-aee1-2d1675186293" />







Head over here and deplete your stamina bar .
And we get a special animation because the game locks our positon as near the ladder as what happens when u get stamina depleted from the ladder ?

Coming back ? the two positons should be around the same and in sync as normal but deeper there is a 4 byte frame buffer between them 

<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/6fa2139b-1719-4520-9f0f-8e507541f987" />


So when a character is moving , the stored is always 4 frames behind .
As the ladder animation is triggered we write into the 4 byte buffer for frames and they are not updated as our character moves . 
I talked about how breaking the charcter with climbing another ladder breaks this .

When our character falls from the ladder theres a swinging animation . Interestingly theres another cool thing thats happening here .
<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/3022d70b-3857-471a-b788-3bf0e3f36468" />



To make the character do this , the game engine HAVOC does a 28 mico-second delay of disabling the gravity for the character .
<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/1e3e598d-36f0-45e4-a687-dba25c4849e3" />


Now we need to write the last buffer into out desired place to load back , so how do we do this ?
Just deplete your stamina and get the gravity null animation effect and this writes the last buffer with the current coordinates . 
The character does not spawn in the Undead Asylum because of a disconnect between two game variables: the stored position and the last area 
The Stored Position: Through the ladder storage glitch, the game keeps your respawn coordinates locked to the Asylum ladder 
The Last Area: This variable determines which map piece is prioritized during loading. Because you are physically standing at the Undead Merchant (in the Undead Burg), the game updates your last area to that location 
When you reload the game, the system attempts to reconcile these two conflicts: it moves you to the coordinates stored for the Asylum ladder, but it loads the Undead Burg map instead . Because your immediate position is now out of bounds relative to the loaded map, the character begins to fall through the void until it hits a valid collision point in the target area

Because the character is not technically touching the ground during these 28 frames, the game is unable to update the player's stored position immediately 
. This brief window allows the game to update the stored position for exactly one frame, replacing it with the ladder's coordinates while the last area variable updates to the current location (like the Undead Merchant) 
Falling Out of Bounds: Upon reloading, the game attempts to place the player at the Asylum ladder's coordinates, but because the Undead Burg map is loaded, the player spawns in mid-air, causing them to fall through the void .

More deeper diving . Tbh i left out one more variable the game generates called the last area . It dictates what part of the game should load while we play so to make the game optimised better . Regions are divided into navmeshes .

<img width="671" height="376" alt="image" src="https://github.com/user-attachments/assets/a97a2c15-afe8-4fec-b08e-0974aa530918" />


So we get a disconnect between the 2 variables 🙂

After reloading the game from here we get warped to the sky , bc its how darkouls game files are mapped . 
Now since both of those areas are connected , we get transported into the sky , essentially skipping a huge chunk of area , 

<img width="679" height="451" alt="image" src="https://github.com/user-attachments/assets/8accd111-71b2-4534-ba3a-60da2a4b6a10" />


But we are in the air rn and there’s still fall damage since the ladder frame is over written .
Falling from the ground usually kills us the second we hit the ground so there’s no gap to quit the game out or anything .
Thankful there are some mechanics in the game which can help us prevent getting the HP bar reduced to zero at the same instant . One is using the fall socery 

<img width="676" height="321" alt="image" src="https://github.com/user-attachments/assets/4870b346-6bd6-473c-a8b6-fb71833de0db" />

Using this we get an single extra frame which we can use to quit the game out while falling : )) .

Now thats out and our current status is we can teleport and wrap and fall down without getting killed .

We have essentially now reached unded parish because the undead asylum is directly placed above undead parish and the next place is Sen’s fortress
<img width="676" height="372" alt="image" src="https://github.com/user-attachments/assets/d4233bf3-6202-4843-ab34-99aa4c1fa4fe" />


There’s a lot of strats to go here so , do the one you’re comfortable with ig ?
Finish up here and reach towards anor londo . 
<img width="676" height="372" alt="image" src="https://github.com/user-attachments/assets/0eca5fb2-0e00-4eec-88af-16c7a4dca87c" />


Since we dont have any weapon right now and there’s legit no weapon in this area . We need someway to kill smough and orenstein .

There’s one viable way to cheese them that most people dont know .
Enemy AI checks for targets every 5 seconds :) , so with a precise animations you can actually make them un activated , how this target check works is , it’s bounded to the weapon toggle , so each weapon toggle resets the boss from  reaching that 5 second window to be

So after killing them , take the left elevator because it's actually slower than oreinsteins .


Shoot gwneviere with a single arrow , ( you need to have 12 dexterity )

<img width="1084" height="743" alt="image" src="https://github.com/user-attachments/assets/7bd1b635-e5bd-472e-b064-00a7a73eb240" />



Now go back and kill the bell gargoyls to get closer to ring the 2 bells , You still need it to ring the two bells to do the final wrong warp . 

Warp back to blightown and kill this NPC , as he will not kill the firekeeper when you come back 

<img width="194" height="259" alt="image" src="https://github.com/user-attachments/assets/88054957-6faf-444e-997d-f00171857fd5" />

We can pivot to using the glitch again here as the area discconects ;


<img width="1084" height="743" alt="image" src="https://github.com/user-attachments/assets/bc7bcced-d58a-4ba8-98b5-a59298f9ac0c" />

Here the new londo area loads first because it's much closer , and the glitch  again works ;

<img width="1056" height="810" alt="image" src="https://github.com/user-attachments/assets/27e0ff39-5da6-4b75-a2e4-a86e4d5ac40b" />
























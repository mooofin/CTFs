>I tried playing the game but sadly it seems rigged 

<img width="795" height="991" alt="image" src="https://github.com/user-attachments/assets/86bb4fa9-e9a4-4a5d-87c3-f10da941f2d7" />

 I got a fail popup menu from this and there are 897 tiles in the game so my approach for now is find that validation logic and and use cheat engine to get a workaround 

 
Since the name of the game is net.exe , i got an to use Dnspy to see the program logic . 

<img width="1917" height="998" alt="image" src="https://github.com/user-attachments/assets/ce1db4eb-18b2-4855-a227-c4baafbda3a1" />


We can see that these might be structs or tempplates the game has to  store the data 

After snooping around and seeing the functions i made some progress , when i identified the popup menus !

<img width="1906" height="1001" alt="image" src="https://github.com/user-attachments/assets/9a6dbf8b-1c88-44ac-a300-27999c9d3af8" />


this should be the output after patching , investigated more around here to see any flags but nah , 


Also i got where the value of 30 was stored :

<img width="1250" height="446" alt="image" src="https://github.com/user-attachments/assets/6e432068-38c7-4e49-a6d0-11680c5b5b44" />



And the function refering it was :

<img width="1329" height="419" alt="image" src="https://github.com/user-attachments/assets/b21be147-b31c-4a33-b615-cd4fa1483f9d" />

In the area for the Mine's files , this part stood out 


```csharp
using System;

namespace UltimateMinesweeper
{
	// Token: 0x02000004 RID: 4
	public class MineField
	{
		// Token: 0x17000003 RID: 3
		// (get) Token: 0x06000014 RID: 20 RVA: 0x00002AE4 File Offset: 0x00000CE4
		// (set) Token: 0x06000015 RID: 21 RVA: 0x00002AEC File Offset: 0x00000CEC
		public bool[,] MinesPresent
		{
			get
			{
				return this.minesPresent;
			}
			set
			{
				this.minesPresent = value;
			}
		}

		// Token: 0x17000004 RID: 4
		// (get) Token: 0x06000016 RID: 22 RVA: 0x00002AE4 File Offset: 0x00000CE4
		// (set) Token: 0x06000017 RID: 23 RVA: 0x00002AEC File Offset: 0x00000CEC
		public bool[,] GarbageCollect
		{
			get
			{
				return this.minesPresent;
			}
			set
			{
				this.minesPresent = value;
			}
		}

		// Token: 0x17000005 RID: 5
		// (get) Token: 0x06000018 RID: 24 RVA: 0x00002AF5 File Offset: 0x00000CF5
		// (set) Token: 0x06000019 RID: 25 RVA: 0x00002AFD File Offset: 0x00000CFD
		public bool[,] MinesVisible
		{
			get
			{
				return this.minesVisible;
			}
			set
			{
				this.minesVisible = value;
			}
		}
```

we could change this to and set a break here with flag = flase or void , and it should show the area where the mines dont exist  . 

I tried following this up , but then id have to click around 1000 boxes : ( 



The microsoft documentation tells us 


Raise events with an event sender
An event is a message sent by an object to signal the occurrence of an action. The action might be user interaction, such as a button press, or it might result from other program logic, such as a property value change. The object that raises the event is called the event sender. The event sender doesn't know the object or method that receives (handles) the events it raises. The event is typically a member of the event sender. For example, the Click event is a member of the Button class, and the PropertyChanged event is a member of the class that implements the INotifyPropertyChanged interface.

To define an event, you use the C# event or the Visual Basic Event keyword in the signature of your event class, and specify the type of delegate for the event. Delegates are described in the next section.



We should investigate more on the mine controll and and see if there are any event handlers in the disass tool 


Which leads us to this :

<img width="1915" height="1012" alt="image" src="https://github.com/user-attachments/assets/da30b47c-40fd-4349-b00a-99f3f03d675e" />


This code handles mouse clicks in a Minesweeper game grid. When you click on the game board, it first figures out which cell you clicked by dividing your mouse position by the cell size to get row and column coordinates.

If you right-click, it toggles a flag on that cell - switching between flagged and unflagged states. The board redraws itself to show the change, and an event notifies other parts of the game about the flag change so it can update things like the remaining mines counter.

If you left-click, it reveals that cell by marking it as visible. Again, the board redraws, and if the cell wasn't already revealed, an event fires to tell the game logic which square was opened. This event likely triggers the logic to check if you hit a mine or need to cascade-reveal adjacent empty squares.

The code also tracks whether this is your very first click in the game. Minesweeper games typically use the first click to either start the timer or guarantee you don't immediately hit a mine by generating the mine positions after that first click. Once any click happens (left or right), it sets a flag and fires a `FirstClick` event to kick off the game.

<img width="1348" height="425" alt="image" src="https://github.com/user-attachments/assets/8341ef9f-be84-4d1a-ba90-7f381462c53f" />

After running it setting a break point here and opening the debug menu :



<img width="1328" height="879" alt="image" src="https://github.com/user-attachments/assets/a28532c0-53b4-4f18-b131-c69931b07603" />


num2 and num have the values of (28,7) in hexadecimal , 

What we need to do now is to process three times, once for each safe square. Click anywhere, modify the coordinates to match a safe square, resume. Click anywhere again, modify to match the second safe square, resume. Click one final time, modify to match the third safe square, and resume. The point isto match  variables to match one of the safe square coordinates like 28 , 7  then let the game continue running. The game has no idea you modified anything

<img width="1919" height="999" alt="image" src="https://github.com/user-attachments/assets/d889739c-e003-40eb-b49c-5e5fa64adb3a" />



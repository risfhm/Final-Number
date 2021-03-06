# RULES AND OTHER INFORMATION

## What is Final Number?

**[Final Number](https://github.com/risfhm/Final-Number)** is a game of choices based on luck and logic, the game has three main elements: Random Number, Final Number, and a Subtractor.

## How this game works?

The main objective of this game is to find the Final Number fromthe Random Number and Subtractor. In short, the Final Number is the result of subtracting the Random Number and Subtractor from this numerical expression: `(random - sub = final_number)`.

There is a system of modes, difficulty and levels to turn the game into something more challenging and dynamic. Below is an explanation of each system: 


* **Modes**: there are two game modes (Casual Mode  and Extreme Mode). The difference between them is the jump (the jump is a number that will be incremented to the initial value until reaching the last level) between each level.

	-  Casual Mode: 2 (jump)
	- Extreme Mode:10 (jump)<br><br>


* **Levels**: the game is divided into 5 levels that vary according to a jump defined by the game mode, on each level the MAX value (the maximum number in the range 1 to MAX) is incremented with the value of the jump defined by the chosen mode (Casual or Extreme).


* **Difficulty**: the difficulty system (Easy, Normal, Hard, Very Hard) defines the amount of attempts the user has for each level.

	* Easy: 5
	* Normal: 3
	* Hard: 2
	* Very Hard: 1<br><br>

	
* **Value Characteristics**:

	1. The Random Number value is generated according to the MAX value at each level, then the 
        MAX is incremented and a new value for Random is generated.
	2. The Final Number value cannot be less than or equal to zero and also must not be greater 
        than the current MAX of the round.
	3. The value of the Subtractor can be negative and does not have the restrictions of the 
        Final Number.
	4. The MAX value always changes according to the jump when the player advances levels and
        consequently the value of the Random Number.
		
## Additional software information

* The game includes a colorization system for the displayed content, so it is easy to understand the information information on the screen:

<p align="center">
  <img height=260 src="assets/main_menu.png" alt="Main Menu - Final Number">
</p>


* There is a final report generation system at the end of the game (reaching level 5 and winning it) that integrates the main data of your game: game mode, difficulty, number of failures to win the game, and more.

<p align="center">
  <img src="assets/report.png" alt="Report Screen - Final Number">
</p>


* The number of failures in the final report defines the amount of wrong moves a certain player faced until he won the game (this amount is cumulative from the moment the player started playing and not restarting after a Gamer Over).

<p align="center">
  <img src="assets/ex3.png" alt='Statistics - Final Number'>
</p>

* There is a naming and swapping system in the game where a player can choose any name to be represented during the game in the necessary reports and messages.

<p align="center">
  <img src="assets/ex.png" alt='Changing name - Final Number'>
</p><br>
<p align="center">
 <img src="assets/ex2.png" alt='JSON - Final Number'>
</p>


Read more: `final-number.py --help`

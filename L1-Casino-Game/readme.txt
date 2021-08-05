
Here we will try to make a little program that we will call ZCasino. 
It will be a very simplified little roulette game in which you can bet a certain amount and win or lose money.
When you run out of money, you have lost.

Rules of the game:

The player bets on a number between 0 and 49 (50 numbers in all). By choosing his number, he deposits the amount he wishes to bet.

Roulette is made up of 50 squares ranging naturally from 0 to 49. Even numbers are black, odd numbers are red. 
The croupier starts the roulette wheel, releases the ball and when the roulette wheel stops, notes the number of the box in which the ball stopped.
The number on which the ball landed is, of course, the winning number.

If the winning number is the one on which the player has bet (probability of 1/50, rather low), the croupier gives him 3 times the amount bet.

Otherwise, the dealer looks to see if the number bet by the player is the same suit as the winning number (whether they are both even or both odd). 
If this is the case, the croupier gives him 50% of the amount wagered. If this is not the case, the player loses his bet.

In the two winning scenarios seen above (the wagered number and the winning number are identical or have the same suit),
the dealer gives the player the amount initially wagered before adding his winnings. 
This means that, in these two scenarios, the player gets the money back. It is only in the third case that he loses the amount wagered. 
We will use the dollar $ instead of the euro as currency for encoding reasons in the Windows console.


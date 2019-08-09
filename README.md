# Monty-hall-problem-tester
Does counter intuitive Monty Hall problem even true???

You can play games here[https://betterexplained.com/articles/understanding-the-monty-hall-problem/]

## Let's try
You can run with following command. 100000 samples.

`python monty_hall_machine.py --test_num 100000`

## Result
```bash
Stick win ratio: 33.398%, Switch win ratio: 66.602%
```

Wow!! It actually have higher winning ratio if you switch.
What the hell is happening?

## Let's investigate!!
Let's run following command to see what is happening. (10 samples with rendering)

`python monty_hall_machine.py --test_num 10 --render`

```bash
0th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| 1st  || Win  ||      |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

1th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
|      || 1st  || Win  |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

2th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| 1st  || Win  ||      |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

3th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
|      ||      || W 1  |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

4th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| Win  ||      || 1st  |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

5th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| Win  || 1st  ||      |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

6th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
|      || W 1  ||      |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

7th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| W 1  ||      ||      |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

8th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| 1st  ||      || Win  |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

9th
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
|      || 1st  || Win  |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|
Stick win ratio: 30.0%, Switch win ratio: 70.0%
```
"Win": Win door. The door which has a prize behind.
"1st": 1st choice of a player among the three doors.
"W 1": "Win"+"1st". The label if the 1st choice of a player is actually a "Win" door. 
"   ": One of the doors without label will be opened by Monty after the first choice.

By checking the rendering, you will be realized that there are essentially only 3 patterns since a player can choose one out of three doors.
```bash
Pattern1                      Pattern2                      Pattern3
 door1   door2   door3         door1   door2   door3         door1   door2   door3  
 ______  ______  ______        ______  ______  ______        ______  ______  ______
|      ||      ||      |      |      ||      ||      |      |      ||      ||      |
|      ||      || W 1  |      |      || 1st  || Win  |      | 1st  ||      || Win  |
|.     ||.     ||.     |      |.     ||.     ||.     |      |.     ||.     ||.     |
|      ||      ||      |      |      ||      ||      |      |      ||      ||      |
|______||______||______|      |______||______||______|      |______||______||______|
```
When the door on the far right is the winner, player can choose right door (Pattern1), middle door (pattern2), left door (pattern3). If you choose to stick to the first door, obviously has only 1/3 of the chance to choose the winner.


Then what happen in the pattern2 and pattern3 case? Well, the point of this game is that Monty knows which door is the winner and he will opens the door that is not the winner after you make the first choice. So, actually it will be like the following.
```bash
Pattern2                      Pattern3                 
 door1   door2   door3         door1   door2   door3   
 ______  ______  ______        ______  ______  ______  
|\    /||      ||      |      |      ||\    /||      | 
| \  / || 1st  || Win  |      | 1st  || \  / || Win  |
|  \/  ||.     ||.     |      |.     ||  \/  ||.     |
|  /\  ||      ||      |      |      ||  /\  ||      |
|_/__\_||______||______|      |______||_/__\_||______|
```



Okay, at this point, how many door you can choose as a "2nd" choice if you "switch" rather than "stick" to the original choice?
Yeah, there is only one 2nd choice you can make. Yes, to the winner.
```bash
Pattern2                      Pattern3                 
 door1   door2   door3         door1   door2   door3   
 ______  ______  ______        ______  ______  ______  
|\    /||      ||      |      |      ||\    /||      | 
| \  / || 1st  || Win  |      | 1st  || \  / || Win  |
|  \/  ||.     ||.     |      |.     ||  \/  ||.     |
|  /\  ||      || 2nd  |      |      ||  /\  || 2nd  |
|_/__\_||______||______|      |______||_/__\_||______|
```
As you see, in pattern2 and pattern3, you can 100% win if you switch, and the probability that you will be in those pattern is 2/3.
What if you switch the door in pattern1? You will miss the prize.

## You can describe this phenomemon in other way like this too.
When you make the first choice (say door1), your winning chance is 1/3, and the rest of doors has 2/3 of chance of winning.
```bash
 door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| 1st  ||      ||      |
|.     ||.     ||.     |
|      ||      ||      |
|______||______||______|

|______||______________|
  1/3          2/3
```

After Monty opens one of the non-winner door (say door3), your door still has 1/3 of winning chance, so rest of the doors still has 2/3 of winning chance. But wait!? There is only one door left because Monty kills one of it...
```bash
 door1   door2   door3
 ______  ______  ______
|      ||      ||\    /|
| 1st  ||      || \  / |
|.     ||.     ||  \/  |
|      ||      ||  /\  |
|______||______||_/__\_|

|______||______|
  1/3     2/3
```
Yes. Believe or not, door2 has winning chance of 2/3, the combined probabilities of door2 and door3.

## Conclusion
No doubt. Just switch your choice when you have an opportunity to play a Monty Hall game.

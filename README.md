# Monty-hall-problem-tester
Does counter intuitive Monty Hall problem even true???



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

By checking the rendering, you know that there are essentially only 3 patterns since a player can choose one out of three doors.
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
When the door on the far right is the winner, player can choose right door (Pattern1), middle door (pattern2), left door (pattern3). If you choose to stick to the first door. 


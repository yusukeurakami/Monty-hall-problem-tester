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
|      || 1st  || Win  |
|      ||      ||      |
 ------  ------  ------

1th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| W 1  ||      ||      |
|      ||      ||      |
 ------  ------  ------

2th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| 1st  ||      || Win  |
|      ||      ||      |
 ------  ------  ------

3th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
|      ||      || W 1  |
|      ||      ||      |
 ------  ------  ------

4th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| Win  ||      || 1st  |
|      ||      ||      |
 ------  ------  ------

5th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| Win  ||      || 1st  |
|      ||      ||      |
 ------  ------  ------

6th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| 1st  ||      || Win  |
|      ||      ||      |
 ------  ------  ------

7th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
|      ||      || W 1  |
|      ||      ||      |
 ------  ------  ------

8th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
|      ||      || W 1  |
|      ||      ||      |
 ------  ------  ------

9th
  door1   door2   door3
 ______  ______  ______
|      ||      ||      |
| Win  || 1st  ||      |
|      ||      ||      |
 ------  ------  ------
Stick win ratio: 40.0%, Switch win ratio: 60.0%
```



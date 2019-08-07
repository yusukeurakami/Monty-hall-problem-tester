# Monty-hall-problem-tester
Does counter intuitive Monty Hall problem even true???



## Let's try
You can run with following command (10 samples with rendering)

`python monty_hall_machine.py --test_num 100000`

## Result
```bash
Stick win ratio: 33.398%, Switch win ratio: 66.602%
```

Wow!! It actually have higher winning ratio if you switch.
What the hell is happening?

## Let's investigate!!
Let's run following command to see what is happening.

`python monty_hall_machine.py --test_num 10 --render`

```bash
 ______  ______  ______
|      ||      ||      |
|      || W 1  ||      |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
| 1st  ||      || Win  |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
| 1st  ||      || Win  |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
|      ||      || W 1  |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
|      || 1st  || Win  |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
| Win  || 1st  ||      |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
| Win  || 1st  ||      |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
|      || W 1  ||      |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
| 1st  || Win  ||      |
|      ||      ||      |
 ------  ------  ------
 ______  ______  ______
|      ||      ||      |
| 1st  ||      || Win  |
|      ||      ||      |
 ------  ------  ------
Stick win ratio: 30.0%, Switch win ratio: 70.0%
```



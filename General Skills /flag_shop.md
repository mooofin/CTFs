![image](https://github.com/user-attachments/assets/5b3cbf04-cd3f-45b2-8306-065df0267d80)

## Writeup: Flag Shop 







The code for purchasing fake flags is:

```c
if(auction_choice == 1){
    printf("These knockoff Flags cost 900 each, enter desired quantity\n");
    int number_flags = 0;
    fflush(stdin);
    scanf("%d", &number_flags);
    if(number_flags > 0){
        int total_cost = 0;
        total_cost = 900*number_flags;
        printf("\nThe final cost is: %d\n", total_cost);
        if(total_cost <= account_balance){
            account_balance = account_balance - total_cost;
            printf("\nYour current balance after transaction: %d\n\n", account_balance);
        }
        else{
            printf("Not enough funds to complete purchase\n");
        }
    }
}
```

At first glance, it looks safe:

* `total_cost` = 900 × number of fake flags
* If the total cost ≤ account balance, it’s subtracted from the balance.

However, notice:

* `total_cost` is a signed integer (`int`), meaning it has a maximum value of 2,147,483,647.
* If `number_flags` is large enough, `900 * number_flags` will exceed this limit and **overflow**, wrapping around to a negative number.

---

### Exploiting Integer Overflow

If `total_cost` becomes negative, then:

```c
account_balance = account_balance - (negative total_cost)
```

Which effectively **increases** your account balance!

---

### Calculation

We want to find a `number_flags` large enough to make `total_cost` negative.

```
900 * number_flags > 2,147,483,647  →  number_flags > 2,386,093
```

Trying a large value like 3,000,000:

```
total_cost = 900 * 3,000,000 = 2,700,000,000
```

Since `2,700,000,000 > 2,147,483,647`, the result **overflows** and becomes negative.

---

### Result

With `total_cost` negative, the condition:

```c
if(total_cost <= account_balance)
```



## HOW TO RUN PROGRAM

- Install python3
- Run this command :

```$ ipython```

```import main``` <br>
```abid = main.Cart(1,1000000000)``` <br>
```abid.add_to_cart()``` <br>
```
{
    select the id of the item you want to buy: 1
    How many do you want: 2
    Checkout? (y/n): y
}
```
```abid.add_to_cart()```
```
{
    select the id of the item you want to buy: 2
    How many do you want: 3
    Checkout? (y/n): n

    select the id of the item you want to buy: 3
    How many do you want: 1
    Checkout? (y/n): n

    select the id of the item you want to buy: 3
    How many do you want: 4
    Checkout? (y/n): n

    select the id of the item you want to buy: 3
    How many do you want: 2
    Checkout? (y/n): y
}
```
```abid.remove_from_cart()```
```
{
    Select id of the item you want remove.: 2
    Do you want to continue removing from cart? (y/n)n
}
```
```abid.checkout_and_pay()```
```
{
    ([{'id': 1, 'name': 'Pisang Hijau', 'unit price': 150000, 'stock': 98.0},
  {'id': 2, 'name': 'Semangka Kuning', 'unit price': 60000, 'stock': nan},
  {'id': 3, 'name': 'Apel Merah', 'unit price': 150000, 'stock': 98.0},
  {'id': 3, 'name': 'Apel Merah', 'unit price': 150000, 'stock': 98.0},
  {'id': 3, 'name': 'Apel Merah', 'unit price': 150000, 'stock': 98.0},
  {'id': 4, 'name': 'Semangka Merah', 'unit price': 60000, 'stock': nan}],
 1,
 998800000.0,
 [{'id': 1,
   'name': 'Pisang Hijau',
   'unit price': 150000,
   'stock': 100,
   'quantity': 2},
  {'id': 3,
   'name': 'Apel Merah',
   'unit price': 150000,
   'stock': 100,
   'quantity': 2},
  {'id': 3,
   'name': 'Apel Merah',
   'unit price': 150000,
   'stock': 100,
   'quantity': 2},
  {'id': 3,
   'name': 'Apel Merah',
   'unit price': 150000,
   'stock': 100,
   'quantity': 2}])
}
```
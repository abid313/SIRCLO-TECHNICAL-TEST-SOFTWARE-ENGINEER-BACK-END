## HOW TO RUN PROGRAM

- Install python3
- Run this command :

```$ ipython```

```import main``` <br>
```abid = main.Cart(1,1000000000)``` <br>
```abid.add_to_cart()``` <br>
```
{
    ** ADD AN ITEM TO CART **
       id             name  unit price  stock
    0   1     Pisang Hijau      150000    100
    1   2  Semangka Kuning       60000    100
    2   3       Apel Merah      150000    100
    3   4   Semangka Merah       60000    100
    select the id of the item you want to buy: 1
    How many do you want: 2
    Checkout? (y/n): n
    ** ADD AN ITEM TO CART **
       id             name  unit price  stock
    0   1     Pisang Hijau      150000    100
    1   2  Semangka Kuning       60000    100
    2   3       Apel Merah      150000    100
    3   4   Semangka Merah       60000    100
    select the id of the item you want to buy: 2
    How many do you want: 3
    Checkout? (y/n): n
    ** ADD AN ITEM TO CART **
       id             name  unit price  stock
    0   1     Pisang Hijau      150000    100
    1   2  Semangka Kuning       60000    100
    2   3       Apel Merah      150000    100
    3   4   Semangka Merah       60000    100
    select the id of the item you want to buy: 3
    How many do you want: 1
    Checkout? (y/n): n
    ** ADD AN ITEM TO CART **
       id             name  unit price  stock
    0   1     Pisang Hijau      150000    100
    1   2  Semangka Kuning       60000    100
    2   3       Apel Merah      150000    100
    3   4   Semangka Merah       60000    100
    select the id of the item you want to buy: 3
    How many do you want: 4
    You already have this item in your cart
    Checkout? (y/n): n
    ** ADD AN ITEM TO CART **
       id             name  unit price  stock
    0   1     Pisang Hijau      150000    100
    1   2  Semangka Kuning       60000    100
    2   3       Apel Merah      150000    100
    3   4   Semangka Merah       60000    100
    select the id of the item you want to buy: 3
    How many do you want: 2
    You already have this item in your cart
    Checkout? (y/n): y
}
```
```abid.remove_from_cart()```
```
{
    Here is your cart:
       id             name  unit price  stock  quantity
    0   1     Pisang Hijau      150000    100         2
    1   2  Semangka Kuning       60000    100         3
    2   3       Apel Merah      150000    100         4
    To quit type a value of id that is not in your cart

    Select id of the item you want remove.: 2
    Do you want to continue removing from cart? (y/n)n
}
```
```abid.checkout_and_pay()```
```
{
        Index(['id', 'name', 'unit price', 'stock', 'quantity'], dtype='object')
    Index(['id', 'name', 'unit price', 'stock', 'quantity_x', 'cart_name',
           'cart_price', 'cart_stock', 'quantity_y'],
          dtype='object')
    Out[5]: 
    ([{'id': 1, 'name': 'Pisang Hijau', 'unit price': 150000, 'stock': 98.0},
      {'id': 2, 'name': 'Semangka Kuning', 'unit price': 60000, 'stock': nan},
      {'id': 3, 'name': 'Apel Merah', 'unit price': 150000, 'stock': 96.0},
      {'id': 4, 'name': 'Semangka Merah', 'unit price': 60000, 'stock': nan}],
     1,
     999100000.0,
     [{'id': 1,
       'name': 'Pisang Hijau',
       'unit price': 150000,
       'stock': 100,
       'quantity': 2},
      {'id': 3,
       'name': 'Apel Merah',
       'unit price': 150000,
       'stock': 100,
       'quantity': 4}])
}
```
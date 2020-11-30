# Shopping Cart REST API 

This is the REST API which performs CRUD operations on users and items and also adds, deletes or removes cart items for a user.

## Getting Started
1. You need to have a mongodb server running on host localhost and port 27017
2. You have to clone this repository and then run the app.py file using
```python app.py ```
3. After that, use a REST api client such as Postman or Insomnia to use one of the following API operations on base URL http://localhost:5000/: 

### Users
1. Get all users : /users
2. Add a user    : /user/add
3. Update a user : /user/update/<uid>
4. Delete a user : /user/delete/<uid>
5. Get a user    : /user/<uid>
  
<img src="https://i.ibb.co/n898n3r/Screenshot-from-2020-11-30-11-12-03.png" />

### Items
1. Get all items : /items
2. Add a item    : /item/add
3. Update a item : /item/update/<itemid>
4. Delete a item : /item/delete/<itemid>
5. Get an item   : /item/<itemid>

<img src="https://i.ibb.co/5cbD1SQ/Screenshot-from-2020-11-30-11-14-42.png" />

### Cart
1. Add cart item    : /user/<u_id>/cart/add/<item_id>
2. Remove cart item : /user/<uid>/cart/delete/<item_id>
3. Discard cart     : /user/<uid>/cart/delete

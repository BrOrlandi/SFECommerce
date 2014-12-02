API Documentation
=================

Resources
------
**Product:**    
`/api/products`  
*GET:* id, name, categories  
require vendor:  
*POST:* name, stock, description, price, is_available, categories(array)  
*PUT:* id, name, stock, description, price, is_available, categories(array)  
*DELETE:* id  
  
**Category:**  
`/api/categories`  
*GET:* id, name  
require vendor:  
*POST:* name  
*PUT:* id, name  
*DELETE:* id  
  
**Order:**  
`/api/orders`  
*GET:* id, user_id  
  
**User:**  
`/api/users`,`/api/admins`,`/api/vendors`,`/api/customers`  
require admin:  
*GET:* id, name, email  

Controllers
-----

**User**:  
  
`/register`  
*POST:* name, email, password,birth_date  
  
`/login`  
*POST:*  email, password  
  
`/logout`  
require login  
*GET:*   
  
`/users/<int:user_id>/set_vendor`  
require admin  
*GET:*  
- Set an user to vendor  
  
`/users/<int:user_id>/set_admin`  
require admin  
*GET:*  
- Set an user to Admin  
  
`/me`  
require login  
*GET:*  
- Get logged user: id, name, email, birth_date, register_date  
  
**Order:**  
  
`/cart`  
require login  
*GET:*  
- Get logged User's Cart, actually is an Order object.  
  
`/cart/add_product`  
require login  
*POST:* id, quantity  
- Will add the product with given ID and quantity to the User's Cart  
  
`/cart/remove_product`  
require login  
*POST:* id  
- Will remove the product with OrderProduct id given from the Cart.  
  
`/cart/close_order`  
require login  
*GET:*  
- Will close the order and set it to 'Awaiting Payment' status.  
  
`/order/update_status`  
require vendor  
*POST:* id, status  
- Will set the Order with given ID to the given Status text. E.g.: Payment Confirmed, Sent, Delivered.  
  
  





from cart import add_to_cart, remove_from_cart

def my_cart_view(request):
  #assign functions to variables for template rendering
  add_item = add_to_cart()
  remove_item = remove_from_cart()
  return render(request,'index.html',{'add_item':add_item,'remove_item':remove_item})
def ecom():
    l=[]
    ch=int(input("Enter your choice 1.Add to cart\n 2.Remove from cart\n 3.Search for a product in cart\n 4.Display all products in card 5.Show total no of products in cart\n 6.sort items alphabetically\n 7.clear the cart\n 8.Exit\n"))
    while ch!=8:
        if ch==1:
            n=str(input("Enter product to add:"))
            l.append(n)
            print(n,"added to cart:")
        elif ch==2:
            n=str(input("enter product to remove"))
            if n in l:
                l.remove(n)
                print(n,"removed from cart")
            else:
                print("product not found")
        elif ch==3:
            n=str(input("Enter product to search:"))
            if n in l:
                print("Product found in cart")
            else:
                print("not found")
        elif ch==4:
             print("Display all products:",l)
        elif ch==5:
             print("total products in cart:",len(l))
        elif ch==6:
             l.sort()
             print("sorted:",l)
        elif ch==7:
             l.clear()
             print("cart is empty:",l)
        else:
             print("enter valid choice")
        ch=int(input("enter choice"))
ecom()
      
    
    
                 

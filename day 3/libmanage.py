def library():
    lib={}

    ch=int(input("1.Add a book\n 2.Remove a book\n 3.search for a book\n 4.Display all books\n 5.Count total no of books\n 6.check if book title exists\n 7.Exit\n "))
    while ch!=7:
        if ch==1:
            bid=int(input("enter book id:"))
            bname=str(input("enter book name:"))
            lib[bid]=bname
            print("added succesfully")
        elif ch==2:
            bid=int(input("enterv book id:"))
            if bid in lib:
                removed=lib.pop(bid)
                print("removed succesfully")
            else:
                print("book does not exist")
        elif ch==3:
            bid=int(input("enter book id:"))
            if bid in lib:
                print("book found:")
            else:
                print("book not found")
        elif ch==4:
            bid=int(input("enter book id"))
            bname=str(input("enter book name:"))
            if bid in lib:
                lib[bid]=bname
                print("updated succesfully")
            else:
                print("bid not found")
        elif ch==5:
            print(lib)
        elif ch==6:
            print("total no of books",len(lib))
        elif ch==7:
            banme=str(input("enter book name:"))
            if bname in lib:
                print("book exists")
            else:
                print("book doent exist")
        else:
            print("enter valid ch")
        ch=int(input("enter choice"))
library()


import billing as bl
def main():
    cart={
        "Phone":56000,
        "Tv":100000,
        "headphones":2000
    }
    bl.generate_invoice(cart,10,18)
if __name__=="__main__":
    main()
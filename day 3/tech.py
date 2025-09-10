def tech(d1,d2,d3):
    d1=set(email.lower() for email in d1)
    d2=set(email.lower() for email in d2)
    d3=set(email.lower() for email in d3)
    attended_all=d1|d2|d3
    print("unique attendees:",attended_all)
    three_days=d1&d2&d3
    print("ppl who attended all 3 days:",three_days)
    only_oneday= (d1-(d2|d3))|(d2-(d1|d3))|(d3-(d1|d2))
    print("ppl who attended only 1 day:",only_oneday)
    overlap1=d1 & d2
    overlap2=d2 & d3
    overlap3=d1 & d3
    print("ppl who attended day 1 and 2",overlap1)
    print("ppl who attended day 2 and 3:",overlap2)
    print("ppl who attended day 1 and 3:",overlap3)
d1=["bhavana@gmail.com","gayathri@gmail.com","arun@gmail.com"]
d2=["gayathri@gmail.com","lyca@gmail.com","arun@gmail.com"]
d3=["gayathri@gmail.com","adi@gmail.com","sid@gmail.com","lucky@gmail.com"]
tech(d1,d2,d3)

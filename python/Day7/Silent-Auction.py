print("/////////////////////////Welcome to the Silent Auction!//////////////////////")

dic = {}
flag = True
while flag:
    name = input("Enter the Bidder Name: ")
    bid = int(input("Enter the Bidding Amount: "))
    dic[name] = bid
    con = input("Are there are any more Bidders? (yes or no): ")
    if con.lower() == "no":
        flag = False
        winnerBid = 0
        winner = ""
        for i in dic:
            if dic[i] > winnerBid:
                winnerBid = dic[i]
                winner = i
        print(f"Winner Name is {winner} & the highest bid is {winnerBid}")



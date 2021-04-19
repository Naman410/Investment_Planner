
class cagr():
    
    def __init__(self) :
        type = input("Enter the wether the investment plan is lumpsump, sip or policy :")
        self.type = type

    def lumpsump(self) :
        deposit = float(input("Enter the your deposit amount in rupees : "))
        term = float(input("Enter the number of years : "))
        mature_amount = float(input("Enter the maturity amount : "))
        cagr = ((((mature_amount/deposit)**(1/term)) - 1)*100)
        print("The compound interest rate for your policy  is : ", cagr)

    def sip(self) :
        print("Enter the frequency of the sip from one of these : ")
        frequency_options = {
            "monthly" : 12,
            "quterly" : 4,
            "half-yearly" : 2,
            "yearly" : 1,
        }
        print (frequency_options.keys())
        frequency = input(" ")
        sipamount = float(input("Enter your sip amount in rupees : "))
        term = float(input("Enter the number of years : "))
        total_deposit = sipamount * frequency_options[frequency] * term
        mature_amount = float(input("Enter the total return amount : "))
        cagr = ((((mature_amount/total_deposit)**(1/term)) - 1)*100)
        print("The compound interest rate for your sip is : ", cagr)

    def policy(self) :
        print("Enter the frequency of the poilicy payments from one of these : ")
        frequency_options = {
            "monthly" : 12,
            "quterly" : 4,
            "half-yearly" : 2,      
            "yearly" : 1,
        }
        print (frequency_options.keys())
        frequency = input(" ")
        single_payment = float(input("Enter your single installment amount in rupees : "))
        term_of_payment = float(input("Enter the number of years you are going to pay the amount : "))
        total_deposit = single_payment * frequency_options[frequency] * term_of_payment
        mature_amount = float(input("Enter the total return amount : "))
        total_time = float(input("Enter the total number of year, till you get the money back : "))
        cagr = ((((mature_amount/total_deposit)**(1/total_time)) - 1)*100)
        print("The compound interest rate for your policy  is : ", cagr)

if __name__ == "__main__":
    naman = cagr()
    if (self.type() == "lumpsump") : 
        naman.lumpsump()

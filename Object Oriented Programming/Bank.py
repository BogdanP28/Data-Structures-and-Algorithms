

class CreditCard:
    """A consumer credit card"""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance
        
        The initial balance is zero
           
        Args:
            customer (str): The name of the customer
            bank (str): The name of the bank
            acnt (str): The account identifier
            limit (int): Credit limit(dollars)
        """
        
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit 
        self._balance = 0 
        
    def get_customer(self):
        """Return name of the customer"""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name"""
        return self._bank
    
    def get_account(self):
        """Return the card identigying number(typically stored as a string)"""
        return self._account
    
    def get_limit(self):
        """Return current credit limit"""
        return self._limit
    
    def get_balance(self):
        """Return current balance"""
        return self._balance
        
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount
        
class PredatoryCreditCard(CreditCard):
        """An extension to CreditCard that compounds interest and fees"""
        def __init__(self, customer, bank, acnt, limit, apr):
            """
                Create a new predatory credit card instance
                The initial balance is zero

            Args:
                customer (_type_): name of the customer
                bank (_type_): name of the bank
                acnt (_type_): acount identifier
                limit (_type_): credit limit
                apr (_type_): annual percentake rate
            """
            super().__init__(customer,bank,acnt,limit) # call super constructor
            self._apr = apr
            
        def charge(self, price):
            """
                Charge given price to the card, assuming sufficient credit limit
            Return True if charge was processed.
            Return False and assess 5$ fee if charge is denied

            Args:
                price (_type_): price
            """
            success = super().charge(price)      # call inherited method
            if not success:
                self._balance += 5               # assess penalty
            return success                       # caller expects return value
        
        def process_month(self):
            """Assess monthly interest on outstanding balance"""
            if self._balance > 0:
                # if positive balance, convert APR to montly multiplicative factor
                monthly_factor = pow(1 + self._apr, 1/12)
                self._balance *= monthly_factor
    
    
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395  1954', 4500))
    wallet.append(CreditCard('Bojack Horseman', 'California Finance', '5391 0375 9387 5309', 8931))
    
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(val*2)
        wallet[2].charge(val*3)
        
    for c in range(2):
        print('Customer =', wallet[c].get_customer())
        
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
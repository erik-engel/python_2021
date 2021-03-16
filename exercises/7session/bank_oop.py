class Bank:
    def __init__(self):
        self.accounts = []

    # accounts
    @property
    def accounts(self):
        return self.__accounts

    # Multiple accounts
    @accounts.setter
    def accounts(self, accounts):
        if type(accounts) == list:
            self.__accounts = accounts
        elif type(accounts == Account:


    # one account
    def addAccount(self, account):
        self.accounts.append(account)

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

    # no
    @property
    def no(self):
        return self.__no

    @no.setter
    def no(self, no)
        self.__

class Customer:
    def __init__(self, name):
        self.name = name

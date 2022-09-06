class SavingAccount(object):
    def __init__(self, name, address):
        self.balance = 1000
        self.name = name
        self.address = address

    def saving_account_balance(self):
        return self.balance


class CurrentAccount(object):
    def __init__(self, name, address):
        self.balance = 500
        self.name = name
        self.address = address

    def current_account_balance(self):
        return self.balance


class PPFAccount(object):
    def __init__(self, name, address):
        self.balance = 100
        self.name = name
        self.address = address

    def ppf_account_balance(self):
        return self.balance


class NPSAccount(object):
    def __init__(self, name, address):
        self.balance = 10
        self.name = name
        self.address = address

    def nps_account_balance(self):
        return self.balance


class PFAccount(object):
    def __init__(self, name, address, company_name):
        self.balance = 0
        self.name = name
        self.address = address
        self.company_name = company_name

    def pf_account_balance(self):
        return self.balance


class AccountInformation(object):
    def __init__(self, name, address, company_name):
        self.available_accounts = ["Savings", "Current", "PPF", "NPS", "PF"]
        self.account_list = {}
        self.name = name
        self.address = address
        self.company_name = company_name

    def get_account_list(self):
        return self.account_list.keys()

    def add_account(self, account_type):
        if account_type in self.available_accounts:
            self.create_account(account_type)
        else:
            return "{} type is not available".format(account_type)

    def create_account(self, account_type):
        if account_type == "Savings":
            self.account_list[account_type] = SavingAccount(self.name, self.address)
        elif account_type == "Current":
            self.account_list[account_type] = CurrentAccount(self.name, self.address)
        elif account_type == "PPF":
            self.account_list[account_type] = PPFAccount(self.name, self.address)
        elif account_type == "NPS":
            self.account_list[account_type] = NPSAccount(self.name, self.address)
        elif account_type == "PF":
            self.account_list[account_type] = PFAccount(self.name, self.address, self.company_name)

    def get_balance(self):
        total_balance = 0
        for account in self.account_list:
            total_balance += self.account_list[account].balance

        return total_balance

    def add_amount(self, account_type, amount):
        account_info = self.account_list[account_type]
        account_info.balance = account_info.balance + amount

    def get_account_information(self):
        complete_info = ""
        complete_info += "Account Information:\n"
        complete_info += "Name: {}\nAddress: {}\n".format(self.name, self.address)
        complete_info += "Company Name: {}\n".format(self.company_name)
        for account in self.account_list:
            complete_info += "{} balance is {}\n".format(account, self.account_list[account].balance)
        return complete_info


person1 = AccountInformation("Person1", "Vijayawada - Andhra Pradesh", "epam")
person1.add_account("Savings")
person1.add_account("Current")
person1.add_account("PF")
person1.add_amount("Savings", 50)
person1.add_amount("PF", 1500)
# print(person1.get_account_list())
# print(person1.get_balance())
print(person1.get_account_information())

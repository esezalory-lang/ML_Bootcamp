# in the_bank.py
from typing import Any


class Account(object):
    ID_COUNT = 1

    def __init__(self: "Account", name: str, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self) -> None:
        self.accounts = []

    def check_corruptacc(self: "Bank", account: Account) -> bool:
        zip_flag = False
        addr_flag = False
        if len(account.__dict__) % 2 == 0:
            return False
        for i in account.__dict__.keys():
            if i.startswith("b"):
                return False
            if i.startswith("zip"):
                zip_flag = True
            if i.startswith("addr"):
                addr_flag = True
        if zip_flag is False or addr_flag is False:
            return False
        if not (hasattr(account, "name") and hasattr(
                account, "id") and hasattr(account, "value")):
            return False
        if not isinstance(getattr(account, "name"), str):
            return False
        if not isinstance(getattr(account, "id"), int):
            return False
        if not isinstance(getattr(account, "value"), (int, float)):
            return False
        return True

    def add(self: "Bank", new_account: Account) -> bool:
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if any(i.name == new_account.name for i in self.accounts):
            return False
        if not isinstance(new_account, Account):
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self: "Bank", origin: str, dest: str,
                 amount: float) -> bool:
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        origin_inst = None
        dest_inst = None
        for account in self.accounts:
            if account.name == origin:
                origin_inst = account
            if account.name == dest:
                dest_inst = account
        if not origin_inst or not dest_inst:
            return False
        if self.check_corruptacc(origin_inst) and self.check_corruptacc(
                dest_inst):
            if origin_inst == dest_inst:
                return True
            if float(getattr(origin_inst, "value")) < 0 or getattr(
                    origin_inst, "value") < amount:
                return False
            dest_inst.transfer(amount)
            origin_inst.transfer(-amount)
            return True
        return False

    def fix_account(self: "Bank", name: str) -> bool:
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        zip_flag = False
        addr_flag = False
        to_fix = None
        if not isinstance(name, str):
            return False
        for account in self.accounts:
            if account.name == name:
                to_fix = account
        if not to_fix:
            return False
        for i in list(to_fix.__dict__.keys()):
            if i.startswith("b"):
                delattr(to_fix, i)
            if i.startswith("zip"):
                zip_flag = True
            if i.startswith("addr"):
                addr_flag = True
        if zip_flag is False:
            setattr(to_fix, "zip", "000-000")
        if addr_flag is False:
            setattr(to_fix, "addr", "[Insert Address Here]")
        if not hasattr(to_fix, "name"):
            setattr(to_fix, "name", "Johnny Appleseed")
        if not hasattr(to_fix, "id"):
            setattr(to_fix, "id", to_fix.ID_COUNT)
            Account.ID_COUNT += 1
        elif not isinstance(getattr(to_fix, "id"), int):
            try:
                setattr(to_fix, "id", int(getattr(to_fix, "id")))
            except (ValueError, TypeError):
                setattr(to_fix, "id", Account.ID_COUNT)
                Account.ID_COUNT += 1
        if not hasattr(to_fix, "value"):
            setattr(to_fix, "value", 0)
        elif not isinstance(getattr(to_fix, "value"), (int, float)):
            try:
                setattr(to_fix, "value", int(getattr(to_fix, "value")))
            except (ValueError, TypeError):
                setattr(to_fix, "value", 0)
        if len(to_fix.__dict__) % 2 == 0:
            setattr(to_fix, "Filler", "Making it odd")
        return True

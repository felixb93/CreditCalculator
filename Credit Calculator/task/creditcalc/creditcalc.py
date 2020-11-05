import math
import argparse


def convert_months(months):
    if months <= 1:
        return "You need 1 month to repay this credit!"
    elif months == 12:
        return "You need 1 year to repay this credit!"
    elif months / 12 <= 1:
        return "You need {} months to repay this credit!".format(months)
    elif months % 12 == 0:
        return "You need {} years to repay this credit!".format(int(months / 12))
    else:
        return "You need {} years and {} months to repay this credit!".format(int(months / 12), math.ceil(months % 12))


def interest(yearly):
    return yearly / (12 * 100)


def overpayment(principal, payment, periods):  # overpayment for annuity type
    return round((math.ceil(payment) * periods) - principal, 2)


class CreditCalculator:
    def __init__(self):
        self.principal = args.principal
        self.months = args.periods
        self.interest_rate = args.interest
        self.payment_number = args.periods
        self.annuity = args.payment

    def differentiated(self):
        total = 0
        for i in range(1, int(self.months) + 1):
            self.annuity = math.ceil((self.principal / self.months) + self.interest_rate *
                                     (self.principal - ((self.principal * (i - 1)) / self.months)))
            print("Month {}: paid out {}".format(i, self.annuity))
            total += self.annuity
        return round(total)

    def func_annuity(self):
        self.payment_number = self.months

        return math.ceil(self.principal * ((self.interest_rate * pow(1 + self.interest_rate, self.payment_number)) /
                                           (pow(1 + self.interest_rate, self.payment_number) - 1)))

    def func_principal(self):
        # self.payment_number = float(input("Enter count of periods:\n"))
        # self.interest_rate = interest(float(input("Enter credit interest:\n")))
        return math.ceil((self.annuity / (((self.interest_rate * pow(1 + self.interest_rate, self.payment_number)) /
                                           (pow(1 + self.interest_rate, self.payment_number) - 1)))))

    def func_paymentnumber(self):
        # self.interest_rate = interest(float(input("Enter credit interest:\n")))
        return math.ceil(
            math.log(self.annuity / (self.annuity - self.interest_rate * self.principal),
                     1.0 + self.interest_rate))

    def main(self):
        if args.type == "diff" and (args.payment is not None):
            return "Incorrect parameters"
        if self.interest_rate is None:
            return "Incorrect parameters"
        self.interest_rate = interest(self.interest_rate)
        if args.type == "diff":
            return "Overpayment = {}".format(round(self.differentiated() - self.principal), 2)
        elif args.type == "annuity":

            if self.annuity is None:
                annuity = self.func_annuity()
                return ("Your annuity payment = {}!\nOverpayment = {}".format(
                    math.ceil(annuity),
                    (overpayment(self.principal, annuity, self.payment_number))))
            elif self.principal is None:
                principal = self.func_principal()
                return ("Your credit principal = {}!\nOverpayment = {}".format(principal,
                                                                               overpayment(principal, self.annuity,
                                                                                           self.payment_number)))
            elif self.payment_number is None:
                periods = self.func_paymentnumber()
                return ("{}\nOverpayment = {}"
                        .format(convert_months(periods),
                                overpayment(self.principal, self.annuity, periods)))
            else:
                return "Incorrect parameters"
        else:
            return "Incorrect parameters"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, help="diff or annuity")
    parser.add_argument("--principal", help="total credit volume", type=float)
    parser.add_argument("--payment", help="monthly payment", type=float)
    parser.add_argument("--periods", help="number of months", type=float)
    parser.add_argument("--interest", type=float)
    args = parser.parse_args()
    # print(args)
    mycreditcalc = CreditCalculator()
    print(mycreditcalc.main())

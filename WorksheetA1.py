print("testing")
# Question 1: Mortgage Payments
# In this part of the assignment, different mortgage payment options are calculated for monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, and rapid weekly intervals.
 
class MortgagePayment:
    def __init__(self, quoted_rate, amort_years):
        # quoted_rate is the interest rate given
        # amort_years is the amortization period in years
        self.quoted_rate = quoted_rate
        self.amort_years = amort_years

    def _pva(self, r, n):
        return (1 - (1 + r) ** (-n)) / r
        # defining the pva formula

    def payments(self, principal):
        # need to first convert the semi-annual coumpounding rate to an effective monthly rate
        semi_rate = self.quoted_rate / 2
        eff_monthly = (1 + semi_rate) ** (1/6) - 1

        # identifying the number of payments (n) for each period (excluding accelerated payments)
        n_monthly = self.amort_years * 12
        n_semi_monthly = self.amort_years * 24
        n_biweekly = self.amort_years * 26
        n_weekly = self.amort_years * 52

        # calculating the rates (r) for the different periods using the effective monthly and semi annual rates
        r_monthly = eff_monthly
        r_semi_monthly = (1 + r_monthly) ** (1/2) - 1 
        r_biweekly = (1 + semi_rate) ** (1/13) - 1
        r_weekly = (1 + semi_rate) ** (1/52) - 1

        # calculating the payments for different periods
        monthly = principal / self._pva(r_monthly, n_monthly)
        semi_monthly = principal / self._pva(r_semi_monthly, n_semi_monthly)
        biweekly = principal / self._pva(r_biweekly, n_biweekly)
        
        # Weekly = half of biweekly
        weekly = biweekly / 2

        # calculating the accelerated payments separately as they are equal to half and one quarter of the monthly payment
        rapid_biweekly = monthly / 2
        rapid_weekly = monthly / 4

        return (round(monthly, 2), round(semi_monthly, 2), round(biweekly, 2), round(weekly, 2), round(rapid_biweekly, 2), round(rapid_weekly, 2))
    
if __name__ == "__main__":
    mortgage = MortgagePayment(0.055, 25)
    payments = mortgage.payments(100000)
    print(payments)

# Repeating the same steps for a principal of $500,000
class MortgagePayment:
    def __init__(self, quoted_rate, amort_years):
        # quoted_rate is the interest rate given
        # amort_years is the amortization period in years
        self.quoted_rate = quoted_rate
        self.amort_years = amort_years

    def _pva(self, r, n):
        return (1 - (1 + r) ** (-n)) / r
        # defining the pva formula

    def payments(self, principal):
        # need to first convert the semi-annual coumpounding rate to an effective monthly rate
        semi_rate = self.quoted_rate / 2
        eff_monthly = (1 + semi_rate) ** (1/6) - 1

        # identifying the number of payments (n) for each period (excluding accelerated payments)
        n_monthly = self.amort_years * 12
        n_semi_monthly = self.amort_years * 24
        n_biweekly = self.amort_years * 26
        n_weekly = self.amort_years * 52

        # calculating the rates (r) for the different periods using the effective monthly and semi annual rates
        r_monthly = eff_monthly
        r_semi_monthly = (1 + r_monthly) ** (1/2) - 1 
        r_biweekly = (1 + semi_rate) ** (1/13) - 1
        r_weekly = (1 + semi_rate) ** (1/52) - 1

        # calculating the payments for different periods
        monthly = principal / self._pva(r_monthly, n_monthly)
        semi_monthly = principal / self._pva(r_semi_monthly, n_semi_monthly)
        biweekly = principal / self._pva(r_biweekly, n_biweekly)
        
        # Weekly = half of biweekly
        weekly = biweekly / 2

        # calculating the accelerated payments separately as they are equal to half and one quarter of the monthly payment
        rapid_biweekly = monthly / 2
        rapid_weekly = monthly / 4

        return (round(monthly, 2), round(semi_monthly, 2), round(biweekly, 2), round(weekly, 2), round(rapid_biweekly, 2), round(rapid_weekly, 2))
    
if __name__ == "__main__":
    mortgage = MortgagePayment(0.055, 25)
    payments = mortgage.payments(500000)
    print(payments)

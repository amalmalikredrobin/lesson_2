# class Bank:
#     interest_rate = 30
#     def calculate_loan(self, customer, loan_money, duration):
#         interest_money = loan_money * (self.interest_rate / 100) * duration
#         total_money = interest_money + loan_money
#         payment_per_month = total_money / (duration * 12)
#         if payment_per_month < customer.salary / 2:
#             return f'Dear, {customer.full_name}! We are ready to offer {loan_money} UZS for a period of {duration} years. The total amount of money will constitue {total_money} UZS. {interest_money} UZS from the total amount is interest money. Your monthly payment will be {round(payment_per_month, 2)} Uzs. Thank you!'
#         else:
#             return

# class Customer:
#     def __init__(self, full_name, salary):
#         self.full_name = full_name
#         self.salary = salary

# kapital_bank  = Bank()
# customer1 = Customer('Amalmalik Abuzarov', 5_000_000)
# kapital_bank.calculate_loan(customer1, 10000000, 1)


class Person:
    def __init__(self, step_length, steps_pm):
        self.step_length = step_length
        self.steps_pm = steps_pm
        self.avg_velocity = ((step_length/100 * steps_pm) * 60) / 1000


class Runner(Person):
    


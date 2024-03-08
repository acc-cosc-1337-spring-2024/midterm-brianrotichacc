def get_bonus_pay(sales):
    if sales < 0 or sales > 1999:
        return "Invalid arguments" 
    elif 0 <= sales <= 499:
        bonus_percentage = 5
    elif 500 <= sales <= 999:
        bonus_percentage = 6
    elif 1000 <= sales <= 1499:
        bonus_percentage = 7
    elif 1500 <= sales <= 1999:
        bonus_percentage = 8
    else:
        return "Unexpected error"
    
    bonus_pay_amount = (bonus_percentage / 100) * sales

    return bonus_pay_amount

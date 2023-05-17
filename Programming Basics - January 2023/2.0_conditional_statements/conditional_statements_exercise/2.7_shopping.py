# read
budget = float(input())
n = int(input())
m = int(input())
p = int(input())

# read prices
p_n = 250
p_m_percent = 35
p_p_percent = 10

# logic
n_sum = n * p_n
m_sum = m * (n_sum * p_m_percent / 100)
p_sum = p * (n_sum * p_p_percent / 100)

sum_total = n_sum + m_sum + p_sum

if n > m:
    sum_total = sum_total - (sum_total * 15 / 100)

if sum_total <= budget:
    excess = budget - sum_total
    print(f"You have {excess:.2f} leva left!")
else:
    deficit = sum_total - budget
    print(f"Not enough money! You need {deficit:.2f} leva more!")

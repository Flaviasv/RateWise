def calculate_total(hourly_rate, hours_per_class, classes_per_week, weeks, rent, commute):
    """Total price = hourly rate × hours × classes/week × weeks + rent + commute."""
    return hourly_rate * hours_per_class * classes_per_week * weeks + rent + commute


def calculate_per_person(total_price, num_people):
    """Price per person = total ÷ number of people."""
    if num_people <= 0:
        return 0
    return total_price / num_people


def apply_discount(price, discount):
    """Discounted price = price × (1 − discount ÷ 100)."""
    return price * (1 - discount / 100)


def calculate_after_costs(price, rent, commute):
    """Amount left for the instructor = price − rent − commute."""
    return price - rent - commute


if __name__ == "__main__":
    total = calculate_total(50, 1.5, 2, 8, 100, 20)
    print("Total:", total)
    print("Per person (4 people):", calculate_per_person(total, 4))
    print("With 10% discount:", apply_discount(total, 10))
    print("After costs:", calculate_after_costs(total, 100, 20))
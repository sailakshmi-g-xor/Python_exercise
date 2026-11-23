def list_stats(numbers):
    total = sum(numbers)
    average = f"{total / len(numbers):.2f}" if numbers else "0.00"
    maximum = max(numbers) if numbers else None
    minimum = min(numbers) if numbers else None
    des = sorted(numbers,reverse=True) if numbers else []
    sec = numbers[::2] if len(numbers) >= 2 else []
    return {
       
        "max": maximum,
        "min": minimum,
        "total": total,
        "average": average,
        "descending":des,
        "second_highest": sec
    }
nums = [14, 3, 9, 27, 8, 21, 5, 18]
dict = list_stats(nums)
print(dict)
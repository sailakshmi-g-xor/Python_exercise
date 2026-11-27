def list_stats(nums):
    total = sum(nums)
    return {
        "max": max(nums) if nums else None,
        "min": min(nums) if nums else None,
        "total": total,
        "average": f"{total / len(nums):.2f}" if nums else "0.00",
        "descending": sorted(nums, reverse=True),
        "every_second": nums[::2],
    }


def main():
    numbers = [14, 3, 9, 27, 8, 21, 5, 18]
    stats = list_stats(numbers)
    print(f"max: {stats['max']}")
    print(f"min: {stats['min']}")
    print(f"total: {stats['total']}")
    print(f"average: {stats['average']}")
    print(f"descending: {stats['descending']}")
    print(f"every second: {stats['every_second']}")


if __name__ == "__main__":
    main()

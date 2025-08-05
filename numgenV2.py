#!/usr/bin/env python3
import datetime

def generate_list(start, end, step, filename=None):
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"numberlist_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for number in range(start, end + 1, step):
            f.write(f"{number}\n")

    print(f"\n✅ List saved to: {filename}")

def main():
    print("=== Number List Generator ===")
    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))
        step_input = input("Enter step increment (default is 1): ").strip()
        step = int(step_input) if step_input else 1

        generate_list(start, end, step)
    except ValueError:
        print("⚠️ Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()

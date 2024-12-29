def is_power_of_8(num):
  if num <= 0:
    return False

  return (num & (num - 1)) == 0 and (num & 0x7) == 0

number = int(input("Enter a number: "))
if is_power_of_8(number):
  print(f"{number} is a power of 8.")
else:
  print(f"{number} is not a power of 8.")

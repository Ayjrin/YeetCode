
   # 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

   # What is the sum of the digits of the number 2^1000?
import time
start = time.time()

print(sum(map(int, str(2**1_000))))

print(str(time.time() - start) + " seconds")

# answer:
# 1366
# 5.650520324707031e-05 seconds

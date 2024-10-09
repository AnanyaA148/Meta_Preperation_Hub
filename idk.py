import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  len1 = len(array_a)

  for i in range(len1):
      if array_a[i] != array_b[i]:
           
           start = i
           break
  
  
  j = start + 1

  while(j<= len1):
      
      if array_a[-1] != array_b[-1]:
        end = len1-1
        break
  
      if array_a[-2] != array_b[-2]:
        end = len1-2
        break
      if array_a[j] == array_b[j]:
           if array_a[j+1] == array_b[j+1]:
                end = j -1
                
                break
  
  count = 0
  end = len1 -1
  while((start + count) <= (start +end)/2):
      if array_a[start] != array_b[end]:
          return False
      count = count +1
  return True
  
  # Write your code here
  










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
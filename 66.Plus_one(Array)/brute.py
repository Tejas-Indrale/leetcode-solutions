class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        combine = int(''.join(str(char) for char in digits)) + 1

        arr = [int(char) for char in str(combine)]

        return arr
    





    



"""
    Let’s say:

python
Copy
Edit
digits = [1, 2, 3]
➤ str(char) for char in digits
This is a generator expression:

Iterates over each digit in the list

Converts each digit to a string:

python
Copy
Edit
['1', '2', '3']
➤ ''.join(...)
This joins the list of strings with '' (no space) between them:

python
Copy
Edit
'1' + '2' + '3' = '123'
➤ int(...)
Converts the string '123' into the integer 123.

➤ + 1
Finally, adds 1 to get 124.

✅ Result:

python
Copy
Edit
combine = 124
"""

"""
    Let’s say:

python
Copy
Edit
combine = 124
➤ str(combine)
Gives: '124'

➤ for char in str(combine)
Loops over:

python
Copy
Edit
['1', '2', '4']
➤ int(char)
Converts each character to an integer:

python
Copy
Edit
[1, 2, 4]
✅ Result:

python
Copy
Edit
arr = [1, 2, 4]
"""
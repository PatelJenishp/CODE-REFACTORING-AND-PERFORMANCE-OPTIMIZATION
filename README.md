COMPANY: CODTECH IT SOLUTIONS

NAME JENISH PATEL

INTER ID: CT06DG826

DOMIN: SOFTWARE DEVELOPMENT

DURATION: 6 WEEK

MENTOR: NEELA SANTOSH



Code Readability:

Replaced multiple lines of logic with Python’s built-in collections.Counter, reducing line count and complexity.

Used Path.read_text() from the pathlib module for modern, clean file handling.

The overall code is shorter, more intuitive, and easier to maintain.

Performance Enhancements:

Counter is implemented in C under the hood and is significantly faster for frequency counting.

Applying .lower() to the full text string instead of inside a loop reduces the number of function calls dramatically.

Eliminated manual file closure, reducing the risk of memory leaks or file lock issues.

This task reinforced the value of built-in Python modules for writing clean, efficient code. Instead of reinventing the wheel, leveraging tools like Counter and Path can significantly improve both performance and readability. It also highlighted the importance of benchmarking and analyzing code before and after refactoring.

Manual file handling with open() and close(), which could lead to errors if not handled properly.

A loop that manually updates a dictionary, which is less efficient and verbose.

Repetitive calls to lower() inside the loop, increasing overhead.



#OUTPUT
<img width="1014" height="510" alt="Image" src="https://github.com/user-attachments/assets/32a4af37-54a0-4282-9096-de2dbc076bba" />

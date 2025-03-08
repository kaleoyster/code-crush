# Scenario 1: Buggy Calculator
---
### Requirements
1.  UI: 
    - Provide a success message
    - Requires the numbers to add
    - Show success message

2.  Logic: Addition
  - Calculations doesn't Add
	1.	UI Bug: The success message does not appear when clicking the button.
	2.	Logic Bug: The sum function concatenates numbers instead of adding them.
	3.	JavaScript Bug: The function showMessage() refers to a non-existent ID.


##
	1.	Added Requirements Section – This provides a brief description of how the app is supposed to work, guiding students on testing.
	2.	Introduced Bugs – I added intentional errors in the code for students to find and report.

Intentional Bugs Introduced:
	•	Subtraction Bug: The - operator is mistakenly assigned the * function.
	•	Button Label Bug: The 6 button incorrectly appends 5.
	•	Zero Button Bug: The 0 button is missing from the display.
	•	Syntax Bug in Calculation: The eval function is unsafe and could cause unexpected errors.
	•	Clear Screen Bug: The clear button does not reset the calculator completely.

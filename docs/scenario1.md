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

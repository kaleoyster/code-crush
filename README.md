# Code-crush (2025)
- Date: March 4th, 2025

## Goal
- Introduce the idea of software quality.
- Each scenario increases in difficulty.

## Scenarios
- Each scenario contains a web app.
- Requirements are specified for each web app.

---

## Scenario 1: Buggy Calculator
### Requirements
1. **UI**:
    - Provide a success message.
    - Requires the user to enter numbers before adding.
    - Show a success message when the calculation completes.

2. **Logic: Addition**
    - The calculation must properly add numbers.

### Bugs to Find:
1. **UI Bug**: The success message does not appear when clicking the button.
2. **Logic Bug**: The sum function concatenates numbers instead of adding them.
3. **JavaScript Bug**: The function `showMessage()` refers to a non-existent ID.

---

## Scenario 2: Buggy Login Screen
### Requirements
1. **UI**:
    - Properly hide the password input field.
    - Display error messages when login fails.
    - Ensure the login button is enabled only when both fields are filled.
2. **Security & Logic**:
    - User passwords should not be visible.
    - Invalid credentials should not log in the user.

### Bugs to Find:
1. **Security Bug**: Password is exposed as plain text instead of hidden input.
2. **Logic Bug**: Incorrect passwords still allow login.
3. **UI Bug**: The login button is always enabled, even when fields are empty.

---

## Scenario 3: Buggy Temperature App
### Requirements
1. **UI**:
    - Allow the user to input temperature in Celsius or Fahrenheit.
    - Provide a button to convert between the two units.
2. **Logic**:
    - The conversion formula should be correct.

### Bugs to Find:
1. **Logic Bug**: The conversion formula is incorrect.
2. **UI Bug**: The input field does not clear when switching units.
3. **JavaScript Bug**: The convert button does nothing when clicked.

---

## Scenario 4: Buggy Shopping Cart
### Requirements
1. **UI**:
    - Items should be added and removed from the cart correctly.
    - Display a total price.
2. **Logic**:
    - The price should be calculated correctly based on the items in the cart.

### Bugs to Find:
1. **Logic Bug**: Items cannot be removed from the cart.
2. **Logic Bug**: Items get added twice when clicking once.
3. **UI Bug**: Prices do not update correctly.

---

## Scenario 5: Buggy Calendar
### Requirements
1. **UI**:
    - Users should be able to navigate between months.
    - Events should be added and displayed on selected dates.
2. **Logic**:
    - Clicking a date should allow event creation.
    - The calendar should correctly update when switching months.

### Bugs to Find:
1. **UI Bug**: Navigation buttons do not work.
2. **Logic Bug**: Events are not saved to the correct date.
3. **JavaScript Bug**: The displayed month does not update when navigating.



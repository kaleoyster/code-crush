# Scenario 2: Buggy Login Screen
---
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

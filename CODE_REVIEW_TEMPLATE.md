# Code Review Template, make sure you fill this up and attach it to the Pull Request

## FUNCTIONAL REVIEW
[√] The change works as you expect

[√] The change matches the specification

## UI, UX & ACCESSIBILITY
[√] UI changes are consistent with other parts of the application

[√] User-visible texts are easy to read

[√] UI changes are accessible

## IMPLEMENTATION
[√] There is no obvious simpler solution

[√] No missed opportunities to use design patterns

[√] Uses best practices for modularization, abstraction and structure

[√] Code uses speaking variable, function and class names

## COMMENTS & DOCUMENTATION
[√] New comments have been added in the code (only) where necessary
Comments should explain why something is done, not how

[√] Existing code comments are still valid
Comments tend to get outdated really quickly, so it's good to double-check existing comments in changed code.

[ ] The user documentation has been updated
The user-facing documentation should include all important features and up-to-date screenshots.

## SECURITY & PRIVACY CONCERNS
[√] Authentication and authorization are checked

[√] Passwords and sensitive data are not stored in plaintext

[√] Sensitive data are not written to logs etc.

[√] All user input is sanitized

[√] Data are stored in accordance with applicable laws (GDPR etc.)

## DEPENDENCIES
[√] The code was written to be testable
Best practice is to write code that can be easily (unit-)tested.

[√] Enough tests have been written (or adapted) for the code changes
Testing can be done in different stages (unit, integration, end-to-end tests)

[√] The test suite passes

## TOOLS & LINTING
[√] No new warnings from linter tools are present
No new findings should be reported for the code changes.

[√] Existing linter warnings in touched code have been fixed
To gradually improve over time, changed code should be cleaned up whenever possible ("boy scout rule")

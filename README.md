### Password Security Checker
A simple Python program designed to evaluate password strength based on standard security requirements and provide constructive feedback to users.
## Features 
 Length Verification: Checks if the password is at least 8 characters long.
 Case Sensitivity Checks: Ensures the presence of both uppercase and lowercase letters.
 Numeric Character Check: Verifies that at least one number is included.
 Special Character Detection: Validates the inclusion of at least one non-alphanumeric character (e.g., !, @, #, $).
 Detailed Feedback: Identifies and displays specific missing requirements to help the user improve their password.
 Strength Rating: Categorizes the password into Weak, Medium, or Strong based on met criteria.
 ## Approach & Logic
  Modular Design: The core logic is encapsulated within a function (check_password) to ensure the code is reusable, testable, and clean.
  Built-in String Methods: Utilized efficient Python built-ins like isupper(), islower(), isdigit(), and isalnum() alongside any() for concise and readable validation.
  Tracking Missing Requirements: Maintained a dynamic list (missing) that logs any failed criteria. If a rule isn't met, a descriptive string is appended to the list.
  Scoring System: Increments a score integer for every passed requirement, which maps directly to the overall strength level:
   - Score $\le$ 2: 
   - WeakScore 3–4:
   - MediumScore 5: Strong
"""
Unit 6 - Lesson 3: Homework Assignment
=======================================
Company Directory System

Your Task:
1. Create employee data (at least 5 employees)
2. Save to "company_directory.json"
3. Create search_by_department() function
4. Print formatted results

Expected Output:
✅ Company directory created with 5 employees

Searching for employees in: IT

Found 2 employees in IT:
  - Michael Chen
    Email: michael@company.com
    Phone: 555-0102

  - Sarah Johnson
    Email: sarah@company.com
    Phone: 555-0103
"""
import json

# =============================================================================
# PART 1: Create Employee Data
# =============================================================================
# TODO: Create a list of at least 5 employee dictionaries
# Each employee should have: employee_id, name, department, email, phone
# Include at least 3 different departments

employees = [
    # TODO: Add your employees here
    # Example format:
    # {
    #     "employee_id": "E001",
    #     "name": "Jennifer Martinez",
    #     "department": "Sales",
    #     "email": "jennifer@company.com",
    #     "phone": "555-0101"
    # },
]


# =============================================================================
# PART 2: Save to JSON File
# =============================================================================
# TODO: Save the employees list to "company_directory.json"
# Remember to use indent=4 for readable formatting
# Print a confirmation message




# =============================================================================
# PART 3: Search Function
# =============================================================================
def search_by_department(department):
    """
    Search for all employees in a specific department.
    
    Args:
        department (str): The department name to search for
    """
    # TODO: Load the JSON file
    
    
    # TODO: Find all employees in the specified department
    
    
    # TODO: Print the count of employees found
    
    
    # TODO: Print each employee's information formatted nicely
    




# =============================================================================
# PART 4: Test Your Function
# =============================================================================
# TODO: Call search_by_department() with different departments
# Test with: IT, Sales, Marketing, or whatever departments you used




# =============================================================================
# 🌟 BONUS CHALLENGES (Optional - Extra Credit!)
# =============================================================================

# Bonus 1: Case-insensitive search
# def search_by_department_case_insensitive(department):
#     """Search for employees by department (case-insensitive)."""
#     # TODO: Make the search work for "IT", "it", "It", etc.
#     pass


# Bonus 2: Search by name
# def search_by_name(name):
#     """Search for an employee by name."""
#     # TODO: Find employee by name (partial match okay)
#     pass


# Bonus 3: Add new employee
# def add_employee(emp_id, name, department, email, phone):
#     """Add a new employee to the directory."""
#     # TODO: Load existing directory
#     # TODO: Create new employee dictionary
#     # TODO: Append to list
#     # TODO: Save back to file
#     pass


# Bonus 4: Department summary
# def show_department_summary():
#     """Show all departments and employee counts."""
#     # TODO: Count employees in each department
#     # TODO: Print summary
#     pass


# Bonus 5: Interactive menu
# def main_menu():
#     """Display an interactive menu for the directory system."""
#     # TODO: Create a menu with options:
#     # 1. Search by department
#     # 2. Search by name
#     # 3. Add employee
#     # 4. Show all employees
#     # 5. Department summary
#     # 6. Exit
#     pass


# =============================================================================
# 📝 NOTES & REMINDERS
# =============================================================================
# ✓ Use json.load() to read from file
# ✓ Use json.dump() with indent=4 to write to file
# ✓ Each employee needs all 5 fields: employee_id, name, department, email, phone
# ✓ Use 'with' statements to handle files properly
# ✓ Print clear, formatted output for the user
# ✓ Test with multiple departments to make sure search works

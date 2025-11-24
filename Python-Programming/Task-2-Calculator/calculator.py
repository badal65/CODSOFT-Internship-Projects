#!/usr/bin/env python3
"""
Advanced Calculator Application
Performs basic and scientific calculations with history tracking
Author: Badal Chaudhary 
CODSOFT Python Programming Internship - Task 2
"""

import math
import operator
from datetime import datetime

class ScientificCalculator:
    """Calculator with extended functionality"""
    
    def __init__(self):
        self.history = []
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
            '%': operator.mod,
            '//': operator.floordiv
        }
    
    def calculate(self, num1, operation, num2):
        """Execute calculation based on operator"""
        try:
            if operation not in self.operations:
                return "Error: Invalid operation"
            
            if operation == '/' and num2 == 0:
                return "Error: Division by zero"
            
            result = self.operations[operation](num1, num2)
            
            # Store in history
            calculation = f"{num1} {operation} {num2} = {result}"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({'calc': calculation, 'time': timestamp})
            
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def scientific_operation(self, operation, value):
        """Perform scientific calculations"""
        try:
            operations_map = {
                'sqrt': lambda x: math.sqrt(x),
                'square': lambda x: x ** 2,
                'cube': lambda x: x ** 3,
                'sin': lambda x: math.sin(math.radians(x)),
                'cos': lambda x: math.cos(math.radians(x)),
                'tan': lambda x: math.tan(math.radians(x)),
                'log': lambda x: math.log10(x),
                'ln': lambda x: math.log(x),
                'factorial': lambda x: math.factorial(int(x))
            }
            
            if operation not in operations_map:
                return "Error: Invalid scientific operation"
            
            result = operations_map[operation](value)
            
            # Store in history
            calculation = f"{operation}({value}) = {result}"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({'calc': calculation, 'time': timestamp})
            
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("\n📊 No history available yet.")
            return
        
        print("\n" + "="*70)
        print("CALCULATION HISTORY".center(70))
        print("="*70)
        
        for i, entry in enumerate(self.history, 1):
            print(f"\n[{i}] {entry['calc']}")
            print(f"    Time: {entry['time']}")
        
        print("\n" + "="*70)
    
    def clear_history(self):
        """Remove all calculation history"""
        self.history = []
        print("\n✓ History cleared successfully!")

def display_menu():
    """Show main menu options"""
    print("\n" + "="*70)
    print("CALCULATOR MENU".center(70))
    print("="*70)
    print("\n[1] Basic Operations (+, -, *, /, **, %, //)")
    print("[2] Scientific Operations (sqrt, sin, cos, tan, log, factorial)")
    print("[3] View History")
    print("[4] Clear History")
    print("[5] Exit")
    print("\n" + "="*70)

def get_number(prompt):
    """Helper function to get numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("✗ Invalid input! Please enter a valid number.")

def main():
    """Main application loop"""
    calc = ScientificCalculator()
    
    print("\n" + "*"*70)
    print("ADVANCED CALCULATOR".center(70))
    print("Perform basic and scientific calculations with ease".center(70))
    print("*"*70)
    
    while True:
        display_menu()
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            print("\n--- Basic Operations ---")
            print("Available: + (add), - (subtract), * (multiply), / (divide)")
            print("          ** (power), % (modulo), // (floor division)")
            
            num1 = get_number("\nEnter first number: ")
            operation = input("Enter operation (+, -, *, /, **, %, //): ").strip()
            num2 = get_number("Enter second number: ")
            
            result = calc.calculate(num1, operation, num2)
            print(f"\n🎯 Result: {num1} {operation} {num2} = {result}")
        
        elif choice == '2':
            print("\n--- Scientific Operations ---")
            print("Available: sqrt, square, cube, sin, cos, tan, log, ln, factorial")
            
            operation = input("\nEnter operation: ").strip().lower()
            value = get_number("Enter value: ")
            
            result = calc.scientific_operation(operation, value)
            print(f"\n🎯 Result: {operation}({value}) = {result}")
        
        elif choice == '3':
            calc.show_history()
        
        elif choice == '4':
            confirm = input("\nAre you sure you want to clear history? (yes/no): ").lower()
            if confirm == 'yes':
                calc.clear_history()
        
        elif choice == '5':
            print("\n" + "*"*70)
            print("Thank you for using Advanced Calculator!".center(70))
            print("Happy Calculating!".center(70))
            print("*"*70 + "\n")
            break
        
        else:
            print("\n✗ Invalid choice! Please select 1-5.")
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()

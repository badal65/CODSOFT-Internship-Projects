#!/usr/bin/env python3
"""
Task Management Application
A simple yet powerful command-line tool for managing daily tasks
Author: Badal Chaudhary 
Project: CODSOFT Python Programming Internship
"""

import json
import os
from datetime import datetime
from typing import List, Dict

class TaskManager:
    """Main class to handle all task operations"""
    
    def __init__(self, storage_file='my_tasks.json'):
        self.storage_file = storage_file
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> List[Dict]:
        """Load existing tasks from file storage"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_tasks(self):
        """Persist tasks to file storage"""
        with open(self.storage_file, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self, description: str, priority: str = 'medium'):
        """Create a new task entry"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'priority': priority,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"\n✓ Task added successfully! (ID: {task['id']})")
    
    def view_tasks(self, filter_type='all'):
        """Display tasks based on filter criteria"""
        if not self.tasks:
            print("\n📋 No tasks found. Start by adding a new task!")
            return
        
        print("\n" + "="*60)
        print("YOUR TASKS".center(60))
        print("="*60)
        
        filtered_tasks = self.tasks
        if filter_type == 'pending':
            filtered_tasks = [t for t in self.tasks if not t['completed']]
        elif filter_type == 'completed':
            filtered_tasks = [t for t in self.tasks if t['completed']]
        
        if not filtered_tasks:
            print(f"\nNo {filter_type} tasks found.")
            return
        
        for task in filtered_tasks:
            status = "✓" if task['completed'] else "○"
            priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}
            icon = priority_icon.get(task['priority'], '⚪')
            
            print(f"\n[{task['id']}] {status} {icon} {task['description']}")
            print(f"    Priority: {task['priority'].upper()} | Created: {task['created_at']}")
        
        print("\n" + "="*60)
    
    def update_task(self, task_id: int, new_description: str):
        """Modify task description"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                self.save_tasks()
                print(f"\n✓ Task {task_id} updated successfully!")
                return
        print(f"\n✗ Task {task_id} not found!")
    
    def mark_complete(self, task_id: int):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"\n✓ Task {task_id} marked as complete!")
                return
        print(f"\n✗ Task {task_id} not found!")
    
    def delete_task(self, task_id: int):
        """Remove a task from the list"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print(f"\n✓ Task {task_id} deleted successfully!")
                return
        print(f"\n✗ Task {task_id} not found!")

def display_menu():
    """Show available options to user"""
    print("\n" + "="*60)
    print("TASK MANAGER MENU".center(60))
    print("="*60)
    print("\n1. Add New Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. View Completed Tasks")
    print("5. Update Task")
    print("6. Mark Task as Complete")
    print("7. Delete Task")
    print("8. Exit Application")
    print("\n" + "="*60)

def main():
    """Main application entry point"""
    manager = TaskManager()
    
    print("\n" + "*"*60)
    print("WELCOME TO YOUR PERSONAL TASK MANAGER".center(60))
    print("*"*60)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            description = input("\nEnter task description: ").strip()
            priority = input("Enter priority (high/medium/low) [default: medium]: ").strip().lower()
            if priority not in ['high', 'medium', 'low']:
                priority = 'medium'
            manager.add_task(description, priority)
        
        elif choice == '2':
            manager.view_tasks('all')
        
        elif choice == '3':
            manager.view_tasks('pending')
        
        elif choice == '4':
            manager.view_tasks('completed')
        
        elif choice == '5':
            try:
                task_id = int(input("\nEnter task ID to update: "))
                new_desc = input("Enter new description: ").strip()
                manager.update_task(task_id, new_desc)
            except ValueError:
                print("\n✗ Invalid task ID!")
        
        elif choice == '6':
            try:
                task_id = int(input("\nEnter task ID to mark complete: "))
                manager.mark_complete(task_id)
            except ValueError:
                print("\n✗ Invalid task ID!")
        
        elif choice == '7':
            try:
                task_id = int(input("\nEnter task ID to delete: "))
                confirm = input(f"Are you sure you want to delete task {task_id}? (yes/no): ").lower()
                if confirm == 'yes':
                    manager.delete_task(task_id)
            except ValueError:
                print("\n✗ Invalid task ID!")
        
        elif choice == '8':
            print("\n" + "*"*60)
            print("Thank you for using Task Manager!".center(60))
            print("Stay productive and organized!".center(60))
            print("*"*60 + "\n")
            break
        
        else:
            print("\n✗ Invalid choice! Please select 1-8.")

if __name__ == '__main__':
    main()

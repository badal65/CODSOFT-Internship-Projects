#!/usr/bin/env python3
"""
Secure Password Generator
Generates strong, customizable passwords for enhanced security
Author: Badal Prajapati
CODSOFT Python Programming Internship - Task 3
"""

import random
import string
import secrets
import pyperclip

class PasswordGenerator:
    """Generate secure passwords with various options"""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation
        self.history = []
    
    def generate_password(self, length=12, use_upper=True, use_lower=True, 
                         use_digits=True, use_symbols=True, exclude_ambiguous=False):
        """Generate a password based on specified criteria"""
        
        if length < 4:
            return "Error: Password length must be at least 4 characters"
        
        char_pool = ''
        required_chars = []
        
        if use_lower:
            chars = self.lowercase
            if exclude_ambiguous:
                chars = chars.replace('l', '').replace('o', '')
            char_pool += chars
            required_chars.append(secrets.choice(chars))
        
        if use_upper:
            chars = self.uppercase
            if exclude_ambiguous:
                chars = chars.replace('I', '').replace('O', '')
            char_pool += chars
            required_chars.append(secrets.choice(chars))
        
        if use_digits:
            chars = self.digits
            if exclude_ambiguous:
                chars = chars.replace('0', '').replace('1', '')
            char_pool += chars
            required_chars.append(secrets.choice(chars))
        
        if use_symbols:
            char_pool += self.symbols
            required_chars.append(secrets.choice(self.symbols))
        
        if not char_pool:
            return "Error: At least one character type must be selected"
        
        # Generate remaining characters
        remaining_length = length - len(required_chars)
        password_chars = required_chars + [secrets.choice(char_pool) for _ in range(remaining_length)]
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        
        # Store in history
        self.history.append(password)
        
        return password
    
    def generate_passphrase(self, word_count=4):
        """Generate memorable passphrase"""
        words = [
            'alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf',
            'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november',
            'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform',
            'victor', 'whiskey', 'xray', 'yankee', 'zulu', 'ocean', 'mountain',
            'river', 'forest', 'desert', 'island', 'valley', 'canyon', 'summit'
        ]
        
        selected_words = [secrets.choice(words).capitalize() for _ in range(word_count)]
        passphrase = '-'.join(selected_words) + str(secrets.randbelow(100))
        
        self.history.append(passphrase)
        return passphrase
    
    def check_strength(self, password):
        """Evaluate password strength"""
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Too short (minimum 8 characters)")
        
        # Character variety
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if any(c in string.punctuation for c in password):
            score += 1
        else:
            feedback.append("Add special characters")
        
        # Determine strength level
        if score >= 5:
            strength = "Strong 🟢"
        elif score >= 3:
            strength = "Medium 🟡"
        else:
            strength = "Weak 🔴"
        
        return {
            'strength': strength,
            'score': score,
            'feedback': feedback
        }
    
    def show_history(self):
        """Display generated passwords"""
        if not self.history:
            print("\n📊 No password history available.")
            return
        
        print("\n" + "="*60)
        print("PASSWORD HISTORY".center(60))
        print("="*60)
        for i, pwd in enumerate(self.history[-10:], 1):
            print(f"\n[{i}] {pwd}")
        print("\n" + "="*60)

def display_menu():
    """Show main menu"""
    print("\n" + "="*60)
    print("PASSWORD GENERATOR MENU".center(60))
    print("="*60)
    print("\n[1] Generate Custom Password")
    print("[2] Generate Passphrase")
    print("[3] Check Password Strength")
    print("[4] View History")
    print("[5] Exit")
    print("\n" + "="*60)

def main():
    """Main application"""
    generator = PasswordGenerator()
    
    print("\n" + "*"*60)
    print("SECURE PASSWORD GENERATOR".center(60))
    print("Create strong passwords for your security".center(60))
    print("*"*60)
    
    while True:
        display_menu()
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            print("\n--- Custom Password Generation ---")
            try:
                length = int(input("Password length (min 4): "))
                use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
                use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
                use_digits = input("Include digits? (y/n): ").lower() == 'y'
                use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
                exclude_ambiguous = input("Exclude ambiguous characters (l,O,0,1)? (y/n): ").lower() == 'y'
                
                password = generator.generate_password(
                    length, use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous
                )
                
                print(f"\n🔑 Generated Password: {password}")
                
                # Check strength
                result = generator.check_strength(password)
                print(f"\nStrength: {result['strength']} (Score: {result['score']}/6)")
                
                if input("\nCopy to clipboard? (y/n): ").lower() == 'y':
                    try:
                        pyperclip.copy(password)
                        print("✓ Password copied to clipboard!")
                    except:
                        print("✗ Clipboard not available")
            
            except ValueError:
                print("✗ Invalid input!")
        
        elif choice == '2':
            print("\n--- Passphrase Generation ---")
            try:
                word_count = int(input("Number of words (3-6): "))
                if 3 <= word_count <= 6:
                    passphrase = generator.generate_passphrase(word_count)
                    print(f"\n🔑 Generated Passphrase: {passphrase}")
                    
                    if input("\nCopy to clipboard? (y/n): ").lower() == 'y':
                        try:
                            pyperclip.copy(passphrase)
                            print("✓ Passphrase copied!")
                        except:
                            print("✗ Clipboard not available")
                else:
                    print("✗ Word count must be between 3 and 6")
            except ValueError:
                print("✗ Invalid input!")
        
        elif choice == '3':
            password = input("\nEnter password to check: ")
            result = generator.check_strength(password)
            print(f"\nStrength: {result['strength']} (Score: {result['score']}/6)")
            if result['feedback']:
                print("\nSuggestions:")
                for suggestion in result['feedback']:
                    print(f"  • {suggestion}")
        
        elif choice == '4':
            generator.show_history()
        
        elif choice == '5':
            print("\n" + "*"*60)
            print("Stay secure with strong passwords!".center(60))
            print("*"*60 + "\n")
            break
        
        else:
            print("✗ Invalid choice!")

if __name__ == '__main__':
    # Note: pyperclip may need installation: pip install pyperclip
    try:
        import pyperclip
    except ImportError:
        print("Note: Install pyperclip for clipboard functionality: pip install pyperclip")
    
    main()

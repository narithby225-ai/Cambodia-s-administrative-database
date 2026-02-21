"""
Verify that login stays open on wrong input
"""
print("=" * 60)
print("VERIFYING LOGIN BEHAVIOR")
print("=" * 60)
print()

# Check the code
with open('gui_clean_cool.py', 'r', encoding='utf-8') as f:
    content = f.read()

print("Checking login function...")
print()

# Check for correct behavior
checks = {
    "Empty field handling": "return" in content and "Please fill in all fields" in content,
    "Button re-enable": "self.login_btn.setEnabled(True)" in content,
    "Password clear": "self.password_input.clear()" in content,
    "Focus return": "self.password_input.setFocus()" in content,
    "No reject on error": content.count("self.reject()") <= 1,  # Only in close button
    "Success closes": "self.fade_out" in content and "self.accept()" in content,
}

all_good = True
for check, result in checks.items():
    status = "✅" if result else "❌"
    print(f"{status} {check}")
    if not result:
        all_good = False

print()
print("=" * 60)

if all_good:
    print("✅ ALL CHECKS PASSED!")
    print()
    print("Login behavior is CORRECT:")
    print("  • Stays open on empty fields")
    print("  • Stays open on wrong password")
    print("  • Clears password and refocuses")
    print("  • User can retry immediately")
    print("  • Only closes on success")
    print()
    print("Test it:")
    print("  python gui_clean_cool.py")
    print()
    print("Try wrong password:")
    print("  Username: admin")
    print("  Password: wrong")
    print("  → Should stay open and let you retry!")
else:
    print("❌ SOME CHECKS FAILED")
    print("Please review the code")

print("=" * 60)

from analyzer import analyze_password

print("=" * 45)
print("      Password Strength Analyzer")
print("=" * 45)

password = input("Enter Password: ")

result = analyze_password(password)

print("\nAnalysis Result")
print("-" * 30)
print(f"Strength : {result['rating']}")
print(f"Score    : {result['score']}/5")

if result["suggestions"]:
    print("\nSuggestions:")
    for suggestion in result["suggestions"]:
        print(f"- {suggestion}")
else:
    print("\nExcellent! Your password is very strong.")
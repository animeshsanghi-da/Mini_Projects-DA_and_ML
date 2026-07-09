import random

def generate_business_names(keyword, count=5):
    """
    Generates professional business names based on a core keyword.
    """
    # Professional prefixes and adjectives
    adjectives = [
        'Apex', 'Vanguard', 'Quantum', 'Luminous', 'Synergy', 
        'Catalyst', 'Prime', 'Agile', 'Dynamic', 'Nexus',
        'Stellar', 'Elevate', 'Omni', 'Pinnacle', 'Vertex'
    ]
    
    # Corporate suffixes
    suffixes = [
        'Solutions', 'Labs', 'Dynamics', 'Ventures', 'Consulting', 
        'Innovations', 'Tech', 'Hub', 'Group', 'Matrix',
        'Systems', 'Partners', 'Analytics', 'Network', 'Corp'
    ]
    
    generated_names = set() # Use a set to prevent duplicate names
    
    # Generate names until we hit the requested count
    while len(generated_names) < count:
        adj = random.choice(adjectives)
        suffix = random.choice(suffixes)
        
        # Randomly vary the structure of the business name
        structure = random.choice([1, 2, 3])
        if structure == 1:
            name = f"{adj} {keyword} {suffix}"
        elif structure == 2:
            name = f"{keyword} {suffix}"
        else:
            name = f"{adj} {keyword}"
            
        generated_names.add(name)
        
    return list(generated_names)

def main():
    print("=" * 40)
    print("🚀 AI-Assisted Business Name Generator")
    print("=" * 40)
    
    keyword = input("\nEnter your core business keyword (e.g., 'Data', 'Bistro', 'Logistics'): ").strip()
    
    if not keyword:
        print("Error: Keyword cannot be empty. Exiting.")
        return

    try:
        count = int(input("How many ideas do you need? (Default is 5): ") or 5)
    except ValueError:
        print("Invalid input. Defaulting to 5 names.")
        count = 5

    print("\nGenerating...\n")
    names = generate_business_names(keyword.capitalize(), count)
    
    print("-" * 40)
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")
    print("-" * 40)

if __name__ == "__main__":
    main()

"""
How to Run & Test

1. Run the script: python name_generator.py
2. Test it by typing a keyword like "Analytics" or "Motors".
"""
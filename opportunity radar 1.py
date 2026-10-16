opportunities = []

while True:
    print("\n===== OPPORTUNITY RADAR =====")
    print("1. Add an opportunity")
    print("2. View opportunities")
    print("3. Delete an opportunity")
    print("4. Count opportunities")
    print("5. Search an opportunity")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter opportunity name: ")
        category = input("Enter category (Hackathon/Internship/Workshop): ")
        deadline = input("Enter deadline: ")

        opportunity = {
            "name": name,
            "category": category,
            "deadline": deadline
        }

        opportunities.append(opportunity)
        print("Opportunity added successfully!")

    elif choice == "2":
        if len(opportunities) == 0:
            print("No opportunities added yet.")
        else:
            for i, opportunity in enumerate(opportunities):
                print("\nOpportunity:", i + 1)
                print("Name:", opportunity["name"])
                print("Category:", opportunity["category"])
                print("Deadline:", opportunity["deadline"])

    elif choice == "3":
        if len(opportunities) == 0:
            print("No opportunities to delete.")
        else:
            for i, opportunity in enumerate(opportunities):
                print(i + 1, opportunity["name"])

            number = int(input("Enter the number to delete: "))

            if 1 <= number <= len(opportunities):
                deleted = opportunities.pop(number - 1)
                print(deleted["name"], "deleted successfully!")
            else:
                print("Invalid opportunity number.")

    elif choice == "4":
        print("Total opportunities:", len(opportunities))

    elif choice == "5":
        search_name = input("Enter opportunity name to search: ")
        found = False

        for opportunity in opportunities:
            if opportunity["name"].lower() == search_name.lower():
                print("\nOpportunity found!")
                print("Name:", opportunity["name"])
                print("Category:", opportunity["category"])
                print("Deadline:", opportunity["deadline"])
                found = True

        if found == False:
            print("Opportunity not found.")

    elif choice == "6":
        print("Thank you for using Opportunity Radar!")
        break

    else:
        print("Invalid choice. Please try again.")
guests  = ['Max', 'Aaron', 'Edgar']
for guest in guests:
    invitation = f"Hello {guest.title()}, please acccept my invitation to dinner."
    print(invitation)

print(f"\nSorry, {guests[1]} can't make it.\n")

guests = ['Max', 'Edgar', 'Tony']
for guest in guests:
    invitation = f"Hello {guest.title()}, please acccept my invitation to dinner."
    print(invitation)
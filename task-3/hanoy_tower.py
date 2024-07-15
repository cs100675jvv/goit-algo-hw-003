def move_disks(n, source, auxiliary, target, state):
    if n == 1:
        # Move the disk from source to target
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
    else:
        # Move n-1 disks from source to auxiliary, using target as auxiliary
        move_disks(n-1, source, target, auxiliary, state)
        # Move the nth disk from source to target
        move_disks(1, source, auxiliary, target, state)
        # Move the n-1 disks from auxiliary to target, using source as auxiliary
        move_disks(n-1, auxiliary, source, target, state)

def hanoi_tower(n):
    # Initial state of the rods
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")
    # Move the disks from rod A to rod C using rod B
    move_disks(n, 'A', 'B', 'C', state)
    print(f"Кінцевий стан: {state}")

# Example usage:
n = 5
hanoi_tower(n)

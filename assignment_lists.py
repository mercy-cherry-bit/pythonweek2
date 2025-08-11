def main():
    my_list = []
    print("Step 1 - empty list:", my_list)
    for v in [10, 20, 30, 40]:
        my_list.append(v)
    print("Step 2 - after append:", my_list)
    my_list.insert(1, 15)
    print("Step 3 - after insert 15 at index 1:", my_list)
    my_list.extend([50, 60, 70])
    print("Step 4 - after extend:", my_list)
    removed = my_list.pop()  
    print(f"Step 5 - removed last element ({removed}):", my_list)
    my_list.sort()
    print("Step 6 - after sort:", my_list)
    index_of_30 = my_list.index(30)
    print("Step 7 - index of 30:", index_of_30)
    print("\nFinal list:", my_list)
    print("Index of 30:", index_of_30)

if _name_ == "_main_":
    main()
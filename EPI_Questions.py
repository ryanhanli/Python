# Write a program which takes as input a sorted array A of integers and a positive integer m, and updates A 
# so that if x appears m times in A it appears exactly min(2,m) times in A.
def delete_duplicates_min(A, m):
    if not A or m <= 0:
        return 0
    write_index = 1
    count = 1
    for i in range(1, len(A)):
        if A[write_index - 1] == A[i]:
            count += 1
        else:
            count = 1
        if A[write_index - 1] != A[i] or count <= min(2, m):
            A[write_index] = A[i]
            write_index += 1
            print(A)
    #print(A)
    return write_index

print(delete_duplicates_min([1,2,3,3,3,3,3,3,3,5,6,7,8,8,9], 2))

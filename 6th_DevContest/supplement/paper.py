def minimize_button_presses(arr):
    n = len(arr)
    presses = 0

    for i in range(n):
        if arr[i] > 0:
            presses += arr[i]
            press_amount = arr[i]

            # Apply the press to the current and adjacent positions
            for j in range(i, min(i + 3, n)):
                arr[j] = max(0, arr[j] - press_amount)

    return presses

# Test the function with the provided array
array = [1,4,2, 10, 4]
print(minimize_button_presses(array))
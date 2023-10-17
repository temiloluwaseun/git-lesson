from collections import Counter

# Sample data from your provided table
data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

# Concatenate the data from all days into a single list of colors
all_colors = [color.strip() for day_colors in data.values() for color in day_colors.split(",")]

# Calculate the mean color
mean_color = max(set(all_colors), key=all_colors.count)

# Calculate the color mostly worn throughout the week
most_common_color = Counter(all_colors).most_common(1)[0][0]

# Calculate the median color
sorted_colors = sorted(all_colors)
middle_index = len(sorted_colors) // 2
median_color = sorted_colors[middle_index]

print("Mean Color:", mean_color)
print("Most Worn Color:", most_common_color)
print("Median Color:", median_color)

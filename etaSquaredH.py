# Function to calculate eta squared for H statistic from Kruskal Wallis one way ANOVA. 
# Eta squared is a measure of effect size
# This function was created to work with scipy's kruskal function, meaning you can easily get the H statistic from that output.
# To get the H statistic, first assign your kruskal output a specific name. Example: my_name = kruskal(args go here) 
# Then set another variable equal to my_name.statistic to capture the H statistic value.

# H = H statistic from the Kruskal Wallis test
# k = number of groups
# n = sample size

def effectSizeH(H,k,n):
    # Begin calculation
    eta_squared = (H - k + 1)/(n - k)
    # Determine strength of effect size
    # Small effect size
    if eta_squared < 0.06:
        effect_size = "small"
    # Moderate effect size
    elif eta_squared >= 0.06 and eta_squared < 0.14:
        effect_size = "moderate"
    # Large effect size
    else:
        effect_size = "large"
    # print out interpretation
    print("Eta squared is ", eta_squared)
    print("The effect size is ", effect_size, ".")

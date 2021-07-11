## consensus.py created by Leslie A. McFarlin
## Calculates the consensus (agreement) and dissention (disagreement) rates among respondents.
## The calculations used are based upon those defined by Tastle & Wierman in their 2006 article,
## Consensus and Dissention: A Measure of Ordinal Dispersion.
## Consensus and dissention are excellent metrics to have for ordinal scale data as it makes no sense to 
## treat those data as if they are interval data, which is a common tactic by researchers.

## consensus.py was originally written for a 5-point Likert scale where 1 = Strongly Disagree and 5 = Strongly Agree
## It assumes that for this type of data, each variable is saved in a unique dictionary that is created from information
## generated by the .describe() and .value_counts() functions.

## For ease of understanding, there are two python functions in this file.
## Probability calculations can be nested into the consensus function if you choose.

## If you have not done so in your analysis, uncomment the line below and begin by importing python's math library.
## import math as mth

## To begin, calculate the probabilities of receiving each value in a Likert Scale
## This function takes a dictionary containing values from .describe() and .value_counts()
def probCalc(dict):
    # Dictionary to hold calculations
    holder_dict = {}
    # Key from existing dictionary may be int or float type
    for key, value in dict.items():
      # This section should be adjusted based on the scale size used for the variable.
      # You may require more or fewer scale items here.
        if key == 5 or key == 5.0:
            prob = value/dict.get('count')
            new_key = "5-prob"
            holder_dict.update({new_key : prob})
        elif key == 4 or key == 4.0:
            prob = value/dict.get('count')
            new_key = "4-prob"
            holder_dict.update({new_key : prob})
        elif key == 3 or key == 3.0:
            prob = value/dict.get('count')
            new_key = "3-prob"
            holder_dict.update({new_key : prob})
        elif key == 2 or key == 2.0:
            prob = value/dict.get('count')
            new_key = "2-prob"
            holder_dict.update({new_key : prob})
        elif key == 1 or key == 1.0:
            prob = value/dict.get('count')
            new_key = "1-prob"
            holder_dict.update({new_key : prob})
        # If the value is not found, it will be skipped.
        else:
            pass
    # Updates the passed dictionary after all iterations are complete.
    dict.update(holder_dict)
    return
  
## Begin calculating the consensus and dissention rates
## Use the dictionary updated by probCalc()
## To make it easier to find issues with calculations, the components of the formula are broken out.
## They can be condensed to save lines.
def consensusRate(dict):
    # Collect the calculations in a list
    calc_list = []
    # Calculate the distance, d
    d = dict.get('max') - dict.get('min')
    # Iterate through the dictionary via key value
    for key, value in dict.items():
        # Calculations per key value
        # When evaluating Likert Scale rating of 5
        if key == 5 or key == 5.0:
            # Get the absolute value for the numerator
            numerator = abs(key - (dict.get('mean')))
            logvalue = mth.log2(1-(numerator/d))
            entvalue = dict.get('5-prob') * logvalue
            calc_list.append(entvalue)
        # When evaluating Likert Scale rating of 4    
        elif key == 4 or key == 4.0:
            # Get the absolute value for the numerator
            numerator = abs(key - (dict.get('mean')))
            logvalue = mth.log2(1-(numerator/d))
            entvalue = dict.get('4-prob') * logvalue
            calc_list.append(entvalue)
        # When evaluating Likert Scale rating of 3    
        elif key == 3 or key == 3.0:
            # Get the absolute value for the numerator
            numerator = abs(key - (dict.get('mean')))
            logvalue = mth.log2(1-(numerator/d))
            entvalue = dict.get('3-prob') * logvalue
            calc_list.append(entvalue)
        # When evaluating Likert Scale rating of 2 
        elif key == 2 or key == 2.0:
            # Get the absolute value for the numerator
            numerator = abs(key - (dict.get('mean')))
            logvalue = mth.log2(1-(numerator/d))
            entvalue = dict.get('2-prob') * logvalue
            calc_list.append(entvalue)
        # When evaluating Likert Scale rating of 1 
        elif key == 1 or key == 1.0:
            # Get the absolute value for the numerator
            numerator = abs(key - (dict.get('mean')))
            logvalue = mth.log2(1-(numerator/d))
            entvalue = dict.get('2-prob') * logvalue
            calc_list.append(entvalue)
        else:
            pass
    # Calculate the Consensus Rate
    consensus = round(1 + sum(calc_list), 2)
    # Update the dictionary with consensus rate
    dict.update({'consensus': consensus})
    # Calculate the Dissention Rate
    dissention = round(1 - consensus, 2)
    # Update the dictionary with dissention rate
    dict.update({'dissention': dissention})
    return
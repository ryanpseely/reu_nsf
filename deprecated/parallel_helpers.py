from scipy.stats import mannwhitneyu
import numpy as np

def compare_word_across_years(j, word_columns, years, year_data):
    results = []

    for i in range(len(years) - 1):
        year1, year2 = years[i], years[i + 1]
        vec1 = X[year_masks[year1], j]
        vec2 = X[year_masks[year2], j]

        prop1 = (vec1 > 0).mean()
        prop2 = (vec2 > 0).mean()
        if prop1 + prop2 == 0:
            continue

        try:
            stat, p = mannwhitneyu(vec1, vec2, alternative='two-sided')
            results.append({
                'Year1': year1,
                'Year2': year2,
                'word': word_columns[j],
                'U_stat': stat,
                'p_value': p,
                'prop1': prop1,
                'prop2': prop2,
                'effect_size': prop2 - prop1
            })
        except ValueError:
            continue
    return results
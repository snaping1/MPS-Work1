banks = {
    "WhatsApp":       [0.72, 0.65, 0.92, 0.9, 0.91, 0.84],
    "Telegram":   [0.88, 0.95, 0.83, 0.77, 0.89, 0.65],
    "Discord":     [0.9, 0.81, 0.79, 0.1, 0.73, 0.79],
    "Skype":     [0.87, 0.9, 0.6, 0.83, 0.71, 0.68]
}

weights = [0.2, 0.2, 0.1, 0.3, 0.1, 0.1]

def scoring_model(data, weights):
    scores = {}
    for bank, criteria in data.items():
        total = 0
        for i in range(len(criteria)):
            total += criteria[i] * weights[i]
        scores[bank] = round(total, 3)
    return scores


def wpm_model(data, weights):
    scores = {}
    for bank, criteria in data.items():
        product = 1
        for i in range(len(criteria)):
            product *= criteria[i] ** weights[i]
        scores[bank] = round(product, 3)
    return scores


def normalized_scoring(data, weights):
    max_values = [max(col) for col in zip(*data.values())]
    scores = {}
    for bank, criteria in data.items():
        total = 0
        for i in range(len(criteria)):
            normalized = criteria[i] / max_values[i]
            total += normalized * weights[i]
        scores[bank] = round(total, 3)
    return scores


scoring = scoring_model(banks, weights)
wpm = wpm_model(banks, weights)
norm = normalized_scoring(banks, weights)

print("Scoring:", dict(sorted(scoring.items(), key=lambda x: x[1], reverse=True)))
print("WPM:", dict(sorted(wpm.items(), key=lambda x: x[1], reverse=True)))
print("Normalized:", dict(sorted(norm.items(), key=lambda x: x[1], reverse=True)))
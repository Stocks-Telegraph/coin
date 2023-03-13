def performance_change(dataFrame):
    final = dataFrame['close'].iloc[0]
    initial = dataFrame['close'].iloc[-1]
    performance = 100 * (final - initial) / abs(initial)
    return round(performance, 2)

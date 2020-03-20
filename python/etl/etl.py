def transform(legacy_data):
    return {letter.lower(): lst for lst in legacy_data for letter in legacy_data[lst]}

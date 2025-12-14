def volum_analysis(collumn, median, min, max):
    volum = ""
    # --- A. Volum (Trafikknivå) ---
    if collumn >= max:
        volum = "Høy"
    elif collumn <= min:
        volum = "Veldig Lav"
    elif collumn >= median:
        volum = "Middels-Høy"
    else:
        volum = "Middels-Lav"
    return volum


def sesong_week_analysis(collumn):
    sesong = ""
    if collumn <= 15:
        sesong = "Tidlig i året (Vår)"
    elif collumn >= 35:
        sesong = "Sent i året (Høst/Vinter)"
    else:
        sesong = "Midt i året (Sommer)"
    return sesong

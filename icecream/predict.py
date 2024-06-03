def predict_sales(temp: int, num_people: int) -> int:
    prediction = 10 + temp * 0.3 + num_people * 0.2
    return int(prediction)


# run new

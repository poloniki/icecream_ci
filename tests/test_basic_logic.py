from icecream.predict import predict_sales


def test_return_type():
    assert isinstance(predict_sales(20, 30), int), "Return type is wrong"


def test_common_sense():
    assert predict_sales(20, 30) > 0, "Sales can not show negative numbers"

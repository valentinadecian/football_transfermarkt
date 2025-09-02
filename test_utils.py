from utils import *

def create_series():
    test_df = pd.DataFrame({'s1': [1, 1, 1, 1, 3, 3, 5, 10, 10, 10, 18, 100]})
    return test_df['s1']

def test_create_plot():
    series = create_series()
    print(series)
    create_plot('box', series, 'my_title', 'my_x_label', 'my_y_label', 'test_file', rotation=0, bottom=0.1, grid=True)
    create_plot('line', series, 'my_title', 'my_x_label', 'my_y_label', 'test_file', rotation=0, bottom=0.1, grid=True)
    create_plot('hist', series, 'my_title', 'my_x_label', 'my_y_label', 'test_file', rotation=0, bottom=0.1, grid=True)

test_create_plot()
import numpy as np
import matplotlib.pyplot as plot
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def split_data():
    # Split the dataset into the training set and test set
    # We're splitting the data in 1/3, so out of 30 rows, 20 rows will go into the training set,
    # and 10 rows will go into the testing set.
    x_train, x_test, y_train, y_test = train_test_split(
        x_values, y_values, test_size=1 / 3, random_state=0
    )

    return (x_train, x_test, y_train, y_test)


def import_data():
    data_set = pandas.read_csv("data.csv")
    x_values = data_set.iloc[:, :-1].values
    y_values = data_set.iloc[:, 1].values
    return x_values, y_values


def plot_data(x_points, y_points, predictor, label):
    plot.scatter(x_points, y_points, color="red")
    plot.plot(x_points, predictor.predict(x_points), color="blue")
    plot.title(label)
    plot.xlabel("Years of Experience")
    plot.ylabel("Salary")
    plot.show()


if __name__ == "__main__":
    x_values, y_values = import_data()
    x_train, x_test, y_train, y_test = split_data()

    linear_regressor = LinearRegression()
    linear_regressor.fit(x_values, y_values)

    y_prediction = linear_regressor.predict(x_test)

    plot_data(x_train, y_train, linear_regressor, "Salary vs Experince (Training set)")
    plot_data(x_test, y_test, linear_regressor, "Salary vs Experince (Test set)")

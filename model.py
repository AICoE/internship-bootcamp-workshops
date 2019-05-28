# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plot
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def import_data_and_split():
    # Import the dataset
    d = pandas.read_csv('data.csv')
    x = d.iloc[:, :-1].values
    y = d.iloc[:, 1].values

    # Split the dataset into the training set and test set
    # We're splitting the data in 1/3, so out of 30 rows, 20 rows will go into the training set,
    # and 10 rows will go into the testing set.
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =1 / 3, random_state = 0)

    return (x_train, x_test, y_train, y_test)



if __name__ == '__main__':
    x_train, x_test, y_train, y_test = import_data_and_split()

    # Creating a LinearRegression object and fitting it
    # on our trainging set.
    linear_regressor = LinearRegression()
    linear_regressor.fit(x_train, y_train)

    # Predicting the test set results
    y_prediction = linear_regressor.predict(x_test)

    # Visualising the training set results
    plot.scatter(x_train, y_train, color ='red')
    plot.plot(x_train, linear_regressor.predict(x_train), color ='blue')
    plot.title('Salary vs Experience (Training set)')
    plot.xlabel('Years of Experience')
    plot.ylabel('Salary')
    plot.show()

    # Visualising the test set results
    plot.scatter(x_test, y_test, color ='red')
    plot.plot(x_test, linear_regressor.predict(x_test), color ='blue')
    plot.title('Salary vs Experience (Test set)')
    plot.xlabel('Years of Experience')
    plot.ylabel('Salary')
    plot.show()

# Workshop: Development and Coding Standards

## Fork and clone

As always you should first *fork* https://github.com/AICoE/workshop-coding-best-practices into your github account.
Click on the `Fork` button in the upper right corner.

Then *clone* your fork to your local machine. 

**REPLACE <my_account_name> with your account name**

`git clone git@github.com:<my_account_name>/workshop-coding-best-practices.git`

If the above fails, make sure you have setup git correctly, for help see: https://help.github.com/en/articles/testing-your-ssh-connection

Now you can `cd workshop-coding-best-practices` into your fork.

## Installation and execution the model code

To manage python requirements we're using [Pipenv](https://github.com/pypa/pipenv#installation). On Fedora you should be
good with running `sudo dnf install pipenv`.

TODO: check if this works and if the interns have rhel CSB?!

Now install all requirements with `pipenv install` and enter a shell with the correct python settings: `pipenv shell`
If some dependencies are missing when you run your code, you might be in another shell without the correct settings.
Again, run `pipenv shell` in this directory or always execute your code with `pipenv run python model.py`

Then you can run the code via `python model.py`

## Clean Code

You'll go through 5 steps of refactoring to make the code a little bit better to understand and read.
This is important, because not only you will need to understand your code one month ahead, but also your peers.
So [Clean Code](https://www.oreilly.com/library/view/clean-code/9780136083238/) is a book and a [Google Search Term](http://lmgtfy.com/?q=clean+code) 
you should remember.

### Naming Convention

> When you write Python code, you have to name a lot of things: variables, functions, classes, packages, and so on. Choosing sensible names will save you time and energy later. You’ll be able to figure out, from the name, what a certain variable, function, or class represents. You’ll also avoid using inappropriate names that might result in errors that are difficult to debug.

[PEP8 Naming Conventions](https://realpython.com/python-pep8/#naming-conventions).

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/db01c83b35a37452586c774fd34144ca675ade23)

### Meaningful names

> This is what makes code self-documenting. When you read over your old code, you shouldn’t have to look over every little comment and run every small piece of code to figure out what it all does!
> The code should roughly read like plain English. This is especially true for variable names, classes, and functions. Those three items should always have names that are self-explanatory. Rather than use a default name like “x” for example, call it “width” or “distance” or whatever the variable is supposed to represent in “read-world” terms. Coding in “real-world” terms will help make your code read in that way

[Choosing Names](https://medium.com/@george.seif94/these-5-clean-code-tips-will-dramatically-improve-your-productivity-b20c152783b)

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/ac522375c622b2cfdcd064f43d737b89b29b7921)

### Single Responsibility

> One method should be responsible only for one action. If your method does two or three different things at a time then you should consider splitting the functionality of this method into other methods.
> Such method is easier to understand, scale and reuse in other methods.

[10 Tips To Keep Your Code Clean](https://medium.com/oril/10-tips-to-keep-your-code-more-clean-2fa9aafea1cf#d065)

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/90fc03ab3437099d68fd544ab76be58d474010f6)

### Keep it DRY

> The DRY principle, formulated by Any Hunt and Dave Thomas in The Pragmatic Programmer, is the use of functions, classes and instances to allow you to avoid retyping code that has already been written once. This fundamental principle allows developers to avoid duplication to produce much cleaner code compared to the programmer who uses unnecessary repetition. Optimizing the code is what often separates a great coder from an average one.

[Don’t Repeat Yourself (DRY)](https://www.codingdojo.com/blog/clean-code-techniques)

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/129f0910586a205f36a025586d8e4d4ba746b229)

### Comments

> 1. Always try to explain yourself in code.
> 2. Don't be redundant.
> 3. Don't add obvious noise.

[Comments Rules by Uncle Bob](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29#comments-rules)

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/0127ea96ae8bd193c433b09672579fb39417e4d8)

### 🐍 Zen of Python

What happens if you run the following import in the Python interpreter?

```python
import this
```

An easter egg shows up - [Zen of Python](https://www.python.org/dev/peps/pep-0020/):

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```



## Data Science Perspective

### Understand Data

#### Preview Data

> It is always important to scan through the raw data to gain insights like the amount of data you are working with, understand data types or errors to see if any preprocessing is required, decide on how to split the data set for training and prediction etc., Here are some of the commands useful in previewing raw data. Try out the commands and observe what information is displayed.

`print(dataset.shape)`

`print(dataset.dtypes)`

`print(dataset.head(15))`

#### Descriptive Statistics

> Descriptive statistics is a crucial step that helps you understand what the data is trying to tell you. Without descriptive statistics, you may miss valuable information that may eventually lead the model to provide incorrect conclusions. Try out the following command and observe the statistics displayed.

`print(dataset.describe())`

#### Correlation

> In the model.py code, we have used linear regression to determine the linear relationship between the dependent and independent variable. But how did we know that there was any association between the variables in the data set before deciding on a dependent or independent variable. It is always recommended to use correlation to observe if there exists any association and if it exists, then progress to determining the linear relationship. Try out the following command to see the correlation matrix that shows the magnitude and direction of association between the variables.

`print(dataset.corr(method='pearson'))`

#### Model accuracy

> Now that we have a model fitted to the data and performed prediction on the test data, it is important to evaluate the quality of this prediction. There are several metrics available to evaluate the accuracy of a predictive model. Try out the following command to view one such metric that shows the average error between the predicted and observed value.

`from sklearn import metrics`

`print(metrics.mean_absolute_error(yPrediction, yTest))`


## Create a PR

* create a PR to the original Repo
* ask for a review by a peer


## 🤖 Bots

Project [Thoth](https://github.com/thoth-station/) provides bots which simplify
workflow for developers. This repository has already set up a bot which
automatically performs tests on the source code each time a new pull request is
opened. If you are interested in bot's configuration, take a look at
[.zuul.yaml](https://github.com/AICoE/workshop-coding-best-practices/pull/4/files)
configuration file which states two types of jobs performing checks -
[Coala](https://coala.io/#/home) and [PyTest](https://docs.pytest.org/en/latest/).

[PyTest](https://docs.pytest.org/en/latest/) is a framework for building
unit-tests for your applications (Python has its own
[unittest](https://docs.python.org/3/library/unittest.html) which is often
sufficient enough but PyTest provides flexibility, extensibility and better user
experience).

---

#### 🤓 Task 0: Prepare your development environment

Before we run tests, let's clone this repository and prepare our virtual
environment if you haven't done so run the following command (note
the ``--dev`` flag which will install development dependencies):

```bash
pipenv install --dev
```

All tests are available under `tests/` directory - to run the test suite, you
can issue the following command:

```bash
PYTHONPATH=. pipenv run python3 setup.py test
```

The ``PYTHONPATH`` directive tells the Python interpreter to consider importing
from local directory to make our codebase importable in tests. Tests are
executed in the virtual environment to guarantee presence of required
development libraries (hence ``pipenv run ...``).

If the command above looks too long for you, you can run a prepared script
``test.sh`` which will in fact run the command above:

```bash
./test.sh
```
[GitHub link](https://github.com/AICoE/workshop-coding-best-practices/blob/master/test.sh)

---

#### 🤔 Task 1: Let's fix tests!

After running commands above, your can see produced output stating each test
and its success or failure with detailed description on what went wrong. Your
real first task would be to fix test suite in a way it runs correctly (all the
tests pass). As a starting point take a look into ``tests/test_generic.py``
file which will help you understand how the testing framework works:

```bash
vim tests/test_generic.py
```
[GitHub link](https://github.com/AICoE/workshop-coding-best-practices/blob/master/tests/test_generic.py)

Now, take a look at failing tests which verify if implementation of Fibonacci
function returns correct results (hint: the actual implementation of ``fib()``
function is implemented correctly, errors are in the test suite).

```bash
vim tests/test_module.py
```
[GitHub link](https://github.com/AICoE/workshop-coding-best-practices/blob/master/tests/test_module.py)

The implementation of ``fib()`` function can be found at:

```bash
vim myproject/module.py
```
[GitHub link](https://github.com/AICoE/workshop-coding-best-practices/blob/master/myproject/module.py)

---

#### 😎 Task 3: Open a pull request fixing issues in the test suite and interact with the bot.

Once you fix issues in the test suite, you can open a pull request. See how
bots comment to your pull-requests and capture the output of test suite. This
helps others verify your changes are correct, and also test changes in
a reproducible environment against the current master branch.

Make sure ``thoth-pytest`` is in successful state. You can check results of a run
by clicking on "thoth-pytest", follow link "ara-report", click on "5 Tasks" in
```pytest.yaml``` row and click on link in "Status column", raw "``thoth-pytest
: run pytest``" (either successful or failed state).

#### 📝 Some notes...

* note that each file has it's header stating author and license - this helps you to know who is the module author so you can reach out to her/him directly in case of any issues

* each file has a brief docstring describing what the module is used for - it helps others and your future self to immediately understand what's the purpose of the module

* tests follow package/module structure - it helps others and your future self to quickly navigate in the project structure and relate sources

* names of tests are based on function (the same would apply for method names) and stating what functionality they test so the output of the test suite is human readable

* at the end of each test run you can see code coverage - how well is your code covered with tests (it does not measure the quality of test suite though!!!)

---

#### 🧚 Automatic management of package updates

Thoth provides a bot called
[Kebechet](https://github.com/thoth-station/kebechet/). It can manage your
dependencies. If you work on a Python project which can benefit from package
updates, feel free to use it (contact one of the thoth-station inhabitants
present in ``AICoE - Thoth Station`` channel on Google Chat).

Relevant info can be also found at [Thoth's
page](http://thoth-station.ninja/kebechet/).

---

#### 🐨 Coala - check your sources

Coala is a tool which can automatically check quality of sources - besides
Python sources, it can also check other source types - for example YAML files.
It comes with plugins called "Bears" which can be configured with paraneters. See
[.coafile](https://github.com/AICoE/workshop-coding-best-practices/blob/master/.coafile)
for configuration used in this repository and [Coala's homepage for more
info](https://coala.io/).

---

#### 💾 Code formatting hints...

To automatically format your code, you can use popular tool called
[black](https://pypi.org/project/black/).

You can install it using:

```bash
pip3 install black
```

Now you just run it and it will automatically format source code for you (note:
some formatting changes might not be compatible with
[PEP8](https://www.python.org/dev/peps/pep-0008/) and Coala might complain).:

```bash
black .  # Directory or path to a file to be formatted (dot for the current directory).
```

## Profiling Code

zak will add stuff


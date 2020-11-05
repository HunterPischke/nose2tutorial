# nose2tutorial

### Background:
Nose2 is a python library used for testing. Like it’s predecessor Nose, Nose2 is at it’s core just unittest with plugins. Nose2’s purpose is to extend unittest to make testing nicer and easier to understand.

### When to Use:
The major competitor to nose2 is pytest. A major advantage of nose 2 is that it allows tests to be regular functions. We don't need to create a class and inherit it from any base class. As long as the function starts with the word test, it is considered a test and executed. On top of this, nose2 comes with many plugins by default and even allows users to download third-party plugins.

### Installation:
To get started with nose2 like many other libraries it is best to use the package manager pip and run the command:

```
pip install nose2
```

### Running Tests:
To run tests make use of the nose2 command inside any directory. It will seek out all subdirectories with unit tests or test files that have lowercase “test” at the front of the name. The command to do this is:

```
nose2
```


### Further Documentation:
Please view the nose2 Tutorial.pdf file in this repository.
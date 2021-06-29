# Test-Driven Development

## What is test driven development?

Test Driven Development is a process in which you write the test before you write the code. And when all tests are passing you clean your kitchen: you make the code better.

Test Driven Development (TDD) is software development approach in which test cases are developed to specify and validate what the code will do. In simple terms, test cases for each functionality are created and tested first and if the test fails then the new code is written in order to pass the test and making code simple and bug-free.

Test-Driven development is a process of developing and running automated test before actual development of the application. Hence, TDD sometimes also called as Test First Development.

## How to perform TDD test

Following steps define how to perform TDD test,

1. Add a test.
2. Run all tests and see if any new test fails.
3. Write some code.
4. Run tests and Refactor code.
5. Repeat.

   <img src='tdd.png'>

## TDD cycle defines:

1. Write a test
2. Make it run.
3. Change the code to make it right i.e. Refactor.
4. Repeat process.

##  Scaling TDD via Agile Model Driven Development (AMDD)

TDD is very good at detailed specification and validation. It fails at thinking through bigger issues such as overall design, use of the system, or UI. AMDD addresses the Agile scaling issues that TDD does not.

Thus AMDD used for bigger issues.


### Lifecycle of AMDD


<img src = 'amdd.png'>

In above figure, each box represents a development activity.

Envisioning is one of the TDD process of predicting/imagining tests which will be performed during the first week of the project. The main goal of envisioning is to identify the scope of the system and architecture of the system. High-level requirements and architecture modeling is done for successful envisioning.

It is the process where not a detailed specification of software/system is done but exploring the requirements of software/system which defines the overall strategy of the project.


## Iteration 0: Envisioning
There are two main sub-activates.

1. Initial requirements envisioning.
It may take several days to identify high-level requirements and scope of the system. The main focus is to explore usage model, Initial domain model, and user interface model (UI).

2. Initial Architectural envisioning.
It also takes several days to identify architecture of the system. It allows setting technical directions for the project. The main focus is to explore technology diagrams, User Interface (UI) flow, domain models, and Change cases.

## Iteration modeling
Here team must plan the work that will be done for each iteration.

-  Agile process is used for each iteration, i.e. during each iteration, new work item will be added with priority.
- First higher prioritized work will be taken into consideration. Work items added may be reprioritized or removed from items stack any time.
- The team discusses how they are going to implement each requirement. Modeling is used for this purpose.
- Modeling analysis and design is done for each requirement which is going to implement for that iteration.
## Model storming
This is also known as Just in time Modeling.

- Here modeling session involves a team of 2/3 members who discuss issues on paper or whiteboard.
- One team member will ask another to model with them. This modeling session will take approximately 5 to 10 minutes. Where team members gather together to share whiteboard/paper.
- They explore issues until they don't find the main cause of the problem. Just in time, if one team member identifies the issue which he/she wants to resolve then he/she will take quick help of other team members.
- Other group members then explore the issue and then everyone continues on as before. It is also called as stand-up modeling or customer QA sessions.
## Test Driven Development (TDD)
- It promotes confirmatory testing of your application code and detailed specification.
- Both acceptance test (detailed requirements) and developer tests (unit test) are inputs for TDD.
- TDD makes the code simpler and clear. It allows the developer to maintain less documentation.
## Reviews
- This is optional. It includes code inspections and model reviews.
- This can be done for each iteration or for the whole project.
- This is a good option to give feedback for the project.

# UNit testing

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

## Basic Example

The unittest module provides a rich set of tools for constructing and running tests. This section demonstrates that a small subset of the tools suffice to meet the needs of most users.

```
import unittest
import duplicates

class TestDuplicates(unittest.TestCase):
    def test_rm_duplicate(self):
        fruits = ['oranges','kiwi','apple','kiwi']
        result = duplicates.rm_duplicate(fruits)
        self.assertEqual(result,['oranges','kiwi','apple'])


if __name__ == '__main__':
    unittest.main() 

    ```


A testcase is created by subclassing ```unittest.TestCase```. The test is defined with  a method whose name start with the letter ```test```. This naming convention informs the test runner about which methods represent tests.  
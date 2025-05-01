# Week 2: Coins

This is a repository for a weekly coding exercise. Each weekly coding exercise involves updating back-end code for a simple Streamlit web app. For the most part, the "exercise" will be updates to the *apputil.py* file.

*Note: these exercises are intended to be used with GitHub Codespaces and Gradescope autograder.*

## setup

*(As of April 2025)*

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your forked repository (this may take a few minutes to load at first). Use the codespace to make changes to the code, and to test the web app.
3. Test your code by submitting your forked repository [to the Gradescope autograder](https://guides.gradescope.com/hc/en-us/articles/21865616724749-Submitting-a-Code-assignment) on Canvas.

**Only update the file(s) noted in the exercise instructions below.** Updating any other files may affect your web app or your feedback.

## instructions

Given enough pennies (1 cent) and nickels (5 cents), write a function which calculates the number of ways you can make change for a given amount of cents. Do this in two ways:

1. Write the function `ways(n)` which does this without using NumPy.
2. Write *another* function `ways_np(n)` which does the same thing, but uses NumPy.

In the *apputil* file, add `ways(n)` and `ways_np(n)` accordingly to return the number of ways to yield `n` cents using only pennies and nickels.

**Packages Available:**

The environment for this exercise is built with the following environment.yml:

```yml
name: coding-exercise
dependencies:
  - python=3.11
  - pip
  - pip:
    - streamlit
    - pandas
    - numpy
```

*Note: you cannot update this environment. This is only shared as reference for you.*
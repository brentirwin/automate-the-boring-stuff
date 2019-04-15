## Chapter 3 - Practice Questions

1. **Why are functions advantageous to have in your programs?**  
	To group code that gets executed multiple times.
2. **When does the code in a function execute: when the function is defined or when the function is called?**  
	When the function is called.
3. **What statement dreates a function?**  
	def
4. **What is the difference between a function and a function call?**  
	A function call is an instance of a function being used.
5. **How many global scopes are there in a Python program? How many local scopes?**  
	There is only one global scope. A local scope is created whenever a function is called.
6. **What happens to variables in a local scope when the function call returns?**  
	The scope is destroyed, and these variables are forgotten.
7. **What is a return value? Can a return value be part of an expression?**  
	A return value is the value that a function call evaluates to, preceded by the word `return` in a return statement.
8. **If a function does not have a return statement, what is the return value of a call to that function?**  
	`None`
9. **How can you force a variable in a function to refer to the global variable?**  
	Use the `global` statement.
10. **What is the data type of `None`?**  
	`NoneType`
11. **What does the `import areallyourpetsnamederic` statement do?**  
	It imports the module called `areallyourpetsnamederic`.
12. **If you had a function named `bacon()` in a module called spam, how would you call it after importing `spam`?**  
	`spam.bacon()`
13. **How can you prevent a program from crashing when it gets an error?**  
	Use a `try`/`except` statement.
14. **What goes in the `try` clause? What goes in the `except` clause?**  
	The code that could potentially have an error is put in the `try` clause. Code that handles what happens when this error occurs is put into the `except` clause.


Readme Instructions to run the tests:

Prerequisites:
1. install Python > =3
2. install pip
3. from commandline
    pip install pytest
    or
    pip install -r requirements.txt

Run Tests:
1.	in commandline > change directory to …./tradeIX folder
2.	verify you are on …./traeIX folder
3.	type `py.test -s` and Enter
4.	this should run 3 tests 
    	Expected: all 3 tests to pass

Considerations: 
1.	Test data used: 
   Created New pet with
   Id: 52
   categoryName:  'categoryname_52'
   petName: 'petname_52'
   status: 'Available'
   tagName: 'Accelerate'
   photoUrl: 'www.google.com'
           Updated New pet with
   Id: 52
   categoryName:  'categoryname_52'
   petName: 'doggie'
   status: 'Available'
   tagName: 'Accelerate'
   photoUrl: 'www.google.com'
          deleted record:
                Id: 52
2.	I have used static data in the test cases, due to time frame set to submit within 24 hours, there can be more improvements to be more dynamic to pass parameters in run time
3.	Verifying data with assertions for correct data, update data, and delete record and verify its deleted



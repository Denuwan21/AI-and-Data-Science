few_shorts = [
    {
        "Question":"List all employees' first and last names.",
        "SQLQuery":"SELECT first_name, last_name FROM employees;",
        "SQLResult":"""first_name, last_name
        
                       Jhon        Smith
                       Sarah       Johnson
                       Michael     Williams 
                       Emily       Brown
                       David       Jones
                       Jennifer    Garcia
                       Robert      Miller
                       Lisa        Davis
                       Thomas      Rodriguez
                       Patricia    Martinez

                    """,
        "Answer": """first_name, last_name
        
                       Jhon        Smith
                       Sarah       Johnson
                       Michael     Williams 
                       Emily       Brown
                       David       Jones
                       Jennifer    Garcia
                       Robert      Miller
                       Lisa        Davis
                       Thomas      Rodriguez
                       Patricia    Martinez

                """
    },
    
    {
        "Question":"Show all employees hired after 2015",
        "SQLQuery":"SELECT first_name, last_name, hire_date FROM employees WHERE hire_date > '2015-01-01';",
        "SQLResult":"""first_name  last_name  hire_date
        
                       Jennifer    Garcia     2015-02-18
                       Robert      Miller     2016-04-30
                       Lisa        Davis      2017-08-12
                       Thomas      Rodriguez  2018-01-25
                       Patricia    Martinez   2019-05-08
                       

                    """,
        "Answer": """first_name  last_name    hire_date
        
                       Jennifer    Garcia     2015-02-18
                       Robert      Miller     2016-04-30
                       Lisa        Davis      2017-08-12
                       Thomas      Rodriguez  2018-01-25
                       Patricia    Martinez   2019-05-08
                       

                    """
    },
    
    
    {
        "Question":"Display the first 3 employees in the database",
        "SQLQuery":"SELECT * FROM employees LIMIT 3;",
        "SQLResult":""" employee_id  first_name  last_name          email                     phone_number      hire_date       job_id     salary       manager_id      department_id
                            
                            1           John        Smith      john.smith@company.com          555-1001         2010-06-01        1        25000.00      NULL               1
                            2           Sarah       Johnson    sarah.johnson@company.com       555-1002         2011-07-15        2        18000.00       1                 1
                            3           Michael     Williams   michael.williams@company.com    555-1003         2012-03-10        3        8000.00        2                 2

                       

                    """,
        "Answer": """ employee_id  first_name  last_name          email                     phone_number      hire_date       job_id     salary       manager_id      department_id
                            
                            1           John        Smith      john.smith@company.com          555-1001         2010-06-01        1        25000.00      NULL               1
                            2           Sarah       Johnson    sarah.johnson@company.com       555-1002         2011-07-15        2        18000.00       1                 1
                            3           Michael     Williams   michael.williams@company.com    555-1003         2012-03-10        3        8000.00        2                 2

                       

                    """
    },
    
    
    {
        "Question":"How many employees are there?",
        "SQLQuery":"SELECT COUNT(*) FROM employees;",
        "SQLResult":"[(10,)]",
        "Answer": "10"
    },
    
    
    {
        "Question":"What is the total salary of all employees?",
        "SQLQuery":"SELECT SUM(salary) FROM employees;",
        "SQLResult":"[(94500.00,)]",
        "Answer": "94500.00"
    },
    
    
    {
        "Question":"What is the average salary",
        "SQLQuery":"SELECT AVG(salary) FROM employees;",
        "SQLResult":"[(9450.000000,)]",
        "Answer": "9450.000000"
    },
    
    
    {
        "Question":"Show the number of employees in each department.",
        "SQLQuery":"SELECT department_id, COUNT(*) FROM employees GROUP BY department_id;",
        "SQLResult":"""department_id      COUNT(*)
                             
                             1               2
                             2               3
                             3               1
                             4               4
                    """,
        "Answer": """department_id      COUNT(*)
                             
                             1               2
                             2               3
                             3               1
                             4               4
                    """
    },
    
    
    
    {
        "Question":"List departments with more than 2 employees",
        "SQLQuery":"SELECT department_id, COUNT(*) AS emp_count FROM employees GROUP BY department_id HAVING emp_count > 2;",
        "SQLResult":"""department_id      emp_count
                             
                             2               3
                             4               4
                    """,
        "Answer": """department_id      emp_count
                             
                             2               3
                             4               4
                    """
    },
    
    
    
    {
        "Question":"List employees ordered by salary ascending",
        "SQLQuery":"SELECT first_name, last_name, salary FROM employees ORDER BY salary ASC;",
        "SQLResult":"""first_name      last_name      salary
                        
                        Patricia        Martinez      3500.00 
                        Thomas          Rodriguez     4000.00
                        Lisa            Davis         4500.00
                        David           Jones         5000.00
                        Robert          Miller        7000.00
                        Jennifer        Garcia        7500.00
                        Michael         Williams      8000.00
                        Emily           Brown         12000.00
                        Sarah           Johnson       18000.00
                        John            Smith         25000.00             
                    """,
        "Answer": """first_name      last_name      salary
                        
                        Patricia        Martinez      3500.00 
                        Thomas          Rodriguez     4000.00
                        Lisa            Davis         4500.00
                        David           Jones         5000.00
                        Robert          Miller        7000.00
                        Jennifer        Garcia        7500.00
                        Michael         Williams      8000.00
                        Emily           Brown         12000.00
                        Sarah           Johnson       18000.00
                        John            Smith         25000.00             
                    """
    },
    
    
    
    
    {
        "Question":"List top 5 highest-paid employees.",
        "SQLQuery":"SELECT first_name, last_name, salary FROM employees ORDER BY salary DESC LIMIT 5;",
        "SQLResult":"""first_name      last_name      salary
                             
                         John           Smith         25000.00
                         Sarah          Johnson       18000.00
                         Emily          Brown         12000.00
                         Michael        Williams      8000.00
                         Jennifer       Garcia        7500.00
                              
                    """,
        "Answer": """first_name      last_name      salary
                             
                         John           Smith         25000.00
                         Sarah          Johnson       18000.00
                         Emily          Brown         12000.00
                         Michael        Williams      8000.00
                         Jennifer       Garcia        7500.00
                              
                    """
    },
    
    
    
    
    {
        "Question":"List employees with their department names.",
        "SQLQuery":"SELECT e.first_name, e.last_name, d.department_name FROM employees e JOIN departments d ON e.department_id = d.department_id;",
        "SQLResult":"""first_name    last_name    department_name
                             
                         John         Smith        Executive
                         Sarah        Johnson      Executive
                         Michael      Williams     IT
                         Jennifer     Garcia       IT
                         Robert       Miller       IT
                         Emily        Brown        Marketing
                         David        Jones        Sales
                         Lisa         Davis        Sales
                         Thomas       Rodriguez    Sales
                         Patricia     Martinez     Sales
                              
                    """,
        "Answer": """first_name    last_name    department_name
                             
                         John         Smith        Executive
                         Sarah        Johnson      Executive
                         Michael      Williams     IT
                         Jennifer     Garcia       IT
                         Robert       Miller       IT
                         Emily        Brown        Marketing
                         David        Jones        Sales
                         Lisa         Davis        Sales
                         Thomas       Rodriguez    Sales
                         Patricia     Martinez     Sales
                              
                    """
    },
    
    
    
     {
        "Question":"List employees with their job titles",
        "SQLQuery":"SELECT e.first_name, e.last_name, j.job_title FROM employees e JOIN jobs j ON e.job_id = j.job_id;",
        "SQLResult":"""first_name  last_name  job_title
                                     
                         John       Smith      President
                         Sarah      Johnson    Administration Vice President
                         Michael    Williams   Programmer
                         Jennifer   Garcia     Programmer
                         Robert     Miller     Programmer
                         Emily      Brown      Marketing Manager
                         David      Jones      Sales Representative
                         Lisa       Davis      Sales Representative
                         Thomas     Rodriguez  Sales Representative
                         Patricia   Martinez   Sales Representative
                              
                    """,
        "Answer": """first_name  last_name  job_title
                                     
                         John       Smith      President
                         Sarah      Johnson    Administration Vice President
                         Michael    Williams   Programmer
                         Jennifer   Garcia     Programmer
                         Robert     Miller     Programmer
                         Emily      Brown      Marketing Manager
                         David      Jones      Sales Representative
                         Lisa       Davis      Sales Representative
                         Thomas     Rodriguez  Sales Representative
                         Patricia   Martinez   Sales Representative
                              
                    """
    },
    
    
    
    {
        "Question":"Show employee names, department names, and city",
        "SQLQuery":"SELECT e.first_name, e.last_name, d.department_name, l.city FROM employees e JOIN departments d ON e.department_id = d.department_id JOIN locations l ON d.location_id = l.location_id;",
        "SQLResult":"""first_name       last_name      department_name        city
        
                         John             Smith           Executive          New York
                         Sarah            Johnson         Executive          New York
                         Michael          Williams        IT                 Berlin
                         Jennifer         Garcia          IT                 Berlin
                         Robert           Miller          IT                 Berlin
                         Emily            Brown           Marketing          Tokyo
                         David            Jones           Sales              Lagos
                         Lisa             Davis           Sales              Lagos
                         Thomas           Rodriguez       Sales              Lagos
                         Patricia         Martinez        Sales              Lagos
                              
                    """,
        "Answer": """first_name       last_name      department_name        city
        
                         John             Smith           Executive          New York
                         Sarah            Johnson         Executive          New York
                         Michael          Williams        IT                 Berlin
                         Jennifer         Garcia          IT                 Berlin
                         Robert           Miller          IT                 Berlin
                         Emily            Brown           Marketing          Tokyo
                         David            Jones           Sales              Lagos
                         Lisa             Davis           Sales              Lagos
                         Thomas           Rodriguez       Sales              Lagos
                         Patricia         Martinez        Sales              Lagos
                              
                    """
    },
    
    
    {
        "Question":"Find employees in the 'IT' department.",
        "SQLQuery":"SELECT e.first_name, e.last_name FROM employees e JOIN departments d ON e.department_id = d.department_id WHERE d.department_name = 'IT';",
        "SQLResult":"""first_name       last_name   
        
                        Michael         Williams
                        Jennifer        Garcia
                        Robert          Miller
                              
                    """,
        "Answer": """first_name       last_name   
        
                        Michael         Williams
                        Jennifer        Garcia
                        Robert          Miller
                              
                    """
    },
    
    
    
    {
        "Question":"Show employee and region name.",
        "SQLQuery":"SELECT e.first_name, e.last_name, r.region_name FROM employees e JOIN departments d ON e.department_id = d.department_id JOIN locations l ON d.location_id = l.location_id JOIN countries c ON l.country_id = c.country_id JOIN regions r ON c.region_id = r.region_id;",
        "SQLResult":"""first_name      last_name      region_name   
        
                        Michael        Williams          Europe
                        Jennifer       Garcia            Europe
                        Robert         Miller            Europe
                        John           Smith             Americas
                        Sarah          Johnson           Americas
                        Emily          Brown             Asia
                        David          Jones             Middle East and Africa
                        Lisa           Davis             Middle East and Africa
                        Thomas         Rodriguez         Middle East and Africa
                        Patricia       Martinez          Middle East and Africa
                              
                    """,
        "Answer": """first_name      last_name      region_name   
        
                        Michael        Williams          Europe
                        Jennifer       Garcia            Europe
                        Robert         Miller            Europe
                        John           Smith             Americas
                        Sarah          Johnson           Americas
                        Emily          Brown             Asia
                        David          Jones             Middle East and Africa
                        Lisa           Davis             Middle East and Africa
                        Thomas         Rodriguez         Middle East and Africa
                        Patricia       Martinez          Middle East and Africa
                              
                    """
    },
    
    
    
    {
        "Question":"Employees earning above average salary.",
        "SQLQuery":"SELECT first_name, last_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);",
        "SQLResult":"""first_name      last_name      salary   
        
                        John            Smith         25000.00
                        Sarah           Johnson       18000.00
                        Emily           Brown         12000.00
                              
                    """,
        "Answer": """first_name      last_name      salary   
        
                        John            Smith         25000.00
                        Sarah           Johnson       18000.00
                        Emily           Brown         12000.00
                              
                    """
    },
    
    
    {
        "Question":"Employees in departments located in Japan",
        "SQLQuery":"SELECT e.first_name, e.last_name FROM employees e WHERE e.department_id IN (SELECT d.department_id FROM departments d JOIN locations l ON d.location_id = l.location_id WHERE l.country_id = 'JP');",
        "SQLResult":"""first_name      last_name        

                        Emily           Brown   
                              
                    """,
        "Answer": """first_name      last_name        

                        Emily           Brown   
                              
                    """
    },
    
    
    
    {
        "Question":"Employees without dependents.",
        "SQLQuery":"SELECT first_name, last_name FROM employees WHERE employee_id NOT IN (SELECT employee_id FROM dependents);",
        "SQLResult":"""first_name      last_name        

                        Patricia        Martinez   
                              
                    """,
        "Answer": """first_name      last_name        

                      Patricia        Martinez   
                              
                    """
    },
    
    
    {
        "Question":"Employees managed by 'Sarah Johnson'",
        "SQLQuery":"SELECT COUNT(*) FROM employees WHERE manager_id = (SELECT employee_id FROM employees WHERE first_name = 'Sarah' AND last_name = 'Johnson');",
        "SQLResult":"[(2,)]",
        "Answer": "2"
    },
    
    
    
    
    {
        "Question":"List dependents with their parent employees.",
        "SQLQuery":"SELECT d.first_name AS dep_first, d.last_name AS dep_last, e.first_name AS emp_first, e.last_name AS emp_last FROM dependents d JOIN employees e ON d.employee_id = e.employee_id;",
        "SQLResult":"""dep_first     dep_last     emp_first     emp_last        

                        Anna           Smith        John          Smith
                        Benjamin       Jones        David         Jones
                        Charlotte      Davis        Lisa          Davis
                        Henry          Rodriguez    Thomas        Rodriguez
                        James          Smith        John          Smith
                        Lucas          Miller       Robert        Miller
                        Mia            Garcia       Jennifer      Garcia
                        Olivia         Johnson      Sarah         Johnson
                        Sophia         Brown        Emily         Brown
                        William        Williams     Michael       Williams   
                              
                    """,
        "Answer": """dep_first     dep_last     emp_first     emp_last        

                        Anna           Smith        John          Smith
                        Benjamin       Jones        David         Jones
                        Charlotte      Davis        Lisa          Davis
                        Henry          Rodriguez    Thomas        Rodriguez
                        James          Smith        John          Smith
                        Lucas          Miller       Robert        Miller
                        Mia            Garcia       Jennifer      Garcia
                        Olivia         Johnson      Sarah         Johnson
                        Sophia         Brown        Emily         Brown
                        William        Williams     Michael       Williams   
                              
                    """,
    },
    
    
    
    
    {
        "Question":"List Employees and their managers.",
        "SQLQuery":"SELECT e.first_name AS employee, m.first_name AS manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.employee_id;",
        "SQLResult":"""employee       manager        
                       
                        David          Emily
                        Emily          Sarah
                        Jennifer       Michael
                        John 
                        Lisa           David
                        Michael        Sarah
                        Patricia       David
                        Robert         Michael
                        Sarah          John
                        Thomas         David
    
                              
                    """,
        "Answer": """employee       manager        
                      
                        David          Emily
                        Emily          Sarah
                        Jennifer       Michael
                        John 
                        Lisa           David
                        Michael        Sarah
                        Patricia       David
                        Robert         Michael
                        Sarah          John
                        Thomas         David
    
                              
                    """
    },
    
    
    
    {
        "Question":"Show number of dependents per employee",
        "SQLQuery":"SELECT e.first_name, COUNT(d.dependent_id) FROM employees e LEFT JOIN dependents d ON e.employee_id = d.employee_id GROUP BY e.employee_id;",
        "SQLResult":"""first_name   COUNT(d.dependent_id)        
                       
                        John                  2
                        Sarah                 1
                        Michael               1
                        Emily                 1
                        David                 1
                        Jennifer              1
                        Robert                1
                        Lisa                  1
                        Thomas                1
                        Patricia              0
    
                              
                    """,
        "Answer": """first_name   COUNT(d.dependent_id)        
                       
                        John                  2
                        Sarah                 1
                        Michael               1
                        Emily                 1
                        David                 1
                        Jennifer              1
                        Robert                1
                        Lisa                  1
                        Thomas                1
                        Patricia              0
    
                              
                    """,
    },
    
    
    {
        "Question":"Employees with email ending in '@company.com'",
        "SQLQuery":"SELECT first_name, last_name, email FROM employees WHERE email LIKE '%@company.com';",
        "SQLResult":"""first_name      last_name,       email        
                       
                        John            Smith           john.smith@company.com
                        Sarah           Johnson         sarah.johnson@company.com
                        Michael         Williams        michael.williams@company.com
                        Emily           Brown           emily.brown@company.com
                        David           Jones           david.jones@company.com
                        Jennifer        Garcia          jennifer.garcia@company.com
                        Robert          Miller          robert.miller@company.com
                        Lisa            Davis           lisa.davis@company.com
                        Thomas          Rodriguez       thomas.rodriguez@company.com
                        Patricia        Martinez        patricia.martinez@company.com
    
                              
                    """,
        "Answer": """first_name      last_name,       email        
                       
                        John            Smith           john.smith@company.com
                        Sarah           Johnson         sarah.johnson@company.com
                        Michael         Williams        michael.williams@company.com
                        Emily           Brown           emily.brown@company.com
                        David           Jones           david.jones@company.com
                        Jennifer        Garcia          jennifer.garcia@company.com
                        Robert          Miller          robert.miller@company.com
                        Lisa            Davis           lisa.davis@company.com
                        Thomas          Rodriguez       thomas.rodriguez@company.com
                        Patricia        Martinez        patricia.martinez@company.com
    
                              
                    """,
    },
    
    
    
    {
        "Question":"Employees with salary between 7000 and 10000.",
        "SQLQuery":"SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 7000 AND 10000;",
        "SQLResult":"""first_name,      last_name,      salary        
                       
                        Michael         Williams        8000.00
                        Jennifer        Garcia          7500.00
                        Robert          Miller          7000.00
    
                              
                    """,
        "Answer": """first_name,      last_name,      salary        
                       
                        Michael         Williams        8000.00
                        Jennifer        Garcia          7500.00
                        Robert          Miller          7000.00
        
                    """
    },
    
    
    
    
    {
        "Question":"Which cities have departments?",
        "SQLQuery":"SELECT DISTINCT l.city FROM departments d JOIN locations l ON d.location_id = l.location_id;",
        "SQLResult":"""city 
        
                        Berlin
                        Lagos
                        New York
                        São Paulo
                        Tokyo
    
                              
                    """,
        "Answer": """city 
        
                        Berlin
                        Lagos
                        New York
                        São Paulo
                        Tokyo
    
                              
                    """
    },
    
    
    
    {
        "Question":"All departments and how many employees in each.",
        "SQLQuery":"SELECT d.department_name, COUNT(e.employee_id) FROM departments d LEFT JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_name;",
        "SQLResult":"""department_name     COUNT(e.employee_id) 
        
                          Executive                 2
                          HR                        0 
                          IT                        3
                          Marketing                 1
                          Sales                     4
    
                              
                    """,
        "Answer": """department_name,    COUNT(e.employee_id) 
        
                          Executive                 2
                          HR                        0 
                          IT                        3
                          Marketing                 1
                          Sales                     4
    
                              
                    """
    },
    
    
    
    {
        "Question":"Departments with their location and city",
        "SQLQuery":"SELECT d.department_name, l.city FROM departments d JOIN locations l ON d.location_id = l.location_id;",
        "SQLResult":"""department_name          city
        
                          Executive            New York
                          HR                   São Paulo
                          IT                   Berlin
                          Marketing            Tokyo
                          Sales                Lagos
    
                              
                    """,
        "Answer": """department_name          city
        
                          Executive            New York
                          HR                   São Paulo
                          IT                   Berlin
                          Marketing            Tokyo
                          Sales                Lagos
    
                              
                    """
    },
    
    
    {
        "Question":"Number of departments per country",
        "SQLQuery":"SELECT c.country_name, COUNT(d.department_id) FROM departments d JOIN locations l ON d.location_id = l.location_id JOIN countries c ON l.country_id = c.country_id GROUP BY c.country_name;",
        "SQLResult":"""country_name     COUNT(d.department_id)
        
                            Brazil            1
                            Germany           1
                            Japan             1
                            Nigeria           1
                            United States     1
    
                              
                    """,
        "Answer": """country_name     COUNT(d.department_id)
        
                            Brazil            1
                            Germany           1
                            Japan             1
                            Nigeria           1
                            United States     1
    
                              
                    """,
    },
    
    
    
    
    {
        "Question":"Employees working in Germany.",
        "SQLQuery":"SELECT e.first_name, e.last_name FROM employees e JOIN departments d ON e.department_id = d.department_id JOIN locations l ON d.location_id = l.location_id WHERE l.country_id = 'DE';",
        "SQLResult":"""first_name,        last_name
        
                            Jennifer       arcia
                            Michael        Williams
                            Robert         Miller
    
                              
                    """,
        "Answer": """first_name,        last_name
        
                            Jennifer       arcia
                            Michael        Williams
                            Robert         Miller
    
                              
                    """,
    },
    
    
    
    {
        "Question":"Job titles with min and max salary",
        "SQLQuery":"SELECT job_title, min_salary, max_salary FROM jobs;",
        "SQLResult":"""job_title,                    min_salary,                     max_salary
        
                       Sales Representative            3000.00                        8000.00
                       Programmer                      4000.00                        10000.00
                       President                       20000.00                       40000.00
                       Marketing Manager               9000.00                        15000.00
                       Administration Vice President   15000.00                       30000.00
    
                              
                    """,
        "Answer": """job_title,                    min_salary,                     max_salary
        
                       Sales Representative            3000.00                        8000.00
                       Programmer                      4000.00                        10000.00
                       President                       20000.00                       40000.00
                       Marketing Manager               9000.00                        15000.00
                       Administration Vice President   15000.00                       30000.00
    
                              
                    """,
    },
    
    
    {
        "Question":"Employee with highest salary",
        "SQLQuery":"SELECT job_title, min_salary, max_salary FROM jobs;",
        "SQLResult":"""first_name          last_name           salary
        
                       John                Smith               25000.00
                         
                    """,
        "Answer": """first_name          last_name           salary
        
                       John                Smith               25000.00
                         
                    """
    },
    
    
    {
        "Question":"Show average salary by department",
        "SQLQuery":"SELECT d.department_name, AVG(e.salary) FROM departments d JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_name;",
        "SQLResult":"""department_name          AVG(e.salary)
        
                       Executive                21500.000000
                       IT                       7500.000000
                       Marketing                12000.000000
                       Sales                    4250.000000
                         
                    """,
        "Answer": """department_name          AVG(e.salary)
        
                       Executive                21500.000000
                       IT                       7500.000000
                       Marketing                12000.000000
                       Sales                    4250.000000
                         
                    """
    },
    
    
    {
        "Question":"Job titles with avg salary > 9000.",
        "SQLQuery":"SELECT j.job_title, AVG(e.salary) AS avg_salary FROM employees e JOIN jobs j ON e.job_id = j.job_id GROUP BY j.job_title HAVING avg_salary > 9000;",
        "SQLResult":"""job_title                        avg_salary
        
                       Administration Vice President    18000.000000
                       Marketing Manager                12000.000000
                       President                        25000.000000
                         
                    """,
        "Answer": """job_title                        avg_salary
        
                       Administration Vice President    18000.000000
                       Marketing Manager                12000.000000
                       President                        25000.000000
                         
                    """
    },
    
    
    
    {
        "Question":"List of Employees hired before 2014",
        "SQLQuery":"SELECT * FROM employees WHERE hire_date < '2014-01-01';",
        "SQLResult":"""employee_id     first_name      last_name      email                            phone_number     hire_date    job_id    salary         manager_id, department_id
                       
                        1              John            Smith          john.smith@company.com           555-1001         2010-06-01    1        25000.00                      1
                        2              Sarah           Johnson        sarah.johnson@company.com        555-1002         2011-07-15    2        18000.00            1         1
                        3              Michael         Williams       michael.williams@company.com     555-1003         2012-03-10    3        8000.00             2         2
                        4              Emily           Brown          emily.brown@company.com          555-1004         2013-09-22    4        12000.00            2         3
                      
                    """,
        "Answer": """employee_id     first_name      last_name      email                            phone_number     hire_date    job_id    salary         manager_id, department_id
                        
                        1              John            Smith          john.smith@company.com           555-1001         2010-06-01    1        25000.00                      1
                        2              Sarah           Johnson        sarah.johnson@company.com        555-1002         2011-07-15    2        18000.00            1         1
                        3              Michael         Williams       michael.williams@company.com     555-1003         2012-03-10    3        8000.00             2         2
                        4              Emily           Brown          emily.brown@company.com          555-1004         2013-09-22    4        12000.00            2         3
                     
                    """
    },
    
    
    
    
    {
        "Question":"Total salary paid in each region.",
        "SQLQuery":"SELECT r.region_name, SUM(e.salary) FROM employees e JOIN departments d ON e.department_id = d.department_id JOIN locations l ON d.location_id = l.location_id JOIN countries c ON l.country_id = c.country_id JOIN regions r ON c.region_id = r.region_id GROUP BY r.region_name;",
        "SQLResult":"""region_name                      SUM(e.salary)
        
                       Asia                             12000.00
                       Middle East and Africa           17000.00
                       Europe                           22500.00
                       Americas                         43000.00
                         
                    """,
        "Answer": """region_name                      SUM(e.salary)
        
                       Asia                             12000.00
                       Middle East and Africa           17000.00
                       Europe                           22500.00
                       Americas                         43000.00
                         
                    """
    },
    
    
    
    
    {
        "Question":"Top 3 departments by number of employees",
        "SQLQuery":"SELECT department_id, COUNT(*) AS count FROM employees GROUP BY department_id ORDER BY count DESC LIMIT 3;",
        "SQLResult":"""department_id                count
                            
                            1                         2
                            2                         3
                            4                         4
                         
                    """,
        "Answer": """department_id                count
                            
                            1                         2
                            2                         3
                            4                         4
                         
                    """
    },
    
    
    
    {
        "Question":"Top 3 departments by number of employees",
        "SQLQuery":"SELECT department_id, COUNT(*) AS count FROM employees GROUP BY department_id ORDER BY count DESC LIMIT 3;",
        "SQLResult":"""job_title                        AVG(e.salary)
                       
                       Administration Vice President    18000.000000
                       Marketing Manager                12000.000000
                       President                        25000.000000
                       Programmer                       7500.000000
                       Sales Representative             4250.000000
                         
                    """,
        "Answer": """job_title                        AVG(e.salary)
                       
                       Administration Vice President    18000.000000
                       Marketing Manager                12000.000000
                       President                        25000.000000
                       Programmer                       7500.000000
                       Sales Representative             4250.000000
                         
                    """
    },
    
    
    {
        "Question":"List of all employees and their email addresses.",
        "SQLQuery":"SELECT first_name, last_name, email FROM employees;",
        "SQLResult":"""first_name       last_name       email
                       
                       David            Jones           david.jones@company.com
                       Emily            Brown           emily.brown@company.com
                       Jennifer         Garcia          jennifer.garcia@company.com
                       John             Smith           john.smith@company.com
                       Lisa             Davis           lisa.davis@company.com
                       Michael          Williams        michael.williams@company.com
                       Patricia         Martinez        patricia.martinez@company.com
                       Robert           Miller          robert.miller@company.com
                       Sarah            Johnson         sarah.johnson@company.com
                       Thomas           Rodriguez       thomas.rodriguez@company.com
                         
                    """,
        "Answer": """first_name       last_name       email
                       
                       David            Jones           david.jones@company.com
                       Emily            Brown           emily.brown@company.com
                       Jennifer         Garcia          jennifer.garcia@company.com
                       John             Smith           john.smith@company.com
                       Lisa             Davis           lisa.davis@company.com
                       Michael          Williams        michael.williams@company.com
                       Patricia         Martinez        patricia.martinez@company.com
                       Robert           Miller          robert.miller@company.com
                       Sarah            Johnson         sarah.johnson@company.com
                       Thomas           Rodriguez       thomas.rodriguez@company.com
                         
                    """
    },
    
    
    
    {
        "Question":"List employee name and job title for salary > 8000.",
        "SQLQuery":"SELECT e.first_name, e.last_name, j.job_title FROM employees e JOIN jobs j ON e.job_id = j.job_id WHERE e.salary > 8000;",
        "SQLResult":"""first_name       last_name      job_title
                       
                       John              Smith          President
                       Sarah             Johnson        Administration Vice President
                       Emily             Brown          Marketing Manager
                         
                    """,
        "Answer": """first_name       last_name      job_title
                       
                       John              Smith          President
                       Sarah             Johnson        Administration Vice President
                       Emily             Brown          Marketing Manager
                         
                    """
    },
    
    
    
    {
        "Question":"All regions and number of employees in each",
        "SQLQuery":"SELECT r.region_name, COUNT(e.employee_id) FROM employees e JOIN departments d ON e.department_id = d.department_id JOIN locations l ON d.location_id = l.location_id JOIN countries c ON l.country_id = c.country_id JOIN regions r ON c.region_id = r.region_id GROUP BY r.region_name;",
        "SQLResult":"""region_name            COUNT(e.employee_id)
                       
                       Americas                    2
                       Asia                        1
                       Europe                      3
                       Middle East and Africa      4
                         
                    """,
        "Answer": """region_name            COUNT(e.employee_id)
                       
                       Americas                    2
                       Asia                        1
                       Europe                      3
                       Middle East and Africa      4
                         
                    """
    },
    
    
    
    {
        "Question":"Departments with average salary > 10,000",
        "SQLQuery":"SELECT d.department_name, AVG(e.salary) AS avg_salary FROM employees e JOIN departments d ON e.department_id = d.department_id GROUP BY d.department_name HAVING avg_salary > 10000;",
        "SQLResult":"""department_name       avg_salary
                       
                       Executive             21500.000000
                       Marketing             12000.000000
                         
                    """,
        "Answer": """department_name         avg_salary
                       
                       Executive             21500.000000
                       Marketing             12000.000000
                  """
    },
    
    
    
    
    {
        "Question":"Names of countries where 'Sales' departments are located.",
        "SQLQuery":"SELECT DISTINCT c.country_name FROM departments d JOIN locations l ON d.location_id = l.location_id JOIN countries c ON l.country_id = c.country_id WHERE d.department_name = 'Sales';",
        "SQLResult":"""country_name        
                       
                        Nigeria

                        
                         
                    """,
        "Answer": """country_name        
                       
                        Nigeria
                  """
    },
    
    
    
    {
        "Question":"Find employees who are managers.",
        "SQLQuery":"SELECT DISTINCT m.first_name, m.last_name FROM employees e JOIN employees m ON e.manager_id = m.employee_id;",
        "SQLResult":"""first_name  last_name        
                       
                        John        Smith
                        Sarah       Johnson
                        Michael     Williams
                        Emily       Brown
                        David       Jones

                        
                         
                    """,
        "Answer": """first_name  last_name        
                       
                        John        Smith
                        Sarah       Johnson
                        Michael     Williams
                        Emily       Brown
                        David       Jones
                  """
    },
    
    
    
    
    {
        "Question":"Find employees who do not manage anyone",
        "SQLQuery":"SELECT first_name, last_name FROM employees WHERE employee_id NOT IN (SELECT DISTINCT manager_id FROM employees WHERE manager_id IS NOT NULL);",
        "SQLResult":"""first_name  last_name        
                       
                        Jennifer   Garcia
                        Robert     Miller
                        Lisa       Davis
                        Thomas     Rodriguez
                        Patricia   Martinez

                        
                         
                    """,
        "Answer": """first_name  last_name        
                       
                        Jennifer   Garcia
                        Robert     Miller
                        Lisa       Davis
                        Thomas     Rodriguez
                        Patricia   Martinez
                  """
    },
    
    
    
    {
        "Question":"List dependents whose parents are in 'Marketing'.",
        "SQLQuery":"SELECT d.first_name, d.last_name FROM dependents d JOIN employees e ON d.employee_id = e.employee_id JOIN departments dep ON e.department_id = dep.department_id WHERE dep.department_name = 'Marketing';",
        "SQLResult":"""first_name  last_name        
                       
                        Sophia      Brown
              
                    """,
        "Answer": """first_name  last_name        
                       
                    Sophia       Brown
                  """
    },
    
    
    
    
    
    {
        "Question":"List job titles available in the company",
        "SQLQuery":"SELECT DISTINCT job_title FROM jobs;",
        "SQLResult":"""job_title       
                       
                        President
                        Administration Vice President
                        Programmer
                        Marketing Manager
                        Sales Representative
              
                    """,
        "Answer": """  job_title       
                       
                        President
                        Administration Vice President
                        Programmer
                        Marketing Manager
                        Sales Representative
                  """
    },
    
    
    
    
    {
        "Question":"Get list of departments without any employees.",
        "SQLQuery":"SELECT department_name FROM departments WHERE department_id NOT IN (SELECT DISTINCT department_id FROM employees);",
        "SQLResult":"""department_name       
                       
                        HR
              
                    """,
        "Answer": """  department_name       
                       
                        HR
                  """
    },
    
    
    {
        "Question":"how job_id and total salary per job",
        "SQLQuery":"SELECT job_id, SUM(salary) FROM employees GROUP BY job_id;",
        "SQLResult":"""job_id     SUM(salary)       
                       
                        1           25000.00
                        2           18000.00
                        3           22500.00
                        4           12000.00
                        5           17000.00
              
                    """,
        "Answer": """  job_id     SUM(salary)       
                       
                        1           25000.00
                        2           18000.00
                        3           22500.00
                        4           12000.00
                        5           17000.00
                  """
    },
    
    
    
    {
        "Question":"List the total number of dependents per relationship type.",
        "SQLQuery":"SELECT relationship, COUNT(*) FROM dependents GROUP BY relationship;",
        "SQLResult":"""relationship  COUNT(*)       
                       
                         Child          8
                         Spouse         2
              
                    """,
        "Answer": """  relationship  COUNT(*)       
                       
                         Child          8
                         Spouse         2
                  """
    },
]
Loan Pricing Engine
---------
https://www.bfgusa.com

#### Overview
This is a mortgage pricing application to check interest rates. The user can input their loan terms and view their available interest rates without reloading the page (via Ajax).

I created this project using the following technologies:

- **Python**: Logic for the investor guidelines
- **Django**: Web framework using the Model-View-Template (MVT) pattern
- **Postgres**: Database to store the county tax rates for each zip code
- **XML**: Interest rates and yield spread premiums (ysp) stored in tables for each investor
- **HTML**: Layout for the site
- **CSS**: *Responsive* and *fluid* structure for mobile usage (columns are based on percentages of screen width, and stack vertically on smaller devices)
- **Javascript**: Dynamic creation of the table rows to display results
- **Jquery**: Data validations to ensure clean user input
- **Ajax**: Interest rates refreshed upon "keyup" without reloading the page
- **Git**: Version control system
- **GitHub**: Source code hosting for the git repository
- **Heroku**: Production web server to host the site

#### APR Calculation

Calculating the APR is particularly challenging because there is no discrete formula. It is calculated through a method of **iteration**, where the the value is determined by "guessing" the IRR (Internal Rate of Return) that makes the NPV (Net Present Value) equivalent to 0. To accomplish this, I implemented a **Binary Search Algorithm** that converges towards the APR by iteratively cutting the range in half until the appropriate value is found. The efficiency of the algorithm is **log (n)** time; more practically, it takes approximately 20 "guesses" (iterations of the While loop) until the actual APR is found (within an accuracy of 4 decimal places).

#### More Information
The application parses each investor's lending guidelines, which are driven heavily by the user's credit score and loan-to-value ratio. The resulting interest rate is then adjusted upwards to cover the title closing costs, which in turn are calculated based on the county tax rates for the user's zip code.

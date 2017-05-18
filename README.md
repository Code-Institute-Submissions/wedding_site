# Wedding Musician Website - Django Project

An exercise in creating a Django based website & CRM for a wedding musician. Includes Account section for customers where they can access all confirmed details of their booking, and pay online for services provided.

When my client's customers contact her, communication arrives through many and varied channels, website contact, email, FaceBook, phone, SMS etc.

This project is an attempt to provide a place where both my client and her customers can go to provide and view confirmed details respectively.

Text content is not intended production.

##
To display the full functionality of this website, I have created a number of dummy user accounts with associated event details which are viewable to the user. A walkthrough is provided here:
### For New Users:
A new visitor to the website will contact my client through one of the afore-mentioned channels.
Once details are confirmed for an event, the web-master asks the user to register on the website if he/she should so desire to avail of this functionality. The webmaster then creates an event in the admin panel that can be viewed by the user and confirmed by paying a deposit through the provided Stripe link.

Create an account to see this functionality working. You can also test password reset emails and contact form functionality, all of which is working correctly as of 16/05/2017. (From time to time Gmail [used here only for testing] resets its SMTP security level so this may not work continuously)

### Dummy Users
#### Login Details (Use these to view confirmed events for different users)
Username: george

Email: george@george.com

Password: georgepassword
##
Username: jenjen

Email: jenjen@jen.com

Password: jenjenpassword
##
Username: montypython

Email: montypython@montypython.com

Password: montypythonpassword



## Getting Started

### Prerequisites

No installation is necessary to view this app online.
A live version of this app is hosted [here](https://com-wedding-site.herokuapp.com/) on Heroku.

If you wish to test/develop this app locally, clone this repo and use the following guidelines:

### Python
You must have Python 2.7 installed on your system, available [here](https://www.python.org/).
Download the correct version for your operating system and follow the installation instructions.

### requirements.txt
Create and activate a local virtual environment and pip install -r requirements.txt

### Local Server
Run your app using the following commands in command line:

$ python manage.py runserver

Navigate to http://localhost:8000/ to view your app locally.

## Built With

- [Django](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design
- [PostgreSQL](https://www.postgresql.org/) - a powerful, open source object-relational database system
- [Stripe](https://stripe.com/) - allows both private individuals and businesses to accept payments over the Internet


## Testing
Manual testing was undertaken for every feature of the website and satisfactorily passed.

All code was run through an online validator at [w3.org](https://validator.w3.org/).


## Responsiveness
Google Chrome responsive tool in inspector is buggy. App displays as desired in actual devices.


## Other Notes
Mindmap created with [coggle.it](https://coggle.it/) before writing any code, available to view [here](https://coggle.it/diagram/WRRcSRe8vAABLQOV).

## Author
Brendan Long

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Neuethemes - Emma Theme](http://wrapbootstrap.com/preview/WB055S9S3)
- Testimonial Slider based on a version by [bmoeller1](https://bootsnipp.com/snippets/featured/responsive-quote-carousel)

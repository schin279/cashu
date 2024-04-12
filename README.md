## Cashu - Casual Jobs Platform
Cashu is a platform designed to connect individuals seeking casual jobs with employers looking for short-term help. Whether you're a student looking to make some extra cash, a freelancer seeking temporary gigs, or a business in need of on-demand assistance, Cashu is here to streamline the process.

## Features
- **User-friendly Interface**: Cashu provides an intuitive and easy-to-use interface for both job seekers and employers
- **Job Listings**: Employers can post job listings detailing the requirements, duration, and compensation for each position.
- **Job Search**: Job seekers can browse through available listings and apply for jobs directly through the platform.
- **Ratings and Reviews**: Both employers and job seekers can leave feedback and ratings based on their experience, fostering trust and accountability within the Cashu community.

## Setup
To get started with Cashu, follow these steps:
1. **Clone the Repository:**
```bash
git clone https://github.com/schin279/cashu
```
2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```
3. **Set Up Database:**  
Cashu uses MySQL. To set up the database, just run the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```
4. **Create Superuser (Optional):**  
To access the Django admin interface, create a superuser:
```bash
python manage.py createsuperuser
```
5. **Start the Development Server:**
```bash
python manage.py runserver
```
6. **Access Cashu:**  
Open web browser and navigate to 'http://localhost:8000' to access Cashu locally.

## Contact
Have questions or feedback? Contact us at a1899082@adelaide.edu.au.

# Booky

Booky is a Django-based web application that allows users to browse, review, and rate books. The project is currently under development, with several features already implemented and more planned for future releases.

## Features

### Implemented:
- **Book Browsing:** Users can browse a catalog of books, view details, and read reviews.
- **User Authentication:** User registration, login, and logout functionalities.
- **Review Submission:** Authenticated users can submit reviews for books.
- **Star Ratings:** Users can rate books using a star rating system.
- **Review Likes:** Users can like reviews submitted by others, with the likes being tracked and displayed.
- **Interactive UI:** Enhanced user experience with interactive star rating and review submission using JavaScript.
- **Admin Interface:** Comprehensive management of books, reviews, and user interactions through Django's admin panel.

### Planned Features:
- **Advanced Search:** Enhanced search functionality to filter books by author, genre, and rating.
- **User Profiles:** Detailed user profiles showing review history, liked books, and other personalized features.
- **Recommendations:** Personalized book recommendations based on user preferences and ratings.
- **Social Features:** Ability to follow other users, comment on reviews, and share book lists.
- **API Integration:** Exposing book and review data through a REST API for external applications.

## Installation

To run the project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/TuranOzdemir/Booky.git
    cd Booky
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
   - Open a web browser and navigate to `http://127.0.0.1:8000/` to view the application.
   - Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

## Contributing

This project is still in development. Contributions, suggestions, and feedback are welcome. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## License

Booky is open-source software licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to modify this as your project evolves!

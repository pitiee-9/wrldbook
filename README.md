## Wrldbook Project Documentation

### Introduction and Project Evolution

Wrldbook began as a practical solution to a local need: a simple note-sharing platform for school announcements and parent inquiries. Its initial form was a basic Flask application, inspired by foundational web development tutorials. The core idea was to provide a centralized digital space for a specific community to exchange information. However, the vision for the platform quickly expanded. Recognizing the potential for broader, more interactive communication, our team embarked on a project to transform this simple utility into a full-fledged social network. The goal was to evolve from a one-way announcement board into a dynamic space where users could create rich profiles, connect with others, and share their thoughts within a personalized network, much like modern social media platforms but with a focus on meaningful, community-driven interactions and privacy.

### Technical Architecture and Project Structure

To manage the application's growing complexity, the project adheres to a standard Flask structure, which organizes code into logical components for scalability and maintainability . The core of the application is a Python package, typically named `website` or `flask`, which contains all the major application components.

The project directory is organized as follows:

```
Wrldbook/
├── website/                 # Python package for the application core
│   ├── __init__.py 
|   ├── database.db        # Application factory function
│   ├── models.py           # Database models (User, Post, Follow)
│   ├── auth.py             # Authentication routes (login, signup)
│   ├── views.py            # Main application routes and logic
│   ├── templates/          # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── signup.html
│   │   └── ...
│   └── static/
│       ├── home.css
│       └── auth.css
├── main.py       # initializes the app
├── requirements.txt        # Project dependencies
└── README.md
```

This structure cleanly separates the application's configuration, data models, business logic, and user interface. The `templates` directory holds the HTML files that render the user's feed, profile pages, and authentication forms, while the `static` directory contains CSS for styling and the profile pictures users can upload . The use of blueprints, as seen in `auth.py` and `views.py`, helps in organizing the routes into modular components .

### Development Process and Implementation

The development of Wrldbook was an iterative process of feature addition and refinement. It started from a single-file Flask application and was gradually refactored into the structured package detailed above. The foundation was the user system, built using Flask-Login for session management. The database, powered by Flask-SQLAlchemy, initially had a simple `User` and `Note` model. As the project evolved into a social network, this was expanded with new models: a `Post` model to handle the main content.

A significant enhancement was the feature of that the home page was completely redesigned from a simple note list into a social feed. This required modifying the view function to query posts from the users that the current user follows, thereby creating a personalized stream of content. Features like post replies and deletion were added incrementally, with AI tools assisting in debugging and ensuring the new HTML templates worked correctly with the Flask server, which significantly accelerated the development cycle.

### Conclusion and Future Directions

Looking forward, the roadmap for Wrldbook includes implementing finer-grained **post visibility controls**, allowing users to choose between public and followers-only posts. Further potential enhancements include introducing a direct messaging system for private conversations, adding post reactions (likes, hearts), and developing a notification system to alert users about new followers or interactions. The current architecture provides a solid and scalable foundation upon which these exciting new features can be built.
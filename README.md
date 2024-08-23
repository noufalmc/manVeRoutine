# ManVeRoutine

ManVeRouting is a comprehensive management tool designed to streamline and organize essential men's activities, ensuring they stay on top of their personal and vehicle maintenance tasks. The platform provides reminders and tracking features for routine activities such as nail cutting, hair cutting, vehicle oil changes, and pollution certificate renewals. By keeping all these important tasks in one place, MenTasker helps users maintain their grooming habits and vehicle upkeep efficiently, reducing the risk of missing critical deadlines and enhancing overall well-being.

## Features
- **Task Management**: Track and manage routine activities such as nail cutting, hair cutting, vehicle oil changes, and pollution certificate renewals.
- **Reminders**: Set up reminders for each activity to ensure nothing is missed.
- **User Dashboard**: A personalized dashboard that displays upcoming tasks and reminders.
- **Reports**: Generate reports of completed tasks and upcoming deadlines.
- **Responsive Design**: Accessible on all devices with a user-friendly interface.

## Technologies Used
### Backend
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Python**: The programming language used for backend logic and data processing.
- **MySQL**: A robust and scalable relational database for storing user data and tasks.

### Frontend
- **Vue.js**: A progressive JavaScript framework used for building the user interface and single-page applications.

## Installation

### Backend Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/mentasker.git
   cd mentasker

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt

4. **Set up the MySQL database:**

    Create a new MySQL database.
    Update the DATABASES setting in mentasker/settings.py with your MySQL credentials.
5. **Apply migrations:**

    ```bash
    python manage.py migrate

6. **Create a superuser::**

    ```bash
    python manage.py createsuperuser
7. **Run the Django development server:**

    ```bash
    python manage.py runserver


### Frontend Setup

1. **Navigate to the frontend directory:**

    ```bash
    cd frontend

2. **Install dependencies:**
    ```bash
    npm install

3. **Run the Vue.js development server:**

    ```bash
    npm run serve




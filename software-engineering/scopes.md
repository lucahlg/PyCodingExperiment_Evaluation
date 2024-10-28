**Development Plan for Smart Fridge Application**

---

**Scope 0: Initialize Project with Tech Stack**

---

**User Story:**

As a developer, I want to set up the project environment with the chosen tech stack so that all team members can start development efficiently.

---

**Design Spec:**

- **Project Repository:**
  - Create a Git repository hosted on a platform like GitHub or GitLab.
  - Include a `.gitignore` file to exclude unnecessary files.
- **Frontend Setup:**
  - Initialize a React application without using any GUI builders.
  - Ensure the project structure supports scalability and maintainability.
- **Backend Setup:**
  - Set up a Flask application with Flask-RestX for building RESTful APIs.
  - Organize the backend code into modules for routes, models, and services.
- **Database Configuration:**
  - Set up a local MySQL database for development purposes.
  - Configure database connections using MySQL Connector for Python.
- **Dependency Management:**
  - Use `package.json` for managing frontend dependencies.
  - Use `requirements.txt` for backend Python dependencies.
- **Environment Variables:**
  - Implement a way to manage environment-specific settings (e.g., using `.env` files).
- **Responsive Design Framework:**
  - Decide on a CSS framework or library (e.g., Bootstrap or Material-UI) to assist with responsive design.
- **Documentation:**
  - Provide a README with setup instructions and project overview.

---

**Technical Spec:**

- **Repository Structure:**
  - Root directory: `smart-fridge-app/`
    - `frontend/` for React application.
    - `backend/` for Flask application.
    - `db/` for database scripts and ER diagrams.
    - `docs/` for documentation and design assets.
  - Initialize Git in the root directory and push to the remote repository.
- **Frontend (React):**
  - Navigate to `frontend/` and initialize the React app:
    - Run `npx create-react-app .` to set up the project.
  - Install necessary packages:
    - `npm install axios react-router-dom bootstrap`
  - Set up initial file structure:
    - `src/components/` for React components.
    - `src/services/` for API service calls.
    - `src/styles/` for CSS files.
  - Configure routing using React Router.
- **Backend (Flask with Flask-RestX):**
  - Navigate to `backend/` and create a virtual environment:
    - `python3 -m venv venv`
  - Activate the virtual environment and install packages:
    - `pip install flask flask-restx mysql-connector-python flask-cors flask-login python-dotenv`
  - Create `app.py` as the entry point for the Flask application.
  - Organize the backend:
    - `app/__init__.py` to initialize the Flask app.
    - `app/routes/` for API endpoints.
    - `app/models/` for database models.
    - `app/services/` for business logic.
  - Configure CORS to allow frontend-backend communication.
- **Database:**
  - In `db/`, create `schema.sql` for database schema creation.
  - Set up local MySQL database and ensure connectivity.
  - Use environment variables to store database credentials securely.
- **Configuration Files:**
  - Frontend: `package.json`, `.env`, `.gitignore`
  - Backend: `requirements.txt`, `.env`, `.gitignore`
- **Testing Setup:**
  - Frontend:
    - Install Jest and React Testing Library.
  - Backend:
    - Set up unittest or pytest for testing API endpoints.
- **Continuous Integration (Optional):**
  - Set up CI/CD pipelines using tools like GitHub Actions or GitLab CI.

---

**Acceptance Criteria:**

- The project repository is initialized and accessible to all team members.
- Frontend and backend environments can be set up locally using provided instructions.
- Frontend and backend servers run without errors and can communicate with each other.
- The local MySQL database is operational and can be connected to by the backend.
- Environment variables are used for sensitive configurations, and `.env` files are excluded from version control.
- QA Verification:
  - Clone the repository on a new machine.
  - Follow the README instructions to set up both frontend and backend.
  - Verify that the frontend displays a basic welcome page.
  - Test that the backend API responds to a test request.
  - Ensure that the frontend can make a successful API call to the backend.
  - Check that the backend can perform a simple database query.

---

**Scope 1: User Authentication and Authorization**

---

**User Story:**

As a user, I want to securely log in to the system so that I can manage my household's fridge contents and recipes.

---

**Design Spec:**

- **Login Page:**
  - A clean, user-friendly login page with fields for email/username and password.
  - Options for user registration and password recovery.
- **Dashboard Redirect:**
  - Upon successful login, users are redirected to their personalized dashboard.
- **Security:**
  - Passwords are hashed and stored securely.
  - Sessions are maintained securely to prevent unauthorized access.
- **Responsive Design:**
  - The login page adapts to both desktop and mobile screens.

---

**Technical Spec:**

- **Frontend (React):**
  - Create `Login`, `Registration`, and `PasswordRecovery` components in `src/components/auth/`.
  - Use React Router for navigation between authentication pages.
  - Implement form validation for user inputs.
- **Backend (Flask with Flask-RestX):**
  - Set up authentication routes in `app/routes/auth.py`.
    - `POST /api/auth/register`: Register a new user.
    - `POST /api/auth/login`: Authenticate a user and start a session.
    - `POST /api/auth/logout`: End user session.
  - Use `Flask-Login` for session management.
  - Store user data in a `users` table in MySQL with fields: `id`, `email`, `password_hash`, `created_at`.
- **Security:**
  - Implement password hashing using `werkzeug.security`.
  - Ensure all authentication routes are secured with SSL (for production).
- **File Structure:**
  - Frontend components in `src/components/auth/`.
  - Backend routes in `app/routes/auth.py`.
  - Models in `app/models/user.py`.

---

**Acceptance Criteria:**

- Users can register with a unique email and secure password.
- Users can log in with valid credentials and are redirected to their dashboard.
- Users cannot access protected routes without authentication.
- Passwords are securely hashed and not stored in plain text.
- QA Verification:
  - Test user registration with valid and invalid inputs.
  - Attempt to log in with correct and incorrect credentials.
  - Ensure unauthorized access is prevented to protected endpoints.
  - Verify that sessions expire upon logout.

---

**Scope 2: Database Schema Design and Setup**

---

**User Story:**

As a developer, I need a structured database schema to store all necessary data entities and their relationships effectively.

---

**Design Spec:**

- **Entity-Relationship Diagram:**
  - Design an ER diagram in Chen notation including entities: User, Household, Person, Fridge, FoodItem, Unit, Quantity, Recipe.
- **Entities and Relationships:**
  - **User** has one or more **Households**.
  - **Household** has many **Persons** and one **Fridge**.
  - **Person** can own many **Recipes**.
  - **Recipe** consists of many **Quantities**.
  - **Quantity** links **FoodItem** and **Unit**.
  - **Fridge** contains many **FoodItems** with associated **Quantities**.
- **Attributes:**
  - Define all necessary attributes for each entity as per requirements.

---

**Technical Spec:**

- **Database (MySQL):**
  - Create tables for each entity with appropriate fields and data types.
  - Implement foreign keys to enforce relationships and referential integrity.
  - Use `InnoDB` engine for transaction support.
- **Scripts:**
  - Write SQL scripts for table creation in `db/schema.sql`.
  - Seed the database with initial data in `db/seeds.sql`.
- **ORM (Optional):**
  - Implement SQLAlchemy models in `app/models/` for each entity.

---

**Acceptance Criteria:**

- The database schema accurately represents all entities and relationships.
- All tables are created with correct fields, data types, and constraints.
- Referential integrity is enforced through foreign keys.
- QA Verification:
  - Inspect the ER diagram and ensure it matches the database schema.
  - Verify that relationships are correctly implemented.
  - Attempt to insert data violating constraints to test integrity enforcement.

---

**Scope 3: CRUD Operations for Units and Food Items**

---

**User Story:**

As a user, I want to manage units and food items so that I can accurately define ingredients and fridge contents.

---

**Design Spec:**

- **Unit Management:**
  - Form to create new units (e.g., grams, liters).
  - List view displaying all units with options to edit or delete.
- **Food Item Management:**
  - Form to create new food items (e.g., milk, eggs).
  - List view displaying all food items with options to edit or delete.
- **Navigation:**
  - Access to unit and food item management from the main menu.
- **Responsive Design:**
  - Ensure forms and lists are usable on both desktop and mobile devices.

---

**Technical Spec:**

- **Frontend (React):**
  - Create `UnitList`, `UnitForm`, `FoodItemList`, `FoodItemForm` components in `src/components/units/` and `src/components/fooditems/`.
  - Implement client-side validation for forms.
- **Backend (Flask with Flask-RestX):**
  - Create API endpoints in `app/routes/units.py` and `app/routes/food_items.py`.
    - Units:
      - `GET /api/units`: Retrieve all units.
      - `POST /api/units`: Create a new unit.
      - `PUT /api/units/<id>`: Update a unit.
      - `DELETE /api/units/<id>`: Delete a unit.
    - Food Items:
      - Similar endpoints as units.
  - Implement models `Unit` and `FoodItem` in `app/models/`.
- **Database:**
  - Tables `units` and `food_items` with necessary fields.

---

**Acceptance Criteria:**

- Users can create, view, edit, and delete units and food items.
- Changes are reflected in the database immediately.
- The UI updates to reflect CRUD operations without requiring a page refresh.
- QA Verification:
  - Perform CRUD operations through the UI.
  - Check the database to ensure data consistency.
  - Test edge cases like duplicate entries or invalid inputs.

---

**Scope 4: Household and Fridge Management**

---

**User Story:**

As a user, I want to create and manage my household and its fridge to organize residents and fridge contents effectively.

---

**Design Spec:**

- **Household Management:**
  - Form to create and edit households with a household name.
  - List view of households the user is part of.
- **Fridge Management:**
  - Each household view includes access to its fridge.
  - Display fridge contents with food items and their quantities.
  - Options to add or remove items from the fridge.
- **Navigation:**
  - Access household and fridge management from the dashboard.
- **Responsive Design:**
  - Ensure usability on all devices.

---

**Technical Spec:**

- **Frontend (React):**
  - Components: `HouseholdList`, `HouseholdForm`, `FridgeView`, `FridgeItemForm`.
  - Organize components under `src/components/households/` and `src/components/fridge/`.
- **Backend (Flask with Flask-RestX):**
  - Routes in `app/routes/households.py` and `app/routes/fridge.py`.
    - Households:
      - `GET /api/households`: List user's households.
      - `POST /api/households`: Create a new household.
      - `PUT /api/households/<id>`: Edit household details.
    - Fridge:
      - `GET /api/households/<id>/fridge`: Get fridge contents.
      - `POST /api/households/<id>/fridge/items`: Add item to fridge.
      - `DELETE /api/households/<id>/fridge/items/<item_id>`: Remove item.
- **Database:**
  - Update `households` table.
  - Create `fridge_items` table linking households to food items with quantities.

---

**Acceptance Criteria:**

- Users can create and edit households.
- Each household has one fridge with contents accurately displayed.
- Users can add and remove items from the fridge.
- Changes persist in the database.
- QA Verification:
  - Test creating households and managing fridge contents.
  - Verify database updates correspond to UI actions.
  - Ensure fridge contents reflect accurate quantities after operations.

---

**Scope 5: Person Management**

---

**User Story:**

As a user, I want to add and manage residents in my household to assign recipes and track ownership.

---

**Design Spec:**

- **Person Management:**
  - Form to add new persons with first name, last name, and nickname.
  - List view of residents in a household with edit and delete options.
- **Association:**
  - Persons are associated with a household.
- **Navigation:**
  - Access person management from the household view.
- **Responsive Design:**
  - Ensure forms and lists are mobile-friendly.

---

**Technical Spec:**

- **Frontend (React):**
  - Components: `PersonList`, `PersonForm`.
  - Located in `src/components/persons/`.
- **Backend (Flask with Flask-RestX):**
  - Routes in `app/routes/persons.py`.
    - `GET /api/households/<id>/persons`: List persons in a household.
    - `POST /api/households/<id>/persons`: Add a new person.
    - `PUT /api/persons/<id>`: Edit person details.
    - `DELETE /api/persons/<id>`: Delete a person.
- **Database:**
  - Table `persons` with foreign key to `households`.

---

**Acceptance Criteria:**

- Users can add, edit, and delete residents within a household.
- Persons are correctly linked to their household.
- Changes reflect in both UI and database.
- QA Verification:
  - Add residents and check their association with the household.
  - Edit and delete residents and verify updates in the database.

---

**Scope 6: Recipe Management (Without Ingredients)**

---

**User Story:**

As a user, I want to create and manage recipes to store cooking instructions and share them with household members.

---

**Design Spec:**

- **Recipe Management:**
  - Form to create and edit recipes with name and number of servings.
  - List view of recipes owned by a person.
- **Ownership:**
  - Recipes are associated with a person (owner).
- **Navigation:**
  - Access recipe management from the dashboard or person's profile.
- **Responsive Design:**
  - Ensure compatibility across devices.

---

**Technical Spec:**

- **Frontend (React):**
  - Components: `RecipeList`, `RecipeForm`.
  - Located in `src/components/recipes/`.
- **Backend (Flask with Flask-RestX):**
  - Routes in `app/routes/recipes.py`.
    - `GET /api/persons/<id>/recipes`: List recipes by a person.
    - `POST /api/persons/<id>/recipes`: Create a new recipe.
    - `PUT /api/recipes/<id>`: Edit a recipe.
    - `DELETE /api/recipes/<id>`: Delete a recipe.
- **Database:**
  - Table `recipes` with foreign key to `persons`.

---

**Acceptance Criteria:**

- Users can create, view, edit, and delete recipes.
- Recipes are correctly associated with their owners.
- All changes are persistent.
- QA Verification:
  - Test recipe CRUD operations.
  - Verify that recipes are linked to the correct person in the database.

---

**Scope 7: Quantity and Ingredient Management**

---

**User Story:**

As a user, I want to specify ingredients for my recipes to know what is needed to prepare them.

---

**Design Spec:**

- **Ingredient Management:**
  - Within the recipe form, options to add multiple ingredients.
  - Each ingredient includes a food item, amount, and unit.
- **Display:**
  - List of ingredients displayed when viewing a recipe.
- **Responsive Design:**
  - Ensure ingredient forms are easy to use on all devices.

---

**Technical Spec:**

- **Frontend (React):**
  - Update `RecipeForm` to include ingredient management.
  - Components: `IngredientList`, `IngredientForm`.
- **Backend (Flask with Flask-RestX):**
  - Routes in `app/routes/ingredients.py`.
    - `POST /api/recipes/<id>/ingredients`: Add an ingredient.
    - `PUT /api/ingredients/<id>`: Edit an ingredient.
    - `DELETE /api/ingredients/<id>`: Delete an ingredient.
- **Database:**
  - Table `quantities` linking `recipes` to `food_items` and `units`.

---

**Acceptance Criteria:**

- Users can add, edit, and delete ingredients within recipes.
- Ingredients correctly display in the recipe view.
- Database reflects all ingredient associations.
- QA Verification:
  - Manage ingredients for a recipe and ensure data integrity.
  - Check that calculations (if any) are correct.

---

**Scope 8: Fridge Content Management (Adding/Removing Items)**

---

**User Story:**

As a user, I want to manage my fridge contents by adding items after shopping and removing items after preparing a recipe.

---

**Design Spec:**

- **Adding Items:**
  - Form to add food items to the fridge with specified quantities.
- **Removing Items:**
  - Option to remove or adjust quantities of items in the fridge.
- **Display:**
  - Updated fridge contents displayed in real-time.
- **Responsive Design:**
  - Ensure forms are accessible on mobile devices.

---

**Technical Spec:**

- **Frontend (React):**
  - Components: `AddFridgeItemForm`, `FridgeItemList`.
- **Backend (Flask with Flask-RestX):**
  - Routes in `app/routes/fridge.py`.
    - `POST /api/households/<id>/fridge/items`: Add items.
    - `PATCH /api/households/<id>/fridge/items/<item_id>`: Update item quantity.
    - `DELETE /api/households/<id>/fridge/items/<item_id>`: Remove item.
- **Database:**
  - Update `fridge_items` table as necessary.

---

**Acceptance Criteria:**

- Users can add items to the fridge with accurate quantities.
- Users can remove items or update quantities.
- Fridge contents update immediately in the UI and database.
- QA Verification:
  - Add and remove items, verifying quantities adjust correctly.
  - Check for data consistency in the database.

---

**Scope 9: Relationships Between Entities**

---

**User Story:**

As a user, I want to assign recipes to persons and residents to households to manage ownership and participation.

---

**Design Spec:**

- **Assignment:**
  - When creating a recipe, select the owning person.
  - Persons are assigned to households upon creation.
- **Validation:**
  - Ensure only residents of a household can own recipes within it.
- **Display:**
  - Show owner information on recipe listings.

---

**Technical Spec:**

- **Frontend (React):**
  - Update `RecipeForm` to include owner selection.
  - Ensure dropdown lists only household residents.
- **Backend (Flask with Flask-RestX):**
  - Validate ownership in `app/routes/recipes.py`.
  - Enforce rules in models and database constraints.
- **Database:**
  - Ensure foreign keys correctly link recipes to persons and persons to households.

---

**Acceptance Criteria:**

- Recipes are owned by persons within the household.
- Only valid associations are allowed.
- QA Verification:
  - Attempt to assign recipes to non-residents (should fail).
  - Verify correct associations in the database.

---

**Scope 10: Querying Recipes Available with Current Stock**

---

**User Story:**

As a user, I want to see which recipes I can prepare with my current fridge contents to decide what to cook.

---

**Design Spec:**

- **Feature:**
  - A "What can I cook?" button on the dashboard.
  - Display a list of recipes that can be fully prepared with current fridge items.
- **Display:**
  - Recipes listed with images (if available) and brief descriptions.
- **Responsive Design:**
  - Ensure the feature works well on mobile devices.

---

**Technical Spec:**

- **Backend (Flask with Flask-RestX):**
  - Endpoint `GET /api/households/<id>/available_recipes`.
  - Logic to compare fridge contents with recipe ingredients.
- **Frontend (React):**
  - Component `AvailableRecipesList` in `src/components/recipes/`.
  - Handle loading states and errors gracefully.
- **Algorithm:**
  - Check for each recipe if all required ingredients and quantities are present in the fridge.

---

**Acceptance Criteria:**

- Only recipes that can be made with current fridge contents are displayed.
- The list updates when fridge contents change.
- QA Verification:
  - Modify fridge contents and verify the available recipes list adjusts accordingly.
  - Ensure calculations for quantities are accurate.

---

**Scope 11: Querying Additional Purchases Needed for a Recipe**

---

**User Story:**

As a user, I want to know what additional items I need to buy to prepare a desired recipe to plan my shopping.

---

**Design Spec:**

- **Feature:**
  - On a recipe page, a "What do I need to buy?" button.
  - Display a list of missing ingredients with required quantities.
- **Display:**
  - Clearly differentiate between items not in the fridge and those insufficient in quantity.
- **Responsive Design:**
  - Ensure readability on all devices.

---

**Technical Spec:**

- **Backend (Flask with Flask-RestX):**
  - Endpoint `GET /api/recipes/<id>/missing_ingredients`.
  - Logic to calculate differences between recipe requirements and fridge contents.
- **Frontend (React):**
  - Update `RecipeView` component to include missing ingredients list.
- **Algorithm:**
  - For each ingredient, subtract fridge quantity from recipe quantity.

---

**Acceptance Criteria:**

- Users see an accurate list of additional items needed.
- Quantities are correctly calculated.
- QA Verification:
  - Test with various fridge contents and recipes.
  - Ensure the list reflects actual needs.

---

**Scope 12: Responsive UI Design for Desktop and Mobile**

---

**User Story:**

As a user, I want to access the system from both desktop and mobile devices to manage my fridge and recipes anywhere.

---

**Design Spec:**

- **Responsive Layouts:**
  - Use fluid grids and flexible images.
  - Implement breakpoints for different screen sizes.
- **Navigation:**
  - Hamburger menus on mobile devices.
  - Persistent navigation bars on desktops.
- **Testing:**
  - Ensure all pages render correctly on common device resolutions.

---

**Technical Spec:**

- **Frontend (React):**
  - Utilize CSS media queries and flexbox/grid layouts.
  - Use a responsive UI library like Bootstrap or Material-UI.
  - Test components in `src/components/` for responsiveness.
- **Assets:**
  - Optimize images for different screen sizes.

---

**Acceptance Criteria:**

- UI adapts seamlessly between desktop and mobile views.
- No functionality is lost on smaller screens.
- QA Verification:
  - Test the application on various devices and browsers.
  - Verify that touch interactions are intuitive on mobile.

---

**Scope 13: Implementing the RESTful APIs for All Functionalities**

---

**User Story:**

As a developer, I need comprehensive RESTful APIs to enable the frontend and backend to communicate effectively.

---

**Design Spec:**

- **API Standards:**
  - Use standard HTTP methods and status codes.
  - Consistent endpoint naming conventions.
- **Documentation:**
  - Provide API documentation using Swagger or similar tools.
- **Security:**
  - Implement authentication for protected routes.

---

**Technical Spec:**

- **Backend (Flask with Flask-RestX):**
  - Organize endpoints under namespaces.
  - Implement error handling and input validation.
  - Use `flask_cors` to handle cross-origin requests.
- **File Structure:**
  - Routes in `app/routes/`.
  - Models in `app/models/`.
- **Testing:**
  - Write unit tests for API endpoints.

---

**Acceptance Criteria:**

- All required endpoints are implemented and tested.
- APIs follow RESTful principles.
- Documentation is accessible and up-to-date.
- QA Verification:
  - Use tools like Postman to test each endpoint.
  - Ensure responses are correct and errors are handled gracefully.

---

**Scope 14: Integration Between Frontend and Backend**

---

**User Story:**

As a user, I want the frontend to interact seamlessly with the backend so that the application functions smoothly.

---

**Design Spec:**

- **Data Flow:**
  - Ensure all frontend actions correspond to backend operations.
- **Error Handling:**
  - Display user-friendly error messages.
- **Feedback:**
  - Provide visual cues during loading states.
- **Responsive Design:**
  - Maintain responsiveness during data fetches.

---

**Technical Spec:**

- **Frontend (React):**
  - Use `axios` or `fetch` API for HTTP requests.
  - Implement global state management with Redux or Context API.
  - Handle asynchronous operations with async/await.
- **Backend (Flask):**
  - Ensure CORS is properly configured.
  - Return consistent and informative error messages.
- **Security:**
  - Implement CSRF protection if necessary.

---

**Acceptance Criteria:**

- All frontend features communicate correctly with the backend.
- Users experience minimal latency and clear feedback.
- QA Verification:
  - Perform end-to-end testing of all functionalities.
  - Check network requests for correctness.
  - Simulate slow network conditions to test loading states.

---

**End of Development Plan**

This updated plan now includes **Scope 0** to initialize the project with the chosen tech stack, ensuring that the foundational setup is in place for efficient development. Each scope provides clear user stories, design and technical specifications, and acceptance criteria to guide the development process and ensure quality outcomes.
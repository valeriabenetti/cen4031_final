# Help Desk Ticket System

This is a Help Desk Ticket System application built with FastAPI for the backend and React for the frontend.

## Prerequisites

- Python 3.7+
- Node.js and npm

## Installation

### Backend Setup

1. Clone the repository:

```bash
git clone https://github.com/valeriabenetti/cen4031_final.git cd cen4031_final
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv source venv/bin/activate # on Windows use venv\Scripts\activate
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install the required npm packages:
```bash
npm install
```

## Running the Application

### Start the Backend Server

1. From the main project directory, run:
```bash
uvicorn main:app --reload
```
The backend server will start and be accessible at `http://localhost:8000`.

### Start the Frontend Development Server

1. In a new terminal, navigate to the frontend directory:
```bash
cd frontend
```

2. Start the React development server:
```bash
npm start
```
The frontend will be accessible at `http://localhost:3000`.

## Using the Application

1. Open your web browser and go to `http://localhost:3000`.
2. You should now see the Help Desk Ticket System interface.
3. You can create, view, and manage tickets through this interface.

## API Documentation

- The FastAPI automatic interactive API documentation is available at `http://localhost:8000/docs`.

## Troubleshooting

If you encounter any issues:
1. Ensure all dependencies are correctly installed.
2. Check that both the backend and frontend servers are running.
3. Review the console output for any error messages.

For more detailed information or if you encounter persistent issues, please refer to the project documentation or open an issue on the GitHub repository.
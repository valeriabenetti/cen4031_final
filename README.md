# TitanHelp Application

The TitanHelp application is a help desk ticket management system that allows users to create and view help desk tickets. This project is a part of the final project for the CEN4031 course and demonstrates the use of a full-stack application with a React frontend and a REST API backend.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [Installation](#installation)
5. [Running the Application](#running-the-application)
6. [API Endpoints](#api-endpoints)
7. [Contributors](#contributors)

## Project Overview

The TitanHelp application allows users to:

- View a list of all help desk tickets.
- Create new help desk tickets by providing a name, date, and problem description.
- Display help desk tickets dynamically in a React frontend.
- Store and retrieve tickets using a RESTful API.

## Technologies Used

### Frontend
- [React](https://reactjs.org/)
- JavaScript (ES6+)
- CSS (for styling)

### Backend
- [Node.js](https://nodejs.org/)
- [Express](https://expressjs.com/)
- [Body-parser](https://www.npmjs.com/package/body-parser)
- [Cors](https://www.npmjs.com/package/cors)

### Tools
- [Git](https://git-scm.com/) (for version control)
- [npm](https://www.npmjs.com/) (for package management)
- [GitHub](https://github.com/) (repository hosting)

## Features

- **Create Ticket**: Users can add new help desk tickets by submitting a form.
- **View Tickets**: All existing tickets are displayed in a list.
- **REST API**: The backend provides a RESTful API to fetch and store ticket data.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- **Node.js** (v12 or higher) - [Install Node.js](https://nodejs.org/)
- **npm** (v6 or higher) - Comes bundled with Node.js
- **Git** (for cloning the project) - [Install Git](https://git-scm.com/)

### Clone the Repository

Start by cloning the project from GitHub:

```bash
git clone https://github.com/your-username/cen4031_final.git
cd cen4031_final

# CEN4031 Final Project

# Group Programming Project: TitanHelp Application

## Overview

This project is designed to demonstrate the knowledge and skills acquired during the course by implementing a full-stack application using various frameworks studied. The **TitanHelp Application** is a help desk ticketing system that allows users to create and manage tickets. The application will showcase different language stacks and their respective frameworks in the presentation, application, and data access layers.

## Group Formation

Students are responsible for forming their own groups. Group members can sign up through the course discussion board, and each team should elect a group leader. 

### Group Leader Responsibilities:
- Make decisions based on group input.
- Provide regular status reports to the instructor.
- Act as the primary contact for project-related issues (not for course-related queries, which any member can address).

Each group member will be responsible for developing one specific layer of the project:
- **Presentation Layer**
- **Application Layer**
- **Data Access Layer**

Collaboration is encouraged, but the majority of work on each layer should be completed by the assigned team member. Contributions will be monitored via GitHub.

## Status Reports

The group leader is required to submit weekly status reports via email. These reports should include:
- Project progress updates.
- Issues with non-participating group members (failure to participate may result in removal from the group).

## Final Project Submission

### Requirements
- Submission of the final project by the due date (refer to the course Dropbox).
- A Word document containing both group and individual sections.
- Screenshots of the running application.
- A link to the GitHub repository.

### Group Section:
The group section of the Word document should include:
1. **Team Members and Roles:** List of members and their assignments.
2. **Project Description:** A general overview of the project.
3. **Initial Requirements:** The original project goals and any requirement changes during the design or implementation.
4. **Mastery of the Topic:** Explanation of how the project demonstrates understanding of the frameworks used, such as the chosen data access patterns in the Data Access Layer.
5. **Design and Implementation Documents:** A collection of status reports and relevant design documents.
6. **User Documentation:** Instructions on running the program and using input files.
7. **Final Project Evaluation:** Reflection on what went well, what went wrong, and potential improvements if more time was available.

### Individual Section:
Each team member will include their individual evaluation of the project, reflecting on:
- Personal understanding of the project and the course.
- Insights gained during the course and their real-life applicability.
- Lessons learned that could improve future iterations of the project.

## Project Implementation

### TitanHelp Application Features:
- **Tickets Page:** Displays all help desk tickets (initially empty).
- **Create Ticket:** A button to create a new ticket, which opens a form to input:
  - Name
  - Date
  - Problem Description
- **Save Button:** Stores the ticket in the database and displays it on the main tickets page.

### Technology Stack:
- **Presentation Layer:** Razor, ASP.NET MVC, or WPF (choose one).
- **Application Layer:** Ticket class implemented as a POCO (Plain Old CLR Object).
- **Data Access Layer:** Entity Framework to handle database interactions.

## License
This project is licensed under the [MIT License](LICENSE).


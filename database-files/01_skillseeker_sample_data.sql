USE skillseeker;

-- ==========================
-- Departments
-- ==========================
INSERT INTO Department (name) VALUES 
('Economics'),
('Computer Science'),
('Mathematics');

-- ==========================
-- Professors
-- ==========================
INSERT INTO Professor (name, email, departmentID) VALUES
('Prof. Johnson', 'johnson@university.edu', 1),
('Prof. Lee', 'lee@university.edu', 1),
('Prof. Patel', 'patel@university.edu', 2),
('Prof. Hernandez', 'hernandez@university.edu', 1),
('Prof. Smith', 'smith@university.edu', 3);

-- ==========================
-- Courses
-- ==========================
INSERT INTO Course (name, description, departmentID, professorID) VALUES
('ECON 1116', 'Principles of Microeconomics', 1, 1),
('ECON 1117', 'Principles of Macroeconomics', 1, 2),
('CS 1010', 'Intro to Computer Science', 2, 3),
('MATH 2210', 'Calculus I', 3, 5);

-- ==========================
-- Students
-- ==========================
INSERT INTO Student (name, email) VALUES
('Alice Kim', 'alice.kim@student.edu'),
('Bob Lee', 'bob.lee@student.edu'),
('Charlie Park', 'charlie.park@student.edu'),
('Dana Nguyen', 'dana.nguyen@student.edu'),
('Ethan Wong', 'ethan.wong@student.edu');

-- ==========================
-- Ratings
-- ==========================
INSERT INTO Rating (studentID, professorID, courseID, clarity, engagement, fairness, helpfulness, comments) VALUES
(1, 1, 1, 5, 4, 5, 5, 'Great lectures and very clear explanations.'),
(2, 1, 1, 4, 5, 4, 5, 'Engaging class, fair grading.'),
(3, 2, 2, 3, 3, 4, 3, 'Lectures were okay, could use more examples.'),
(4, 3, 3, 5, 5, 5, 5, 'Excellent teaching, very helpful outside class.'),
(5, 5, 4, 4, 4, 4, 4, 'Good course, learned a lot.');

-- ==========================
-- Course_Professor (for multiple professors per course)
-- ==========================
INSERT INTO Course_Professor (courseID, professorID) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 5);

-- ==========================
-- Department_Course (optional)
-- ==========================
INSERT INTO Department_Course (departmentID, courseID) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 4);

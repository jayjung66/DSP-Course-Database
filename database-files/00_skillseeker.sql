CREATE DATABASE IF NOT EXISTS skillseeker;

USE course_ratings;

-- ==========================
-- Department Table
-- ==========================
CREATE TABLE IF NOT EXISTS Department (
    departmentID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

-- ==========================
-- Professor Table
-- ==========================
CREATE TABLE IF NOT EXISTS Professor (
    professorID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    departmentID INT,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID) ON DELETE SET NULL
);

-- ==========================
-- Course Table
-- ==========================
CREATE TABLE IF NOT EXISTS Course (
    courseID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    departmentID INT,
    professorID INT,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID) ON DELETE SET NULL,
    FOREIGN KEY (professorID) REFERENCES Professor(professorID) ON DELETE SET NULL
);

-- ==========================
-- Student Table
-- ==========================
CREATE TABLE IF NOT EXISTS Student (
    studentID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE
);

-- ==========================
-- Rating Table
-- ==========================
CREATE TABLE IF NOT EXISTS Rating (
    ratingID INT PRIMARY KEY AUTO_INCREMENT,
    studentID INT,
    professorID INT,
    courseID INT,
    clarity INT CHECK (clarity BETWEEN 1 AND 5),
    engagement INT CHECK (engagement BETWEEN 1 AND 5),
    fairness INT CHECK (fairness BETWEEN 1 AND 5),
    helpfulness INT CHECK (helpfulness BETWEEN 1 AND 5),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (studentID) REFERENCES Student(studentID) ON DELETE SET NULL,
    FOREIGN KEY (professorID) REFERENCES Professor(professorID) ON DELETE CASCADE,
    FOREIGN KEY (courseID) REFERENCES Course(courseID) ON DELETE CASCADE
);

-- ==========================
-- Course_Professor (for multiple profs per course)
-- ==========================
CREATE TABLE IF NOT EXISTS Course_Professor (
    courseID INT,
    professorID INT,
    PRIMARY KEY (courseID, professorID),
    FOREIGN KEY (courseID) REFERENCES Course(courseID) ON DELETE CASCADE,
    FOREIGN KEY (professorID) REFERENCES Professor(professorID) ON DELETE CASCADE
);

-- ==========================
-- Optional: Department_Course (if needed for flexibility)
-- ==========================
CREATE TABLE IF NOT EXISTS Department_Course (
    departmentID INT,
    courseID INT,
    PRIMARY KEY (departmentID, courseID),
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID) ON DELETE CASCADE,
    FOREIGN KEY (courseID) REFERENCES Course(courseID) ON DELETE CASCADE
);

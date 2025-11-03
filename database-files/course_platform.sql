CREATE DATABASE IF NOT EXISTS course_platform;
USE course_platform;

-- Main Course Table
CREATE TABLE IF NOT EXISTS Course (
    course_number VARCHAR(10) PRIMARY KEY,  -- e.g. CS2500
    name VARCHAR(255) NOT NULL,
    description TEXT
);

-- Uploads Table for HW/Exams/Notes with Ratings
CREATE TABLE IF NOT EXISTS Submission (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_number VARCHAR(10),
    category ENUM('homework', 'exam', 'note') NOT NULL,
    content TEXT NOT NULL,
    rating INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_number) REFERENCES Course(course_number) ON DELETE CASCADE
);

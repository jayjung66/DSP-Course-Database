from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Create a new Blueprint object for professors
professors = Blueprint('professors', __name__)

# Get all professors in the database
@professors.route('/professorsgetall', methods=['GET'])
def get_all_professors():
    query = '''
        SELECT *
        FROM Professor
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return make_response(jsonify(data), 200)
    except Exception as e:
        current_app.logger.error(f"Error fetching professors: {e}")
        return make_response({"error": str(e)}, 500)


# Add a professor
@professors.route('/add', methods=['POST'])
def add_professor():
    """
    Add a new professor to the database.
    """
    the_data = request.json
    current_app.logger.info(f"Adding professor: {the_data}")

    query = '''
        INSERT INTO Professor (name, email, departmentID)
        VALUES (%s, %s, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (
            the_data['name'],
            the_data['email'],
            the_data['departmentID']
        ))
        db.get_db().commit()

        response = make_response("Professor added successfully", 201)
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error adding professor: {e}")
        response = make_response({"error": str(e)}, 500)
    
    return response

@professors.route('/rate', methods=['POST'])
def rate_professor():
    """
    Add a new rating for a professor and update their rating as a running average.
    """
    the_data = request.json
    current_app.logger.info(f"Adding rating: {the_data}")
    
    db_conn = db.get_db()
    cursor = db_conn.cursor()
    
    try:
        professor_id = the_data['professorID']
        
        # Insert new rating into Rating table
        cursor.execute('''
            INSERT INTO Rating (professorID, clarity, engagement, fairness, helpfulness, comments)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (
            professor_id,
            the_data.get('clarity', 0),
            the_data.get('engagement', 0),
            the_data.get('fairness', 0),
            the_data.get('helpfulness', 0),
            the_data.get('comments', '')
        ))
        
        # Fetch current average rating
        cursor.execute('SELECT rating FROM Professor WHERE professorID = %s', (professor_id,))
        current_avg = cursor.fetchone()[0] or 0
        
        # Calculate new rating as average of previous avg and new rating
        new_rating = (
            the_data.get('clarity', 0) +
            the_data.get('engagement', 0) +
            the_data.get('fairness', 0) +
            the_data.get('helpfulness', 0)
        ) / 4
        
        updated_avg = round((current_avg + new_rating) / 2, 2)
        
        # Update Professor table
        cursor.execute('UPDATE Professor SET rating = %s WHERE professorID = %s', (updated_avg, professor_id))
        
        db_conn.commit()
        response = make_response("Rating added and professor average updated", 201)
    
    except Exception as e:
        db_conn.rollback()
        current_app.logger.error(f"Error adding rating: {e}")
        response = make_response({"error": str(e)}, 500)
    
    return response



# Delete a professor
@professors.route('/<int:professorID>/delete', methods=['DELETE'])
def delete_professor(professorID):
    """
    Delete a professor by their ID.
    """
    query = 'DELETE FROM Professor WHERE professorID = %s'
    current_app.logger.info(f"Deleting professor with ID: {professorID}")
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (professorID,))
        db.get_db().commit()

        if cursor.rowcount == 0:
            response = make_response("Professor not found", 404)
        else:
            response = make_response("Professor deleted successfully", 200)
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error deleting professor: {e}")
        response = make_response({"error": str(e)}, 500)

    return response

# Get detailed information about a specific professor by their ID

@professors.route('/professors/<int:professor_id>', methods=['GET'])
def get_professor_by_id(professor_id):
    query = '''
        SELECT P.id, P.name, D.name AS department, GROUP_CONCAT(C.name) AS courses
        FROM Professor P
        LEFT JOIN Departments D ON P.department_id = D.id
        LEFT JOIN Courses C ON P.id = C.professor_id
        WHERE P.id = %s
        GROUP BY P.id, P.name, D.name
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (professor_id,))
    data = cursor.fetchone()
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response("Professor not found", 404)
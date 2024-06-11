import sqlite3
conn = sqlite3.connect('data\oewn-2024-sqlite-2.1.1.sqlite')


def get_definitions_and_pronunciations(word):
    # Establish a connection to the SQLite database
    cursor = conn.cursor()

    # SQL query to get definitions and samples
    query_definitions = """
    SELECT w.word, s.synsetid, s.definition, sa.sample
    FROM words w
    LEFT JOIN senses se ON w.wordid = se.wordid
    LEFT JOIN synsets s ON se.synsetid = s.synsetid
    LEFT JOIN samples sa ON s.synsetid = sa.synsetid
    WHERE w.word = ?
    ORDER BY s.definition
    """

    # SQL query to get pronunciations
    query_pronunciations = """
    SELECT w.word, p.pronunciation
    FROM words w
    INNER JOIN lexes_pronunciations lp ON w.wordid = lp.wordid
    LEFT JOIN pronunciations p ON lp.pronunciationid = p.pronunciationid
    WHERE w.word = ?
    ORDER BY p.pronunciation
    """

    # Execute queries
    cursor.execute(query_definitions, (word,))
    definitions = cursor.fetchall()

    cursor.execute(query_pronunciations, (word,))
    pronunciations = cursor.fetchall()

    # Close the connection
    conn.close()

    # Organize the results
    result = {
        'word': word,
        'definitions': [],
        'pronunciations': []
    }

    for row in definitions:
        result['definitions'].append({
            'definition': row[2],
            'sample': row[3] if row[3] else None
        })

    for row in pronunciations:
        result['pronunciations'].append(row[1])

    return result

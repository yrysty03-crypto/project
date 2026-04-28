import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",
    password="12345"
)

conn.set_client_encoding('UTF8')
cur = conn.cursor()

def create_player(username):
    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    res = cur.fetchone()
    if res:
        return res[0]

    cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
    conn.commit()
    return cur.fetchone()[0]

def save_score(player_id, score, level):
    cur.execute(
        "INSERT INTO game_sessions(player_id, score, level_reached) VALUES(%s,%s,%s)",
        (player_id, score, level)
    )
    conn.commit()

def get_top():
    cur.execute("""
        SELECT players.username, game_sessions.score
        FROM game_sessions
        JOIN players ON players.id = game_sessions.player_id
        ORDER BY score DESC LIMIT 10
    """)
    return cur.fetchall()

def get_best(player_id):
    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id=%s", (player_id,))
    res = cur.fetchone()[0]
    return res if res else 0
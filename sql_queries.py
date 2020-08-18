# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay
                                (time_stamp varchar,
                                user_id int,
                                level varchar,
                                song_id varchar,
                                artist_id varchar,
                                session_id int,
                                location varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users
                            (user_id int,
                            firstName varchar,
                            lastName varchar,
                            gender varchar,
                            level varchar)

""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs
                            (song_id varchar, 
                             title varchar, 
                             artist_id varchar,
                             year int,
                             duration float8)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
                            (artist_id varchar,
                             artist_name varchar,
                             location varchar,
                             latitude float8,
                             longitude float8)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time
                            (time_stamp varchar, 
                             hour int, 
                             day int,
                             week int,
                             year int,
                             weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay
                                (time_stamp,
                                 user_id,
                                 level,
                                 song_id,
                                 artist_id,
                                 session_id,
                                 location)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users
                            (user_id,
                             firstName,
                             lastName,
                             gender,
                             level)
                        VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs
                            (song_id, 
                             title, 
                             artist_id,
                             year,
                             duration)
                        VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists
                            (artist_id,
                             artist_name,
                             location,
                             latitude,
                             longitude)
                           VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time
                            (time_stamp, 
                             hour, 
                             day,
                             week,
                             year,
                             weekday)
                        VALUES (%s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""SELECT song_id, artists.artist_id FROM songs 
                  INNER JOIN artists ON songs.artist_id = artists.artist_id
                  WHERE title = %s 
                  AND artist_name = %s 
                  AND duration = %s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, 
                        user_table_create, 
                        song_table_create, 
                        artist_table_create, 
                        time_table_create]

drop_table_queries = [songplay_table_drop, 
                      user_table_drop, 
                      song_table_drop, 
                      artist_table_drop, 
                      time_table_drop]


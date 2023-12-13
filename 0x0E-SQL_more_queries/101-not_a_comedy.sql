-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT tv_genres.name FROM tv_genres WHERE tv_genres.id NOT IN (
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tv_shows_rate.rating) AS rating_sum FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows_rate ON tv_show_genres.show_id = tv_shows_rate.show_id
GROUP BY tv_genres.name ORDER BY rating_sum DESC;

-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(tv_shows_ratings.rate) AS 'rating' FROM tv_shows
LEFT JOIN tv_shows_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title ORDER BY rating DESC;

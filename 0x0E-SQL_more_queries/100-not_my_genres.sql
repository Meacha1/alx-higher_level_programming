--  List genres of the Dexter show using the hbtn_0d_tvshows database
SELECT DISTINCT name
     FROM tv_genres
LEFT JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows
       ON tv_show_genres.show_id = tv_shows.id
    WHERE name NOT IN (
    SELECT name
      FROM tv_genres
     LEFT JOIN tv_show_genres
            ON genre_id = tv_genres.id
     LEFT JOIN tv_shows
            ON show_id = tv_shows.id
	         WHERE title = "Dexter")
 ORDER BY name ASC;
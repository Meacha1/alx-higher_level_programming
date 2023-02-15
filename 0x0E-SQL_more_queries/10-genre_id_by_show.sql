-- Lists all shows contained in hbtn_0d_tvshows with at least one linked genre
-- If it does not exists, then create it
  CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
  SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    JOIN tv_show_genres
      ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;
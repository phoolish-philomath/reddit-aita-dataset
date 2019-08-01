with total as (select count(*) as total from posts)
   select flair, count(*) * 100.0 / total.total as share
      from total, posts group by flair;


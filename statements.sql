

UPDATE `newswhip` n, urls u SET n.url_id = u.id WHERE n.link_text = u.url_raw;


UPDATE `comment` c, urls u SET c.url_id = u.id WHERE c.url_text = u.url_no_www;


UPDATE `newswhip_topic` t SET num_articles = (SELECT COUNT(*) FROM newswhip_topic_set s WHERE s.topic_id = t.id);


UPDATE `clickstream_raw` c, urls u SET c.url_id = u.id WHERE c.raw_url = u.url_no_http;
# Rows matched: 810013  Changed: 810013  Warnings: 0

UPDATE `clickstream_raw` c, urls u SET c.url_id = u.id WHERE c.raw_url = u.url_no_www;
# Rows matched: 1799  Changed: 0  Warnings: 0

UPDATE `clickstream_raw` c, urls u SET c.url_id = u.id WHERE c.raw_url = u.url_no_http_www;
# Rows matched: 1799  Changed: 0  Warnings: 0

UPDATE `clickstream_raw` c, urls u SET c.url_id = u.id WHERE c.raw_url = u.url_raw;
# Rows matched: 26400  Changed: 24601  Warnings: 0

UPDATE `clickstream_raw` c, urls u SET c.url_id = u.id WHERE CONCAT(c.raw_url, '/') = u.url_no_http;
# Rows matched: 1336236  Changed: 1336236  Warnings: 0

UPDATE `clickstream_raw` c, urls u SET c.url_id = u.id WHERE CONCAT(c.raw_url, '/') = u.url_no_www;
#

UPDATE `clickstream_raw` c, urls u SET c.url_id = u.id WHERE CONCAT(c.raw_url, '/') = u.url_no_http_www;
#

UPDATE `clickstream_raw` c, urls u SET c.url_id = u.id WHERE CONCAT(c.raw_url, '/') = u.url_raw;
#


UPDATE `urls` u SET comment_count = (
    SELECT COUNT(*) FROM comment c WHERE c.url_id = u.id
);

UPDATE `urls` u SET visit_count = (
    SELECT COUNT(*) FROM clickstream_raw c WHERE c.url_id = u.id
);


SELECT COUNT(DISTINCT(raw_url)) FROM `clickstream_raw` WHERE `raw_url` like '%2014%';
# 50894

SELECT COUNT(*) FROM `urls` WHERE `url_raw` like '%2014%';
# 952 total


UPDATE `newswhip`
SET `publication_datetime` = FROM_UNIXTIME(ROUND(publication_timestamp_text/1000));
# Rows matched: 3439  Changed: 3439  Warnings: 0


UPDATE `clickstream_raw`
SET `date_click` = FROM_UNIXTIME(ROUND(timestamp/1000))
WHERE url_id > 0;
# Rows matched: 834614  Changed: 834614  Warnings: 834605



SELECT url_id, COUNT(*) as num_u FROM `clickstream_raw`
GROUP BY url_id
ORDER BY num_u DESC;
# Showing rows 0 - 24 (4584 total, Query took 4.3529 seconds.)


# Used for insert
SELECT null, url_id, date_click, count(*) FROM `clickstream_raw` WHERE url_id > 0 GROUP BY url_id, date_click ORDER BY url_id



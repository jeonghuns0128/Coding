-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') from BOOK
where PUBLISHED_DATE >= '2021-01-01 00:00:00'
and PUBLISHED_DATE <= '2021-12-31 00:00:00'
and CATEGORY = '인문'
order by PUBLISHED_DATE asc 
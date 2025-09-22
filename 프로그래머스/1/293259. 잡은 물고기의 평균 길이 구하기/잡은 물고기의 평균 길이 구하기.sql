select ROUND(AVG((case when LENGTH > 10 then LENGTH else 10 END)), 2) AS AVERAGE_LENGTH
from FISH_INFO;
# %%
import numpy as np
import pandas as pd
import sqlite3

# %%
nbadb = sqlite3.connect('nba2024.db')

# %%
myquery = """
SELECT *
FROM games
WHERE sellout = 1
ORDER BY duration DESC;
"""

# %%
pd.read_sql_query(myquery, con=nbadb)

# %%
# same query bad etiquette
myquery = 'select * from games where sellout = 1 order by duration desc'
pd.read_sql_query(myquery, con=nbadb)

# %%
# good etiquette
#clauses in all caps
#clases in new line
#except for clauses part of other clauses
    #on the samle line or on  new line with indent ton indicate it is part of the last clause

myquery = '''
SELECT * 
FROM games 
WHERE sellout = 1
ORDER BY duration DESC
'''
pd.read_sql_query(myquery, con=nbadb)

# %% [markdown]
# ## MVP?

# %%
myquery = '''
SELECT * 
FROM playergames

'''
pd.read_sql_query(myquery, con=nbadb)

# %%
myquery = '''
SELECT personid,
       points, threepointersmade, fieldgoalsmade, fieldgoalsattempted, freethrowsmade, 
       freethrowsattempted, reboundstotal, assists, steals, blocks, turnovers
FROM playergames


'''
pd.read_sql_query(myquery, con=nbadb)

# %%
myquery = '''
SELECT personid,
       points + threepointersmade + 2*fieldgoalsmade - fieldgoalsattempted + freethrowsmade - 
       freethrowsattempted +reboundstotal+ 2*assists+ 4*steals+ 4*blocks- 2*turnovers
FROM playergames


'''
pd.read_sql_query(myquery, con=nbadb)

# %%
myquery = '''
SELECT personid,
       points + threepointersmade + 2*fieldgoalsmade - fieldgoalsattempted + freethrowsmade - 
       freethrowsattempted +reboundstotal+ 2*assists+ 4*steals+ 4*blocks- 2*turnovers AS mvp_points
FROM playergames


'''
pd.read_sql_query(myquery, con=nbadb)

# %%
myquery = '''
SELECT personid,
       SUM(points + threepointersmade + 2*fieldgoalsmade - fieldgoalsattempted + freethrowsmade - 
       freethrowsattempted +reboundstotal+ 2*assists+ 4*steals+ 4*blocks- 2*turnovers) AS mvp_points
FROM playergames
GROUP BY personid

'''
pd.read_sql_query(myquery, con=nbadb)

# %%
myquery = '''
SELECT personid,
       SUM(points + threepointersmade + 2*fieldgoalsmade - fieldgoalsattempted + freethrowsmade - 
       freethrowsattempted +reboundstotal+ 2*assists+ 4*steals+ 4*blocks- 2*turnovers) AS mvp_points
FROM playergames
GROUP BY personid
ORDER BY mvp_points DESC
'''
pd.read_sql_query(myquery, con=nbadb)

# %%
myquery = '''
SELECT p.display_first_last,
       SUM(pg.points + pg.threepointersmade + 2*pg.fieldgoalsmade - pg.fieldgoalsattempted + pg.freethrowsmade - 
       pg.freethrowsattempted +pg.reboundstotal+ 2*pg.assists+ 4*pg.steals+ 4*pg.blocks- 2*pg.turnovers) AS mvp_points
FROM playergames pg
LEFT JOIN players p
    ON pg.personid = p.personid
GROUP BY pg.personid, p.display_first_last
ORDER BY mvp_points DESC
'''
pd.read_sql_query(myquery, con=nbadb)

# %% [markdown]
# ## Challenge; all scores that happened without considering which score belongs to home and away, with latest date that score was achieved and also the count of times that score occured

# %%


# %%
myquery = '''


SELECT win_score, lose_score, COUNT(*) as count, MAX(game_date) as date
FROM (SELECT gameid, game_date, MAX(pts) as win_score, MIN(pts) as lose_score
      FROM teamgames
      GROUP BY gameid, game_date)y
GROUP BY win_score, lose_score
ORDER BY count DESC
'''
pd.read_sql_query(myquery, con=nbadb)



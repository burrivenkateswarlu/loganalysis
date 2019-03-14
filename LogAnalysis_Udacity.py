#!/usr/bin/env python
import psycopg2
# first top 3 articles execution


def Dine_Articles():
    connec = psycopg2.connect(
        dbname="news", user='vagrant', password='vagrant')
    curso = connec.cursor()
    q1 = ("SELECT title, count(*) as views FROM articles \n"
          "JOIN log\n"
          "ON articles.slug = substring(log.path, 10)\n"
          "GROUP BY title ORDER BY views DESC LIMIT 3;")
    try:
        if (q1):
            curso.execute(q1)
            rs = curso.fetchall()
            print(" \n  *What are the most popular three"
                  " articles of all time ? \n")
            count = 1
            for result in rs:
                num = '(' + str(count) + ') "'
                tit = result[0]
                views = ' " ' + str(result[1]) + " views"
                print(num + tit + views)
                count = count+1
        else:
            print("program does not have query")
    except Exception as error:
        print(error)
# print('  "{0}"===>{1} views'.format(result[0], result[1]))
# top 4 authors


def Dine_Authors():
    connec = psycopg2.connect(
        dbname="news", user='vagrant', password='vagrant')
    curso = connec.cursor()
    q2 = ("SELECT authors.name, count(*) as views\n"
          "    FROM articles \n"
          "    JOIN authors\n"
          "    ON articles.author = authors.id \n"
          "    JOIN log \n"
          "    ON articles.slug = substring(log.path, 10)\n"
          "    WHERE log.status LIKE '200 OK'\n"
          "    GROUP BY authors.name ORDER BY views DESC;")
    try:
        if (q2):
            curso.execute(q2)
            rs = curso.fetchall()
            print("\n  **Who are the most popular article"
                  " authors of all time ? \n")
            count = 1
            for result in rs:
                num = '(' + str(count) + ') " '
                tit = result[0]
                views = ' " -- ' + str(result[1]) + " views"
                print(num + tit + views)
                count = count+1
        else:
            print(" program does not have query ")
    except Exception as error:
        print(error)
# print('  "{0}"====>{1} views'.format(result[0], result[1]))
# lead errors


def Dine_Error_Analysis():
    connec = psycopg2.connect(
        dbname="news", user='vagrant', password='vagrant')
    curso = connec.cursor()
    q3 = """SELECT errorlogs.date, round(100.0*errorcount/logcount,2) as percent
            FROM logs, errorlogs
            WHERE logs.date = errorlogs.date
            AND errorcount > logcount/100;"""
    try:
        if (q3):
            curso.execute(q3)
            rs = curso.fetchall()
            print(" \n  ***Days on which more than 1% of"
                  " requests lead to errors ? ")
            for reu in rs:
                print('\n  On ' + str(
                    reu[0]) + '   ===>   ' + '%.1f' % reu[1] + '% errors\n')
                print(' ')
        else:
            print(" program does not have query ")
    except Exception as error:
        print(error)
Dine_Articles()
Dine_Authors()
Dine_Error_Analysis()

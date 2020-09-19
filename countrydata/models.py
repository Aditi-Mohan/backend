from django.db import models, connection
from sqlalchemy import create_engine
import pandas as pd

# Create your models here.
class Confirmed(models.Model):
    country = models.TextField(primary_key=True)
    startdate = models.TextField(db_column='startDate', blank=True, null=True)
    enddate = models.TextField(db_column='endDate', blank=True, null=True)
    counts = models.TextField(db_column='counts', blank=True, null=True)

    def __str__(self):
        return self.country

    class Meta:
        managed = False
        db_table = 'confirmed'

class Recovery(models.Model):
    country = models.TextField(primary_key=True)
    startdate = models.TextField(db_column='startDate', blank=True, null=True)
    enddate = models.TextField(db_column='endDate', blank=True, null=True)
    counts = models.TextField(db_column='counts', blank=True, null=True)

    def __str__(self):
        return self.country

    class Meta:
        managed = False
        db_table = 'recovery'

class Death(models.Model):
    country = models.TextField(primary_key=True)
    startdate = models.TextField(db_column='startDate', blank=True, null=True)
    enddate = models.TextField(db_column='endDate', blank=True, null=True)
    counts = models.TextField(db_column='counts', blank=True, null=True)

    def __str__(self):
        return self.country

    class Meta:
        managed = False
        db_table = 'death'

def initialise_table(url, name):
    df = pd.read_csv(url)
    df.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)
    df.rename(columns = {'Country/Region': 'Country'}, inplace=True)
    countries = []
    start_dates = []
    end_dates = []
    counts = []
    for i in range(len(df)):
        country = df.loc[i]['Country']
        if country in countries:
            continue
        start_date = df.loc[i][1:].keys()[0]
        end_date = df.loc[i][1:].keys()[-1]
        count = df[df['Country'] == country][df.columns[1:]].sum().values.tolist()
        countries.append(country)
        start_dates.append(start_date)
        end_dates.append(end_date)
        count_str = str(count[0])
        for each in count[1:]:
            count_str +=','+str(each)
        counts.append(count_str)
    df = pd.DataFrame({'country': countries, 'startDate': start_dates, 'endDate': end_dates, 'counts': counts})
    engine = create_engine('postgresql://postgres:popo1234@localhost:5432/test')
    table = df.to_sql(name, engine, if_exists='replace', index=False)
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE %s ADD PRIMARY KEY (country);", [name])

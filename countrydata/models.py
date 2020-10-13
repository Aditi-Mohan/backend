from django.db import models, connection
from sqlalchemy import create_engine, types
from django.contrib.postgres.fields import ArrayField
import pandas as pd

# Create your models here.
class Data(models.Model):
    country = models.TextField(db_column='Country', primary_key=True)  # Field name made lowercase.
    confirmed = models.TextField(db_column='Confirmed', blank=True, null=True)  # Field name made lowercase.
    startdate = models.TextField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.TextField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    currconfirmed = models.BigIntegerField(db_column='CurrConfirmed', blank=True, null=True)  # Field name made lowercase.
    death = models.TextField(db_column='Death', blank=True, null=True)  # Field name made lowercase.
    currdeath = models.BigIntegerField(db_column='CurrDeath', blank=True, null=True)  # Field name made lowercase.
    recovery = models.TextField(db_column='Recovery', blank=True, null=True)  # Field name made lowercase.
    currrecovery = models.BigIntegerField(db_column='CurrRecovery', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    curractive = models.BigIntegerField(db_column='CurrActive', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data'

class Subscriber(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    watchlist = models.TextField(blank=True, null=True)
    top5 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriber'

def process_df(df, name):
    df.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)
    df.rename(columns = {'Country/Region': 'Country'}, inplace=True)
    new_df= []
    curr_counts = []
    for country in df['Country'].unique():
        count = df[df['Country'] == country][df.columns[1:]].sum().values.tolist()
        new_df.append(count)
        curr_counts.append(count[-1])
    df = pd.DataFrame({'Country': df['Country'].unique(), name: new_df, 'StartDate': [df.columns[1]]*len(new_df), 'EndDate': [df.columns[-1]]*len(new_df), 'Curr'+name: curr_counts})
    return df

def get_active(conf, c_name, death, d_name, rec, r_name):
    counts = [[c-(d+r) for c,d,r in zip(ci,di,ri)] for ci,di,ri in zip(conf[c_name], death[d_name], rec[r_name])]
    curr_counts = [c-(d+r) for c,d,r in zip(conf['Curr'+c_name], death['Curr'+d_name], rec['Curr'+r_name])]
    df = pd.DataFrame({'Country': conf['Country'].values, 'Active': counts, 'StartDate': conf['StartDate'], 'EndDate': conf['EndDate'], 'CurrActive': curr_counts})
    return df

def combine_into_single_df(conf, death, rec, active):
    df = pd.merge(conf, death, on=['Country', 'StartDate', 'EndDate'])
    df = pd.merge(df, rec, on=['Country', 'StartDate', 'EndDate'])
    df = pd.merge(df, active, on=['Country', 'StartDate', 'EndDate'])
    return df

def get_ranks(df):
    df = df.sort_values('CurrActive', ascending=False)
    df['Rank'] = range(1,len(df)+1)
    return df

def make_table(df):
    engine = create_engine('postgresql://postgres:popo1234@localhost:5432/test')
    table = df.to_sql('data', engine, if_exists='replace', index=False, dtype={
    'Country': types.String(),'Confirmed': types.ARRAY(types.Integer), 'StartDate': types.String(),
    'EndDate': types.String(), 'CurrConfirmed': types.Integer(), 'Death': types.ARRAY(types.Integer),
    'CurrDeath': types.Integer(), 'Recovery': types.ARRAY(types.Integer), 'CurrEecovery': types.Integer(),
    'Active': types.ARRAY(types.Integer), 'CurrActive': types.Integer(), 'Rank': types.Integer()
})
    with connection.cursor() as cursor:
        cursor.execute('ALTER TABLE data ADD PRIMARY KEY ("Country");')

def initialize():
    conf = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    death = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    rec = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    conf = process_df(conf, 'Confirmed')
    death = process_df(death, 'Death')
    rec = process_df(rec, 'Recovery')
    active = get_active(conf, 'Confirmed', death, 'Death', rec, 'Recovery')
    merged_df = combine_into_single_df(conf, death, rec, active)
    df = get_ranks(merged_df)
    make_table(df)

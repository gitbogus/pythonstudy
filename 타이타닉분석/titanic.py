import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')

titanic.head

titanic.describe()

titanic.var()

titanic.mad()

titanic.groupby('class').count()

sns.countplot(y = 'class', data=titanic);

sns.countplot(y = 'sex', data=titanic);

sns.countplot(y = 'alive', data=titanic);

sns.countplot(y = 'alone', data=titanic);

titanic.groupby('class').std()

titanic.groupby('class')['fare'].median()

titanic.groupby('class')['age'].describe()

titanic.groupby('sex')['age'].aggregate([min, np.median, max])

titanic.query("age > 30").groupby('class').median()

titanic.query("fare < 20").groupby('class').median()

titanic.groupby(['class', 'sex'])['age'].mean().unstack()

sns.catplot(x = 'sex', y = 'age',
            hue = 'class', kind = 'bar',
            data = titanic);


sns.catplot(x = 'who', y = 'age',
            hue = 'class', kind = 'bar',
            data = titanic);

titanic.groupby(['class', 'sex'])['fare'].mean().unstack()

titanic.groupby(['class', 'who'])['fare'].mean().unstack()

sns.catplot(x = 'who', y = 'fare',
            hue = 'class', kind='bar',
            data = titanic);

titanic.groupby(['class', 'sex'])['survived'].mean().unstack()

titanic.pivot_table('survived', index = 'class', columns='who')

sns.catplot(x='class', y ='survived',
            hue = 'sex')

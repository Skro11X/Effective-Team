from django.db import models


class Creator(models.Model):
    name = models.CharField(max_length=30, verbose_name="Team creator")
    score = models.FloatField(verbose_name='Score')

    class Meta:
        ordering = ['id']
        verbose_name = 'Creator'
        verbose_name_plural = 'Creators'

    def __str__(self):
        return f'{self.name} with score {self.score}'


class Team(models.Model):
    name = models.CharField(unique=True, max_length=60, verbose_name='Team name')
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, verbose_name='Team creator')

    class Meta:
        ordering = ['id']
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return f'{self.name} which {self.creator} created'


class Member(models.Model):
    name = models.CharField(max_length=30, verbose_name='Team member')
    endurance = models.IntegerField(verbose_name='Member endurance')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, verbose_name='Team')

    class Meta:
        ordering = ['id']
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return f'{self.name} from {self.team} with endurance {self.endurance}'


class TeamApplication(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Member')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Team')

    class Meta:
        ordering = ['id']
        verbose_name = 'Team Application'
        verbose_name_plural = 'Teams Applications'

    def __str__(self):
        return f'{self.member} sent a request {self.team}'


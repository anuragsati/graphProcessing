from django.db import models

class Graph(models.Model):
    startNode = models.IntegerField(blank=True,null=True)
    endNode = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.startNode) + ' -> ' + str(self.endNode)

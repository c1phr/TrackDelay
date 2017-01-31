import peewee


class TrainDelay(peewee.Model):
    severity = peewee.TextField()
    line = peewee.TextField()
    branch = peewee.TextField()
    start_time = peewee.TextField()
    end_time = peewee.TextField()
    header_text = peewee.TextField()
    cause = peewee.TextField()

    class Meta:
        database = 

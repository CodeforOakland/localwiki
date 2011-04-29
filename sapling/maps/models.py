from django.contrib.gis.db import models
from django.contrib.gis.geos import *
from django.core.urlresolvers import reverse

from versionutils.versioning import TrackChanges
from pages.models import Page

from fields import *


class MapData(models.Model):
    points = models.MultiPointField(null=True, blank=True)
    lines = models.MultiLineStringField(null=True, blank=True)
    polys = models.MultiPolygonField(null=True, blank=True)
    geom = FlatCollectionFrom(points='points', lines='lines', polys='polys')

    page = models.OneToOneField(Page)

    objects = models.GeoManager()
    history = TrackChanges()

    def get_absolute_url(self):
        return reverse('maps:show', args=[self.page.pretty_slug])
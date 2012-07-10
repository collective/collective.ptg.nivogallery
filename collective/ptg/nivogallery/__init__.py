from zope.i18nmessageid import MessageFactory
from collective.plonetruegallery.utils import createSettingsFactory
from collective.plonetruegallery.browser.views.display import BaseDisplayType
from collective.plonetruegallery.browser.views.display import jsbool
from collective.plonetruegallery.interfaces import IBaseSettings
from zope import schema

_ = MessageFactory('collective.ptg.nivogallery')

class INivogalleryDisplaySettings(IBaseSettings):
    nivogallery_directionnav = schema.Bool(
        title=_(u"label_nivogallery_directionnav",
            default=u"Show navigation arrows on the image"),
        default=True)
    nivogallery_progressbar = schema.Bool(
        title=_(u"label_nivogallery_progressbar",
            default=u"Show progressbar at the top"),
        default=True)
    nivogallery_width = schema.TextLine(
        title=_(u"label_nivogallery_width",
            default=u"Width of the gallery"),
        default=u"600px")
    nivogallery_height = schema.TextLine(
        title=_(u"label_nivogallery_height",
            default=u"Height of the gallery. You can not set the height in %"),
        default=u"350px")


class NivogalleryDisplayType(BaseDisplayType):

    name = u"nivogallery"
    schema = INivogalleryDisplaySettings
    description = _(u"label_nivogallery_display_type",
        default=u"Nivogallery")

    def javascript(self):
        return u"""
        <script type="text/javascript"
src="%(portal_url)s/++resource++ptg.nivogallery/js/jquery.nivo.gallery.min.js">
</script>
    <script type="text/javascript">
$(document).ready(function() {
    $('#gallery').nivoGallery({
    pauseTime: %(delay)i,
    animSpeed: %(duration)i,
    effect: 'fade',
    startPaused: false,
    directionNav: %(directionnav)s,
    progressBar: %(progressbar)s
    });
});
</script>

""" % {
         'portal_url': self.portal_url,
         'duration': self.settings.duration,
         'timed': jsbool(self.settings.timed),
         'delay': self.settings.delay,
         'start_automatically': jsbool(self.settings.timed),
         'directionnav': jsbool(self.settings.nivogallery_directionnav),
         'progressbar': jsbool(self.settings.nivogallery_progressbar),
    }

    def css(self):
        base_url = '%s/++resource++ptg.nivogallery' % (
            self.portal_url)
        return u"""
        <style>
       .nivoGallery {
        height: %(height)s;
        width: %(width)s;
        }
        </style>
<link rel="stylesheet" type="text/css" href="%(base_url)s/css/style.css"/>
""" % {
        'height': self.settings.nivogallery_height,
        'width': self.settings.nivogallery_width,
        'base_url': base_url
       }
NivogallerySettings = createSettingsFactory(NivogalleryDisplayType.schema)